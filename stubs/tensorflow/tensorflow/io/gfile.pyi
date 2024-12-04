"""Public API for tf._api.v2.io.gfile namespace"""

from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Iterable

def rmtree(path: StrOrBytesPath) -> None:
    """
    Deletes everything under path recursively.

    Args:
      path: string, a path

    Raises:
      errors.OpError: If the operation fails.
    """
    ...
def isdir(path: StrOrBytesPath) -> bool:
    """
    Returns whether the path is a directory or not.

    Args:
      path: string, path to a potential directory

    Returns:
      True, if the path is a directory; False otherwise
    """
    ...
def listdir(path: StrOrBytesPath) -> list[str]:
    """
    Returns a list of entries contained within a directory.

    The list is in arbitrary order. It does not contain the special entries "."
    and "..".

    Args:
      path: string, path to a directory

    Returns:
      [filename1, filename2, ... filenameN] as strings

    Raises:
      errors.NotFoundError if directory doesn't exist
    """
    ...
def exists(path: StrOrBytesPath) -> bool:
    """
    Determines whether a path exists or not.

    >>> with open("/tmp/x", "w") as f:
    ...   f.write("asdf")
    ...
    4
    >>> tf.io.gfile.exists("/tmp/x")
    True

    You can also specify the URI scheme for selecting a different filesystem:

    >>> # for a GCS filesystem path:
    >>> # tf.io.gfile.exists("gs://bucket/file")
    >>> # for a local filesystem:
    >>> with open("/tmp/x", "w") as f:
    ...   f.write("asdf")
    ...
    4
    >>> tf.io.gfile.exists("file:///tmp/x")
    True

    This currently returns `True` for existing directories but don't rely on this
    behavior, especially if you are using cloud filesystems (e.g., GCS, S3,
    Hadoop):

    >>> tf.io.gfile.exists("/tmp")
    True

    Args:
      path: string, a path

    Returns:
      True if the path exists, whether it's a file or a directory.
      False if the path does not exist and there are no filesystem errors.

    Raises:
      errors.OpError: Propagates any errors reported by the FileSystem API.
    """
    ...
def copy(src: StrOrBytesPath, dst: StrOrBytesPath, overwrite: bool = False) -> None:
    """
    Copies data from `src` to `dst`.

    >>> with open("/tmp/x", "w") as f:
    ...   f.write("asdf")
    ...
    4
    >>> tf.io.gfile.exists("/tmp/x")
    True
    >>> tf.io.gfile.copy("/tmp/x", "/tmp/y")
    >>> tf.io.gfile.exists("/tmp/y")
    True
    >>> tf.io.gfile.remove("/tmp/y")

    You can also specify the URI scheme for selecting a different filesystem:

    >>> with open("/tmp/x", "w") as f:
    ...   f.write("asdf")
    ...
    4
    >>> tf.io.gfile.copy("/tmp/x", "file:///tmp/y")
    >>> tf.io.gfile.exists("/tmp/y")
    True
    >>> tf.io.gfile.remove("/tmp/y")

    Note that you need to always specify a file name, even if moving into a new
    directory. This is because some cloud filesystems don't have the concept of a
    directory.

    >>> with open("/tmp/x", "w") as f:
    ...   f.write("asdf")
    ...
    4
    >>> tf.io.gfile.mkdir("/tmp/new_dir")
    >>> tf.io.gfile.copy("/tmp/x", "/tmp/new_dir/y")
    >>> tf.io.gfile.exists("/tmp/new_dir/y")
    True
    >>> tf.io.gfile.rmtree("/tmp/new_dir")

    If you want to prevent errors if the path already exists, you can use
    `overwrite` argument:

    >>> with open("/tmp/x", "w") as f:
    ...   f.write("asdf")
    ...
    4
    >>> tf.io.gfile.copy("/tmp/x", "file:///tmp/y")
    >>> tf.io.gfile.copy("/tmp/x", "file:///tmp/y", overwrite=True)
    >>> tf.io.gfile.remove("/tmp/y")

    Note that the above will still result in an error if you try to overwrite a
    directory with a file.

    Note that you cannot copy a directory, only file arguments are supported.

    Args:
      src: string, name of the file whose contents need to be copied
      dst: string, name of the file to which to copy to
      overwrite: boolean, if false it's an error for `dst` to be occupied by an
        existing file.

    Raises:
      errors.OpError: If the operation fails.
    """
    ...
def makedirs(path: StrOrBytesPath) -> None:
    """
    Creates a directory and all parent/intermediate directories.

    It succeeds if path already exists and is writable.

    Args:
      path: string, name of the directory to be created

    Raises:
      errors.OpError: If the operation fails.
    """
    ...
def glob(pattern: str | bytes | Iterable[str | bytes]) -> list[str]:
    r"""
    Returns a list of files that match the given pattern(s).

    The patterns are defined as strings. Supported patterns are defined
    here. Note that the pattern can be a Python iteratable of string patterns.

    The format definition of the pattern is:

    **pattern**: `{ term }`

    **term**:
      * `'*'`: matches any sequence of non-'/' characters
      * `'?'`: matches a single non-'/' character
      * `'[' [ '^' ] { match-list } ']'`: matches any single
        character (not) on the list
      * `c`: matches character `c`  where `c != '*', '?', '\\', '['`
      * `'\\' c`: matches character `c`

    **character range**:
      * `c`: matches character `c` while `c != '\\', '-', ']'`
      * `'\\' c`: matches character `c`
      * `lo '-' hi`: matches character `c` for `lo <= c <= hi`

    Examples:

    >>> tf.io.gfile.glob("*.py")
    ... # For example, ['__init__.py']

    >>> tf.io.gfile.glob("__init__.??")
    ... # As above

    >>> files = {"*.py"}
    >>> the_iterator = iter(files)
    >>> tf.io.gfile.glob(the_iterator)
    ... # As above

    See the C++ function `GetMatchingPaths` in
    [`core/platform/file_system.h`]
    (../../../core/platform/file_system.h)
    for implementation details.

    Args:
      pattern: string or iterable of strings. The glob pattern(s).

    Returns:
      A list of strings containing filenames that match the given pattern(s).

    Raises:
      errors.OpError: If there are filesystem / directory listing errors.
      errors.NotFoundError: If pattern to be matched is an invalid directory.
    """
    ...
def __getattr__(name: str) -> Incomplete: ...
