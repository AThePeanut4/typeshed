"""Python bindings for libgit2."""

from _typeshed import StrOrBytesPath
from collections.abc import Iterator
from io import IOBase
from typing import Any, Literal, final, overload
from typing_extensions import TypeAlias

from . import Index
from .enums import (
    ApplyLocation,
    BranchType,
    DiffFind,
    DiffFlag,
    DiffOption,
    DiffStatsFormat,
    FileMode,
    FileStatus,
    MergeAnalysis,
    MergePreference,
    ObjectType,
    Option,
    ReferenceFilter,
    ReferenceType,
    ResetMode,
    SortMode,
)
from .filter import Filter

GIT_APPLY_LOCATION_BOTH: int
GIT_APPLY_LOCATION_INDEX: int
GIT_APPLY_LOCATION_WORKDIR: int
GIT_BLAME_FIRST_PARENT: int
GIT_BLAME_IGNORE_WHITESPACE: int
GIT_BLAME_NORMAL: int
GIT_BLAME_TRACK_COPIES_ANY_COMMIT_COPIES: int
GIT_BLAME_TRACK_COPIES_SAME_COMMIT_COPIES: int
GIT_BLAME_TRACK_COPIES_SAME_COMMIT_MOVES: int
GIT_BLAME_TRACK_COPIES_SAME_FILE: int
GIT_BLAME_USE_MAILMAP: int
GIT_BLOB_FILTER_ATTRIBUTES_FROM_COMMIT: int
GIT_BLOB_FILTER_ATTRIBUTES_FROM_HEAD: int
GIT_BLOB_FILTER_CHECK_FOR_BINARY: int
GIT_BLOB_FILTER_NO_SYSTEM_ATTRIBUTES: int
GIT_BRANCH_ALL: int
GIT_BRANCH_LOCAL: int
GIT_BRANCH_REMOTE: int
GIT_CHECKOUT_ALLOW_CONFLICTS: int
GIT_CHECKOUT_CONFLICT_STYLE_DIFF3: int
GIT_CHECKOUT_CONFLICT_STYLE_MERGE: int
GIT_CHECKOUT_CONFLICT_STYLE_ZDIFF3: int
GIT_CHECKOUT_DISABLE_PATHSPEC_MATCH: int
GIT_CHECKOUT_DONT_OVERWRITE_IGNORED: int
GIT_CHECKOUT_DONT_REMOVE_EXISTING: int
GIT_CHECKOUT_DONT_UPDATE_INDEX: int
GIT_CHECKOUT_DONT_WRITE_INDEX: int
GIT_CHECKOUT_DRY_RUN: int
GIT_CHECKOUT_FORCE: int
GIT_CHECKOUT_NONE: int
GIT_CHECKOUT_NO_REFRESH: int
GIT_CHECKOUT_RECREATE_MISSING: int
GIT_CHECKOUT_REMOVE_IGNORED: int
GIT_CHECKOUT_REMOVE_UNTRACKED: int
GIT_CHECKOUT_SAFE: int
GIT_CHECKOUT_SKIP_LOCKED_DIRECTORIES: int
GIT_CHECKOUT_SKIP_UNMERGED: int
GIT_CHECKOUT_UPDATE_ONLY: int
GIT_CHECKOUT_USE_OURS: int
GIT_CHECKOUT_USE_THEIRS: int
GIT_CONFIG_HIGHEST_LEVEL: int
GIT_CONFIG_LEVEL_APP: int
GIT_CONFIG_LEVEL_WORKTREE: int
GIT_CONFIG_LEVEL_GLOBAL: int
GIT_CONFIG_LEVEL_LOCAL: int
GIT_CONFIG_LEVEL_PROGRAMDATA: int
GIT_CONFIG_LEVEL_SYSTEM: int
GIT_CONFIG_LEVEL_XDG: int
GIT_DELTA_ADDED: int
GIT_DELTA_CONFLICTED: int
GIT_DELTA_COPIED: int
GIT_DELTA_DELETED: int
GIT_DELTA_IGNORED: int
GIT_DELTA_MODIFIED: int
GIT_DELTA_RENAMED: int
GIT_DELTA_TYPECHANGE: int
GIT_DELTA_UNMODIFIED: int
GIT_DELTA_UNREADABLE: int
GIT_DELTA_UNTRACKED: int
GIT_DESCRIBE_ALL: int
GIT_DESCRIBE_DEFAULT: int
GIT_DESCRIBE_TAGS: int
GIT_DIFF_BREAK_REWRITES: int
GIT_DIFF_BREAK_REWRITES_FOR_RENAMES_ONLY: int
GIT_DIFF_DISABLE_PATHSPEC_MATCH: int
GIT_DIFF_ENABLE_FAST_UNTRACKED_DIRS: int
GIT_DIFF_FIND_ALL: int
GIT_DIFF_FIND_AND_BREAK_REWRITES: int
GIT_DIFF_FIND_BY_CONFIG: int
GIT_DIFF_FIND_COPIES: int
GIT_DIFF_FIND_COPIES_FROM_UNMODIFIED: int
GIT_DIFF_FIND_DONT_IGNORE_WHITESPACE: int
GIT_DIFF_FIND_EXACT_MATCH_ONLY: int
GIT_DIFF_FIND_FOR_UNTRACKED: int
GIT_DIFF_FIND_IGNORE_LEADING_WHITESPACE: int
GIT_DIFF_FIND_IGNORE_WHITESPACE: int
GIT_DIFF_FIND_REMOVE_UNMODIFIED: int
GIT_DIFF_FIND_RENAMES: int
GIT_DIFF_FIND_RENAMES_FROM_REWRITES: int
GIT_DIFF_FIND_REWRITES: int
GIT_DIFF_FLAG_BINARY: int
GIT_DIFF_FLAG_EXISTS: int
GIT_DIFF_FLAG_NOT_BINARY: int
GIT_DIFF_FLAG_VALID_ID: int
GIT_DIFF_FLAG_VALID_SIZE: int
GIT_DIFF_FORCE_BINARY: int
GIT_DIFF_FORCE_TEXT: int
GIT_DIFF_IGNORE_BLANK_LINES: int
GIT_DIFF_IGNORE_CASE: int
GIT_DIFF_IGNORE_FILEMODE: int
GIT_DIFF_IGNORE_SUBMODULES: int
GIT_DIFF_IGNORE_WHITESPACE: int
GIT_DIFF_IGNORE_WHITESPACE_CHANGE: int
GIT_DIFF_IGNORE_WHITESPACE_EOL: int
GIT_DIFF_INCLUDE_CASECHANGE: int
GIT_DIFF_INCLUDE_IGNORED: int
GIT_DIFF_INCLUDE_TYPECHANGE: int
GIT_DIFF_INCLUDE_TYPECHANGE_TREES: int
GIT_DIFF_INCLUDE_UNMODIFIED: int
GIT_DIFF_INCLUDE_UNREADABLE: int
GIT_DIFF_INCLUDE_UNREADABLE_AS_UNTRACKED: int
GIT_DIFF_INCLUDE_UNTRACKED: int
GIT_DIFF_INDENT_HEURISTIC: int
GIT_DIFF_MINIMAL: int
GIT_DIFF_NORMAL: int
GIT_DIFF_PATIENCE: int
GIT_DIFF_RECURSE_IGNORED_DIRS: int
GIT_DIFF_RECURSE_UNTRACKED_DIRS: int
GIT_DIFF_REVERSE: int
GIT_DIFF_SHOW_BINARY: int
GIT_DIFF_SHOW_UNMODIFIED: int
GIT_DIFF_SHOW_UNTRACKED_CONTENT: int
GIT_DIFF_SKIP_BINARY_CHECK: int
GIT_DIFF_STATS_FULL: int
GIT_DIFF_STATS_INCLUDE_SUMMARY: int
GIT_DIFF_STATS_NONE: int
GIT_DIFF_STATS_NUMBER: int
GIT_DIFF_STATS_SHORT: int
GIT_DIFF_UPDATE_INDEX: int
GIT_FILEMODE_BLOB: int
GIT_FILEMODE_BLOB_EXECUTABLE: int
GIT_FILEMODE_COMMIT: int
GIT_FILEMODE_LINK: int
GIT_FILEMODE_TREE: int
GIT_FILEMODE_UNREADABLE: int
GIT_FILTER_ALLOW_UNSAFE: int
GIT_FILTER_ATTRIBUTES_FROM_COMMIT: int
GIT_FILTER_ATTRIBUTES_FROM_HEAD: int
GIT_FILTER_CLEAN: int
GIT_FILTER_DEFAULT: int
GIT_FILTER_DRIVER_PRIORITY: int
GIT_FILTER_NO_SYSTEM_ATTRIBUTES: int
GIT_FILTER_SMUDGE: int
GIT_FILTER_TO_ODB: int
GIT_FILTER_TO_WORKTREE: int
GIT_MERGE_ANALYSIS_FASTFORWARD: int
GIT_MERGE_ANALYSIS_NONE: int
GIT_MERGE_ANALYSIS_NORMAL: int
GIT_MERGE_ANALYSIS_UNBORN: int
GIT_MERGE_ANALYSIS_UP_TO_DATE: int
GIT_MERGE_PREFERENCE_FASTFORWARD_ONLY: int
GIT_MERGE_PREFERENCE_NONE: int
GIT_MERGE_PREFERENCE_NO_FASTFORWARD: int
GIT_OBJECT_ANY: int
GIT_OBJECT_BLOB: int
GIT_OBJECT_COMMIT: int
GIT_OBJECT_INVALID: int
GIT_OBJECT_OFS_DELTA: int
GIT_OBJECT_REF_DELTA: int
GIT_OBJECT_TAG: int
GIT_OBJECT_TREE: int
GIT_OID_HEXSZ: int
GIT_OID_HEX_ZERO: str
GIT_OID_MINPREFIXLEN: int
GIT_OID_RAWSZ: int
GIT_OPT_DISABLE_PACK_KEEP_FILE_CHECKS: int
GIT_OPT_ENABLE_CACHING: int
GIT_OPT_ENABLE_FSYNC_GITDIR: int
GIT_OPT_ENABLE_OFS_DELTA: int
GIT_OPT_ENABLE_STRICT_HASH_VERIFICATION: int
GIT_OPT_ENABLE_STRICT_OBJECT_CREATION: int
GIT_OPT_ENABLE_STRICT_SYMBOLIC_REF_CREATION: int
GIT_OPT_ENABLE_UNSAVED_INDEX_SAFETY: int
GIT_OPT_GET_CACHED_MEMORY: int
GIT_OPT_GET_MWINDOW_MAPPED_LIMIT: int
GIT_OPT_GET_MWINDOW_SIZE: int
GIT_OPT_GET_OWNER_VALIDATION: int
GIT_OPT_GET_PACK_MAX_OBJECTS: int
GIT_OPT_GET_SEARCH_PATH: int
GIT_OPT_GET_TEMPLATE_PATH: int
GIT_OPT_GET_USER_AGENT: int
GIT_OPT_GET_WINDOWS_SHAREMODE: int
GIT_OPT_SET_ALLOCATOR: int
GIT_OPT_SET_CACHE_MAX_SIZE: int
GIT_OPT_SET_CACHE_OBJECT_LIMIT: int
GIT_OPT_SET_MWINDOW_MAPPED_LIMIT: int
GIT_OPT_SET_MWINDOW_SIZE: int
GIT_OPT_SET_OWNER_VALIDATION: int
GIT_OPT_SET_PACK_MAX_OBJECTS: int
GIT_OPT_SET_SEARCH_PATH: int
GIT_OPT_SET_SSL_CERT_LOCATIONS: int
GIT_OPT_SET_SSL_CIPHERS: int
GIT_OPT_SET_TEMPLATE_PATH: int
GIT_OPT_SET_USER_AGENT: int
GIT_OPT_SET_WINDOWS_SHAREMODE: int
GIT_REFERENCES_ALL: int
GIT_REFERENCES_BRANCHES: int
GIT_REFERENCES_TAGS: int
GIT_RESET_HARD: int
GIT_RESET_MIXED: int
GIT_RESET_SOFT: int
GIT_REVSPEC_MERGE_BASE: int
GIT_REVSPEC_RANGE: int
GIT_REVSPEC_SINGLE: int
GIT_SORT_NONE: int
GIT_SORT_REVERSE: int
GIT_SORT_TIME: int
GIT_SORT_TOPOLOGICAL: int
GIT_STASH_APPLY_DEFAULT: int
GIT_STASH_APPLY_REINSTATE_INDEX: int
GIT_STASH_DEFAULT: int
GIT_STASH_INCLUDE_IGNORED: int
GIT_STASH_INCLUDE_UNTRACKED: int
GIT_STASH_KEEP_ALL: int
GIT_STASH_KEEP_INDEX: int
GIT_STATUS_CONFLICTED: int
GIT_STATUS_CURRENT: int
GIT_STATUS_IGNORED: int
GIT_STATUS_INDEX_DELETED: int
GIT_STATUS_INDEX_MODIFIED: int
GIT_STATUS_INDEX_NEW: int
GIT_STATUS_INDEX_RENAMED: int
GIT_STATUS_INDEX_TYPECHANGE: int
GIT_STATUS_WT_DELETED: int
GIT_STATUS_WT_MODIFIED: int
GIT_STATUS_WT_NEW: int
GIT_STATUS_WT_RENAMED: int
GIT_STATUS_WT_TYPECHANGE: int
GIT_STATUS_WT_UNREADABLE: int
GIT_SUBMODULE_IGNORE_ALL: int
GIT_SUBMODULE_IGNORE_DIRTY: int
GIT_SUBMODULE_IGNORE_NONE: int
GIT_SUBMODULE_IGNORE_UNSPECIFIED: int
GIT_SUBMODULE_IGNORE_UNTRACKED: int
GIT_SUBMODULE_STATUS_INDEX_ADDED: int
GIT_SUBMODULE_STATUS_INDEX_DELETED: int
GIT_SUBMODULE_STATUS_INDEX_MODIFIED: int
GIT_SUBMODULE_STATUS_IN_CONFIG: int
GIT_SUBMODULE_STATUS_IN_HEAD: int
GIT_SUBMODULE_STATUS_IN_INDEX: int
GIT_SUBMODULE_STATUS_IN_WD: int
GIT_SUBMODULE_STATUS_WD_ADDED: int
GIT_SUBMODULE_STATUS_WD_DELETED: int
GIT_SUBMODULE_STATUS_WD_INDEX_MODIFIED: int
GIT_SUBMODULE_STATUS_WD_MODIFIED: int
GIT_SUBMODULE_STATUS_WD_UNINITIALIZED: int
GIT_SUBMODULE_STATUS_WD_UNTRACKED: int
GIT_SUBMODULE_STATUS_WD_WD_MODIFIED: int
LIBGIT2_VERSION: str
LIBGIT2_VER_MAJOR: int
LIBGIT2_VER_MINOR: int
LIBGIT2_VER_REVISION: int

_GIT_OBJ_BLOB: TypeAlias = Literal[3]
_GIT_OBJ_COMMIT: TypeAlias = Literal[1]
_GIT_OBJ_TAG: TypeAlias = Literal[4]
_GIT_OBJ_TREE: TypeAlias = Literal[2]

class Object:
    """Base class for Git objects."""
    _pointer: bytes
    filemode: FileMode
    id: Oid
    name: str | None
    raw_name: bytes | None
    short_id: str
    type: Literal[_GIT_OBJ_COMMIT, _GIT_OBJ_TREE, _GIT_OBJ_TAG, _GIT_OBJ_BLOB]
    type_str: Literal["commit", "tree", "tag", "blob"]
    @overload
    def peel(self, target_type: Literal[_GIT_OBJ_COMMIT]) -> Commit:
        """
        peel(target_type) -> Object

        Peel the current object and returns the first object of the given type.

        If you pass None as the target type, then the object will be peeled
        until the type changes. A tag will be peeled until the referenced object
        is no longer a tag, and a commit will be peeled to a tree. Any other
        object type will raise InvalidSpecError.
        """
        ...
    @overload
    def peel(self, target_type: Literal[_GIT_OBJ_TREE]) -> Tree:
        """
        peel(target_type) -> Object

        Peel the current object and returns the first object of the given type.

        If you pass None as the target type, then the object will be peeled
        until the type changes. A tag will be peeled until the referenced object
        is no longer a tag, and a commit will be peeled to a tree. Any other
        object type will raise InvalidSpecError.
        """
        ...
    @overload
    def peel(self, target_type: Literal[_GIT_OBJ_TAG]) -> Tag:
        """
        peel(target_type) -> Object

        Peel the current object and returns the first object of the given type.

        If you pass None as the target type, then the object will be peeled
        until the type changes. A tag will be peeled until the referenced object
        is no longer a tag, and a commit will be peeled to a tree. Any other
        object type will raise InvalidSpecError.
        """
        ...
    @overload
    def peel(self, target_type: Literal[_GIT_OBJ_BLOB]) -> Blob:
        """
        peel(target_type) -> Object

        Peel the current object and returns the first object of the given type.

        If you pass None as the target type, then the object will be peeled
        until the type changes. A tag will be peeled until the referenced object
        is no longer a tag, and a commit will be peeled to a tree. Any other
        object type will raise InvalidSpecError.
        """
        ...
    @overload
    def peel(self, target_type: None) -> Commit | Tree | Blob:
        """
        peel(target_type) -> Object

        Peel the current object and returns the first object of the given type.

        If you pass None as the target type, then the object will be peeled
        until the type changes. A tag will be peeled until the referenced object
        is no longer a tag, and a commit will be peeled to a tree. Any other
        object type will raise InvalidSpecError.
        """
        ...
    def read_raw(self) -> bytes:
        """
        read_raw() -> bytes

        Returns the byte string with the raw contents of the object.
        """
        ...
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
        ...
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
        ...
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
        ...
    def __hash__(self) -> int:
        """Return hash(self)."""
        ...
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
        ...
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
        ...
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
        ...

@final
class Reference:
    """
    Reference(name: str, target: str): create a symbolic reference

    Reference(name: str, oid: Oid, peel: Oid): create a direct reference

    'peel' is the first non-tag object's OID, or None.

    The purpose of this constructor is for use in custom refdb backends.
    References created with this function are unlikely to work as
    expected in other contexts.
    """
    name: str
    raw_name: bytes
    raw_shorthand: bytes
    raw_target: Oid | bytes
    shorthand: str
    target: Oid | str
    type: ReferenceType
    @overload
    def __init__(self, name: str, target: str) -> None: ...
    @overload
    def __init__(self, name: str, oid: Oid, peel: Oid) -> None: ...
    def delete(self) -> None:
        """
        delete()

        Delete this reference. It will no longer be valid!
        """
        ...
    def log(self) -> Iterator[RefLogEntry]:
        """
        log() -> RefLogIter

        Retrieves the current reference log.
        """
        ...
    @overload
    def peel(self, type: Literal[_GIT_OBJ_COMMIT]) -> Commit:
        """
        peel(type=None) -> Object

        Retrieve an object of the given type by recursive peeling.

        If no type is provided, the first non-tag object will be returned.
        """
        ...
    @overload
    def peel(self, type: Literal[_GIT_OBJ_TREE]) -> Tree:
        """
        peel(type=None) -> Object

        Retrieve an object of the given type by recursive peeling.

        If no type is provided, the first non-tag object will be returned.
        """
        ...
    @overload
    def peel(self, type: Literal[_GIT_OBJ_TAG]) -> Tag:
        """
        peel(type=None) -> Object

        Retrieve an object of the given type by recursive peeling.

        If no type is provided, the first non-tag object will be returned.
        """
        ...
    @overload
    def peel(self, type: Literal[_GIT_OBJ_BLOB]) -> Blob:
        """
        peel(type=None) -> Object

        Retrieve an object of the given type by recursive peeling.

        If no type is provided, the first non-tag object will be returned.
        """
        ...
    @overload
    def peel(self, type: None) -> Commit | Tree | Blob:
        """
        peel(type=None) -> Object

        Retrieve an object of the given type by recursive peeling.

        If no type is provided, the first non-tag object will be returned.
        """
        ...
    def rename(self, new_name: str) -> None:
        """
        rename(new_name: str)

        Rename the reference.
        """
        ...
    def resolve(self) -> Reference:
        """
        resolve() -> Reference

        Resolve a symbolic reference and return a direct reference.
        """
        ...
    def set_target(self, target: _OidArg, message: str = ...) -> None:
        """
        set_target(target[, message: str])

        Set the target of this reference. Creates a new entry in the reflog.

        Parameters:

        target
            The new target for this reference

        message
            Message to use for the reflog.
        """
        ...
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
        ...
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
        ...
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
        ...
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
        ...
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
        ...
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
        ...

class AlreadyExistsError(ValueError): ...

@final
class Blob(Object):
    """
    Blob object.

    Blobs implement the buffer interface, which means you can get access
    to its data via `memoryview(blob)` without the need to create a copy.
    """
    data: bytes
    is_binary: bool
    size: int
    def diff(self, blob: Blob = ..., flag: int = ..., old_as_path: str = ..., new_as_path: str = ...) -> Patch:
        """
        diff([blob: Blob, flag: int = GIT_DIFF_NORMAL, old_as_path: str, new_as_path: str]) -> Patch

        Directly generate a :py:class:`pygit2.Patch` from the difference
        between two blobs.

        Returns: Patch.

        Parameters:

        blob : Blob
            The :py:class:`~pygit2.Blob` to diff.

        flag
            A GIT_DIFF_* constant.

        old_as_path : str
            Treat old blob as if it had this filename.

        new_as_path : str
            Treat new blob as if it had this filename.
        """
        ...
    def diff_to_buffer(
        self, buffer: bytes | None = None, flag: DiffOption = ..., old_as_path: str = ..., buffer_as_path: str = ...
    ) -> Patch:
        """
        diff_to_buffer(buffer: bytes = None, flag: int = GIT_DIFF_NORMAL[, old_as_path: str, buffer_as_path: str]) -> Patch

        Directly generate a :py:class:`~pygit2.Patch` from the difference
        between a blob and a buffer.

        Returns: Patch.

        Parameters:

        buffer : bytes
            Raw data for new side of diff.

        flag
            A GIT_DIFF_* constant.

        old_as_path : str
            Treat old blob as if it had this filename.

        buffer_as_path : str
            Treat buffer as if it had this filename.
        """
        ...

# This is not a real subclassing. Just ensuring type-checkers sees this type as compatible with _CDataBase
# pyright has no error code for subclassing final
@final
class Branch(Reference):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    """Branch."""
    branch_name: str
    raw_branch_name: bytes
    remote_name: str
    upstream: Branch
    upstream_name: str
    def delete(self) -> None:
        """
        delete()

        Delete this branch. It will no longer be valid!
        """
        ...
    def is_checked_out(self) -> bool:
        """
        is_checked_out() -> bool

        True if branch is checked out by any repo connected to the current one,  False otherwise.
        """
        ...
    def is_head(self) -> bool:
        """
        is_head() -> bool

        True if HEAD points at the branch, False otherwise.
        """
        ...
    def rename(self, name: str, force: bool = False) -> None:
        """
        rename(name: str, force: bool = False)

        Move/rename an existing local branch reference. The new branch name will be checked for validity.
        Returns the new branch.
        """
        ...

@final
class Commit(Object):
    """Commit objects."""
    author: Signature
    commit_time: int
    commit_time_offset: int
    committer: Signature
    gpg_signature: tuple[bytes, bytes]
    message: str
    message_encoding: str
    message_trailers: dict[str, str]
    parent_ids: list[Oid]
    parents: list[Commit]
    raw_message: bytes
    tree: Tree
    tree_id: Oid

class Diff:
    """Diff objects."""
    deltas: Iterator[DiffDelta]
    patch: str | None
    patchid: Oid
    stats: DiffStats
    def find_similar(
        self,
        flags: DiffFind = ...,
        rename_threshold: int = 50,
        copy_threshold: int = 50,
        rename_from_rewrite_threshold: int = 50,
        break_rewrite_threshold: int = 60,
        rename_limit: int = 1000,
    ) -> None:
        """
        find_similar(flags: enums.DiffFind = enums.DiffFind.FIND_BY_CONFIG, rename_threshold: int = 50, copy_threshold: int = 50, rename_from_rewrite_threshold: int = 50, break_rewrite_threshold: int = 60, rename_limit: int = 1000)

        Transform a diff marking file renames, copies, etc.

        This modifies a diff in place, replacing old entries that look like
        renames or copies with new entries reflecting those changes. This also will, if requested, break modified files into add/remove pairs if the amount of change is above a threshold.

        flags - Combination of enums.DiffFind.FIND_* and enums.DiffFind.BREAK_* constants.
        """
        ...
    def merge(self, diff: Diff) -> None:
        """
        merge(diff: Diff)

        Merge one diff into another.
        """
        ...
    @staticmethod
    def from_c(diff: bytes, repo: Repository) -> Diff:
        """Method exposed for Index to hook into"""
        ...
    @staticmethod
    def parse_diff(git_diff: str | bytes) -> Diff:
        """
        parse_diff(git_diff: str | bytes) -> Diff

        Parses a git unified diff into a diff object without a repository
        """
        ...
    def __getitem__(self, index: int) -> Patch:
        """Return self[key]."""
        ...
    def __iter__(self) -> Iterator[Patch]:
        """Implement iter(self)."""
        ...
    def __len__(self) -> int:
        """Return len(self)."""
        ...

@final
class DiffDelta:
    """DiffDelta object."""
    flags: DiffFlag
    is_binary: bool
    nfiles: int
    new_file: DiffFile
    old_file: DiffFile
    similarity: int
    status: FileStatus
    def status_char(self) -> str:
        """
        status_char() -> str

        Return the single character abbreviation for a delta status code.
        """
        ...

@final
class DiffFile:
    """DiffFile object."""
    flags: DiffFlag
    id: Oid
    mode: FileMode
    path: str
    raw_path: bytes
    size: int
    @staticmethod
    def from_c(ptr: bytes) -> DiffFile:
        """Method exposed for _checkout_notify_cb to hook into"""
        ...

class DiffHunk:
    """DiffHunk object."""
    header: str
    lines: list[DiffLine]
    new_lines: int
    new_start: int
    old_lines: int
    old_start: int

@final
class DiffLine:
    """DiffLine object."""
    content: str
    content_offset: int
    new_lineno: int
    num_lines: int
    old_lineno: int
    origin: str
    raw_content: bytes

class DiffStats:
    """DiffStats object."""
    deletions: int
    files_changed: int
    insertions: int
    def format(self, format: DiffStatsFormat, width: int) -> str:
        """
        format(format: enums.DiffStatsFormat, width: int) -> str

        Format the stats as a string.

        Returns: str.

        Parameters:

        format
            The format to use. A combination of DiffStatsFormat constants.

        width
            The width of the output. The output will be scaled to fit.
        """
        ...

@final
class FilterSource:
    """A filter source represents the file/blob to be processed."""
    repo: Repository
    path: str
    filemode: int
    oid: Oid
    mode: int
    flags: int

class GitError(Exception): ...
class InvalidSpecError(ValueError): ...

@final
class Mailmap:
    """Mailmap object."""
    def __init__(self) -> None: ...
    def add_entry(
        self, real_name: str = ..., real_email: str = ..., replace_name: str = ..., replace_email: str = ...
    ) -> None:
        """
        add_entry(real_name: str = None, real_email: str = None, replace_name: str = None, replace_email: str)

        Add a new entry to the mailmap, overriding existing entries.
        """
        ...
    @staticmethod
    def from_buffer(buffer: str | bytes) -> Mailmap:
        """
        from_buffer(buffer: str) -> Mailmap

        Parse a passed-in buffer and construct a mailmap object.
        """
        ...
    @staticmethod
    def from_repository(repository: Repository) -> Mailmap:
        """
        from_repository(repository: Repository) -> Mailmap

        Create a new mailmap instance from a repository, loading mailmap files based on the repository's configuration.

        Mailmaps are loaded in the following order:
         1. '.mailmap' in the root of the repository's working directory, if present.
         2. The blob object identified by the 'mailmap.blob' config entry, if set.
            [NOTE: 'mailmap.blob' defaults to 'HEAD:.mailmap' in bare repositories]
         3. The path in the 'mailmap.file' config entry, if set.
        """
        ...
    def resolve(self, name: str, email: str) -> tuple[str, str]:
        """
        resolve(name: str, email: str) -> tuple[str, str]

        Resolve name & email to a real name and email.
        """
        ...
    def resolve_signature(self, sig: Signature) -> Signature:
        """
        resolve_signature(sig: Signature) -> Signature

        Resolve signature to real name and email.
        """
        ...

@final
class Note:
    """Note object."""
    annotated_id: Oid
    id: Oid
    message: str
    def remove(self, author: Signature, committer: Signature, ref: str = "refs/notes/commits") -> None:
        """
        remove(author: Signature, committer: Signature, ref: str = "refs/notes/commits")

        Removes a note for an annotated object
        """
        ...

@final
class Odb:
    """Object database."""
    backends: Iterator[OdbBackend]
    def __init__(self, path: StrOrBytesPath | None = None) -> None: ...
    def add_backend(self, backend: OdbBackend, priority: int) -> None:
        """
        add_backend(backend: OdbBackend, priority: int)

        Adds an OdbBackend to the list of backends for this object database.
        """
        ...
    def add_disk_alternate(self, path: str) -> None:
        """
        add_disk_alternate(path: str)

        Adds a path on disk as an alternate backend for objects.
        Alternate backends are checked for objects only *after* the main backends
        are checked. Writing is disabled on alternate backends.
        """
        ...
    def exists(self, oid: _OidArg) -> bool:
        """
        exists(oid: Oid) -> bool

        Returns true if the given oid can be found in this odb.
        """
        ...
    def read(self, oid: _OidArg) -> tuple[int, int, bytes]:
        """
        read(oid) -> type, data, size

        Read raw object data from the object db.
        """
        ...
    def write(self, type: int, data: bytes) -> Oid:
        """
        write(type: int, data: bytes) -> Oid

        Write raw object data into the object db. First arg is the object
        type, the second one a buffer with data. Return the Oid of the created
        object.
        """
        ...
    def __contains__(self, other: _OidArg) -> bool:
        """Return bool(key in self)."""
        ...
    def __iter__(self) -> Iterator[Oid]:
        """Implement iter(self)."""
        ...

class OdbBackend:
    """Object database backend."""
    def __init__(self) -> None: ...
    def exists(self, oid: _OidArg) -> bool:
        """
        exists(oid: Oid) -> bool

        Returns true if the given oid can be found in this odb.
        """
        ...
    def exists_prefix(self, partial_id: _OidArg) -> Oid:
        """
        exists_prefix(partial_id: Oid) -> Oid

        Given a partial oid, returns the full oid. Raises KeyError if not found,
        or ValueError if ambiguous.
        """
        ...
    def read(self, oid: _OidArg) -> tuple[int, bytes]:
        """
        read(oid) -> (type, data)

        Read raw object data from this odb backend.
        """
        ...
    def read_header(self, oid: _OidArg) -> tuple[int, int]:
        """
        read_header(oid) -> (type, len)

        Read raw object header from this odb backend.
        """
        ...
    def read_prefix(self, oid: _OidArg) -> tuple[int, bytes, Oid]:
        """
        read_prefix(oid: Oid) -> tuple[int, bytes, Oid]

        Read raw object data from this odb backend based on an oid prefix.
        The returned tuple contains (type, data, oid).
        """
        ...
    def refresh(self) -> None:
        """
        refresh()

        If the backend supports a refreshing mechanism, this function will invoke
        it. However, the backend implementation should try to stay up-to-date as
        much as possible by itself as libgit2 will not automatically invoke this
        function. For instance, a potential strategy for the backend
        implementation to utilize this could be internally calling the refresh
        function on failed lookups.
        """
        ...
    def __iter__(self) -> Iterator[Oid]:
        """Implement iter(self)."""
        ...

@final
class OdbBackendLoose(OdbBackend):
    """
    OdbBackendLoose(objects_dir, compression_level, do_fsync, dir_mode=0, file_mode=0)

    Object database backend for loose objects.

    Parameters:

    objects_dir
        path to top-level object dir on disk

    compression_level
        zlib compression level to use

    do_fsync
        true to fsync() after writing

    dir_mode
        mode for new directories, or 0 for default

    file_mode
        mode for new files, or 0 for default
    """
    def __init__(
        self, objects_dir: StrOrBytesPath, compression_level: int, do_fsync: bool, dir_mode: int = 0, file_mode: int = 0
    ) -> None: ...

@final
class OdbBackendPack(OdbBackend):
    """Object database backend for packfiles."""
    def __init__(self, path: StrOrBytesPath) -> None: ...

@final
class Oid:
    """Object id."""
    raw: bytes
    def __init__(self, raw: bytes = ..., hex: str = ...) -> None: ...
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
        ...
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
        ...
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
        ...
    def __hash__(self) -> int:
        """Return hash(self)."""
        ...
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
        ...
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
        ...
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
        ...

@final
class Patch:
    """Diff patch object."""
    data: bytes
    delta: DiffDelta
    hunks: list[DiffHunk]
    line_stats: tuple[int, int, int]  # context, additions, deletions
    text: str | None

    @staticmethod
    def create_from(
        old: Blob | bytes | None,
        new: Blob | bytes | None,
        old_as_path: str = ...,
        new_as_path: str = ...,
        flag: DiffOption = ...,
        context_lines: int = 3,
        interhunk_lines: int = 0,
    ) -> Patch:
        """Create a patch from blobs, buffers, or a blob and a buffer"""
        ...

@final
class RefLogEntry:
    """Reference log object."""
    committer: Signature
    message: str
    oid_new: Oid
    oid_old: Oid

@final
class Refdb:
    """Reference database."""
    def compress(self) -> None:
        """
        compress()

        Suggests that the given refdb compress or optimize its references.
        This mechanism is implementation specific.  For on-disk reference
        databases, for example, this may pack all loose references.
        """
        ...
    @staticmethod
    def new(repo: Repository) -> Refdb:
        """
        Refdb.new(repo: Repository) -> Refdb
        Creates a new refdb with no backend.
        """
        ...
    @staticmethod
    def open(repo: Repository) -> Refdb:
        """
        open(repo: Repository) -> Refdb

        Create a new reference database and automatically add
        the default backends, assuming the repository dir as the folder.
        """
        ...
    def set_backend(self, backend: RefdbBackend) -> None:
        """
        set_backend(backend: RefdbBackend)

        Sets a custom RefdbBackend for this Refdb.
        """
        ...

class RefdbBackend:
    """Reference database backend."""
    def __init__(self) -> None: ...
    def compress(self) -> None:
        """
        compress()

        Suggests that the implementation compress or optimize its references.
        This behavior is implementation-specific.
        """
        ...
    def delete(self, ref_name: str, old_id: _OidArg, old_target: str) -> None:
        """
        delete(ref_name: str, old_id: Oid, old_target: str)

        Deletes a reference.
        """
        ...
    def ensure_log(self, ref_name: str) -> bool:
        """
        ensure_log(ref_name: str) -> bool

        Ensure that a particular reference will have a reflog which will be
        appended to on writes.
        """
        ...
    def exists(self, refname: str) -> bool:
        """
        exists(refname: str) -> bool

        Returns True if a ref by this name exists, or False otherwise.
        """
        ...
    def has_log(self, ref_name: str) -> bool:
        """
        has_log(ref_name: str) -> bool

        Returns True if a ref log is available for this reference.
        It may be empty even if it exists.
        """
        ...
    def lookup(self, refname: str) -> Reference:
        """
        lookup(refname: str) -> Reference

        Looks up a reference and returns it, or None if not found.
        """
        ...
    def rename(self, old_name: str, new_name: str, force: bool, who: Signature, message: str) -> Reference:
        """
        rename(old_name: str, new_name: str, force: bool, who: Signature, message: str) -> Reference

        Renames a reference.
        """
        ...
    def write(self, ref: Reference, force: bool, who: Signature, message: str, old: _OidArg, old_target: str) -> None:
        """
        write(ref: Reference, force: bool, who: Signature, message: str, old: Oid, old_target: str)

        Writes a new reference to the reference database.
        """
        ...

@final
class RefdbFsBackend(RefdbBackend):
    """
    RefdbFsBackend(repo: Repository)

    Reference database filesystem backend. The path to the repository
    is used as the basis of the reference database.
    """
    def __init__(self, repo: Repository) -> None: ...

class Repository:
    """
    Repository(backend) -> Repository

    Git repository.
    """
    _pointer: bytes
    default_signature: Signature
    head: Reference
    head_is_detached: bool
    head_is_unborn: bool
    is_bare: bool
    is_empty: bool
    is_shallow: bool
    odb: Odb
    path: str
    refdb: Refdb
    workdir: str
    def __init__(self, backend: object | None = None) -> None: ...
    def TreeBuilder(self, src: Tree | _OidArg = ...) -> TreeBuilder:
        """
        TreeBuilder([tree]) -> TreeBuilder

        Create a TreeBuilder object for this repository.
        """
        ...
    def _disown(self) -> None:
        """Mark the object as not-owned by us. For internal use only."""
        ...
    def _from_c(self, pointer: bytes, free: bool) -> None:
        """Init a Repository from a pointer. For internal use only."""
        ...
    def add_worktree(self, name: str, path: str, ref: Reference = ...) -> Worktree:
        """
        add_worktree(name: str, path: str | bytes[, ref: Reference]) -> Worktree

        Create a new worktree for this repository. If ref is specified, no new     branch will be created and the provided ref will be checked out instead.
        """
        ...
    def applies(self, diff: Diff, location: ApplyLocation = ..., raise_error: bool = False) -> bool:
        """
        applies(diff: Diff, location: int = GIT_APPLY_LOCATION_INDEX, raise_error: bool = False) -> bool

        Tests if the given patch will apply to HEAD, without writing it.

        Parameters:

        diff
            The Diff to apply.

        location
            The location to apply: GIT_APPLY_LOCATION_WORKDIR,
            GIT_APPLY_LOCATION_INDEX (default), or GIT_APPLY_LOCATION_BOTH.

        raise_error
            If the patch doesn't apply, raise an exception containing more details
            about the failure instead of returning False.
        """
        ...
    def apply(self, diff: Diff, location: ApplyLocation = ...) -> None:
        """
        apply(diff: Diff, location: ApplyLocation = ApplyLocation.WORKDIR)

        Applies the given Diff object to HEAD, writing the results into the
        working directory, the index, or both.

        Parameters:

        diff
            The Diff to apply.

        location
            The location to apply: ApplyLocation.WORKDIR (default),
            ApplyLocation.INDEX, or ApplyLocation.BOTH.
        """
        ...
    def cherrypick(self, id: _OidArg) -> None:
        """
        cherrypick(id: Oid)

        Cherry-pick the given oid, producing changes in the index and working directory.

        Merges the given commit into HEAD as a cherrypick, writing the results into the
        working directory. Any changes are staged for commit and any conflicts
        are written to the index. Callers should inspect the repository's
        index after this completes, resolve any conflicts and prepare a
        commit.
        """
        ...
    def compress_references(self) -> None:
        """
        compress_references()

        Suggest that the repository compress or optimize its references.
        This mechanism is implementation-specific.  For on-disk reference
        databases, for example, this may pack all loose references.
        """
        ...
    def create_blob(self, data: bytes) -> Oid:
        """
        create_blob(data: bytes) -> Oid

        Create a new blob from a bytes string. The blob is added to the Git
        object database. Returns the oid of the blob.
        """
        ...
    def create_blob_fromdisk(self, path: str) -> Oid:
        """
        create_blob_fromdisk(path: str) -> Oid

        Create a new blob from a file anywhere (no working directory check).
        """
        ...
    def create_blob_fromiobase(self, iobase: IOBase) -> Oid:
        """
        create_blob_fromiobase(io.IOBase) -> Oid

        Create a new blob from an IOBase object.
        """
        ...
    def create_blob_fromworkdir(self, path: str) -> Oid:
        """
        create_blob_fromworkdir(path: str) -> Oid

        Create a new blob from a file within the working directory. The given
        path must be relative to the working directory, if it is not an error
        is raised.
        """
        ...
    def create_branch(self, name: str, commit: Commit, force: bool = False) -> Branch:
        """
        create_branch(name: str, commit: Commit, force: bool = False) -> Branch

        Create a new branch "name" which points to a commit.

        Returns: Branch

        Parameters:

        force
            If True branches will be overridden, otherwise (the default) an
            exception is raised.

        Examples::

            repo.create_branch('foo', repo.head.peel(), force=False)
        """
        ...
    def create_commit(
        self,
        reference_name: str | None,
        author: Signature,
        committer: Signature,
        message: str | bytes,
        tree: _OidArg,
        parents: list[_OidArg],
        encoding: str = ...,
    ) -> Oid:
        """
        create_commit(reference_name: str, author: Signature, committer: Signature, message: bytes | str, tree: Oid, parents: list[Oid][, encoding: str]) -> Oid

        Create a new commit object, return its oid.
        """
        ...
    def create_commit_string(
        self,
        author: Signature,
        committer: Signature,
        message: str | bytes,
        tree: _OidArg,
        parents: list[_OidArg],
        encoding: str = ...,
    ) -> Oid:
        """
        create_commit_string(author: Signature, committer: Signature, message: bytes | str, tree: Oid, parents: list[Oid][, encoding: str]) -> str

        Create a new commit but return it as a string.
        """
        ...
    def create_commit_with_signature(self, content: str, signature: str, signature_field: str | None = None) -> Oid:
        """
        create_commit_with_signature(content: str, signature: str[, field_name: str]) -> Oid

        Create a new signed commit object, return its oid.
        """
        ...
    def create_note(
        self,
        message: str,
        author: Signature,
        committer: Signature,
        annotated_id: str,
        ref: str = "refs/notes/commits",
        force: bool = False,
    ) -> Oid:
        """
        create_note(message: str, author: Signature, committer: Signature, annotated_id: str, ref: str = "refs/notes/commits", force: bool = False) -> Oid

        Create a new note for an object, return its SHA-ID.If no ref is given 'refs/notes/commits' will be used.
        """
        ...
    def create_reference_direct(self, name: str, target: _OidArg, force: bool, message: str | None = None) -> Reference:
        """
        create_reference_direct(name: str, target: Oid, force: bool, message=None) -> Reference

        Create a new reference "name" which points to an object.

        Returns: Reference

        Parameters:

        force
            If True references will be overridden, otherwise (the default) an
            exception is raised.

        message
            Optional message to use for the reflog.

        Examples::

            repo.create_reference_direct('refs/heads/foo', repo.head.target, False)
        """
        ...
    def create_reference_symbolic(self, name: str, target: str, force: bool, message: str | None = None) -> Reference:
        """
        create_reference_symbolic(name: str, target: str, force: bool, message: str = None) -> Reference

        Create a new reference "name" which points to another reference.

        Returns: Reference

        Parameters:

        force
            If True references will be overridden, otherwise (the default) an
            exception is raised.

        message
            Optional message to use for the reflog.

        Examples::

            repo.create_reference_symbolic('refs/tags/foo', 'refs/heads/master', False)
        """
        ...
    def create_tag(self, name: str, oid: _OidArg, type: ObjectType, tagger: Signature, message: str) -> Oid:
        """
        create_tag(name: str, oid: Oid, type: enums.ObjectType, tagger: Signature[, message: str]) -> Oid

        Create a new tag object, return its oid.
        """
        ...
    def descendant_of(self, oid1: _OidArg, oid2: _OidArg) -> bool:
        """
        descendant_of(oid1: Oid, oid2: Oid) -> bool

        Determine if the first commit is a descendant of the second commit.
        Note that a commit is not considered a descendant of itself.
        """
        ...
    def expand_id(self, hex: str) -> Oid:
        """
        expand_id(hex: str) -> Oid

        Expand a string into a full Oid according to the objects in this repsitory.
        """
        ...
    def free(self) -> None:
        """
        free()

        Releases handles to the Git database without deallocating the repository.
        """
        ...
    def git_object_lookup_prefix(self, oid: _OidArg) -> Object:
        """
        git_object_lookup_prefix(oid: Oid) -> Object

        Returns the Git object with the given oid.
        """
        ...
    def list_worktrees(self) -> list[str]:
        """
        list_worktrees() -> list[str]

        Return a list with all the worktrees of this repository.
        """
        ...
    def listall_branches(self, flag: BranchType = ...) -> list[str]:
        """
        listall_branches(flag: BranchType = BranchType.LOCAL) -> list[str]

        Return a list with all the branches in the repository.

        The *flag* may be:

        - BranchType.LOCAL - return all local branches (set by default)
        - BranchType.REMOTE - return all remote-tracking branches
        - BranchType.ALL - return local branches and remote-tracking branches
        """
        ...
    def listall_mergeheads(self) -> list[Oid]:
        """
        listall_mergeheads() -> list[Oid]

        If a merge is in progress, return a list of all commit oids in the MERGE_HEAD file.
        Return an empty list if there is no MERGE_HEAD file (no merge in progress).
        """
        ...
    def listall_stashes(self) -> list[Stash]:
        """
        listall_stashes() -> list[Stash]

        Return a list with all stashed commits in the repository.
        """
        ...
    def listall_submodules(self) -> list[str]:
        """
        listall_submodules() -> list[str]

        Return a list with all submodule paths in the repository.
        """
        ...
    def lookup_branch(self, branch_name: str, branch_type: BranchType = ...) -> Branch:
        """
        lookup_branch(branch_name: str, branch_type: BranchType = BranchType.LOCAL) -> Branch

        Returns the Git reference for the given branch name (local or remote).
        If branch_type is BranchType.REMOTE, you must include the remote name
        in the branch name (eg 'origin/master').
        """
        ...
    def lookup_note(self, annotated_id: str, ref: str = "refs/notes/commits") -> Note:
        """
        lookup_note(annotated_id: str, ref: str = "refs/notes/commits") -> Note

        Lookup a note for an annotated object in a repository.
        """
        ...
    def lookup_reference(self, name: str) -> Reference:
        """
        lookup_reference(name: str) -> Reference

        Lookup a reference by its name in a repository.
        """
        ...
    def lookup_reference_dwim(self, name: str) -> Reference:
        """
        lookup_reference_dwim(name: str) -> Reference

        Lookup a reference by doing-what-i-mean'ing its short name.
        """
        ...
    def lookup_worktree(self, name: str) -> Worktree:
        """
        lookup_worktree(name: str) -> Worktree

        Lookup a worktree from its name.
        """
        ...
    def merge_analysis(self, their_head: _OidArg, our_ref: str = "HEAD") -> tuple[MergeAnalysis, MergePreference]:
        """
        merge_analysis(their_head: Oid, our_ref: str = "HEAD") -> tuple[MergeAnalysis, MergePreference]

        Analyzes the given branch and determines the opportunities for
        merging it into a reference (defaults to HEAD).

        Parameters:

        our_ref
            The reference name (String) to perform the analysis from

        their_head
            Head (commit Oid) to merge into

        The first returned value is a mixture of the MergeAnalysis.NONE, NORMAL,
        UP_TO_DATE, FASTFORWARD and UNBORN flags.
        The second value is the user's preference from 'merge.ff'
        """
        ...
    def merge_base(self, oid1: _OidArg, oid2: _OidArg) -> Oid:
        """
        merge_base(oid1: Oid, oid2: Oid) -> Oid

        Find as good common ancestors as possible for a merge.
        Returns None if there is no merge base between the commits
        """
        ...
    def merge_base_many(self, oids: list[_OidArg]) -> Oid:
        """
        merge_base_many(oids: list[Oid]) -> Oid

        Find as good common ancestors as possible for an n-way merge.
        Returns None if there is no merge base between the commits
        """
        ...
    def merge_base_octopus(self, oids: list[_OidArg]) -> Oid:
        """
        merge_base_octopus(oids: list[Oid]) -> Oid

        Find as good common ancestors as possible for an n-way octopus merge.
        Returns None if there is no merge base between the commits
        """
        ...
    def notes(self) -> Iterator[Note]: ...
    def path_is_ignored(self, path: str) -> bool:
        """
        path_is_ignored(path: str) -> bool

        Check if a path is ignored in the repository.
        """
        ...
    def raw_listall_branches(self, flag: BranchType = ...) -> list[bytes]:
        """
        raw_listall_branches(flag: BranchType = BranchType.LOCAL) -> list[bytes]

        Return a list with all the branches in the repository.

        The *flag* may be:

        - BranchType.LOCAL - return all local branches (set by default)
        - BranchType.REMOTE - return all remote-tracking branches
        - BranchType.ALL - return local branches and remote-tracking branches
        """
        ...
    def raw_listall_references(self) -> list[bytes]:
        """
        raw_listall_references() -> list[bytes]

        Return a list with all the references in the repository.
        """
        ...
    def references_iterator_init(self) -> Iterator[Reference]:
        """
        references_iterator_init() -> git_reference_iterator

        Creates and returns an iterator for references.
        """
        ...
    def references_iterator_next(self, iter: Iterator[Reference], references_return_type: ReferenceFilter = ...) -> Reference:
        """
        references_iterator_next(iter: Iterator[Reference], references_return_type: ReferenceFilter = ReferenceFilter.ALL) -> Reference

        Returns next reference object for repository. Optionally, can filter 
        based on value of references_return_type.
        Acceptable values of references_return_type:
        ReferenceFilter.ALL -> returns all refs, this is the default
        ReferenceFilter.BRANCHES -> returns all branches
        ReferenceFilter.TAGS -> returns all tags
        all other values -> will return None
        """
        ...
    def reset(self, oid: _OidArg, reset_type: ResetMode) -> None:
        """
        reset(oid: Oid, reset_mode: enums.ResetMode)

        Resets the current head.

        Parameters:

        oid
            The oid of the commit to reset to.

        reset_mode
            * SOFT: resets head to point to oid, but does not modify
              working copy, and leaves the changes in the index.
            * MIXED: resets head to point to oid, but does not modify
              working copy. It empties the index too.
            * HARD: resets head to point to oid, and resets too the
              working copy and the content of the index.
        """
        ...
    def revparse(self, revspec: str) -> RevSpec:
        """
        revparse(revspec: str) -> RevSpec

        Parse a revision string for from, to, and intent. See `man gitrevisions`,
        or the documentation for `git rev-parse` for information on the syntax
        accepted.
        """
        ...
    def revparse_ext(self, revision: str) -> tuple[Object, Reference]:
        """
        revparse_ext(revision: str) -> tuple[Object, Reference]

        Find a single object and intermediate reference, as specified by a revision
        string. See `man gitrevisions`, or the documentation for `git rev-parse`
        for information on the syntax accepted.

        In some cases (@{<-n>} or <branchname>@{upstream}), the expression may
        point to an intermediate reference, which is returned in the second element
        of the result tuple.
        """
        ...
    def revparse_single(self, revision: str) -> Object:
        """
        revparse_single(revision: str) -> Object

        Find an object, as specified by a revision string. See
        `man gitrevisions`, or the documentation for `git rev-parse` for
        information on the syntax accepted.
        """
        ...
    def set_odb(self, odb: Odb) -> None:
        """
        set_odb(odb: Odb)

        Sets the object database for this repository.
        This is a low-level function, most users won't need it.
        """
        ...
    def set_refdb(self, refdb: Refdb) -> None:
        """
        set_refdb(refdb: Refdb)

        Sets the reference database for this repository.
        This is a low-level function, most users won't need it.
        """
        ...
    def status(self, untracked_files: str = "all", ignored: bool = False) -> dict[str, int]:
        """
        status(untracked_files: str = "all", ignored: bool = False) -> dict[str, enums.FileStatus]

        Reads the status of the repository and returns a dictionary with file
        paths as keys and FileStatus flags as values.

        Parameters:

        untracked_files
            How to handle untracked files, defaults to "all":

            - "no": do not return untracked files
            - "normal": include untracked files/directories but no dot recurse subdirectories
            - "all": include all files in untracked directories

            Using `untracked_files="no"` or "normal"can be faster than "all" when the worktree
            contains many untracked files/directories.

        ignored
            Whether to show ignored files with untracked files. Ignored when untracked_files == "no"
            Defaults to False.
        """
        ...
    def status_file(self, path: str) -> int:
        """
        status_file(path: str) -> enums.FileStatus

        Returns the status of the given file path.
        """
        ...
    def walk(self, oid: _OidArg | None, sort_mode: SortMode = ...) -> Walker:
        """
        walk(oid: Oid | None, sort_mode: enums.SortMode = enums.SortMode.NONE) -> Walker

        Start traversing the history from the given commit.
        The following SortMode values can be used to control the walk:

        * NONE. Sort the output with the same default method from
          `git`: reverse chronological order. This is the default sorting for
          new walkers.
        * TOPOLOGICAL. Sort the repository contents in topological order
          (no parents before all of its children are shown); this sorting mode
          can be combined with time sorting to produce `git`'s `--date-order``.
        * TIME. Sort the repository contents by commit time; this sorting
          mode can be combined with topological sorting.
        * REVERSE.  Iterate through the repository contents in reverse
          order; this sorting mode can be combined with any of the above.

        Example:

          >>> from pygit2 import Repository
          >>> from pygit2.enums import SortMode
          >>> repo = Repository('.git')
          >>> for commit in repo.walk(repo.head.target, SortMode.TOPOLOGICAL):
          ...    print(commit.message)
          >>> for commit in repo.walk(repo.head.target, SortMode.TOPOLOGICAL | SortMode.REVERSE):
          ...    print(commit.message)
          >>>
        """
        ...

class RevSpec:
    """RevSpec object, output from Repository.revparse()."""
    flags: int
    from_object: Object
    to_object: Object

@final
class Signature:
    """Signature."""
    _encoding: str | None
    _pointer: bytes
    email: str
    name: str
    offset: int
    raw_email: bytes
    raw_name: bytes
    time: int
    def __init__(self, name: str, email: str, time: int = -1, offset: int = 0, encoding: str | None = None) -> None: ...
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
        ...
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
        ...
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
        ...
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
        ...
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
        ...
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
        ...

@final
class Stash:
    """Stashed state."""
    commit_id: Oid
    message: str
    raw_message: bytes
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
        ...
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
        ...
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
        ...
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
        ...
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
        ...
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
        ...

@final
class Tag(Object):
    """Tag objects."""
    message: str
    name: str
    raw_message: bytes
    raw_name: bytes
    tagger: Signature
    target: Oid
    def get_object(self) -> Object:
        """
        get_object() -> Object

        Retrieves the object the current tag is pointing to.
        """
        ...

class Tree(Object):
    """Tree objects."""
    def diff_to_index(self, index: Index, flags: DiffOption = ..., context_lines: int = 3, interhunk_lines: int = 0) -> Diff:
        """
        diff_to_index(index: Index, flags: enums.DiffOption = enums.DiffOption.NORMAL, context_lines: int = 3, interhunk_lines: int = 0) -> Diff

        Show the changes between the index and a given :py:class:`~pygit2.Tree`.

        Parameters:

        index : :py:class:`~pygit2.Index`
            The index to diff.

        flags
            A combination of enums.DiffOption constants.

        context_lines
            The number of unchanged lines that define the boundary of a hunk
            (and to display before and after).

        interhunk_lines
            The maximum number of unchanged lines between hunk boundaries before
            the hunks will be merged into a one.
        """
        ...
    def diff_to_tree(
        self, tree: Tree = ..., flags: DiffOption = ..., context_lines: int = 3, interhunk_lines: int = 3, swap: bool = False
    ) -> Diff:
        """
        diff_to_tree([tree: Tree, flags: enums.DiffOption = enums.DiffOption.NORMAL, context_lines: int = 3, interhunk_lines: int = 0, swap: bool = False]) -> Diff

        Show the changes between two trees.

        Parameters:

        tree: :py:class:`~pygit2.Tree`
            The tree to diff. If no tree is given the empty tree will be used
            instead.

        flags
            A combination of enums.DiffOption constants.

        context_lines
            The number of unchanged lines that define the boundary of a hunk
            (and to display before and after).

        interhunk_lines
            The maximum number of unchanged lines between hunk boundaries before
            the hunks will be merged into a one.

        swap
            Instead of diffing a to b. Diff b to a.
        """
        ...
    def diff_to_workdir(self, flags: DiffOption = ..., context_lines: int = 3, interhunk_lines: int = 0) -> Diff:
        """
        diff_to_workdir(flags: enums.DiffOption = enums.DiffOption.NORMAL, context_lines: int = 3, interhunk_lines: int = 0) -> Diff

        Show the changes between the :py:class:`~pygit2.Tree` and the workdir.

        Parameters:

        flags
            A combination of enums.DiffOption constants.

        context_lines
            The number of unchanged lines that define the boundary of a hunk
            (and to display before and after).

        interhunk_lines
            The maximum number of unchanged lines between hunk boundaries before
            the hunks will be merged into a one.
        """
        ...
    def __contains__(self, other: str) -> bool:
        """Return bool(key in self)."""
        ...
    def __getitem__(self, index: str | int) -> Object:
        """Return self[key]."""
        ...
    def __iter__(self) -> Iterator[Object]:
        """Implement iter(self)."""
        ...
    def __len__(self) -> int:
        """Return len(self)."""
        ...
    def __rtruediv__(self, other: str) -> Object:
        """Return value/self."""
        ...
    def __truediv__(self, other: str) -> Object:
        """Return self/value."""
        ...

class TreeBuilder:
    """TreeBuilder objects."""
    def clear(self) -> None:
        """
        clear()

        Clear all the entries in the builder.
        """
        ...
    def get(self, name: str) -> Object:
        """
        get(name: str) -> Object

        Return the Object for the given name, or None if there is not.
        """
        ...
    def insert(self, name: str, oid: _OidArg, attr: int) -> None:
        """
        insert(name: str, oid: Oid, attr: FileMode)

        Insert or replace an entry in the treebuilder.

        Parameters:

        attr
            Available values are FileMode.BLOB, FileMode.BLOB_EXECUTABLE,
            FileMode.TREE, FileMode.LINK and FileMode.COMMIT.
        """
        ...
    def remove(self, name: str) -> None:
        """
        remove(name: str)

        Remove an entry from the builder.
        """
        ...
    def write(self) -> Oid:
        """
        write() -> Oid

        Write the tree to the given repository.
        """
        ...
    def __len__(self) -> int:
        """Return len(self)."""
        ...

@final
class Walker:
    """Revision walker."""
    def hide(self, oid: _OidArg) -> None:
        """
        hide(oid: Oid)

        Mark a commit (and its ancestors) uninteresting for the output.
        """
        ...
    def push(self, oid: _OidArg) -> None:
        """
        push(oid: Oid)

        Mark a commit to start traversal from.
        """
        ...
    def reset(self) -> None:
        """
        reset()

        Reset the walking machinery for reuse.
        """
        ...
    def simplify_first_parent(self) -> None:
        """
        simplify_first_parent()

        Simplify the history by first-parent.
        """
        ...
    def sort(self, mode: SortMode) -> None:
        """
        sort(mode: enums.SortMode)

        Change the sorting mode (this resets the walker).
        """
        ...
    def __iter__(self) -> Iterator[Commit]:
        """Implement iter(self)."""
        ...
    def __next__(self) -> Commit:
        """Implement next(self)."""
        ...

@final
class Worktree:
    """Worktree object."""
    is_prunable: bool
    name: str
    path: str
    def prune(self, force: bool = False) -> None:
        """
        prune(force=False)

        Prune a worktree object.
        """
        ...

def discover_repository(path: str, across_fs: bool = False, ceiling_dirs: str = ...) -> str:
    """
    discover_repository(path: str, across_fs: bool = False[, ceiling_dirs: str]) -> str

    Look for a git repository and return its path. If not found returns None.
    """
    ...
def filter_register(name: str, filter_cls: type[Filter], priority: int = ...) -> None:
    """
    filter_register(name: str, filter_cls: Type[Filter], [priority: int = C.GIT_FILTER_DRIVER_PRIORITY]) -> None

    Register a filter under the given name.

    Filters will be run in order of `priority` on smudge (to workdir) and in
    reverse order of priority on clean (to odb).

    Two filters are preregistered with libgit2:
        - GIT_FILTER_CRLF with priority 0
        - GIT_FILTER_IDENT with priority 100

    `priority` defaults to GIT_FILTER_DRIVER_PRIORITY which imitates a core
    Git filter driver that will be run last on checkout (smudge) and first 
    on checkin (clean).

    Note that the filter registry is not thread safe. Any registering or
    deregistering of filters should be done outside of any possible usage
    of the filters.
    """
    ...
def filter_unregister(name: str) -> None:
    """
    filter_unregister(name: str) -> None

    Unregister the given filter.

    Note that the filter registry is not thread safe. Any registering or
    deregistering of filters should be done outside of any possible usage
    of the filters.
    """
    ...
def hash(data: bytes) -> Oid:
    """
    hash(data: bytes) -> Oid

    Returns the oid of a new blob from a string without actually writing to
    the odb.
    """
    ...
def hashfile(path: str) -> Oid:
    """
    hashfile(path: str) -> Oid

    Returns the oid of a new blob from a file path without actually writing
    to the odb.
    """
    ...
def init_file_backend(path: str, flags: int = 0) -> object:
    """
    init_file_backend(path: str, flags: int = 0) -> object

    Open repo backend given path.
    """
    ...
def option(opt: Option, *args: Any) -> int | str | tuple[int, int] | None:
    """
    option(option, ...)

    Get or set a libgit2 option.

    Parameters:

    GIT_OPT_GET_SEARCH_PATH, level
        Get the config search path for the given level.

    GIT_OPT_SET_SEARCH_PATH, level, path
        Set the config search path for the given level.

    GIT_OPT_GET_MWINDOW_SIZE
        Get the maximum mmap window size.

    GIT_OPT_SET_MWINDOW_SIZE, size
        Set the maximum mmap window size.

    GIT_OPT_GET_OWNER_VALIDATION
        Gets the owner validation setting for repository directories.

    GIT_OPT_SET_OWNER_VALIDATION, enabled
        Set that repository directories should be owned by the current user.
        The default is to validate ownership.
    """
    ...
def reference_is_valid_name(refname: str) -> bool:
    """
    reference_is_valid_name(refname: str) -> bool

    Check if the passed string is a valid reference name.
    """
    ...
def tree_entry_cmp(a: Object, b: Object) -> int:
    """
    tree_entry_cmp(a: Object, b: Object) -> int

    Rich comparison for objects, only available when the objects have been
    obtained through a tree. The sort criteria is the one Git uses to sort
    tree entries in a tree object. This function wraps git_tree_entry_cmp.

    Returns < 0 if a is before b, > 0 if a is after b, and 0 if a and b are
    the same.
    """
    ...
def _cache_enums() -> None:
    """
    _cache_enums()

    For internal use only. Do not call this from user code.

    Let the _pygit2 C module cache references to Python enums
    defined in pygit2.enums.
    """
    ...

_OidArg: TypeAlias = str | Oid
