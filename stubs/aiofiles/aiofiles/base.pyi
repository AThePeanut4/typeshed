"""Various base classes."""

from collections.abc import Awaitable, Callable, Generator
from contextlib import AbstractAsyncContextManager
from types import TracebackType
from typing import Any, BinaryIO, Generic, TextIO, TypeVar
from typing_extensions import Self

_T = TypeVar("_T")
_V_co = TypeVar("_V_co", covariant=True)

class AsyncBase(Generic[_T]):
    def __init__(self, file: TextIO | BinaryIO | None, loop: Any, executor: Any) -> None: ...
    def __aiter__(self) -> Self:
        """We are our own iterator."""
        ...
    async def __anext__(self) -> _T:
        """Simulate normal file iteration."""
        ...

class AsyncIndirectBase(AsyncBase[_T]):
    def __init__(self, name: str, loop: Any, executor: Any, indirect: Callable[[], TextIO | BinaryIO]) -> None: ...

class AiofilesContextManager(Awaitable[_V_co], AbstractAsyncContextManager[_V_co]):
    """An adjusted async context manager for aiofiles."""
    def __init__(self, coro: Awaitable[_V_co]) -> None: ...
    def __await__(self) -> Generator[Any, Any, _V_co]: ...
    async def __aenter__(self) -> _V_co: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
