from _typeshed import StrOrBytesPath, SupportsAllComparisons
from collections.abc import Callable

# This is intentionally duplicated and placed above the _pygit2
# star-import to workaround mypy issue #16972, so that consumers
# of the stubs see the correct, wrapped type for the name
# "Repository".
from .repository import Repository as Repository  # isort: skip

from . import enums
from ._build import __version__ as __version__
from ._pygit2 import *  # type: ignore[assignment]
from .blame import Blame as Blame, BlameHunk as BlameHunk
from .blob import BlobIO as BlobIO
from .callbacks import (
    CheckoutCallbacks as CheckoutCallbacks,
    Payload as Payload,
    RemoteCallbacks as RemoteCallbacks,
    StashApplyCallbacks as StashApplyCallbacks,
    get_credentials as get_credentials,
)
from .config import Config as Config
from .credentials import *
from .errors import Passthrough as Passthrough
from .filter import Filter as Filter
from .index import Index as Index, IndexEntry as IndexEntry
from .legacyenums import *
from .packbuilder import PackBuilder as PackBuilder
from .remotes import Remote as Remote
from .repository import Repository as Repository  # noqa: F811 # intentional workaround
from .settings import Settings
from .submodules import Submodule as Submodule

features: enums.Feature
LIBGIT2_VER: tuple[int, int, int]

def init_repository(
    path: StrOrBytesPath | None,
    bare: bool = False,
    flags: enums.RepositoryInitFlag = ...,
    mode: int | enums.RepositoryInitMode = ...,
    workdir_path: str | None = None,
    description: str | None = None,
    template_path: str | None = None,
    initial_head: str | None = None,
    origin_url: str | None = None,
) -> Repository:
    """
    Creates a new Git repository in the given *path*.

    If *bare* is True the repository will be bare, i.e. it will not have a
    working copy.

    The *flags* may be a combination of enums.RepositoryInitFlag constants:

    - BARE (overriden by the *bare* parameter)
    - NO_REINIT
    - NO_DOTGIT_DIR
    - MKDIR
    - MKPATH (set by default)
    - EXTERNAL_TEMPLATE

    The *mode* parameter may be any of the predefined modes in
    enums.RepositoryInitMode (SHARED_UMASK being the default), or a custom int.

    The *workdir_path*, *description*, *template_path*, *initial_head* and
    *origin_url* are all strings.

    See libgit2's documentation on git_repository_init_ext for further details.
    """
    ...
def clone_repository(
    url: str,
    path: str,
    bare: bool = False,
    repository: Callable[[str, bool], Repository] | None = None,
    remote: Callable[[Repository, str, str], Remote] | None = None,
    checkout_branch: str | None = None,
    callbacks: RemoteCallbacks | None = None,
    depth: int = 0,
) -> Repository:
    """
    Clones a new Git repository from *url* in the given *path*.

    Returns: a Repository class pointing to the newly cloned repository.

    Parameters:

    url : str
        URL of the repository to clone.
    path : str
        Local path to clone into.
    bare : bool
        Whether the local repository should be bare.
    remote : callable
        Callback for the remote to use.

        The remote callback has `(Repository, name, url) -> Remote` as a
        signature. The Remote it returns will be used instead of the default
        one.
    repository : callable
        Callback for the repository to use.

        The repository callback has `(path, bare) -> Repository` as a
        signature. The Repository it returns will be used instead of creating a
        new one.
    checkout_branch : str
        Branch to checkout after the clone. The default is to use the remote's
        default branch.
    callbacks : RemoteCallbacks
        Object which implements the callbacks as methods.

        The callbacks should be an object which inherits from
        `pyclass:RemoteCallbacks`.
    depth : int
        Number of commits to clone.

        If greater than 0, creates a shallow clone with a history truncated to
        the specified number of commits.
        The default is 0 (full commit history).
    """
    ...

tree_entry_key: Callable[[Object], SupportsAllComparisons]  # functools.cmp_to_key(tree_entry_cmp)
settings: Settings
