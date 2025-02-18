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

compress = ZSTD_compress
dumps = ZSTD_compress
encode = ZSTD_compress

def ZSTD_check(data: ReadableBuffer) -> int:
    """
    check(bytes): string -- Returns 0 or 1.

    Raises a zstd.Error exception if any error occurs.
    """
    ...

check = ZSTD_check
verify = ZSTD_check

def ZSTD_uncompress(data: ReadableBuffer, /) -> bytes:
    """
    decompress(bytes): string -- Returns uncompressed string.

    Raises a zstd.Error exception if any error occurs.
    """
    ...

decompress = ZSTD_uncompress
uncompress = ZSTD_uncompress
loads = ZSTD_uncompress
decode = ZSTD_uncompress

def ZSTD_version() -> str: ...
def ZSTD_version_number() -> int: ...
def ZSTD_threads_count() -> int: ...
def ZSTD_max_threads_count() -> int: ...
def ZSTD_external() -> int: ...
def ZSTD_with_asm() -> int: ...
def ZSTD_with_threads() -> int: ...
def ZSTD_legacy_support() -> int: ...
def ZSTD_max_compression_level() -> int: ...
def ZSTD_min_compression_level() -> int: ...
def version() -> str: ...
