"""
This modules provides a conversion to / from a ragged (or "jagged") array
representation of the geometries.

A ragged array is an irregular array of arrays of which each element can have
a different length. As a result, such an array cannot be represented as a
standard, rectangular nD array.
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
    geometries: OptGeoArrayLikeSeq, include_z: bool | None = None
) -> tuple[GeometryType, NDArray[np.float64], tuple[NDArray[np.int64], ...]]:
    """
    Converts geometries to a ragged array representation using a contiguous
    array of coordinates and offset arrays.

    This function converts an array of geometries to a ragged array
    (i.e. irregular array of arrays) of coordinates, represented in memory
    using a single contiguous array of the coordinates, and
    up to 3 offset arrays that keep track where each sub-array
    starts and ends.

    This follows the in-memory layout of the variable size list arrays defined
    by Apache Arrow, as specified for geometries by the GeoArrow project:
    https://github.com/geoarrow/geoarrow.

    Parameters
    ----------
    geometries : array_like
        Array of geometries (1-dimensional).
    include_z : bool, default None
        If False, return 2D geometries. If True, include the third dimension
        in the output (if a geometry has no third dimension, the z-coordinates
        will be NaN). By default, will infer the dimensionality from the
        input geometries. Note that this inference can be unreliable with
        empty geometries (for a guaranteed result, it is recommended to
        specify the keyword).

    Returns
    -------
    tuple of (geometry_type, coords, offsets)
        geometry_type : GeometryType
            The type of the input geometries (required information for
            roundtrip).
        coords : np.ndarray
            Contiguous array of shape (n, 2) or (n, 3) of all coordinates
            of all input geometries.
        offsets: tuple of np.ndarray
            Offset arrays that make it possible to reconstruct the
            geometries from the flat coordinates array. The number of
            offset arrays depends on the geometry type. See
            https://github.com/geoarrow/geoarrow/blob/main/format.md
            for details.

    Notes
    -----
    Mixed singular and multi geometry types of the same basic type are
    allowed (e.g., Point and MultiPoint) and all singular types will be
    treated as multi types.
    GeometryCollections and other mixed geometry types are not supported.

    See also
    --------
    from_ragged_array

    Examples
    --------
    Consider a Polygon with one hole (interior ring):

    >>> import shapely
    >>> polygon = shapely.Polygon(
    ...     [(0, 0), (10, 0), (10, 10), (0, 10)],
    ...     holes=[[(2, 2), (3, 2), (2, 3)]]
    ... )
    >>> polygon
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0), (2 2, 3 2, 2 3, 2 2))>

    This polygon can be thought of as a list of rings (first ring is the
    exterior ring, subsequent rings are the interior rings), and each ring
    as a list of coordinate pairs. This is very similar to how GeoJSON
    represents the coordinates:

    >>> import json
    >>> json.loads(shapely.to_geojson(polygon))["coordinates"]
    [[[0.0, 0.0], [10.0, 0.0], [10.0, 10.0], [0.0, 10.0], [0.0, 0.0]],
     [[2.0, 2.0], [3.0, 2.0], [2.0, 3.0], [2.0, 2.0]]]

    This function will return a similar list of lists of lists, but
    using a single contiguous array of coordinates, and multiple arrays of
    offsets:

    >>> geometry_type, coords, offsets = shapely.to_ragged_array([polygon])
    >>> geometry_type
    <GeometryType.POLYGON: 3>
    >>> coords
    array([[ 0.,  0.],
           [10.,  0.],
           [10., 10.],
           [ 0., 10.],
           [ 0.,  0.],
           [ 2.,  2.],
           [ 3.,  2.],
           [ 2.,  3.],
           [ 2.,  2.]])

    >>> offsets
    (array([0, 5, 9]), array([0, 2]))

    As an example how to interpret the offsets: the i-th ring in the
    coordinates is represented by ``offsets[0][i]`` to ``offsets[0][i+1]``:

    >>> exterior_ring_start, exterior_ring_end = offsets[0][0], offsets[0][1]
    >>> coords[exterior_ring_start:exterior_ring_end]
    array([[ 0.,  0.],
           [10.,  0.],
           [10., 10.],
           [ 0., 10.],
           [ 0.,  0.]])
    """
    ...
def from_ragged_array(
    geometry_type: GeometryType, coords: ArrayLike[float], offsets: ArrayLikeSeq[int] | None = None
) -> GeoArray:
    """
    Creates geometries from a contiguous array of coordinates
    and offset arrays.

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
