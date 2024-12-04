"""Compression implementations for a Transport."""

from _typeshed import ReadableBuffer
from zlib import _Compress, _Decompress

class ZlibCompressor:
    z: _Compress
    def __init__(self) -> None: ...
    def __call__(self, data: ReadableBuffer) -> bytes: ...

class ZlibDecompressor:
    z: _Decompress
    def __init__(self) -> None: ...
    def __call__(self, data: ReadableBuffer) -> bytes: ...
