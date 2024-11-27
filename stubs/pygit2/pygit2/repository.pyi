from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterator
from tarfile import TarInfo
from typing import IO, Any, Protocol
from typing_extensions import TypeAlias

from ._pygit2 import Blob, Commit, Diff, Object, Oid, Reference, Repository as _Repository, Signature, Tree, _OidArg
from .blame import Blame
from .branches import Branches
from .callbacks import CheckoutCallbacks, StashApplyCallbacks
from .config import Config
from .enums import (
    AttrCheck,
    BlameFlag,
    BranchType as BranchType,
    CheckoutStrategy,
    DescribeStrategy,
    DiffOption,
    MergeFavor,
    MergeFileFlag,
    MergeFlag,
    RepositoryOpenFlag,
    RepositoryState,
)
from .index import Index, IndexEntry
from .packbuilder import PackBuilder
from .references import References
from .remotes import RemoteCollection
from .submodules import SubmoduleCollection
from .utils import _IntoStrArray

_PackDelegate: TypeAlias = Callable[[PackBuilder], None]

class _SupportsAddfile(Protocol):
    def addfile(self, tarinfo: TarInfo, fileobj: IO[bytes] | None = None) -> None: ...

class BaseRepository(_Repository):
    branches: Branches
    references: References
    remotes: RemoteCollection
    submodules: SubmoduleCollection

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...  # not meant for direct use
    def read(self, oid: _OidArg) -> tuple[int, int, bytes]:
        """
        read(oid) -> type, data, size

        Read raw object data from the repository.
        """
        ...
    def write(self, type: int, data: bytes) -> Oid:
        """
        write(type, data) -> Oid

        Write raw object data into the repository. First arg is the object
        type, the second one a buffer with data. Return the Oid of the created
        object.
        """
        ...
    def pack(
        self, path: StrOrBytesPath | None = None, pack_delegate: _PackDelegate | None = None, n_threads: int | None = None
    ) -> int:
        """
        Pack the objects in the odb chosen by the pack_delegate function
        and write `.pack` and `.idx` files for them.

        Returns: the number of objects written to the pack

        Parameters:

        path
            The path to which the `.pack` and `.idx` files should be written. `None` will write to the default location.

        pack_delegate
            The method which will provide add the objects to the pack builder. Defaults to all objects.

        n_threads
            The number of threads the `PackBuilder` will spawn. If set to 0, libgit2 will autodetect the number of CPUs.
        """
        ...
    def __iter__(self) -> Iterator[Oid]: ...
    def get(self, key: _OidArg, default: Object | None = None) -> Object | None: ...
    def __getitem__(self, key: _OidArg) -> Object: ...
    def __contains__(self, key: _OidArg) -> bool: ...
    @property
    def config(self) -> Config:
        """
        The configuration file for this repository.

        If a the configuration hasn't been set yet, the default config for
        repository will be returned, including global and system configurations
        (if they are available).
        """
        ...
    @property
    def config_snapshot(self) -> Config:
        """
        A snapshot for this repositiory's configuration

        This allows reads over multiple values to use the same version
        of the configuration files.
        """
        ...
    def create_reference(self, name: str, target: _OidArg, force: bool = False, message: str | None = None) -> Reference:
        """
        Create a new reference "name" which points to an object or to
        another reference.

        Based on the type and value of the target parameter, this method tries
        to guess whether it is a direct or a symbolic reference.

        Keyword arguments:

        force: bool
            If True references will be overridden, otherwise (the default) an
            exception is raised.

        message: str
            Optional message to use for the reflog.

        Examples::

            repo.create_reference('refs/heads/foo', repo.head.target)
            repo.create_reference('refs/tags/foo', 'refs/heads/master')
            repo.create_reference('refs/tags/foo', 'bbb78a9cec580')
        """
        ...
    def listall_references(self) -> list[str]:
        """Return a list with all the references in the repository."""
        ...
    def listall_reference_objects(self) -> list[Reference]:
        """Return a list with all the reference objects in the repository."""
        ...
    def resolve_refish(self, refish: str) -> tuple[Commit, Reference]:
        """
        Convert a reference-like short name "ref-ish" to a valid
        (commit, reference) pair.

        If ref-ish points to a commit, the reference element of the result
        will be None.

        Examples::

            repo.resolve_refish('mybranch')
            repo.resolve_refish('sometag')
            repo.resolve_refish('origin/master')
            repo.resolve_refish('bbb78a9')
        """
        ...
    def checkout_head(
        self,
        *,
        callbacks: CheckoutCallbacks | None = None,
        strategy: CheckoutStrategy | None = None,
        directory: str | None = None,
        paths: _IntoStrArray = None,
    ) -> None:
        """
        Checkout HEAD

        For arguments, see Repository.checkout().
        """
        ...
    def checkout_index(
        self,
        index: Index | None = None,
        *,
        callbacks: CheckoutCallbacks | None = None,
        strategy: CheckoutStrategy | None = None,
        directory: str | None = None,
        paths: _IntoStrArray = None,
    ) -> None:
        """
        Checkout the given index or the repository's index

        For arguments, see Repository.checkout().
        """
        ...
    def checkout_tree(
        self,
        treeish: Object,
        *,
        callbacks: CheckoutCallbacks | None = None,
        strategy: CheckoutStrategy | None = None,
        directory: str | None = None,
        paths: _IntoStrArray = None,
    ) -> None:
        """
        Checkout the given treeish

        For arguments, see Repository.checkout().
        """
        ...
    def checkout(
        self,
        refname: str | Reference | None = None,
        *,
        callbacks: CheckoutCallbacks | None = None,
        strategy: CheckoutStrategy | None = None,
        directory: str | None = None,
        paths: _IntoStrArray = None,
    ) -> None:
        """
        Checkout the given reference using the given strategy, and update the
        HEAD.
        The reference may be a reference name or a Reference object.
        The default strategy is SAFE | RECREATE_MISSING.

        If no reference is given, checkout from the index.

        Parameters:

        refname : str or Reference
            The reference to checkout. After checkout, the current branch will
            be switched to this one.

        strategy : CheckoutStrategy
            A ``CheckoutStrategy`` value. The default is ``SAFE | RECREATE_MISSING``.

        directory : str
            Alternative checkout path to workdir.

        paths : list[str]
            A list of files to checkout from the given reference.
            If paths is provided, HEAD will not be set to the reference.

        callbacks : CheckoutCallbacks
            Optional. Supply a `callbacks` object to get information about
            conflicted files, updated files, etc. as the checkout is being
            performed. The callbacks can also abort the checkout prematurely.

            The callbacks should be an object which inherits from
            `pyclass:CheckoutCallbacks`. It should implement the callbacks
            as overridden methods.

        Examples:

        * To checkout from the HEAD, just pass 'HEAD'::

            >>> checkout('HEAD')

          This is identical to calling checkout_head().
        """
        ...
    def set_head(self, target: _OidArg) -> None:
        """
        Set HEAD to point to the given target.

        Parameters:

        target
            The new target for HEAD. Can be a string or Oid (to detach).
        """
        ...
    def diff(
        self,
        a: bytes | str | Oid | Blob | Tree | None = None,
        b: bytes | str | Oid | Blob | Tree | None = None,
        cached: bool = False,
        flags: DiffOption = ...,
        context_lines: int = 3,
        interhunk_lines: int = 0,
    ) -> Diff:
        """
        Show changes between the working tree and the index or a tree,
        changes between the index and a tree, changes between two trees, or
        changes between two blobs.

        Keyword arguments:

        a
            None, a str (that refers to an Object, see revparse_single()) or a
            Reference object.
            If None, b must be None, too. In this case the working directory is
            compared with the index. Otherwise the referred object is compared to
            'b'.

        b
            None, a str (that refers to an Object, see revparse_single()) or a
            Reference object.
            If None, the working directory is compared to 'a'. (except
            'cached' is True, in which case the index is compared to 'a').
            Otherwise the referred object is compared to 'a'

        cached
            If 'b' is None, by default the working directory is compared to 'a'.
            If 'cached' is set to True, the index/staging area is used for comparing.

        flag
            A combination of enums.DiffOption constants.

        context_lines
            The number of unchanged lines that define the boundary of a hunk
            (and to display before and after)

        interhunk_lines
            The maximum number of unchanged lines between hunk boundaries
            before the hunks will be merged into a one

        Examples::

          # Changes in the working tree not yet staged for the next commit
          >>> diff()

          # Changes between the index and your last commit
          >>> diff(cached=True)

          # Changes in the working tree since your last commit
          >>> diff('HEAD')

          # Changes between commits
          >>> t0 = revparse_single('HEAD')
          >>> t1 = revparse_single('HEAD^')
          >>> diff(t0, t1)
          >>> diff('HEAD', 'HEAD^') # equivalent

        If you want to diff a tree against an empty tree, use the low level
        API (Tree.diff_to_tree()) directly.
        """
        ...
    def state(self) -> RepositoryState:
        """
        Determines the state of a git repository - ie, whether an operation
        (merge, cherry-pick, etc) is in progress.

        Returns a RepositoryState constant.
        """
        ...
    def state_cleanup(self) -> None:
        """
        Remove all the metadata associated with an ongoing command like
        merge, revert, cherry-pick, etc. For example: MERGE_HEAD, MERGE_MSG,
        etc.
        """
        ...
    def blame(
        self,
        path: StrOrBytesPath,
        flags: BlameFlag = ...,
        min_match_characters: int | None = None,
        newest_commit: _OidArg | None = None,
        oldest_commit: _OidArg | None = None,
        min_line: int | None = None,
        max_line: int | None = None,
    ) -> Blame:
        """
        Return a Blame object for a single file.

        Parameters:

        path
            Path to the file to blame.

        flags
            An enums.BlameFlag constant.

        min_match_characters
            The number of alphanum chars that must be detected as moving/copying
            within a file for it to associate those lines with the parent commit.

        newest_commit
            The id of the newest commit to consider.

        oldest_commit
            The id of the oldest commit to consider.

        min_line
            The first line in the file to blame.

        max_line
            The last line in the file to blame.

        Examples::

            repo.blame('foo.c', flags=enums.BlameFlag.IGNORE_WHITESPACE)
        """
        ...
    @property
    def index(self) -> Index:
        """Index representing the repository's index file."""
        ...
    def merge_file_from_index(self, ancestor: IndexEntry | None, ours: IndexEntry | None, theirs: IndexEntry | None) -> str:
        """
        Merge files from index. Return a string with the merge result
        containing possible conflicts.

        ancestor
            The index entry which will be used as a common
            ancestor.
        ours
            The index entry to take as "ours" or base.
        theirs
            The index entry which will be merged into "ours"
        """
        ...
    def merge_commits(
        self,
        ours: str | Oid | Commit,
        theirs: str | Oid | Commit,
        favor: MergeFavor = ...,
        flags: MergeFlag = ...,
        file_flags: MergeFileFlag = ...,
    ) -> Index:
        """
        Merge two arbitrary commits.

        Returns: an index with the result of the merge.

        Parameters:

        ours
            The commit to take as "ours" or base.

        theirs
            The commit which will be merged into "ours"

        favor
            An enums.MergeFavor constant specifying how to deal with file-level conflicts.
            For all but NORMAL, the index will not record a conflict.

        flags
            A combination of enums.MergeFlag constants.

        file_flags
            A combination of enums.MergeFileFlag constants.

        Both "ours" and "theirs" can be any object which peels to a commit or
        the id (string or Oid) of an object which peels to a commit.
        """
        ...
    def merge_trees(
        self,
        ancestor: str | Oid | Tree,
        ours: str | Oid | Tree,
        theirs: str | Oid | Tree,
        favor: MergeFavor = ...,
        flags: MergeFlag = ...,
        file_flags: MergeFileFlag = ...,
    ) -> Index:
        """
        Merge two trees.

        Returns: an Index that reflects the result of the merge.

        Parameters:

        ancestor
            The tree which is the common ancestor between 'ours' and 'theirs'.

        ours
            The commit to take as "ours" or base.

        theirs
            The commit which will be merged into "ours".

        favor
            An enums.MergeFavor constant specifying how to deal with file-level conflicts.
            For all but NORMAL, the index will not record a conflict.

        flags
            A combination of enums.MergeFlag constants.

        file_flags
            A combination of enums.MergeFileFlag constants.
        """
        ...
    def merge(self, id: Oid | str, favor: MergeFavor = ..., flags: MergeFlag = ..., file_flags: MergeFileFlag = ...) -> None:
        """
        Merges the given id into HEAD.

        Merges the given commit(s) into HEAD, writing the results into the working directory.
        Any changes are staged for commit and any conflicts are written to the index.
        Callers should inspect the repository's index after this completes,
        resolve any conflicts and prepare a commit.

        Parameters:

        id
            The id to merge into HEAD

        favor
            An enums.MergeFavor constant specifying how to deal with file-level conflicts.
            For all but NORMAL, the index will not record a conflict.

        flags
            A combination of enums.MergeFlag constants.

        file_flags
            A combination of enums.MergeFileFlag constants.
        """
        ...
    @property
    def raw_message(self) -> bytes:
        """
        Retrieve git's prepared message (bytes).
        See `Repository.message` for more information.
        """
        ...
    @property
    def message(self) -> str:
        """
        Retrieve git's prepared message.

        Operations such as git revert/cherry-pick/merge with the -n option stop
        just short of creating a commit with the changes and save their
        prepared message in .git/MERGE_MSG so the next git-commit execution can
        present it to the user for them to amend if they wish.

        Use this function to get the contents of this file. Don't forget to
        call `Repository.remove_message()` after you create the commit.

        Note that the message is also removed by `Repository.state_cleanup()`.

        If there is no such message, an empty string is returned.
        """
        ...
    def remove_message(self) -> None:
        """Remove git's prepared message."""
        ...
    def describe(
        self,
        committish: str | Reference | Commit | None = None,
        max_candidates_tags: int | None = None,
        describe_strategy: DescribeStrategy = ...,
        pattern: str | None = None,
        only_follow_first_parent: bool | None = None,
        show_commit_oid_as_fallback: bool | None = None,
        abbreviated_size: int | None = None,
        always_use_long_format: bool | None = None,
        dirty_suffix: str | None = None,
    ) -> str:
        """
        Describe a commit-ish or the current working tree.

        Returns: The description (str).

        Parameters:

        committish : `str`, :class:`~.Reference`, or :class:`~.Commit`
            Commit-ish object or object name to describe, or `None` to describe
            the current working tree.

        max_candidates_tags : int
            The number of candidate tags to consider. Increasing above 10 will
            take slightly longer but may produce a more accurate result. A
            value of 0 will cause only exact matches to be output.

        describe_strategy : DescribeStrategy
            Can be one of:

            * `DescribeStrategy.DEFAULT` - Only match annotated tags.
            * `DescribeStrategy.TAGS` - Match everything under refs/tags/
              (includes lightweight tags).
            * `DescribeStrategy.ALL` - Match everything under refs/ (includes
              branches).

        pattern : str
            Only consider tags matching the given `glob(7)` pattern, excluding
            the "refs/tags/" prefix.

        only_follow_first_parent : bool
            Follow only the first parent commit upon seeing a merge commit.

        show_commit_oid_as_fallback : bool
            Show uniquely abbreviated commit object as fallback.

        abbreviated_size : int
            The minimum number of hexadecimal digits to show for abbreviated
            object names. A value of 0 will suppress long format, only showing
            the closest tag.

        always_use_long_format : bool
            Always output the long format (the nearest tag, the number of
            commits, and the abbrevated commit name) even when the committish
            matches a tag.

        dirty_suffix : str
            A string to append if the working tree is dirty.

        Example::

            repo.describe(pattern='public/*', dirty_suffix='-dirty')
        """
        ...
    def stash(
        self,
        stasher: Signature,
        message: str | None = None,
        keep_index: bool = False,
        include_untracked: bool = False,
        include_ignored: bool = False,
        keep_all: bool = False,
        paths: list[str] | None = None,
    ) -> Oid:
        """
        Save changes to the working directory to the stash.

        Returns: The Oid of the stash merge commit (Oid).

        Parameters:

        stasher : Signature
            The identity of the person doing the stashing.

        message : str
            An optional description of stashed state.

        keep_index : bool
            Leave changes already added to the index in the working directory.

        include_untracked : bool
            Also stash untracked files.

        include_ignored : bool
            Also stash ignored files.

        keep_all : bool
            All changes in the index and working directory are left intact.

        paths : list[str]
            An optional list of paths that control which files are stashed.

        Example::

            >>> repo = pygit2.Repository('.')
            >>> repo.stash(repo.default_signature(), 'WIP: stashing')
        """
        ...
    def stash_apply(
        self,
        index: int = 0,
        *,
        callbacks: StashApplyCallbacks | None = None,
        reinstate_index: bool = False,
        strategy: CheckoutStrategy | None = None,
        directory: str | None = None,
        paths: _IntoStrArray = None,
    ) -> None:
        """
        Apply a stashed state in the stash list to the working directory.

        Parameters:

        index : int
            The position within the stash list of the stash to apply. 0 is the
            most recent stash.

        reinstate_index : bool
            Try to reinstate stashed changes to the index.

        callbacks : StashApplyCallbacks
            Optional. Supply a `callbacks` object to get information about
            the progress of the stash application as it is being performed.

            The callbacks should be an object which inherits from
            `pyclass:StashApplyCallbacks`. It should implement the callbacks
            as overridden methods.

            Note that this class inherits from CheckoutCallbacks, so you can
            also get information from the checkout part of the unstashing
            process via the callbacks.

        The checkout options may be customized using the same arguments taken by
        Repository.checkout().

        Example::

            >>> repo = pygit2.Repository('.')
            >>> repo.stash(repo.default_signature(), 'WIP: stashing')
            >>> repo.stash_apply(strategy=CheckoutStrategy.ALLOW_CONFLICTS)
        """
        ...
    def stash_drop(self, index: int = 0) -> None:
        """
        Remove a stashed state from the stash list.

        Parameters:

        index : int
            The position within the stash list of the stash to remove. 0 is
            the most recent stash.
        """
        ...
    def stash_pop(
        self,
        index: int = 0,
        *,
        callbacks: StashApplyCallbacks | None = None,
        reinstate_index: bool = False,
        strategy: CheckoutStrategy | None = None,
        directory: str | None = None,
        paths: _IntoStrArray = None,
    ) -> None:
        """
        Apply a stashed state and remove it from the stash list.

        For arguments, see Repository.stash_apply().
        """
        ...
    def write_archive(
        self, treeish: _OidArg | Tree, archive: _SupportsAddfile, timestamp: int | None = None, prefix: str = ""
    ) -> None:
        """
        Write treeish into an archive.

        If no timestamp is provided and 'treeish' is a commit, its committer
        timestamp will be used. Otherwise the current time will be used.

        All path names in the archive are added to 'prefix', which defaults to
        an empty string.

        Parameters:

        treeish
            The treeish to write.

        archive
            An archive from the 'tarfile' module.

        timestamp
            Timestamp to use for the files in the archive.

        prefix
            Extra prefix to add to the path names in the archive.

        Example::

            >>> import tarfile, pygit2
            >>> with tarfile.open('foo.tar', 'w') as archive:
            >>>     repo = pygit2.Repository('.')
            >>>     repo.write_archive(repo.head.target, archive)
        """
        ...
    def ahead_behind(self, local: _OidArg, upstream: _OidArg) -> tuple[int, int]:
        """
        Calculate how many different commits are in the non-common parts of the
        history between the two given ids.

        Ahead is how many commits are in the ancestry of the `local` commit
        which are not in the `upstream` commit. Behind is the opposite.

        Returns: a tuple of two integers with the number of commits ahead and
        behind respectively.

        Parameters:

        local
            The commit which is considered the local or current state.

        upstream
            The commit which is considered the upstream.
        """
        ...
    def get_attr(
        self, path: StrOrBytesPath, name: str | bytes, flags: AttrCheck = ..., commit: Oid | str | None = None
    ) -> bool | None | str:
        """
        Retrieve an attribute for a file by path.

        Returns: a boolean, `None` if the value is unspecified, or string with
        the value of the attribute.

        Parameters:

        path
            The path of the file to look up attributes for, relative to the
            workdir root.

        name
            The name of the attribute to look up.

        flags
            A combination of enums.AttrCheck flags which determine the lookup order.

        commit
            Optional id of commit to load attributes from when the
            `INCLUDE_COMMIT` flag is specified.

        Examples::

            >>> print(repo.get_attr('splash.bmp', 'binary'))
            True
            >>> print(repo.get_attr('splash.bmp', 'unknown-attr'))
            None
            >>> repo.get_attr('test.h', 'whitespace')
            'tab-in-indent,trailing-space'
        """
        ...
    @property
    def ident(self) -> tuple[str, str]: ...
    def set_ident(self, name: bytes | str | None, email: bytes | str | None) -> None:
        """
        Set the identity to be used for reference operations.

        Updates to some references also append data to their
        reflog. You can use this method to set what identity will be
        used. If none is set, it will be read from the configuration.
        """
        ...
    def revert(self, commit: Commit) -> None:
        """
        Revert the given commit, producing changes in the index and working
        directory.

        This operation updates the repository's state and prepared message
        (MERGE_MSG).
        """
        ...
    def revert_commit(self, revert_commit: Commit, our_commit: Commit, mainline: int = 0) -> Index:
        """
        Revert the given Commit against the given "our" Commit, producing an
        Index that reflects the result of the revert.

        Returns: an Index with the result of the revert.

        Parameters:

        revert_commit
            The Commit to revert.

        our_commit
            The Commit to revert against (eg, HEAD).

        mainline
            The parent of the revert Commit, if it is a merge (i.e. 1, 2).
        """
        ...
    def amend_commit(
        self,
        commit: Commit | _OidArg,
        refname: Reference | str | None,
        author: Signature | None = None,
        committer: Signature | None = None,
        message: bytes | str | None = None,
        tree: Tree | _OidArg | None = None,
        encoding: str = "UTF-8",
    ) -> Oid:
        """
        Amend an existing commit by replacing only explicitly passed values,
        return the rewritten commit's oid.

        This creates a new commit that is exactly the same as the old commit,
        except that any explicitly passed values will be updated. The new
        commit has the same parents as the old commit.

        You may omit the `author`, `committer`, `message`, `tree`, and
        `encoding` parameters, in which case this will use the values
        from the original `commit`.

        Parameters:

        commit : Commit, Oid, or str
            The commit to amend.

        refname : Reference or str
            If not `None`, name of the reference that will be updated to point
            to the newly rewritten commit. Use "HEAD" to update the HEAD of the
            current branch and make it point to the rewritten commit.
            If you want to amend a commit that is not currently the tip of the
            branch and then rewrite the following commits to reach a ref, pass
            this as `None` and update the rest of the commit chain and ref
            separately.

        author : Signature
            If not None, replace the old commit's author signature with this
            one.

        committer : Signature
            If not None, replace the old commit's committer signature with this
            one.

        message : str
            If not None, replace the old commit's message with this one.

        tree : Tree, Oid, or str
            If not None, replace the old commit's tree with this one.

        encoding : str
            Optional encoding for `message`.
        """
        ...

class Repository(BaseRepository):
    def __init__(self, path: str | None = None, flags: RepositoryOpenFlag = ...) -> None:
        """
        The Repository constructor will commonly be called with one argument,
        the path of the repository to open.

        Alternatively, constructing a repository with no arguments will create
        a repository with no backends. You can use this path to create
        repositories with custom backends. Note that most operations on the
        repository are considered invalid and may lead to undefined behavior if
        attempted before providing an odb and refdb via set_odb and set_refdb.

        Parameters:

        path : str
        The path to open - if not provided, the repository will have no backend.

        flags : enums.RepositoryOpenFlag
        An optional combination of enums.RepositoryOpenFlag constants
        controlling how to open the repository.
        """
        ...
