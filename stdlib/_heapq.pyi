"""
Heap queue algorithm (a.k.a. priority queue).

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.

Usage:

heap = []            # creates an empty heap
heappush(heap, item) # pushes a new item on the heap
item = heappop(heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heapreplace(heap, item) # pops and returns smallest item, and adds
                               # new item; the heap size is unchanged

Our API differs from textbook heap algorithms as follows:

- We use 0-based indexing.  This makes the relationship between the
  index for a node and the indexes for its children slightly less
  obvious, but is more suitable since Python uses 0-based indexing.

- Our heappop() method returns the smallest item, not the largest.

These two make it possible to view the heap as a regular Python list
without surprises: heap[0] is the smallest item, and heap.sort()
maintains the heap invariant!
"""

import sys
from _typeshed import SupportsRichComparisonT as _T  # All type variable use in this module requires comparability.
from typing import Final

__about__: Final[str]

def heapify(heap: list[_T], /) -> None: ...
def heappop(heap: list[_T], /) -> _T: ...
def heappush(heap: list[_T], item: _T, /) -> None: ...
def heappushpop(heap: list[_T], item: _T, /) -> _T: ...
def heapreplace(heap: list[_T], item: _T, /) -> _T: ...

if sys.version_info >= (3, 14):
    def heapify_max(heap: list[_T], /) -> None: ...
    def heappop_max(heap: list[_T], /) -> _T: ...
    def heappush_max(heap: list[_T], item: _T, /) -> None: ...
    def heappushpop_max(heap: list[_T], item: _T, /) -> _T: ...
    def heapreplace_max(heap: list[_T], item: _T, /) -> _T: ...
