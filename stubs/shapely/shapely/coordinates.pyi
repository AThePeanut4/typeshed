from collections.abc import Callable
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from ._typing import ArrayLikeSeq, GeoArray, GeoT, OptGeoArrayLike, OptGeoArrayLikeSeq, OptGeoT

__all__ = ["transform", "count_coordinates", "get_coordinates", "set_coordinates"]

@overload
def transform(
    geometry: OptGeoT,
    transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]],
    include_z: bool = False,
    *,
    interleaved: bool = True,
) -> OptGeoT: ...
@overload
def transform(
    geometry: OptGeoArrayLikeSeq,
    transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]],
    include_z: bool = False,
    *,
    interleaved: bool = True,
) -> GeoArray: ...
def count_coordinates(geometry: OptGeoArrayLike) -> int: ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool = False, return_index: Literal[False] = False, *, include_m: bool = False
) -> NDArray[np.float64]: ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool = False, *, return_index: Literal[True], include_m: bool = False
) -> tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool, return_index: Literal[True], *, include_m: bool = False
) -> tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool = False, *, return_index: bool, include_m: bool = False
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]: ...
@overload
def get_coordinates(
    geometry: OptGeoArrayLike, include_z: bool, return_index: bool, *, include_m: bool = False
) -> NDArray[np.float64] | tuple[NDArray[np.float64], NDArray[np.int64]]: ...
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
