from enum import IntEnum, IntFlag

class ApplyLocation(IntEnum):
    """Possible application locations for patches"""
    WORKDIR = 0
    INDEX = 1
    BOTH = 2

class AttrCheck(IntFlag):
    """An enumeration."""
    FILE_THEN_INDEX = 0x0
    INDEX_THEN_FILE = 0x1
    INDEX_ONLY = 0x2
    NO_SYSTEM = 0x4
    INCLUDE_HEAD = 0x8
    INCLUDE_COMMIT = 0x10

class BlameFlag(IntFlag):
    """An enumeration."""
    NORMAL = 0x0
    TRACK_COPIES_SAME_FILE = 0x1
    TRACK_COPIES_SAME_COMMIT_MOVES = 0x2
    TRACK_COPIES_SAME_COMMIT_COPIES = 0x4
    TRACK_COPIES_ANY_COMMIT_COPIES = 0x8
    FIRST_PARENT = 0x10
    USE_MAILMAP = 0x20
    IGNORE_WHITESPACE = 0x40

class BlobFilter(IntFlag):
    """An enumeration."""
    CHECK_FOR_BINARY = 0x1
    NO_SYSTEM_ATTRIBUTES = 0x2
    ATTRIBUTES_FROM_HEAD = 0x4
    ATTRIBUTES_FROM_COMMIT = 0x8

class BranchType(IntFlag):
    """An enumeration."""
    LOCAL = 0x1
    REMOTE = 0x2
    ALL = 0x3

class CheckoutNotify(IntFlag):
    """
    Checkout notification flags

    Checkout will invoke an options notification callback
    (`CheckoutCallbacks.checkout_notify`) for certain cases - you pick which
    ones via `CheckoutCallbacks.checkout_notify_flags`.
    """
    NONE = 0x0
    CONFLICT = 0x1
    DIRTY = 0x2
    UPDATED = 0x4
    UNTRACKED = 0x8
    IGNORED = 0x10
    ALL = 0xFFFF

class CheckoutStrategy(IntFlag):
    """An enumeration."""
    NONE = 0x0
    SAFE = 0x1
    FORCE = 0x2
    RECREATE_MISSING = 0x4
    ALLOW_CONFLICTS = 0x10
    REMOVE_UNTRACKED = 0x20
    REMOVE_IGNORED = 0x40
    UPDATE_ONLY = 0x80
    DONT_UPDATE_INDEX = 0x100
    NO_REFRESH = 0x200
    SKIP_UNMERGED = 0x400
    USE_OURS = 0x800
    USE_THEIRS = 0x1000
    DISABLE_PATHSPEC_MATCH = 0x2000
    SKIP_LOCKED_DIRECTORIES = 0x40000
    DONT_OVERWRITE_IGNORED = 0x80000
    CONFLICT_STYLE_MERGE = 0x100000
    CONFLICT_STYLE_DIFF3 = 0x200000
    DONT_REMOVE_EXISTING = 0x400000
    DONT_WRITE_INDEX = 0x800000
    DRY_RUN = 0x1000000
    CONFLICT_STYLE_ZDIFF3 = 0x200000

class ConfigLevel(IntEnum):
    """
    Priority level of a config file.
    These priority levels correspond to the natural escalation logic
    (from higher to lower) when searching for config entries in git.git.
    """
    PROGRAMDATA = 1
    SYSTEM = 2
    XDG = 3
    GLOBAL = 4
    LOCAL = 5
    WORKTREE = 6
    APP = 7
    HIGHEST_LEVEL = -1

class CredentialType(IntFlag):
    """
    Supported credential types. This represents the various types of
    authentication methods supported by the library.
    """
    USERPASS_PLAINTEXT = 0x1
    SSH_KEY = 0x2
    SSH_CUSTOM = 0x4
    DEFAULT = 0x8
    SSH_INTERACTIVE = 0x10
    USERNAME = 0x20
    SSH_MEMORY = 0x40

class DeltaStatus(IntEnum):
    """
    What type of change is described by a DiffDelta?

    `RENAMED` and `COPIED` will only show up if you run
    `find_similar()` on the Diff object.

    `TYPECHANGE` only shows up given `INCLUDE_TYPECHANGE`
    in the DiffOption option flags (otherwise type changes
    will be split into ADDED / DELETED pairs).
    """
    UNMODIFIED = 0
    ADDED = 1
    DELETED = 2
    MODIFIED = 3
    RENAMED = 4
    COPIED = 5
    IGNORED = 6
    UNTRACKED = 7
    TYPECHANGE = 8
    UNREADABLE = 9
    CONFLICTED = 10

class DescribeStrategy(IntEnum):
    """
    Reference lookup strategy.

    These behave like the --tags and --all options to git-describe,
    namely they say to look for any reference in either refs/tags/ or
    refs/ respectively.
    """
    DEFAULT = 0
    TAGS = 1
    ALL = 2

class DiffFind(IntFlag):
    """Flags to control the behavior of diff rename/copy detection."""
    FIND_BY_CONFIG = 0x0
    FIND_RENAMES = 0x1
    FIND_RENAMES_FROM_REWRITES = 0x2
    FIND_COPIES = 0x4
    FIND_COPIES_FROM_UNMODIFIED = 0x8
    FIND_REWRITES = 0x10
    BREAK_REWRITES = 0x20
    FIND_AND_BREAK_REWRITES = 0x30
    FIND_FOR_UNTRACKED = 0x40
    FIND_ALL = 0xFF
    FIND_IGNORE_LEADING_WHITESPACE = 0x0
    FIND_IGNORE_WHITESPACE = 0x1000
    FIND_DONT_IGNORE_WHITESPACE = 0x2000
    FIND_EXACT_MATCH_ONLY = 0x4000
    BREAK_REWRITES_FOR_RENAMES_ONLY = 0x8000
    FIND_REMOVE_UNMODIFIED = 0x10000

class DiffFlag(IntFlag):
    """
    Flags for the delta object and the file objects on each side.

    These flags are used for both the `flags` value of the `DiffDelta`
    and the flags for the `DiffFile` objects representing the old and
    new sides of the delta.  Values outside of this public range should be
    considered reserved for internal or future use.
    """
    BINARY = 0x1
    NOT_BINARY = 0x2
    VALID_ID = 0x4
    EXISTS = 0x8
    VALID_SIZE = 0x10

class DiffOption(IntFlag):
    """
    Flags for diff options.  A combination of these flags can be passed
    in via the `flags` value in `diff_*` functions.
    """
    NORMAL = 0x0
    REVERSE = 0x1
    INCLUDE_IGNORED = 0x2
    RECURSE_IGNORED_DIRS = 0x4
    INCLUDE_UNTRACKED = 0x8
    RECURSE_UNTRACKED_DIRS = 0x10
    INCLUDE_UNMODIFIED = 0x20
    INCLUDE_TYPECHANGE = 0x40
    INCLUDE_TYPECHANGE_TREES = 0x80
    IGNORE_FILEMODE = 0x100
    IGNORE_SUBMODULES = 0x200
    IGNORE_CASE = 0x400
    INCLUDE_CASECHANGE = 0x800
    DISABLE_PATHSPEC_MATCH = 0x1000
    SKIP_BINARY_CHECK = 0x2000
    ENABLE_FAST_UNTRACKED_DIRS = 0x4000
    UPDATE_INDEX = 0x8000
    INCLUDE_UNREADABLE = 0x10000
    INCLUDE_UNREADABLE_AS_UNTRACKED = 0x20000
    INDENT_HEURISTIC = 0x40000
    IGNORE_BLANK_LINES = 0x80000
    FORCE_TEXT = 0x100000
    FORCE_BINARY = 0x200000
    IGNORE_WHITESPACE = 0x400000
    IGNORE_WHITESPACE_CHANGE = 0x800000
    IGNORE_WHITESPACE_EOL = 0x1000000
    SHOW_UNTRACKED_CONTENT = 0x2000000
    SHOW_UNMODIFIED = 0x4000000
    PATIENCE = 0x10000000
    MINIMAL = 0x20000000
    SHOW_BINARY = 0x40000000

class DiffStatsFormat(IntFlag):
    """Formatting options for diff stats"""
    NONE = 0x0
    FULL = 0x1
    SHORT = 0x2
    NUMBER = 0x4
    INCLUDE_SUMMARY = 0x8

class Feature(IntFlag):
    """
    Combinations of these values describe the features with which libgit2
    was compiled.
    """
    THREADS = 0x1
    HTTPS = 0x2
    SSH = 0x4
    NSEC = 0x8

class FetchPrune(IntEnum):
    """Acceptable prune settings when fetching."""
    UNSPECIFIED = 0
    PRUNE = 1
    NO_PRUNE = 2

class FileMode(IntFlag):
    """An enumeration."""
    UNREADABLE = 0x0
    TREE = 0x4000
    BLOB = 0x81A4
    BLOB_EXECUTABLE = 0x81ED
    LINK = 0xA000
    COMMIT = 0xE000

class FileStatus(IntFlag):
    """
    Status flags for a single file.

    A combination of these values will be returned to indicate the status of
    a file. Status compares the working directory, the index, and the current
    HEAD of the repository.  The `INDEX_...` set of flags represents the status
    of the file in the index relative to the HEAD, and the `WT_...` set of
    flags represents the status of the file in the working directory relative
    to the index.
    """
    CURRENT = 0x0
    INDEX_NEW = 0x1
    INDEX_MODIFIED = 0x2
    INDEX_DELETED = 0x4
    INDEX_RENAMED = 0x8
    INDEX_TYPECHANGE = 0x10
    WT_NEW = 0x80
    WT_MODIFIED = 0x100
    WT_DELETED = 0x200
    WT_TYPECHANGE = 0x400
    WT_RENAMED = 0x800
    WT_UNREADABLE = 0x1000
    IGNORED = 0x4000
    CONFLICTED = 0x8000

class FilterFlag(IntFlag):
    """Filter option flags."""
    DEFAULT = 0x0
    ALLOW_UNSAFE = 0x1
    NO_SYSTEM_ATTRIBUTES = 0x2
    ATTRIBUTES_FROM_HEAD = 0x4
    ATTRIBUTES_FROM_COMMIT = 0x8

class FilterMode(IntEnum):
    """
    Filters are applied in one of two directions: smudging - which is
    exporting a file from the Git object database to the working directory,
    and cleaning - which is importing a file from the working directory to
    the Git object database.  These values control which direction of
    change is being applied.
    """
    TO_WORKTREE = 0
    SMUDGE = 0
    TO_ODB = 1
    CLEAN = 1

class MergeAnalysis(IntFlag):
    """The results of `Repository.merge_analysis` indicate the merge opportunities."""
    NONE = 0x0
    NORMAL = 0x1
    UP_TO_DATE = 0x2
    FASTFORWARD = 0x4
    UNBORN = 0x8

class MergeFavor(IntEnum):
    """
    Merge file favor options for `Repository.merge` instruct the file-level
    merging functionality how to deal with conflicting regions of the files.
    """
    NORMAL = 0
    OURS = 1
    THEIRS = 2
    UNION = 3

class MergeFileFlag(IntFlag):
    """File merging flags"""
    DEFAULT = 0x0
    STYLE_MERGE = 0x1
    STYLE_DIFF3 = 0x2
    SIMPLIFY_ALNUM = 0x4
    IGNORE_WHITESPACE = 0x8
    IGNORE_WHITESPACE_CHANGE = 0x10
    IGNORE_WHITESPACE_EOL = 0x20
    DIFF_PATIENCE = 0x40
    DIFF_MINIMAL = 0x80
    STYLE_ZDIFF3 = 0x100
    ACCEPT_CONFLICTS = 0x200

class MergeFlag(IntFlag):
    """
    Flags for `Repository.merge` options.
    A combination of these flags can be passed in via the `flags` value.
    """
    FIND_RENAMES = 0x1
    FAIL_ON_CONFLICT = 0x2
    SKIP_REUC = 0x4
    NO_RECURSIVE = 0x8
    VIRTUAL_BASE = 0x10

class MergePreference(IntFlag):
    """The user's stated preference for merges."""
    NONE = 0x0
    NO_FASTFORWARD = 0x1
    FASTFORWARD_ONLY = 0x2

class ObjectType(IntEnum):
    """An enumeration."""
    ANY = -2
    INVALID = -1
    COMMIT = 1
    TREE = 2
    BLOB = 3
    TAG = 4
    OFS_DELTA = 6
    REF_DELTA = 7

class Option(IntEnum):
    """Global libgit2 library options"""
    GET_MWINDOW_SIZE = 0
    SET_MWINDOW_SIZE = 1
    GET_MWINDOW_MAPPED_LIMIT = 2
    SET_MWINDOW_MAPPED_LIMIT = 3
    GET_SEARCH_PATH = 4
    SET_SEARCH_PATH = 5
    SET_CACHE_OBJECT_LIMIT = 6
    SET_CACHE_MAX_SIZE = 7
    ENABLE_CACHING = 8
    GET_CACHED_MEMORY = 9
    GET_TEMPLATE_PATH = 10
    SET_TEMPLATE_PATH = 11
    SET_SSL_CERT_LOCATIONS = 12
    SET_USER_AGENT = 13
    ENABLE_STRICT_OBJECT_CREATION = 14
    ENABLE_STRICT_SYMBOLIC_REF_CREATION = 15
    SET_SSL_CIPHERS = 16
    GET_USER_AGENT = 17
    ENABLE_OFS_DELTA = 18
    ENABLE_FSYNC_GITDIR = 19
    GET_WINDOWS_SHAREMODE = 20
    SET_WINDOWS_SHAREMODE = 21
    ENABLE_STRICT_HASH_VERIFICATION = 22
    SET_ALLOCATOR = 23
    ENABLE_UNSAVED_INDEX_SAFETY = 24
    GET_PACK_MAX_OBJECTS = 25
    SET_PACK_MAX_OBJECTS = 26
    DISABLE_PACK_KEEP_FILE_CHECKS = 27
    GET_OWNER_VALIDATION = 35
    SET_OWNER_VALIDATION = 36

class ReferenceFilter(IntEnum):
    """Filters for References.iterator()."""
    ALL = 0
    BRANCHES = 1
    TAGS = 2

class ReferenceType(IntFlag):
    """Basic type of any Git reference."""
    INVALID = 0x0
    DIRECT = 0x1
    SYMBOLIC = 0x2
    ALL = 0x3

class RepositoryInitFlag(IntFlag):
    """Option flags for pygit2.init_repository()."""
    BARE = 0x1
    NO_REINIT = 0x2
    NO_DOTGIT_DIR = 0x4
    MKDIR = 0x8
    MKPATH = 0x10
    EXTERNAL_TEMPLATE = 0x20
    RELATIVE_GITLINK = 0x40

class RepositoryInitMode(IntEnum):
    """Mode options for pygit2.init_repository()."""
    SHARED_UMASK = 0
    SHARED_GROUP = 1533
    SHARED_ALL = 1535

class RepositoryOpenFlag(IntFlag):
    """Option flags for Repository.__init__()."""
    DEFAULT = 0x0
    NO_SEARCH = 0x1
    CROSS_FS = 0x2
    BARE = 0x4
    NO_DOTGIT = 0x8
    FROM_ENV = 0x10

class RepositoryState(IntEnum):
    """
    Repository state: These values represent possible states for the repository
    to be in, based on the current operation which is ongoing.
    """
    NONE = 0
    MERGE = 1
    REVERT = 2
    REVERT_SEQUENCE = 3
    CHERRYPICK = 4
    CHERRYPICK_SEQUENCE = 5
    BISECT = 6
    REBASE = 7
    REBASE_INTERACTIVE = 8
    REBASE_MERGE = 9
    APPLY_MAILBOX = 10
    APPLY_MAILBOX_OR_REBASE = 11

class ResetMode(IntEnum):
    """Kinds of reset operation."""
    SOFT = 1
    MIXED = 2
    HARD = 3

class RevSpecFlag(IntFlag):
    """
    Revparse flags.
    These indicate the intended behavior of the spec passed to Repository.revparse()
    """
    SINGLE = 0x1
    RANGE = 0x2
    MERGE_BASE = 0x4

class SortMode(IntFlag):
    """Flags to specify the sorting which a revwalk should perform."""
    NONE = 0x0
    TOPOLOGICAL = 0x1
    TIME = 0x2
    REVERSE = 0x4

class StashApplyProgress(IntEnum):
    """Stash apply progression states"""
    NONE = 0
    LOADING_STASH = 1
    ANALYZE_INDEX = 2
    ANALYZE_MODIFIED = 3
    ANALYZE_UNTRACKED = 4
    CHECKOUT_UNTRACKED = 5
    CHECKOUT_MODIFIED = 6
    DONE = 7

class SubmoduleIgnore(IntEnum):
    """An enumeration."""
    UNSPECIFIED = -1
    NONE = 1
    UNTRACKED = 2
    DIRTY = 3
    ALL = 4

class SubmoduleStatus(IntFlag):
    """An enumeration."""
    IN_HEAD = 0x1
    IN_INDEX = 0x2
    IN_CONFIG = 0x4
    IN_WD = 0x8
    INDEX_ADDED = 0x10
    INDEX_DELETED = 0x20
    INDEX_MODIFIED = 0x40
    WD_UNINITIALIZED = 0x80
    WD_ADDED = 0x100
    WD_DELETED = 0x200
    WD_MODIFIED = 0x400
    WD_INDEX_MODIFIED = 0x800
    WD_WD_MODIFIED = 0x1000
    WD_UNTRACKED = 0x2000
