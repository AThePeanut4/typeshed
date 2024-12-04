"""
GIT_* enum values for compatibility with legacy code.

These values are deprecated starting with pygit2 1.14.
User programs should migrate to the enum classes defined in `pygit2.enums`.

Note that our C module _pygit2 already exports many libgit2 enums
(which are all imported by __init__.py). This file only exposes the enums
that are not available through _pygit2.
"""

GIT_FEATURE_THREADS: int
GIT_FEATURE_HTTPS: int
GIT_FEATURE_SSH: int
GIT_FEATURE_NSEC: int
GIT_REPOSITORY_INIT_BARE: int
GIT_REPOSITORY_INIT_NO_REINIT: int
GIT_REPOSITORY_INIT_NO_DOTGIT_DIR: int
GIT_REPOSITORY_INIT_MKDIR: int
GIT_REPOSITORY_INIT_MKPATH: int
GIT_REPOSITORY_INIT_EXTERNAL_TEMPLATE: int
GIT_REPOSITORY_INIT_RELATIVE_GITLINK: int
GIT_REPOSITORY_INIT_SHARED_UMASK: int
GIT_REPOSITORY_INIT_SHARED_GROUP: int
GIT_REPOSITORY_INIT_SHARED_ALL: int
GIT_REPOSITORY_OPEN_NO_SEARCH: int
GIT_REPOSITORY_OPEN_CROSS_FS: int
GIT_REPOSITORY_OPEN_BARE: int
GIT_REPOSITORY_OPEN_NO_DOTGIT: int
GIT_REPOSITORY_OPEN_FROM_ENV: int
GIT_REPOSITORY_STATE_NONE: int
GIT_REPOSITORY_STATE_MERGE: int
GIT_REPOSITORY_STATE_REVERT: int
GIT_REPOSITORY_STATE_REVERT_SEQUENCE: int
GIT_REPOSITORY_STATE_CHERRYPICK: int
GIT_REPOSITORY_STATE_CHERRYPICK_SEQUENCE: int
GIT_REPOSITORY_STATE_BISECT: int
GIT_REPOSITORY_STATE_REBASE: int
GIT_REPOSITORY_STATE_REBASE_INTERACTIVE: int
GIT_REPOSITORY_STATE_REBASE_MERGE: int
GIT_REPOSITORY_STATE_APPLY_MAILBOX: int
GIT_REPOSITORY_STATE_APPLY_MAILBOX_OR_REBASE: int
GIT_ATTR_CHECK_FILE_THEN_INDEX: int
GIT_ATTR_CHECK_INDEX_THEN_FILE: int
GIT_ATTR_CHECK_INDEX_ONLY: int
GIT_ATTR_CHECK_NO_SYSTEM: int
GIT_ATTR_CHECK_INCLUDE_HEAD: int
GIT_ATTR_CHECK_INCLUDE_COMMIT: int
GIT_FETCH_PRUNE_UNSPECIFIED: int
GIT_FETCH_PRUNE: int
GIT_FETCH_NO_PRUNE: int
GIT_CHECKOUT_NOTIFY_NONE: int
GIT_CHECKOUT_NOTIFY_CONFLICT: int
GIT_CHECKOUT_NOTIFY_DIRTY: int
GIT_CHECKOUT_NOTIFY_UPDATED: int
GIT_CHECKOUT_NOTIFY_UNTRACKED: int
GIT_CHECKOUT_NOTIFY_IGNORED: int
GIT_CHECKOUT_NOTIFY_ALL: int
GIT_STASH_APPLY_PROGRESS_NONE: int
GIT_STASH_APPLY_PROGRESS_LOADING_STASH: int
GIT_STASH_APPLY_PROGRESS_ANALYZE_INDEX: int
GIT_STASH_APPLY_PROGRESS_ANALYZE_MODIFIED: int
GIT_STASH_APPLY_PROGRESS_ANALYZE_UNTRACKED: int
GIT_STASH_APPLY_PROGRESS_CHECKOUT_UNTRACKED: int
GIT_STASH_APPLY_PROGRESS_CHECKOUT_MODIFIED: int
GIT_STASH_APPLY_PROGRESS_DONE: int
GIT_CREDENTIAL_USERPASS_PLAINTEXT: int
GIT_CREDENTIAL_SSH_KEY: int
GIT_CREDENTIAL_SSH_CUSTOM: int
GIT_CREDENTIAL_DEFAULT: int
GIT_CREDENTIAL_SSH_INTERACTIVE: int
GIT_CREDENTIAL_USERNAME: int
GIT_CREDENTIAL_SSH_MEMORY: int
