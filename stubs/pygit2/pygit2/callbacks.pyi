"""
In this module we keep everything concerning callback. This is how it works,
with an example:

1. The pygit2 API calls libgit2, it passes a payload object
   e.g. Remote.fetch calls git_remote_fetch

2. libgit2 calls Python callbacks
   e.g. git_remote_fetch calls _transfer_progress_cb

3. Optionally, the Python callback may proxy to a user defined function
   e.g. _transfer_progress_cb calls RemoteCallbacks.transfer_progress

4. The user defined function may return something on success, or raise an
   exception on error, or raise the special Passthrough exception.

5. The callback may return in 3 different ways to libgit2:

   - Returns GIT_OK on success.
   - Returns GIT_PASSTHROUGH if the user defined function raised Passthrough,
     this tells libgit2 to act as if this callback didn't exist in the first
     place.
   - Returns GIT_EUSER if another exception was raised, and keeps the exception
     in the payload to be re-raised later.

6. libgit2 returns to the pygit2 API, with an error code
   e.g. git_remote_fetch returns to Remote.fetch

7. The pygit2 API will:

   - Return something on success.
   - Raise the original exception if libgit2 returns GIT_EUSER
   - Raise another exception if libgit2 returns another error code

The payload object is passed all the way, so pygit2 API can send information to
the inner user defined function, and this can send back results to the pygit2
API.
"""

from _typeshed import StrOrBytesPath
from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import Protocol
from typing_extensions import ParamSpec, Self, TypeAlias

from _cffi_backend import _CDataBase

from ._pygit2 import DiffFile, Oid
from .enums import CheckoutNotify, CheckoutStrategy, CredentialType, StashApplyProgress
from .remotes import TransferProgress
from .utils import _IntoStrArray

class Payload:
    def __init__(self, **kw: object) -> None: ...
    def check_error(self, error_code: int) -> None: ...

# Upstream is not yet defining a concrete type for certificates, and no usage example is
# available either.
_Certificate: TypeAlias = None

class _Credentials(Protocol):
    @property
    def credential_type(self) -> CredentialType: ...
    @property
    def credential_tuple(self) -> tuple[str, ...]: ...
    def __call__(self, _url: str, _username: str | None, _allowed: CredentialType) -> Self: ...

class RemoteCallbacks(Payload):
    """
    Base class for pygit2 remote callbacks.

    Inherit from this class and override the callbacks which you want to use
    in your class, which you can then pass to the network operations.

    For the credentials, you can either subclass and override the 'credentials'
    method, or if it's a constant value, pass the value to the constructor,
    e.g. RemoteCallbacks(credentials=credentials).

    You can as well pass the certificate the same way, for example:
    RemoteCallbacks(certificate=certificate).
    """
    # Upstream code is broken: the credentials() method is shadowed if the constructor
    # gets passed a non-None "credentials".
    # credentials: _Credentials | None
    certificate: _Certificate | None
    def __init__(self, credentials: _Credentials | None = None, certificate: _Certificate | None = None) -> None: ...
    def sideband_progress(self, string: str) -> None:
        """
        Progress output callback.  Override this function with your own
        progress reporting function

        Parameters:

        string : str
            Progress output from the remote.
        """
        ...
    def credentials(self, url: str, username_from_url: str | None, allowed_types: CredentialType) -> _Credentials:
        """
        Credentials callback.  If the remote server requires authentication,
        this function will be called and its return value used for
        authentication. Override it if you want to be able to perform
        authentication.

        Returns: credential

        Parameters:

        url : str
            The url of the remote.

        username_from_url : str or None
            Username extracted from the url, if any.

        allowed_types : CredentialType
            A combination of CredentialType bitflags representing the
            credential types supported by the remote.
        """
        ...
    def certificate_check(self, certificate: _Certificate, valid: bool, host: str) -> bool:
        """
        Certificate callback. Override with your own function to determine
        whether to accept the server's certificate.

        Returns: True to connect, False to abort.

        Parameters:

        certificate : None
            The certificate. It is currently always None while we figure out
            how to represent it cross-platform.

        valid : bool
            Whether the TLS/SSH library thinks the certificate is valid.

        host : str
            The hostname we want to connect to.
        """
        ...
    def transfer_progress(self, stats: TransferProgress) -> None:
        """
        Transfer progress callback. Override with your own function to report
        transfer progress.

        Parameters:

        stats : TransferProgress
            The progress up to now.
        """
        ...
    def update_tips(self, refname: str, old: Oid, new: Oid) -> None:
        """
        Update tips callback. Override with your own function to report
        reference updates.

        Parameters:

        refname : str
            The name of the reference that's being updated.

        old : Oid
            The reference's old value.

        new : Oid
            The reference's new value.
        """
        ...
    def push_update_reference(self, refname: str, message: str) -> None:
        """
        Push update reference callback. Override with your own function to
        report the remote's acceptance or rejection of reference updates.

        refname : str
            The name of the reference (on the remote).

        message : str
            Rejection message from the remote. If None, the update was accepted.
        """
        ...

class CheckoutCallbacks(Payload):
    """
    Base class for pygit2 checkout callbacks.

    Inherit from this class and override the callbacks that you want to use
    in your class, which you can then pass to checkout operations.
    """
    def __init__(self) -> None: ...
    def checkout_notify_flags(self) -> CheckoutNotify:
        """
        Returns a bit mask of the notifications to receive from a checkout
        (a combination of enums.CheckoutNotify constants).

        By default, if you override `checkout_notify`, all notifications will
        be enabled. You can fine tune the notification types to enable by
        overriding `checkout_notify_flags`.

        Please note that the flags are only sampled once when checkout begins.
        You cannot change the flags while a checkout is in progress.
        """
        ...
    def checkout_notify(
        self, why: CheckoutNotify, path: str, baseline: DiffFile | None, target: DiffFile | None, workdir: DiffFile | None
    ) -> None:
        """
        Checkout will invoke an optional notification callback for
        certain cases - you pick which ones via `checkout_notify_flags`.

        Raising an exception from this callback will cancel the checkout.
        The exception will be propagated back and raised by the
        Repository.checkout_... call.

        Notification callbacks are made prior to modifying any files on disk,
        so canceling on any notification will still happen prior to any files
        being modified.
        """
        ...
    def checkout_progress(self, path: str, completed_steps: int, total_steps: int) -> None:
        """Optional callback to notify the consumer of checkout progress."""
        ...

class StashApplyCallbacks(CheckoutCallbacks):
    """
    Base class for pygit2 stash apply callbacks.

    Inherit from this class and override the callbacks that you want to use
    in your class, which you can then pass to stash apply or pop operations.
    """
    def stash_apply_progress(self, progress: StashApplyProgress) -> None:
        """
        Stash application progress notification function.

        `progress` is a StashApplyProgress constant.

        Raising an exception from this callback will abort the stash
        application.
        """
        ...

def git_clone_options(payload: Payload, opts: _CDataBase | None = None) -> AbstractContextManager[Payload]: ...
def git_fetch_options(payload: Payload, opts: _CDataBase | None = None) -> AbstractContextManager[Payload]: ...
def git_push_options(payload: Payload, opts: _CDataBase | None = None) -> AbstractContextManager[Payload]: ...
def git_remote_callbacks(payload: Payload) -> AbstractContextManager[Payload]: ...

_P = ParamSpec("_P")

def libgit2_callback(f: Callable[_P, int]) -> Callable[_P, int]: ...
def libgit2_callback_void(f: Callable[_P, None]) -> Callable[_P, None]: ...

_CredentialsFn: TypeAlias = Callable[[str | None, str | None, CredentialType], _Credentials]

def get_credentials(fn: _CredentialsFn, url: _CDataBase, username: _CDataBase, allowed: CredentialType) -> _CDataBase:
    """Call fn and return the credentials object."""
    ...
def git_checkout_options(
    callbacks: CheckoutCallbacks | None = None,
    strategy: CheckoutStrategy | None = None,
    directory: StrOrBytesPath | None = None,
    paths: _IntoStrArray = None,
) -> AbstractContextManager[Payload]: ...
def git_stash_apply_options(
    callbacks: StashApplyCallbacks | None = None,
    reinstate_index: bool = False,
    strategy: CheckoutStrategy | None = None,
    directory: StrOrBytesPath | None = None,
    paths: _IntoStrArray = None,
) -> AbstractContextManager[Payload]: ...
