import sys
from _heapq import *
from _typeshed import SupportsRichComparison
from collections.abc import Callable, Generator, Iterable
from typing import Any, Final, TypeVar

__all__ = ["heappush", "heappop", "heapify", "heapreplace", "merge", "nlargest", "nsmallest", "heappushpop"]

if sys.version_info >= (3, 14):
    # Added to __all__ in 3.14.1
    __all__ += ["heapify_max", "heappop_max", "heappush_max", "heappushpop_max", "heapreplace_max"]

_S = TypeVar("_S")

__about__: Final[str]

def merge(
    *iterables: Iterable[_S], key: Callable[[_S], SupportsRichComparison] | None = None, reverse: bool = False
) -> Generator[_S]:
    """
    Merge multiple sorted inputs into a single sorted output.

    Similar to sorted(itertools.chain(*iterables)) but returns a generator,
    does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

    If *key* is not None, applies a key function to each element to determine
    its sort order.

    >>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
    ['dog', 'cat', 'fish', 'horse', 'kangaroo']
    """
    ...
def nlargest(n: int, iterable: Iterable[_S], key: Callable[[_S], SupportsRichComparison] | None = None) -> list[_S]:
    """
    Find the n largest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    """
    ...
def nsmallest(n: int, iterable: Iterable[_S], key: Callable[[_S], SupportsRichComparison] | None = None) -> list[_S]:
    """
    Find the n smallest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key)[:n]
    """
    ...
def _heapify_max(heap: list[Any], /) -> None:
    """Maxheap variant of heapify."""
    ...
