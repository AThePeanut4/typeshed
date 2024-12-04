from collections.abc import Iterator
from typing import Literal, TypedDict
from typing_extensions import TypeAlias

from _cffi_backend import _CDataBase

from ._pygit2 import Oid
from .callbacks import RemoteCallbacks
from .enums import FetchPrune
from .refspec import Refspec
from .repository import BaseRepository
from .utils import _IntoStrArray

class TransferProgress:
    """Progress downloading and indexing data during a fetch."""
    total_objects: int
    indexed_objects: int
    received_objects: int
    local_objects: int
    total_deltas: int
    indexed_deltas: int
    received_bytes: int
    def __init__(self, tp: _CDataBase) -> None: ...

_ProxySpec: TypeAlias = Literal[True] | str | None

class _LsRemotesResultEntry(TypedDict):
    local: bool
    loid: Oid | None
    name: str | None
    symref_target: str | None
    oid: Oid

class Remote:
    def __init__(self, repo: BaseRepository, ptr: _CDataBase) -> None:
        """The constructor is for internal use only."""
        ...
    def __del__(self) -> None: ...
    @property
    def name(self) -> str | None:
        """Name of the remote"""
        ...
    @property
    def url(self) -> str | None:
        """Url of the remote"""
        ...
    @property
    def push_url(self) -> str | None:
        """Push url of the remote"""
        ...
    def connect(self, callbacks: RemoteCallbacks | None = None, direction: int = 0, proxy: _ProxySpec = None) -> None:
        """
        Connect to the remote.

        Parameters:

        proxy : None or True or str
            Proxy configuration. Can be one of:

            * `None` (the default) to disable proxy usage
            * `True` to enable automatic proxy detection
            * an url to a proxy (`http://proxy.example.org:3128/`)
        """
        ...
    def fetch(
        self,
        refspecs: _IntoStrArray = None,
        message: bytes | str | None = None,
        callbacks: RemoteCallbacks | None = None,
        prune: FetchPrune = ...,
        proxy: _ProxySpec = None,
        depth: int = 0,
    ) -> TransferProgress:
        """
        Perform a fetch against this remote. Returns a <TransferProgress>
        object.

        Parameters:

        prune : enums.FetchPrune
            * `UNSPECIFIED`: use the configuration from the repository.
            * `PRUNE`: remove any remote branch in the local repository
               that does not exist in the remote.
            * `NO_PRUNE`: always keep the remote branches

        proxy : None or True or str
            Proxy configuration. Can be one of:

            * `None` (the default) to disable proxy usage
            * `True` to enable automatic proxy detection
            * an url to a proxy (`http://proxy.example.org:3128/`)

        depth : int
            Number of commits from the tip of each remote branch history to fetch.

            If non-zero, the number of commits from the tip of each remote
            branch history to fetch. If zero, all history is fetched.
            The default is 0 (all history is fetched).
        """
        ...
    def ls_remotes(self, callbacks: RemoteCallbacks | None = None, proxy: _ProxySpec = None) -> list[_LsRemotesResultEntry]:
        """
        Return a list of dicts that maps to `git_remote_head` from a
        `ls_remotes` call.

        Parameters:

        callbacks : Passed to connect()

        proxy : Passed to connect()
        """
        ...
    def prune(self, callbacks: RemoteCallbacks | None = None) -> None:
        """Perform a prune against this remote."""
        ...
    @property
    def refspec_count(self) -> int:
        """Total number of refspecs in this remote"""
        ...
    def get_refspec(self, n: int) -> Refspec:
        """Return the <Refspec> object at the given position."""
        ...
    @property
    def fetch_refspecs(self) -> list[str]:
        """Refspecs that will be used for fetching"""
        ...
    @property
    def push_refspecs(self) -> list[str]:
        """Refspecs that will be used for pushing"""
        ...
    def push(
        self,
        specs: _IntoStrArray,
        callbacks: RemoteCallbacks | None = None,
        proxy: _ProxySpec = None,
        push_options: _IntoStrArray | None = None,
    ) -> None:
        """
        Push the given refspec to the remote. Raises ``GitError`` on protocol
        error or unpack failure.

        When the remote has a githook installed, that denies the reference this
        function will return successfully. Thus it is strongly recommended to
        install a callback, that implements
        :py:meth:`RemoteCallbacks.push_update_reference` and check the passed
        parameters for successfull operations.

        Parameters:

        specs : [str]
            Push refspecs to use.

        proxy : None or True or str
            Proxy configuration. Can be one of:

            * `None` (the default) to disable proxy usage
            * `True` to enable automatic proxy detection
            * an url to a proxy (`http://proxy.example.org:3128/`)

        push_options : [str]
            Push options to send to the server, which passes them to the
            pre-receive as well as the post-receive hook.
        """
        ...

_RemoteName: TypeAlias = bytes | str

class RemoteCollection:
    """
    Collection of configured remotes

    You can use this class to look up and manage the remotes configured
    in a repository.  You can access repositories using index
    access. E.g. to look up the "origin" remote, you can use

    >>> repo.remotes["origin"]
    """
    def __init__(self, repo: BaseRepository) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Remote]: ...
    def __getitem__(self, name: int | _RemoteName) -> Remote: ...
    def names(self) -> Iterator[str | None]:
        """An iterator over the names of the available remotes."""
        ...
    def create(self, name: _RemoteName, url: bytes | str, fetch: bytes | str | None = None) -> Remote:
        """
        Create a new remote with the given name and url. Returns a <Remote>
        object.

        If 'fetch' is provided, this fetch refspec will be used instead of the
        default.
        """
        ...
    def create_anonymous(self, url: bytes | str) -> Remote:
        """
        Create a new anonymous (in-memory only) remote with the given URL.
        Returns a <Remote> object.
        """
        ...
    def rename(self, name: _RemoteName, new_name: bytes | str) -> list[str]:
        """
        Rename a remote in the configuration. The refspecs in standard
        format will be renamed.

        Returns a list of fetch refspecs (list of strings) which were not in
        the standard format and thus could not be remapped.
        """
        ...
    def delete(self, name: _RemoteName) -> None:
        """
        Remove a remote from the configuration

        All remote-tracking branches and configuration settings for the remote will be removed.
        """
        ...
    def set_url(self, name: _RemoteName, url: bytes | str) -> None:
        """Set the URL for a remote"""
        ...
    def set_push_url(self, name: _RemoteName, url: bytes | str) -> None:
        """Set the push-URL for a remote"""
        ...
    def add_fetch(self, name: _RemoteName, refspec: bytes | str) -> None:
        """Add a fetch refspec (str) to the remote"""
        ...
    def add_push(self, name: _RemoteName, refspec: bytes | str) -> None:
        """Add a push refspec (str) to the remote"""
        ...
