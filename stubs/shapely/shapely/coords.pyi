"""Coordinate sequence utilities"""

from array import array
from collections.abc import Iterator
from typing import Literal, overload

import numpy as np
from numpy.typing import DTypeLike, NDArray

class CoordinateSequence:
    """
    Iterative access to coordinate tuples from the parent geometry's coordinate
    sequence.

    Example:

      >>> from shapely.wkt import loads
      >>> g = loads('POINT (0.0 0.0)')
      >>> list(g.coords)
      [(0.0, 0.0)]
    """
    def __init__(self, coords: NDArray[np.float64]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[float, float]]: ...
    @overload
    def __getitem__(self, key: int) -> tuple[float, float]: ...
    @overload
    def __getitem__(self, key: slice) -> list[tuple[float, float]]: ...
    def __array__(self, dtype: DTypeLike | None = None, copy: Literal[True] | None = None) -> NDArray[np.float64]: ...
    @property
    def xy(self) -> tuple[array[float], array[float]]:
        """X and Y arrays"""
        ...
