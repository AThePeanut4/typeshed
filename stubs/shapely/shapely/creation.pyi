from collections.abc import Sequence
from typing import Literal, SupportsIndex, overload
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from ._enum import ParamEnum
from ._geometry import GeometryType
from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq
from .geometry import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
from .lib import Geometry

__all__ = [
    "points",
    "linestrings",
    "linearrings",
    "polygons",
    "multipoints",
    "multilinestrings",
    "multipolygons",
    "geometrycollections",
    "box",
    "prepare",
    "destroy_prepared",
    "empty",
]

class HandleNaN(ParamEnum):
    allow = 0
    skip = 1
    error = 2

_HandleNaN: TypeAlias = Literal[0, 1, 2] | HandleNaN

@overload
def points(
    coords: float,
    y: float,
    z: float | None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: None = None,
    **kwargs,  # acts as x
) -> Point: ...
@overload
def points(
    coords: Sequence[float],
    y: None = None,
    z: None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: None = None,
    **kwargs,  # acts as x, y[, z]
) -> Point: ...
@overload
def points(
    coords: Sequence[float],  # acts as (x1, x2, ...)
    y: Sequence[float],  # must be (y1, y2, ...)
    z: Sequence[float] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create an array of points.

    Parameters
    ----------
    coords : array_like
        An array of coordinate tuples (2- or 3-dimensional) or, if ``y`` is
        provided, an array of x coordinates.
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> points([[0, 1], [4, 5]]).tolist()
    [<POINT (0 1)>, <POINT (4 5)>]
    >>> points([0, 1, 2])
    <POINT Z (0 1 2)>

    Notes
    -----

    - GEOS 3.10, 3.11 and 3.12 automatically converts POINT (nan nan) to POINT EMPTY.
    - GEOS 3.10 and 3.11 will transform a 3D point to 2D if its Z coordinate is NaN.
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as an array with shape ``(..., 2)`` or ``(..., 3)`` using only the ``coords`` argument.
    """
    ...
@overload
def points(
    coords: Sequence[Sequence[float]],  # acts as (x1, x2, ...), (y1, y2, ...)[, (z1, z2, ...)]
    y: None = None,
    z: None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create an array of points.

    Parameters
    ----------
    coords : array_like
        An array of coordinate tuples (2- or 3-dimensional) or, if ``y`` is
        provided, an array of x coordinates.
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> points([[0, 1], [4, 5]]).tolist()
    [<POINT (0 1)>, <POINT (4 5)>]
    >>> points([0, 1, 2])
    <POINT Z (0 1 2)>

    Notes
    -----

    - GEOS 3.10, 3.11 and 3.12 automatically converts POINT (nan nan) to POINT EMPTY.
    - GEOS 3.10 and 3.11 will transform a 3D point to 2D if its Z coordinate is NaN.
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as an array with shape ``(..., 2)`` or ``(..., 3)`` using only the ``coords`` argument.
    """
    ...
@overload
def points(
    coords: ArrayLike[float],
    y: ArrayLike[float],
    z: ArrayLike[float] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> Point | GeoArray:
    """
    Create an array of points.

    Parameters
    ----------
    coords : array_like
        An array of coordinate tuples (2- or 3-dimensional) or, if ``y`` is
        provided, an array of x coordinates.
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> points([[0, 1], [4, 5]]).tolist()
    [<POINT (0 1)>, <POINT (4 5)>]
    >>> points([0, 1, 2])
    <POINT Z (0 1 2)>

    Notes
    -----

    - GEOS 3.10, 3.11 and 3.12 automatically converts POINT (nan nan) to POINT EMPTY.
    - GEOS 3.10 and 3.11 will transform a 3D point to 2D if its Z coordinate is NaN.
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as an array with shape ``(..., 2)`` or ``(..., 3)`` using only the ``coords`` argument.
    """
    ...
@overload
def points(
    coords: ArrayLikeSeq[float],
    y: ArrayLike[float] | None = None,
    z: ArrayLike[float] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> Point | GeoArray:
    """
    Create an array of points.

    Parameters
    ----------
    coords : array_like
        An array of coordinate tuples (2- or 3-dimensional) or, if ``y`` is
        provided, an array of x coordinates.
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> points([[0, 1], [4, 5]]).tolist()
    [<POINT (0 1)>, <POINT (4 5)>]
    >>> points([0, 1, 2])
    <POINT Z (0 1 2)>

    Notes
    -----

    - GEOS 3.10, 3.11 and 3.12 automatically converts POINT (nan nan) to POINT EMPTY.
    - GEOS 3.10 and 3.11 will transform a 3D point to 2D if its Z coordinate is NaN.
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as an array with shape ``(..., 2)`` or ``(..., 3)`` using only the ``coords`` argument.
    """
    ...
@overload
def linestrings(
    coords: Sequence[float],  # acts as (x1, x2, ...)
    y: Sequence[float],
    z: Sequence[float] | None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: None = None,
    **kwargs,
) -> LineString:
    """
    Create an array of linestrings.

    This function will raise an exception if a linestring contains less than
    two points.

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> linestrings([[[0, 1], [4, 5]], [[2, 3], [5, 6]]]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6)>]
    >>> linestrings([[0, 1], [4, 5], [2, 3], [5, 6], [7, 8]], indices=[0, 0, 1, 1, 1]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6, 7 8)>]

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linestrings(
    coords: Sequence[Sequence[float]],  # acts as (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: None = None,
    **kwargs,
) -> LineString:
    """
    Create an array of linestrings.

    This function will raise an exception if a linestring contains less than
    two points.

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> linestrings([[[0, 1], [4, 5]], [[2, 3], [5, 6]]]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6)>]
    >>> linestrings([[0, 1], [4, 5], [2, 3], [5, 6], [7, 8]], indices=[0, 0, 1, 1, 1]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6, 7 8)>]

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linestrings(
    coords: Sequence[Sequence[Sequence[float]]],  # acts as seq of (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create an array of linestrings.

    This function will raise an exception if a linestring contains less than
    two points.

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> linestrings([[[0, 1], [4, 5]], [[2, 3], [5, 6]]]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6)>]
    >>> linestrings([[0, 1], [4, 5], [2, 3], [5, 6], [7, 8]], indices=[0, 0, 1, 1, 1]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6, 7 8)>]

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linestrings(
    coords: ArrayLikeSeq[float],
    y: ArrayLikeSeq[float] | None = None,
    z: ArrayLikeSeq[float] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> LineString | GeoArray:
    """
    Create an array of linestrings.

    This function will raise an exception if a linestring contains less than
    two points.

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    >>> linestrings([[[0, 1], [4, 5]], [[2, 3], [5, 6]]]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6)>]
    >>> linestrings([[0, 1], [4, 5], [2, 3], [5, 6], [7, 8]], indices=[0, 0, 1, 1, 1]).tolist()
    [<LINESTRING (0 1, 4 5)>, <LINESTRING (2 3, 5 6, 7 8)>]

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linearrings(
    coords: Sequence[float],  # acts as (x1, x2, ...)
    y: Sequence[float],
    z: Sequence[float] | None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: None = None,
    **kwargs,
) -> LinearRing:
    """
    Create an array of linearrings.

    If the provided coords do not constitute a closed linestring, or if there
    are only 3 provided coords, the first
    coordinate is duplicated at the end to close the ring. This function will
    raise an exception if a linearring contains less than three points or if
    the terminal coordinates contain NaN (not-a-number).

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    linestrings

    Examples
    --------
    >>> linearrings([[0, 0], [0, 1], [1, 1], [0, 0]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>
    >>> linearrings([[0, 0], [0, 1], [1, 1]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linearrings(
    coords: Sequence[Sequence[float]],  # acts as (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: None = None,
    **kwargs,
) -> LinearRing:
    """
    Create an array of linearrings.

    If the provided coords do not constitute a closed linestring, or if there
    are only 3 provided coords, the first
    coordinate is duplicated at the end to close the ring. This function will
    raise an exception if a linearring contains less than three points or if
    the terminal coordinates contain NaN (not-a-number).

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    linestrings

    Examples
    --------
    >>> linearrings([[0, 0], [0, 1], [1, 1], [0, 0]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>
    >>> linearrings([[0, 0], [0, 1], [1, 1]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linearrings(
    coords: Sequence[Sequence[Sequence[float]]],  # acts as seq of (x1, y1[, z1]), (x2, y2[, z2]), ...
    y: None = None,
    z: None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create an array of linearrings.

    If the provided coords do not constitute a closed linestring, or if there
    are only 3 provided coords, the first
    coordinate is duplicated at the end to close the ring. This function will
    raise an exception if a linearring contains less than three points or if
    the terminal coordinates contain NaN (not-a-number).

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    linestrings

    Examples
    --------
    >>> linearrings([[0, 0], [0, 1], [1, 1], [0, 0]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>
    >>> linearrings([[0, 0], [0, 1], [1, 1]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def linearrings(
    coords: ArrayLikeSeq[float],
    y: ArrayLikeSeq[float] | None = None,
    z: ArrayLikeSeq[float] | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    handle_nan: _HandleNaN = 0,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> LinearRing | GeoArray:
    """
    Create an array of linearrings.

    If the provided coords do not constitute a closed linestring, or if there
    are only 3 provided coords, the first
    coordinate is duplicated at the end to close the ring. This function will
    raise an exception if a linearring contains less than three points or if
    the terminal coordinates contain NaN (not-a-number).

    Parameters
    ----------
    coords : array_like
        An array of lists of coordinate tuples (2- or 3-dimensional) or, if ``y``
        is provided, an array of lists of x coordinates
    y : array_like, optional
    z : array_like, optional
    indices : array_like, optional
        Indices into the target array where input coordinates belong. If
        provided, the coords should be 2D with shape (N, 2) or (N, 3) and
        indices should be an array of shape (N,) with integers in increasing
        order. Missing indices result in a ValueError unless ``out`` is
        provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    linestrings

    Examples
    --------
    >>> linearrings([[0, 0], [0, 1], [1, 1], [0, 0]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>
    >>> linearrings([[0, 0], [0, 1], [1, 1]])
    <LINEARRING (0 0, 0 1, 1 1, 0 0)>

    Notes
    -----
    - Usage of the ``y`` and ``z`` arguments will prevents lazy evaluation in ``dask``.
      Instead provide the coordinates as a ``(..., 2)`` or ``(..., 3)`` array using only ``coords``.
    """
    ...
@overload
def polygons(
    geometries: LinearRing | Sequence[Sequence[float]] | None,
    holes: ArrayLikeSeq[float] | OptGeoArrayLikeSeq | None = None,
    indices: None = None,
    *,
    out: None = None,
    **kwargs,
) -> Polygon:
    """
    Create an array of polygons.

    Parameters
    ----------
    geometries : array_like
        An array of linearrings or coordinates (see linearrings).
        Unless ``indices`` are given (see description below), this
        include the outer shells only. The ``holes`` argument should be used
        to create polygons with holes.
    holes : array_like, optional
        An array of lists of linearrings that constitute holes for each shell.
        Not to be used in combination with ``indices``.
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, the holes are expected to be present inside ``geometries``;
        the first geometry for each index is the outer shell
        and all subsequent geometries in that index are the holes.
        Both geometries and indices should be 1D and have matching sizes.
        Indices should be in increasing order. Missing indices result in a ValueError
        unless ``out`` is  provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    Polygons are constructed from rings:

    >>> ring_1 = linearrings([[0, 0], [0, 10], [10, 10], [10, 0]])
    >>> ring_2 = linearrings([[2, 6], [2, 7], [3, 7], [3, 6]])
    >>> polygons([ring_1, ring_2])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, ring_2])[1]
    <POLYGON ((2 6, 2 7, 3 7, 3 6, 2 6))>

    Or from coordinates directly:

    >>> polygons([[0, 0], [0, 10], [10, 10], [10, 0]])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>

    Adding holes can be done using the ``holes`` keyword argument:

    >>> polygons(ring_1, holes=[ring_2])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 6, 2 7, 3 7, 3 6, 2 6))>

    Or using the ``indices`` argument:

    >>> polygons([ring_1, ring_2], indices=[0, 1])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, ring_2], indices=[0, 1])[1]
    <POLYGON ((2 6, 2 7, 3 7, 3 6, 2 6))>
    >>> polygons([ring_1, ring_2], indices=[0, 0])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 6, 2 7, 3 7, 3 6, 2 6))>

    Missing input values (``None``) are ignored and may result in an
    empty polygon:

    >>> polygons(None)
    <POLYGON EMPTY>
    >>> polygons(ring_1, holes=[None])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, None], indices=[0, 0])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    ...
@overload
def polygons(
    geometries: Sequence[LinearRing | Sequence[Sequence[float]] | None],
    holes: ArrayLikeSeq[float] | OptGeoArrayLikeSeq | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create an array of polygons.

    Parameters
    ----------
    geometries : array_like
        An array of linearrings or coordinates (see linearrings).
        Unless ``indices`` are given (see description below), this
        include the outer shells only. The ``holes`` argument should be used
        to create polygons with holes.
    holes : array_like, optional
        An array of lists of linearrings that constitute holes for each shell.
        Not to be used in combination with ``indices``.
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, the holes are expected to be present inside ``geometries``;
        the first geometry for each index is the outer shell
        and all subsequent geometries in that index are the holes.
        Both geometries and indices should be 1D and have matching sizes.
        Indices should be in increasing order. Missing indices result in a ValueError
        unless ``out`` is  provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    Polygons are constructed from rings:

    >>> ring_1 = linearrings([[0, 0], [0, 10], [10, 10], [10, 0]])
    >>> ring_2 = linearrings([[2, 6], [2, 7], [3, 7], [3, 6]])
    >>> polygons([ring_1, ring_2])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, ring_2])[1]
    <POLYGON ((2 6, 2 7, 3 7, 3 6, 2 6))>

    Or from coordinates directly:

    >>> polygons([[0, 0], [0, 10], [10, 10], [10, 0]])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>

    Adding holes can be done using the ``holes`` keyword argument:

    >>> polygons(ring_1, holes=[ring_2])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 6, 2 7, 3 7, 3 6, 2 6))>

    Or using the ``indices`` argument:

    >>> polygons([ring_1, ring_2], indices=[0, 1])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, ring_2], indices=[0, 1])[1]
    <POLYGON ((2 6, 2 7, 3 7, 3 6, 2 6))>
    >>> polygons([ring_1, ring_2], indices=[0, 0])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 6, 2 7, 3 7, 3 6, 2 6))>

    Missing input values (``None``) are ignored and may result in an
    empty polygon:

    >>> polygons(None)
    <POLYGON EMPTY>
    >>> polygons(ring_1, holes=[None])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, None], indices=[0, 0])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    ...
@overload
def polygons(
    geometries: ArrayLikeSeq[float] | OptGeoArrayLikeSeq,
    holes: ArrayLikeSeq[float] | OptGeoArrayLikeSeq | None = None,
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> Polygon | GeoArray:
    """
    Create an array of polygons.

    Parameters
    ----------
    geometries : array_like
        An array of linearrings or coordinates (see linearrings).
        Unless ``indices`` are given (see description below), this
        include the outer shells only. The ``holes`` argument should be used
        to create polygons with holes.
    holes : array_like, optional
        An array of lists of linearrings that constitute holes for each shell.
        Not to be used in combination with ``indices``.
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, the holes are expected to be present inside ``geometries``;
        the first geometry for each index is the outer shell
        and all subsequent geometries in that index are the holes.
        Both geometries and indices should be 1D and have matching sizes.
        Indices should be in increasing order. Missing indices result in a ValueError
        unless ``out`` is  provided, in which case the original value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    Polygons are constructed from rings:

    >>> ring_1 = linearrings([[0, 0], [0, 10], [10, 10], [10, 0]])
    >>> ring_2 = linearrings([[2, 6], [2, 7], [3, 7], [3, 6]])
    >>> polygons([ring_1, ring_2])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, ring_2])[1]
    <POLYGON ((2 6, 2 7, 3 7, 3 6, 2 6))>

    Or from coordinates directly:

    >>> polygons([[0, 0], [0, 10], [10, 10], [10, 0]])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>

    Adding holes can be done using the ``holes`` keyword argument:

    >>> polygons(ring_1, holes=[ring_2])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 6, 2 7, 3 7, 3 6, 2 6))>

    Or using the ``indices`` argument:

    >>> polygons([ring_1, ring_2], indices=[0, 1])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, ring_2], indices=[0, 1])[1]
    <POLYGON ((2 6, 2 7, 3 7, 3 6, 2 6))>
    >>> polygons([ring_1, ring_2], indices=[0, 0])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 6, 2 7, 3 7, 3 6, 2 6))>

    Missing input values (``None``) are ignored and may result in an
    empty polygon:

    >>> polygons(None)
    <POLYGON EMPTY>
    >>> polygons(ring_1, holes=[None])
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    >>> polygons([ring_1, None], indices=[0, 0])[0]
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    ...
@overload
def box(xmin: float, ymin: float, xmax: float, ymax: float, ccw: bool = True, **kwargs) -> Polygon:
    """
    Create box polygons.

    Parameters
    ----------
    xmin : array_like
    ymin : array_like
    xmax : array_like
    ymax : array_like
    ccw : bool, default True
        If True, box will be created in counterclockwise direction starting
        from bottom right coordinate (xmax, ymin).
        If False, box will be created in clockwise direction starting from
        bottom left coordinate (xmin, ymin).
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> box(0, 0, 1, 1)
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> box(0, 0, 1, 1, ccw=False)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    ...
@overload
def box(
    xmin: ArrayLikeSeq[float],
    ymin: ArrayLikeSeq[float],
    xmax: ArrayLikeSeq[float],
    ymax: ArrayLikeSeq[float],
    ccw: bool = True,
    **kwargs,
) -> GeoArray:
    """
    Create box polygons.

    Parameters
    ----------
    xmin : array_like
    ymin : array_like
    xmax : array_like
    ymax : array_like
    ccw : bool, default True
        If True, box will be created in counterclockwise direction starting
        from bottom right coordinate (xmax, ymin).
        If False, box will be created in clockwise direction starting from
        bottom left coordinate (xmin, ymin).
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> box(0, 0, 1, 1)
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> box(0, 0, 1, 1, ccw=False)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    ...
@overload
def multipoints(
    geometries: Sequence[Point | Sequence[float] | None], indices: None = None, *, out: None = None, **kwargs
) -> MultiPoint: ...
@overload
def multipoints(
    geometries: Sequence[Sequence[Point | Sequence[float] | None]],
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create multipoints from arrays of points

    Parameters
    ----------
    geometries : array_like
        An array of points or coordinates (see points).
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, both geometries and indices should be 1D and have matching
        sizes. Indices should be in increasing order. Missing indices result
        in a ValueError unless ``out`` is  provided, in which case the original
        value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    Examples
    --------
    Multipoints are constructed from points:

    >>> point_1 = points([1, 1])
    >>> point_2 = points([2, 2])
    >>> multipoints([point_1, point_2])
    <MULTIPOINT (1 1, 2 2)>
    >>> multipoints([[point_1, point_2], [point_2, None]]).tolist()
    [<MULTIPOINT (1 1, 2 2)>, <MULTIPOINT (2 2)>]

    Or from coordinates directly:

    >>> multipoints([[0, 0], [2, 2], [3, 3]])
    <MULTIPOINT (0 0, 2 2, 3 3)>

    Multiple multipoints of different sizes can be constructed efficiently using the
    ``indices`` keyword argument:

    >>> multipoints([point_1, point_2, point_2], indices=[0, 0, 1]).tolist()
    [<MULTIPOINT (1 1, 2 2)>, <MULTIPOINT (2 2)>]

    Missing input values (``None``) are ignored and may result in an
    empty multipoint:

    >>> multipoints([None])
    <MULTIPOINT EMPTY>
    >>> multipoints([point_1, None], indices=[0, 0]).tolist()
    [<MULTIPOINT (1 1)>]
    >>> multipoints([point_1, None], indices=[0, 1]).tolist()
    [<MULTIPOINT (1 1)>, <MULTIPOINT EMPTY>]
    """
    ...
@overload
def multipoints(
    geometries: OptGeoArrayLikeSeq, indices: ArrayLikeSeq[int] | None = None, *, out: NDArray[np.object_] | None = None, **kwargs
) -> MultiPoint | GeoArray: ...
@overload
def multilinestrings(
    geometries: Sequence[LineString | Sequence[Sequence[float]] | None], indices: None = None, *, out: None = None, **kwargs
) -> MultiLineString: ...
@overload
def multilinestrings(
    geometries: Sequence[Sequence[LineString | Sequence[Sequence[float]] | None]],
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create multilinestrings from arrays of linestrings

    Parameters
    ----------
    geometries : array_like
        An array of linestrings or coordinates (see linestrings).
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, both geometries and indices should be 1D and have matching
        sizes. Indices should be in increasing order. Missing indices result
        in a ValueError unless ``out`` is  provided, in which case the original
        value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    multipoints
    """
    ...
@overload
def multilinestrings(
    geometries: OptGeoArrayLikeSeq, indices: ArrayLikeSeq[int] | None = None, *, out: NDArray[np.object_] | None = None, **kwargs
) -> MultiLineString | GeoArray: ...
@overload
def multipolygons(
    geometries: Sequence[Polygon | Sequence[Sequence[float]] | None], indices: None = None, *, out: None = None, **kwargs
) -> MultiPolygon: ...
@overload
def multipolygons(
    geometries: Sequence[Sequence[Polygon | Sequence[Sequence[float]] | None]],
    indices: ArrayLikeSeq[int] | None = None,
    *,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create multipolygons from arrays of polygons

    Parameters
    ----------
    geometries : array_like
        An array of polygons or coordinates (see polygons).
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, both geometries and indices should be 1D and have matching
        sizes. Indices should be in increasing order. Missing indices result
        in a ValueError unless ``out`` is  provided, in which case the original
        value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    multipoints
    """
    ...
@overload
def multipolygons(
    geometries: OptGeoArrayLikeSeq, indices: ArrayLikeSeq[int] | None = None, *, out: NDArray[np.object_] | None = None, **kwargs
) -> MultiPolygon | GeoArray: ...
@overload
def geometrycollections(
    geometries: Sequence[Geometry | None], indices: None = None, out: None = None, **kwargs
) -> GeometryCollection:
    """
    Create geometrycollections from arrays of geometries

    Parameters
    ----------
    geometries : array_like
        An array of geometries
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, both geometries and indices should be 1D and have matching
        sizes. Indices should be in increasing order. Missing indices result
        in a ValueError unless ``out`` is  provided, in which case the original
        value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    multipoints
    """
    ...
@overload
def geometrycollections(
    geometries: Sequence[Sequence[Geometry | None]],
    indices: ArrayLikeSeq[int] | None = None,
    out: NDArray[np.object_] | None = None,
    **kwargs,
) -> GeoArray:
    """
    Create geometrycollections from arrays of geometries

    Parameters
    ----------
    geometries : array_like
        An array of geometries
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, both geometries and indices should be 1D and have matching
        sizes. Indices should be in increasing order. Missing indices result
        in a ValueError unless ``out`` is  provided, in which case the original
        value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    multipoints
    """
    ...
@overload
def geometrycollections(
    geometries: OptGeoArrayLikeSeq, indices: ArrayLikeSeq[int] | None = None, out: NDArray[np.object_] | None = None, **kwargs
) -> GeometryCollection | GeoArray:
    """
    Create geometrycollections from arrays of geometries

    Parameters
    ----------
    geometries : array_like
        An array of geometries
    indices : array_like, optional
        Indices into the target array where input geometries belong. If
        provided, both geometries and indices should be 1D and have matching
        sizes. Indices should be in increasing order. Missing indices result
        in a ValueError unless ``out`` is  provided, in which case the original
        value in ``out`` is kept.
    out : ndarray, optional
        An array (with dtype object) to output the geometries into.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.
        Ignored if ``indices`` is provided.

    See also
    --------
    multipoints
    """
    ...
def prepare(geometry: OptGeoArrayLike, **kwargs) -> None:
    """
    Prepare a geometry, improving performance of other operations.

    A prepared geometry is a normal geometry with added information such as an
    index on the line segments. This improves the performance of the following operations:
    contains, contains_properly, covered_by, covers, crosses, disjoint, intersects,
    overlaps, touches, and within.

    Note that if a prepared geometry is modified, the newly created Geometry object is
    not prepared. In that case, ``prepare`` should be called again.

    This function does not recompute previously prepared geometries;
    it is efficient to call this function on an array that partially contains prepared geometries.

    This function does not return any values; geometries are modified in place.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometries are changed in place
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    is_prepared : Identify whether a geometry is prepared already.
    destroy_prepared : Destroy the prepared part of a geometry.

    Examples
    --------
    >>> from shapely import Point, buffer, prepare, contains_properly
    >>> poly = buffer(Point(1.0, 1.0), 1)
    >>> prepare(poly)
    >>> contains_properly(poly, [Point(0.0, 0.0), Point(0.5, 0.5)]).tolist()
    [False, True]
    """
    ...
def destroy_prepared(geometry: OptGeoArrayLike, **kwargs) -> None:
    """
    Destroy the prepared part of a geometry, freeing up memory.

    Note that the prepared geometry will always be cleaned up if the geometry itself
    is dereferenced. This function needs only be called in very specific circumstances,
    such as freeing up memory without losing the geometries, or benchmarking.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometries are changed in-place
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    prepare
    """
    ...
def empty(
    shape: SupportsIndex | Sequence[SupportsIndex], geom_type: GeometryType | int | None = None, order: Literal["C", "F"] = "C"
) -> NDArray[np.object_]:
    """
    Create a geometry array prefilled with None or with empty geometries.

    Parameters
    ----------
    shape : int or tuple of int
        Shape of the empty array, e.g., ``(2, 3)`` or ``2``.
    geom_type : shapely.GeometryType, optional
        The desired geometry type in case the array should be prefilled
        with empty geometries. Default ``None``.
    order : {'C', 'F'}, optional, default: 'C'
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.

    Examples
    --------
    >>> empty((2, 3)).tolist()
    [[None, None, None], [None, None, None]]
    >>> empty(2, geom_type=GeometryType.POINT).tolist()
    [<POINT EMPTY>, <POINT EMPTY>]
    """
    ...
