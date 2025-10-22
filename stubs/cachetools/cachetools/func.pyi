"""`functools.lru_cache` compatible memoizing function decorators."""

from collections.abc import Callable, Sequence
from typing import Any, Final, Generic, NamedTuple, TypeVar, overload

__all__: Final = ("fifo_cache", "lfu_cache", "lru_cache", "rr_cache", "ttl_cache")

_T = TypeVar("_T")
_R = TypeVar("_R")

class _CacheInfo(NamedTuple):
    hits: int
    misses: int
    maxsize: int | None
    currsize: int

class _cachetools_cache_wrapper(Generic[_R]):
    __wrapped__: Callable[..., _R]
    def __call__(self, /, *args: Any, **kwargs: Any) -> _R: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    def cache_parameters(self) -> dict[str, Any]: ...

@overload
def fifo_cache(
    maxsize: int | None = 128, typed: bool = False
) -> Callable[[Callable[..., _R]], _cachetools_cache_wrapper[_R]]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a First In First Out (FIFO)
    algorithm.
    """
    ...
@overload
def fifo_cache(maxsize: Callable[..., _R], typed: bool = False) -> _cachetools_cache_wrapper[_R]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a First In First Out (FIFO)
    algorithm.
    """
    ...
@overload
def lfu_cache(maxsize: int | None = 128, typed: bool = False) -> Callable[[Callable[..., _R]], _cachetools_cache_wrapper[_R]]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.
    """
    ...
@overload
def lfu_cache(maxsize: Callable[..., _R], typed: bool = False) -> _cachetools_cache_wrapper[_R]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.
    """
    ...
@overload
def lru_cache(maxsize: int | None = 128, typed: bool = False) -> Callable[[Callable[..., _R]], _cachetools_cache_wrapper[_R]]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm.
    """
    ...
@overload
def lru_cache(maxsize: Callable[..., _R], typed: bool = False) -> _cachetools_cache_wrapper[_R]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm.
    """
    ...
@overload
def rr_cache(
    maxsize: int | None = 128, choice: Callable[[Sequence[_T]], _T] | None = ..., typed: bool = False
) -> Callable[[Callable[..., _R]], _cachetools_cache_wrapper[_R]]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Random Replacement (RR)
    algorithm.
    """
    ...
@overload
def rr_cache(
    maxsize: Callable[..., _R], choice: Callable[[Sequence[_T]], _T] | None = ..., typed: bool = False
) -> _cachetools_cache_wrapper[_R]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Random Replacement (RR)
    algorithm.
    """
    ...
@overload
def ttl_cache(
    maxsize: int | None = 128, ttl: float = 600, timer: Callable[[], float] = ..., typed: bool = False
) -> Callable[[Callable[..., _R]], _cachetools_cache_wrapper[_R]]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    ...
@overload
def ttl_cache(
    maxsize: Callable[..., _R], ttl: float = 600, timer: Callable[[], float] = ..., typed: bool = False
) -> _cachetools_cache_wrapper[_R]:
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.
    """
    ...
