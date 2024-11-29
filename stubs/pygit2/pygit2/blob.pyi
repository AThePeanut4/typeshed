import io
import types
from _typeshed import WriteableBuffer
from contextlib import AbstractContextManager

from ._pygit2 import Blob, Oid
from .enums import BlobFilter

class _BlobIO(io.RawIOBase):
    """
    Low-level wrapper for streaming blob content.

    The underlying libgit2 git_writestream filter chain will be run
    in a separate thread. The GIL will be released while running
    libgit2 filtering.
    """
    def __init__(self, blob: Blob, as_path: str | None = None, flags: BlobFilter = ..., commit_id: Oid | None = None) -> None: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...
    def isatty() -> bool: ...  # type: ignore[misc]
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def readinto(self, b: WriteableBuffer, /) -> int: ...
    def close(self) -> None: ...

class BlobIO(io.BufferedReader, AbstractContextManager[_BlobIO]):  # type: ignore[misc]
    """
    Read-only wrapper for streaming blob content.

    Supports reading both raw and filtered blob content.
    Implements io.BufferedReader.

    Example:

        >>> with BlobIO(blob) as f:
        ...     while True:
        ...         # Read blob data in 1KB chunks until EOF is reached
        ...         chunk = f.read(1024)
        ...         if not chunk:
        ...             break

    By default, `BlobIO` will stream the raw contents of the blob, but it
    can also be used to stream filtered content (i.e. to read the content
    after applying filters which would be used when checking out the blob
    to the working directory).

    Example:

        >>> with BlobIO(blob, as_path='my_file.ext') as f:
        ...     # Read the filtered content which would be returned upon
        ...     # running 'git checkout -- my_file.txt'
        ...     filtered_data = f.read()
    """
    def __init__(self, blob: Blob, as_path: str | None = None, flags: BlobFilter = ..., commit_id: Oid | None = None) -> None:
        """
        Wrap the specified blob.

        Parameters:
            blob: The blob to wrap.
            as_path: Filter the contents of the blob as if it had the specified
                path. If `as_path` is None, the raw contents of the blob will
                be read.
            flags: A combination of enums.BlobFilter constants
                (only applicable when `as_path` is set).
            commit_id: Commit to load attributes from when
                ATTRIBUTES_FROM_COMMIT is specified in `flags`
                (only applicable when `as_path` is set).
        """
        ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...
