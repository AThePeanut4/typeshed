"""Async wrappers for spooled temp files and temp directory objects"""

from _typeshed import Incomplete, OpenBinaryMode
from asyncio import AbstractEventLoop
from collections.abc import Generator, Iterable
from tempfile import TemporaryDirectory
from typing import TypeVar

from aiofiles.base import AsyncBase as AsyncBase
from aiofiles.threadpool.utils import (
    cond_delegate_to_executor as cond_delegate_to_executor,
    delegate_to_executor as delegate_to_executor,
    proxy_property_directly as proxy_property_directly,
)

_T = TypeVar("_T")

class AsyncSpooledTemporaryFile(AsyncBase[_T]):
    """Async wrapper for SpooledTemporaryFile class"""
    def fileno(self) -> Generator[Incomplete, Incomplete, Incomplete]: ...
    def rollover(self) -> Generator[Incomplete, Incomplete, Incomplete]: ...
    async def close(self) -> None: ...
    async def flush(self) -> None: ...
    async def isatty(self) -> bool: ...
    # All must return `AnyStr`:
    async def read(self, n: int = ..., /): ...
    async def readline(self, limit: int | None = ..., /): ...
    async def readlines(self, hint: int = ..., /) -> list[Incomplete]: ...
    # ---
    async def seek(self, offset: int, whence: int = ...) -> int: ...
    async def tell(self) -> int: ...
    async def truncate(self, size: int | None = ...) -> None: ...
    @property
    def closed(self) -> bool: ...
    @property
    def encoding(self) -> str: ...
    @property
    def mode(self) -> OpenBinaryMode: ...
    @property
    def name(self) -> str: ...
    @property
    def newlines(self) -> str: ...
    # Both should work with `AnyStr`, like in `tempfile`:
    async def write(self, s) -> int:
        """Implementation to anticipate rollover"""
        ...
    async def writelines(self, iterable: Iterable[Incomplete]) -> None:
        """Implementation to anticipate rollover"""
        ...

class AsyncTemporaryDirectory:
    """Async wrapper for TemporaryDirectory class"""
    async def cleanup(self) -> None: ...
    @property
    def name(self): ...  # should be `AnyStr`
    def __init__(
        self, file: TemporaryDirectory[Incomplete], loop: AbstractEventLoop | None, executor: Incomplete | None
    ) -> None: ...
    async def close(self) -> None: ...
