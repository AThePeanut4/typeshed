from _typeshed import ReadableBuffer

class Error(Exception): ...

def ZSTD_compress(data: ReadableBuffer, level: int = ..., threads: int = ..., /) -> bytes:
    """
    compress_mt(string[, level, threads]): bytes -- Returns compressed string.

    Optional arg level is the compression level, from 1 (fastest) to 22 (slowest). The default value is 3.
    Optional arg threads is the number of worker threads, from 0 to 200. 0 - auto-tune by cpu cores count. The default value is 0.
    Also supports ultra-fast levels from -100 (fastest) to -1 (less fast) since module compiled with ZSTD 1.3.4+.

    Input data length limited by 2Gb by Python API.
    Raises a zstd.Error exception if any error occurs.
    """
    ...
def ZSTD_external() -> int:
    """ZSTD_external(): int -- Returns 0 or 1 if ZSTD library build as external."""
    ...
def ZSTD_uncompress(data: ReadableBuffer, /) -> bytes:
    """
    decompress(bytes): string -- Returns uncompressed string.

    Raises a zstd.Error exception if any error occurs.
    """
    ...
def ZSTD_version() -> str:
    """ZSTD_version(): string -- Returns ZSTD library version as string."""
    ...
def ZSTD_version_number() -> int:
    """
    ZSTD_version_number(): int -- Returns ZSTD library version as integer.
    Format of the number is: major * 100*100 + minor * 100 + release.
    """
    ...
def ZSTD_threads_count() -> int:
    """ZSTD_threads_count(): int -- Returns ZSTD determined CPU cores count in integer."""
    ...
def ZSTD_max_threads_count() -> int:
    """ZSTD_max_threads_count(): int -- Returns ZSTD library determined maximum working threads count in integer."""
    ...
def compress(data: ReadableBuffer, level: int = ..., threads: int = ..., /) -> bytes:
    """
    compress_mt(string[, level, threads]): bytes -- Returns compressed string.

    Optional arg level is the compression level, from 1 (fastest) to 22 (slowest). The default value is 3.
    Optional arg threads is the number of worker threads, from 0 to 200. 0 - auto-tune by cpu cores count. The default value is 0.
    Also supports ultra-fast levels from -100 (fastest) to -1 (less fast) since module compiled with ZSTD 1.3.4+.

    Input data length limited by 2Gb by Python API.
    Raises a zstd.Error exception if any error occurs.
    """
    ...
def decompress(data: ReadableBuffer, /) -> bytes:
    """
    decompress(bytes): string -- Returns uncompressed string.

    Raises a zstd.Error exception if any error occurs.
    """
    ...
def dumps(data: ReadableBuffer, level: int = ..., threads: int = ..., /) -> bytes:
    """
    compress_mt(string[, level, threads]): bytes -- Returns compressed string.

    Optional arg level is the compression level, from 1 (fastest) to 22 (slowest). The default value is 3.
    Optional arg threads is the number of worker threads, from 0 to 200. 0 - auto-tune by cpu cores count. The default value is 0.
    Also supports ultra-fast levels from -100 (fastest) to -1 (less fast) since module compiled with ZSTD 1.3.4+.

    Input data length limited by 2Gb by Python API.
    Raises a zstd.Error exception if any error occurs.
    """
    ...
def loads(data: ReadableBuffer, /) -> bytes:
    """
    decompress(bytes): string -- Returns uncompressed string.

    Raises a zstd.Error exception if any error occurs.
    """
    ...
def uncompress(data: ReadableBuffer, /) -> bytes:
    """
    decompress(bytes): string -- Returns uncompressed string.

    Raises a zstd.Error exception if any error occurs.
    """
    ...
def version() -> str:
    """version(): string -- Returns this module version as string."""
    ...
