from collections.abc import Iterable, Iterator

from ._pygit2 import Oid
from .callbacks import RemoteCallbacks
from .enums import SubmoduleIgnore, SubmoduleStatus
from .repository import BaseRepository, Repository

class Submodule:
    def __del__(self) -> None: ...
    def open(self) -> Repository:
        """Open the repository for a submodule."""
        ...
    def init(self, overwrite: bool = False) -> None:
        """
        Just like "git submodule init", this copies information about the submodule
        into ".git/config".

        Parameters:

        overwrite
            By default, existing submodule entries will not be overwritten,
            but setting this to True forces them to be updated.
        """
        ...
    def update(self, init: bool = False, callbacks: RemoteCallbacks | None = None, depth: int = 0) -> None:
        """
        Update a submodule. This will clone a missing submodule and checkout
        the subrepository to the commit specified in the index of the
        containing repository. If the submodule repository doesn't contain the
        target commit (e.g. because fetchRecurseSubmodules isn't set), then the
        submodule is fetched using the fetch options supplied in options.

        Parameters:

        init
            If the submodule is not initialized, setting this flag to True will
            initialize the submodule before updating. Otherwise, this will raise
            an error if attempting to update an uninitialized repository.

        callbacks
            Optional RemoteCallbacks to clone or fetch the submodule.

        depth
            Number of commits to fetch.
            The default is 0 (full commit history).
        """
        ...
    def reload(self, force: bool = False) -> None:
        """
        Reread submodule info from config, index, and HEAD.

        Call this to reread cached submodule information for this submodule if
        you have reason to believe that it has changed.

        Parameters:

        force
            Force reload even if the data doesn't seem out of date
        """
        ...
    @property
    def name(self) -> str:
        """Name of the submodule."""
        ...
    @property
    def path(self) -> str:
        """Path of the submodule."""
        ...
    @property
    def url(self) -> str | None:
        """URL of the submodule."""
        ...
    @property
    def branch(self) -> str:
        """Branch that is to be tracked by the submodule."""
        ...
    @property
    def head_id(self) -> Oid | None:
        """
        The submodule's HEAD commit id (as recorded in the superproject's
        current HEAD tree).
        Returns None if the superproject's HEAD doesn't contain the submodule.
        """
        ...

class SubmoduleCollection:
    """Collection of submodules in a repository."""
    def __init__(self, repository: BaseRepository) -> None: ...
    def __getitem__(self, name: str) -> Submodule:
        """
        Look up submodule information by name or path.
        Raises KeyError if there is no such submodule.
        """
        ...
    def __contains__(self, name: str) -> bool: ...
    def __iter__(self) -> Iterator[Submodule]: ...
    def get(self, name: str) -> Submodule | None:
        """
        Look up submodule information by name or path.
        Unlike __getitem__, this returns None if the submodule is not found.
        """
        ...
    def add(
        self, url: str, path: str, link: bool = True, callbacks: RemoteCallbacks | None = None, depth: int = 0
    ) -> Submodule:
        """
        Add a submodule to the index.
        The submodule is automatically cloned.

        Returns: the submodule that was added.

        Parameters:

        url
            The URL of the submodule.

        path
            The path within the parent repository to add the submodule

        link
            Should workdir contain a gitlink to the repo in `.git/modules` vs. repo directly in workdir.

        callbacks
            Optional RemoteCallbacks to clone the submodule.

        depth
            Number of commits to fetch.
            The default is 0 (full commit history).
        """
        ...
    def init(self, submodules: Iterable[str] | None = None, overwrite: bool = False) -> None:
        """
        Initialize submodules in the repository. Just like "git submodule init",
        this copies information about the submodules into ".git/config".

        Parameters:

        submodules
            Optional list of submodule paths or names to initialize.
            Default argument initializes all submodules.

        overwrite
            Flag indicating if initialization should overwrite submodule entries.
        """
        ...
    def update(
        self,
        submodules: Iterable[str] | None = None,
        init: bool = False,
        callbacks: RemoteCallbacks | None = None,
        depth: int = 0,
    ) -> None:
        """
        Update submodules. This will clone a missing submodule and checkout
        the subrepository to the commit specified in the index of the
        containing repository. If the submodule repository doesn't contain the
        target commit (e.g. because fetchRecurseSubmodules isn't set), then the
        submodule is fetched using the fetch options supplied in options.

        Parameters:

        submodules
            Optional list of submodule paths or names. If you omit this parameter
            or pass None, all submodules will be updated.

        init
            If the submodule is not initialized, setting this flag to True will
            initialize the submodule before updating. Otherwise, this will raise
            an error if attempting to update an uninitialized repository.

        callbacks
            Optional RemoteCallbacks to clone or fetch the submodule.

        depth
            Number of commits to fetch.
            The default is 0 (full commit history).
        """
        ...
    def status(self, name: str, ignore: SubmoduleIgnore = ...) -> SubmoduleStatus:
        """
        Get the status of a submodule.

        Returns: A combination of SubmoduleStatus flags.

        Parameters:

        name
            Submodule name or path.

        ignore
            A SubmoduleIgnore value indicating how deeply to examine the working directory.
        """
        ...
    def cache_all(self) -> None:
        """
        Load and cache all submodules in the repository.

        Because the `.gitmodules` file is unstructured, loading submodules is an
        O(N) operation.  Any operation that requires accessing all submodules is O(N^2)
        in the number of submodules, if it has to look each one up individually.
        This function loads all submodules and caches them so that subsequent
        submodule lookups by name are O(1).
        """
        ...
    def cache_clear(self) -> None:
        """
        Clear the submodule cache populated by `submodule_cache_all`.
        If there is no cache, do nothing.

        The cache incorporates data from the repository's configuration, as well
        as the state of the working tree, the index, and HEAD. So any time any
        of these has changed, the cache might become invalid.
        """
        ...
