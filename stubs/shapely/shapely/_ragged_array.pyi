"""
Provides a conversion to / from a ragged array representation of geometries.

A ragged (or "jagged") array is an irregular array of arrays of which each
element can have a different length. As a result, such an array cannot be
represented as a standard, rectangular nD array.
The coordinates of geometries can be represented as arrays of arrays of
coordinate pairs (possibly multiple levels of nesting, depending on the
geometry type).

Geometries, as a ragged array of coordinates, can be efficiently represented
as contiguous arrays of coordinates provided that there is another data
structure that keeps track of which range of coordinate values corresponds
to a given geometry. This can be done using offsets, counts, or indices.

This module currently implements offsets into the coordinates array. This
is the ragged array representation defined by the the Apache Arrow project
as "variable size list array" (https://arrow.apache.org/docs/format/Columnar.html#variable-size-list-layout).
See for example https://cfconventions.org/Data/cf-conventions/cf-conventions-1.9/cf-conventions.html#representations-features
for different options.

The exact usage of the Arrow list array with varying degrees of nesting for the
different geometry types is defined by the GeoArrow project:
https://github.com/geoarrow/geoarrow
"""

import numpy as np
from numpy.typing import NDArray

from ._geometry import GeometryType
from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLikeSeq

def to_ragged_array(
    geometries: OptGeoArrayLikeSeq, include_z: bool | None = None, include_m: bool | None = None
) -> tuple[GeometryType, NDArray[np.float64], tuple[NDArray[np.int32], ...]]: ...
def from_ragged_array(
    geometry_type: GeometryType, coords: ArrayLike[float], offsets: ArrayLikeSeq[int] | None = None
) -> GeoArray:
    """
    Create geometries from a contiguous array of coordinates and offset arrays.

    This function creates geometries from the ragged array representation
    as returned by ``to_ragged_array``.

    This follows the in-memory layout of the variable size list arrays defined
    by Apache Arrow, as specified for geometries by the GeoArrow project:
    https://github.com/geoarrow/geoarrow.

    See :func:`to_ragged_array` for more details.

    Parameters
    ----------
    geometry_type : GeometryType
        The type of geometry to create.
    coords : np.ndarray
        Contiguous array of shape (n, 2) or (n, 3) of all coordinates
        for the geometries.
    offsets: tuple of np.ndarray
        Offset arrays that allow to reconstruct the geometries based on the
        flat coordinates array. The number of offset arrays depends on the
        geometry type. See
        https://github.com/geoarrow/geoarrow/blob/main/format.md for details.

    Returns
    -------
    np.ndarray
        Array of geometries (1-dimensional).

    See Also
    --------
    to_ragged_array
    """
    ...

__all__ = ["to_ragged_array", "from_ragged_array"]
