from collections.abc import Callable
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from ._typing import ArrayLikeSeq, GeoArray, GeoT, OptGeoArrayLike, OptGeoArrayLikeSeq, OptGeoT

__all__ = ["transform", "count_coordinates", "get_coordinates", "set_coordinates"]

@overload
def transform(
    geometry: OptGeoT, transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]], include_z: bool = False
) -> OptGeoT:
    """
    Returns a copy of a geometry array with a function applied to its
    coordinates.

    With the default of ``include_z=False``, all returned geometries will be
    two-dimensional; the third dimension will be discarded, if present.
    When specifying ``include_z=True``, the returned geometries preserve
    the dimensionality of the respective input geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    transformation : function
        A function that transforms a (N, 2) or (N, 3) ndarray of float64 to
        another (N, 2) or (N, 3) ndarray of float64.
    include_z : bool, default False
        If True, include the third dimension in the coordinates array
        that is passed to the ``transformation`` function. If a
        geometry has no third dimension, the z-coordinates passed to the
        function will be NaN.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> transform(Point(0, 0), lambda x: x + 1)
    <POINT (1 1)>
    >>> transform(LineString([(2, 2), (4, 4)]), lambda x: x * [2, 3])
    <LINESTRING (4 6, 8 12)>
    >>> transform(None, lambda x: x) is None
    True
    >>> transform([Point(0, 0), None], lambda x: x).tolist()
    [<POINT (0 0)>, None]

    By default, the third dimension is ignored:

    >>> transform(Point(0, 0, 0), lambda x: x + 1)
    <POINT (1 1)>
    >>> transform(Point(0, 0, 0), lambda x: x + 1, include_z=True)
    <POINT Z (1 1 1)>
    """
    ...
@overload
def transform(
    geometry: OptGeoArrayLikeSeq, transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]], include_z: bool = False
) -> GeoArray:
    """
    Returns a copy of a geometry array with a function applied to its
    coordinates.

    With the default of ``include_z=False``, all returned geometries will be
    two-dimensional; the third dimension will be discarded, if present.
    When specifying ``include_z=True``, the returned geometries preserve
    the dimensionality of the respective input geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    transformation : function
        A function that transforms a (N, 2) or (N, 3) ndarray of float64 to
        another (N, 2) or (N, 3) ndarray of float64.
    include_z : bool, default False
        If True, include the third dimension in the coordinates array
        that is passed to the ``transformation`` function. If a
        geometry has no third dimension, the z-coordinates passed to the
        function will be NaN.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> transform(Point(0, 0), lambda x: x + 1)
    <POINT (1 1)>
    >>> transform(LineString([(2, 2), (4, 4)]), lambda x: x * [2, 3])
    <LINESTRING (4 6, 8 12)>
    >>> transform(None, lambda x: x) is None
    True
    >>> transform([Point(0, 0), None], lambda x: x).tolist()
    [<POINT (0 0)>, None]

    By default, the third dimension is ignored:

    >>> transform(Point(0, 0, 0), lambda x: x + 1)
    <POINT (1 1)>
    >>> transform(Point(0, 0, 0), lambda x: x + 1, include_z=True)
    <POINT Z (1 1 1)>
    """
    ...
def count_coordinates(geometry: OptGeoArrayLike) -> int:
    """
    Counts the number of coordinate pairs in a geometry array.

    Parameters
    ----------
    geometry : Geometry or array_like

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> count_coordinates(Point(0, 0))
    1
    >>> count_coordinates(LineString([(2, 2), (4, 2)]))
    2
    >>> count_coordinates(None)
    0
    >>> count_coordinates([Point(0, 0), None])
    1
    """
    ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool = False, return_index: Literal[False] = False
) -> NDArray[np.float64]:
    """
    Gets coordinates from a geometry array as an array of floats.

    The shape of the returned array is (N, 2), with N being the number of
    coordinate pairs. With the default of ``include_z=False``, three-dimensional
    data is ignored. When specifying ``include_z=True``, the shape of the
    returned array is (N, 3).

    Parameters
    ----------
    geometry : Geometry or array_like
    include_z : bool, default False
        If, True include the third dimension in the output. If a geometry
        has no third dimension, the z-coordinates will be NaN.
    return_index : bool, default False
        If True, also return the index of each returned geometry as a separate
        ndarray of integers. For multidimensional arrays, this indexes into the
        flattened array (in C contiguous order).

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> get_coordinates(Point(0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(LineString([(2, 2), (4, 4)])).tolist()
    [[2.0, 2.0], [4.0, 4.0]]
    >>> get_coordinates(None)
    array([], shape=(0, 2), dtype=float64)

    By default the third dimension is ignored:

    >>> get_coordinates(Point(0, 0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(Point(0, 0, 0), include_z=True).tolist()
    [[0.0, 0.0, 0.0]]

    When return_index=True, indexes are returned also:

    >>> geometries = [LineString([(2, 2), (4, 4)]), Point(0, 0)]
    >>> coordinates, index = get_coordinates(geometries, return_index=True)
    >>> coordinates.tolist(), index.tolist()
    ([[2.0, 2.0], [4.0, 4.0], [0.0, 0.0]], [0, 0, 1])
    """
    ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool = False, *, return_index: Literal[True]
) -> tuple[NDArray[np.float64], NDArray[np.int64]]:
    """
    Gets coordinates from a geometry array as an array of floats.

    The shape of the returned array is (N, 2), with N being the number of
    coordinate pairs. With the default of ``include_z=False``, three-dimensional
    data is ignored. When specifying ``include_z=True``, the shape of the
    returned array is (N, 3).

    Parameters
    ----------
    geometry : Geometry or array_like
    include_z : bool, default False
        If, True include the third dimension in the output. If a geometry
        has no third dimension, the z-coordinates will be NaN.
    return_index : bool, default False
        If True, also return the index of each returned geometry as a separate
        ndarray of integers. For multidimensional arrays, this indexes into the
        flattened array (in C contiguous order).

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> get_coordinates(Point(0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(LineString([(2, 2), (4, 4)])).tolist()
    [[2.0, 2.0], [4.0, 4.0]]
    >>> get_coordinates(None)
    array([], shape=(0, 2), dtype=float64)

    By default the third dimension is ignored:

    >>> get_coordinates(Point(0, 0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(Point(0, 0, 0), include_z=True).tolist()
    [[0.0, 0.0, 0.0]]

    When return_index=True, indexes are returned also:

    >>> geometries = [LineString([(2, 2), (4, 4)]), Point(0, 0)]
    >>> coordinates, index = get_coordinates(geometries, return_index=True)
    >>> coordinates.tolist(), index.tolist()
    ([[2.0, 2.0], [4.0, 4.0], [0.0, 0.0]], [0, 0, 1])
    """
    ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool, return_index: Literal[True]
) -> tuple[NDArray[np.float64], NDArray[np.int64]]:
    """
    Gets coordinates from a geometry array as an array of floats.

    The shape of the returned array is (N, 2), with N being the number of
    coordinate pairs. With the default of ``include_z=False``, three-dimensional
    data is ignored. When specifying ``include_z=True``, the shape of the
    returned array is (N, 3).

    Parameters
    ----------
    geometry : Geometry or array_like
    include_z : bool, default False
        If, True include the third dimension in the output. If a geometry
        has no third dimension, the z-coordinates will be NaN.
    return_index : bool, default False
        If True, also return the index of each returned geometry as a separate
        ndarray of integers. For multidimensional arrays, this indexes into the
        flattened array (in C contiguous order).

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> get_coordinates(Point(0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(LineString([(2, 2), (4, 4)])).tolist()
    [[2.0, 2.0], [4.0, 4.0]]
    >>> get_coordinates(None)
    array([], shape=(0, 2), dtype=float64)

    By default the third dimension is ignored:

    >>> get_coordinates(Point(0, 0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(Point(0, 0, 0), include_z=True).tolist()
    [[0.0, 0.0, 0.0]]

    When return_index=True, indexes are returned also:

    >>> geometries = [LineString([(2, 2), (4, 4)]), Point(0, 0)]
    >>> coordinates, index = get_coordinates(geometries, return_index=True)
    >>> coordinates.tolist(), index.tolist()
    ([[2.0, 2.0], [4.0, 4.0], [0.0, 0.0]], [0, 0, 1])
    """
    ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool = False, *, return_index: bool
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]:
    """
    Gets coordinates from a geometry array as an array of floats.

    The shape of the returned array is (N, 2), with N being the number of
    coordinate pairs. With the default of ``include_z=False``, three-dimensional
    data is ignored. When specifying ``include_z=True``, the shape of the
    returned array is (N, 3).

    Parameters
    ----------
    geometry : Geometry or array_like
    include_z : bool, default False
        If, True include the third dimension in the output. If a geometry
        has no third dimension, the z-coordinates will be NaN.
    return_index : bool, default False
        If True, also return the index of each returned geometry as a separate
        ndarray of integers. For multidimensional arrays, this indexes into the
        flattened array (in C contiguous order).

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> get_coordinates(Point(0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(LineString([(2, 2), (4, 4)])).tolist()
    [[2.0, 2.0], [4.0, 4.0]]
    >>> get_coordinates(None)
    array([], shape=(0, 2), dtype=float64)

    By default the third dimension is ignored:

    >>> get_coordinates(Point(0, 0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(Point(0, 0, 0), include_z=True).tolist()
    [[0.0, 0.0, 0.0]]

    When return_index=True, indexes are returned also:

    >>> geometries = [LineString([(2, 2), (4, 4)]), Point(0, 0)]
    >>> coordinates, index = get_coordinates(geometries, return_index=True)
    >>> coordinates.tolist(), index.tolist()
    ([[2.0, 2.0], [4.0, 4.0], [0.0, 0.0]], [0, 0, 1])
    """
    ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool, return_index: bool
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]:
    """
    Gets coordinates from a geometry array as an array of floats.

    The shape of the returned array is (N, 2), with N being the number of
    coordinate pairs. With the default of ``include_z=False``, three-dimensional
    data is ignored. When specifying ``include_z=True``, the shape of the
    returned array is (N, 3).

    Parameters
    ----------
    geometry : Geometry or array_like
    include_z : bool, default False
        If, True include the third dimension in the output. If a geometry
        has no third dimension, the z-coordinates will be NaN.
    return_index : bool, default False
        If True, also return the index of each returned geometry as a separate
        ndarray of integers. For multidimensional arrays, this indexes into the
        flattened array (in C contiguous order).

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> get_coordinates(Point(0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(LineString([(2, 2), (4, 4)])).tolist()
    [[2.0, 2.0], [4.0, 4.0]]
    >>> get_coordinates(None)
    array([], shape=(0, 2), dtype=float64)

    By default the third dimension is ignored:

    >>> get_coordinates(Point(0, 0, 0)).tolist()
    [[0.0, 0.0]]
    >>> get_coordinates(Point(0, 0, 0), include_z=True).tolist()
    [[0.0, 0.0, 0.0]]

    When return_index=True, indexes are returned also:

    >>> geometries = [LineString([(2, 2), (4, 4)]), Point(0, 0)]
    >>> coordinates, index = get_coordinates(geometries, return_index=True)
    >>> coordinates.tolist(), index.tolist()
    ([[2.0, 2.0], [4.0, 4.0], [0.0, 0.0]], [0, 0, 1])
    """
    ...
@overload
def set_coordinates(geometry: GeoT, coordinates: ArrayLikeSeq[float]) -> GeoT:
    """
    Adapts the coordinates of a geometry array in-place.

    If the coordinates array has shape (N, 2), all returned geometries
    will be two-dimensional, and the third dimension will be discarded,
    if present. If the coordinates array has shape (N, 3), the returned
    geometries preserve the dimensionality of the input geometries.

    .. warning::

        The geometry array is modified in-place! If you do not want to
        modify the original array, you can do
        ``set_coordinates(arr.copy(), newcoords)``.

    Parameters
    ----------
    geometry : Geometry or array_like
    coordinates: array_like

    See Also
    --------
    transform : Returns a copy of a geometry array with a function applied to its
        coordinates.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> set_coordinates(Point(0, 0), [[1, 1]])
    <POINT (1 1)>
    >>> set_coordinates([Point(0, 0), LineString([(0, 0), (0, 0)])], [[1, 2], [3, 4], [5, 6]]).tolist()
    [<POINT (1 2)>, <LINESTRING (3 4, 5 6)>]
    >>> set_coordinates([None, Point(0, 0)], [[1, 2]]).tolist()
    [None, <POINT (1 2)>]

    Third dimension of input geometry is discarded if coordinates array does
    not include one:

    >>> set_coordinates(Point(0, 0, 0), [[1, 1]])
    <POINT (1 1)>
    >>> set_coordinates(Point(0, 0, 0), [[1, 1, 1]])
    <POINT Z (1 1 1)>
    """
    ...
@overload
def set_coordinates(geometry: OptGeoArrayLikeSeq, coordinates: ArrayLikeSeq[float]) -> GeoArray:
    """
    Adapts the coordinates of a geometry array in-place.

    If the coordinates array has shape (N, 2), all returned geometries
    will be two-dimensional, and the third dimension will be discarded,
    if present. If the coordinates array has shape (N, 3), the returned
    geometries preserve the dimensionality of the input geometries.

    .. warning::

        The geometry array is modified in-place! If you do not want to
        modify the original array, you can do
        ``set_coordinates(arr.copy(), newcoords)``.

    Parameters
    ----------
    geometry : Geometry or array_like
    coordinates: array_like

    See Also
    --------
    transform : Returns a copy of a geometry array with a function applied to its
        coordinates.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> set_coordinates(Point(0, 0), [[1, 1]])
    <POINT (1 1)>
    >>> set_coordinates([Point(0, 0), LineString([(0, 0), (0, 0)])], [[1, 2], [3, 4], [5, 6]]).tolist()
    [<POINT (1 2)>, <LINESTRING (3 4, 5 6)>]
    >>> set_coordinates([None, Point(0, 0)], [[1, 2]]).tolist()
    [None, <POINT (1 2)>]

    Third dimension of input geometry is discarded if coordinates array does
    not include one:

    >>> set_coordinates(Point(0, 0, 0), [[1, 1]])
    <POINT (1 1)>
    >>> set_coordinates(Point(0, 0, 0), [[1, 1, 1]])
    <POINT Z (1 1 1)>
    """
    ...
