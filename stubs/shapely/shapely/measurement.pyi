from typing import overload

import numpy as np
from numpy.typing import NDArray

from ._typing import ArrayLike, ArrayLikeSeq, OptGeoArrayLike, OptGeoArrayLikeSeq
from .lib import Geometry

__all__ = [
    "area",
    "distance",
    "bounds",
    "total_bounds",
    "length",
    "hausdorff_distance",
    "frechet_distance",
    "minimum_clearance",
    "minimum_bounding_radius",
]

@overload
def area(geometry: Geometry | None, **kwargs) -> float:
    """
    Computes the area of a (multi)polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPolygon, Polygon
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> area(polygon)
    100.0
    >>> area(MultiPolygon([polygon, Polygon([(10, 10), (10, 20), (20, 20), (20, 10), (10, 10)])]))
    200.0
    >>> area(Polygon())
    0.0
    >>> area(None)
    nan
    """
    ...
@overload
def area(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Computes the area of a (multi)polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPolygon, Polygon
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> area(polygon)
    100.0
    >>> area(MultiPolygon([polygon, Polygon([(10, 10), (10, 20), (20, 20), (20, 10), (10, 10)])]))
    200.0
    >>> area(Polygon())
    0.0
    >>> area(None)
    nan
    """
    ...
@overload
def distance(a: Geometry | None, b: Geometry | None, **kwargs) -> float:
    """
    Computes the Cartesian distance between two geometries.

    Parameters
    ----------
    a, b : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> point = Point(0, 0)
    >>> distance(Point(10, 0), point)
    10.0
    >>> distance(LineString([(1, 1), (1, -1)]), point)
    1.0
    >>> distance(Polygon([(3, 0), (5, 0), (5, 5), (3, 5), (3, 0)]), point)
    3.0
    >>> distance(Point(), point)
    nan
    >>> distance(None, point)
    nan
    """
    ...
@overload
def distance(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> NDArray[np.float64]:
    """
    Computes the Cartesian distance between two geometries.

    Parameters
    ----------
    a, b : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> point = Point(0, 0)
    >>> distance(Point(10, 0), point)
    10.0
    >>> distance(LineString([(1, 1), (1, -1)]), point)
    1.0
    >>> distance(Polygon([(3, 0), (5, 0), (5, 5), (3, 5), (3, 0)]), point)
    3.0
    >>> distance(Point(), point)
    nan
    >>> distance(None, point)
    nan
    """
    ...
@overload
def distance(a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Computes the Cartesian distance between two geometries.

    Parameters
    ----------
    a, b : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> point = Point(0, 0)
    >>> distance(Point(10, 0), point)
    10.0
    >>> distance(LineString([(1, 1), (1, -1)]), point)
    1.0
    >>> distance(Polygon([(3, 0), (5, 0), (5, 5), (3, 5), (3, 0)]), point)
    3.0
    >>> distance(Point(), point)
    nan
    >>> distance(None, point)
    nan
    """
    ...
def bounds(geometry: OptGeoArrayLike, **kwargs) -> NDArray[np.float64]:
    """
    Computes the bounds (extent) of a geometry.

    For each geometry these 4 numbers are returned: min x, min y, max x, max y.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> bounds(Point(2, 3)).tolist()
    [2.0, 3.0, 2.0, 3.0]
    >>> bounds(LineString([(0, 0), (0, 2), (3, 2)])).tolist()
    [0.0, 0.0, 3.0, 2.0]
    >>> bounds(Polygon()).tolist()
    [nan, nan, nan, nan]
    >>> bounds(None).tolist()
    [nan, nan, nan, nan]
    """
    ...
def total_bounds(geometry: OptGeoArrayLike, **kwargs) -> NDArray[np.float64]:
    """
    Computes the total bounds (extent) of the geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    numpy ndarray of [xmin, ymin, xmax, ymax]

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> total_bounds(Point(2, 3)).tolist()
    [2.0, 3.0, 2.0, 3.0]
    >>> total_bounds([Point(2, 3), Point(4, 5)]).tolist()
    [2.0, 3.0, 4.0, 5.0]
    >>> total_bounds([
    ...     LineString([(0, 1), (0, 2), (3, 2)]),
    ...     LineString([(4, 4), (4, 6), (6, 7)])
    ... ]).tolist()
    [0.0, 1.0, 6.0, 7.0]
    >>> total_bounds(Polygon()).tolist()
    [nan, nan, nan, nan]
    >>> total_bounds([Polygon(), Point(2, 3)]).tolist()
    [2.0, 3.0, 2.0, 3.0]
    >>> total_bounds(None).tolist()
    [nan, nan, nan, nan]
    """
    ...
@overload
def length(geometry: Geometry | None, **kwargs) -> float:
    """
    Computes the length of a (multi)linestring or polygon perimeter.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiLineString, Polygon
    >>> length(LineString([(0, 0), (0, 2), (3, 2)]))
    5.0
    >>> length(MultiLineString([
    ...     LineString([(0, 0), (1, 0)]),
    ...     LineString([(1, 0), (2, 0)])
    ... ]))
    2.0
    >>> length(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    40.0
    >>> length(LineString())
    0.0
    >>> length(None)
    nan
    """
    ...
@overload
def length(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Computes the length of a (multi)linestring or polygon perimeter.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiLineString, Polygon
    >>> length(LineString([(0, 0), (0, 2), (3, 2)]))
    5.0
    >>> length(MultiLineString([
    ...     LineString([(0, 0), (1, 0)]),
    ...     LineString([(1, 0), (2, 0)])
    ... ]))
    2.0
    >>> length(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    40.0
    >>> length(LineString())
    0.0
    >>> length(None)
    nan
    """
    ...
@overload
def hausdorff_distance(a: Geometry | None, b: Geometry | None, densify: float | None = None, **kwargs) -> float:
    """
    Compute the discrete Hausdorff distance between two geometries.

    The Hausdorff distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(130, 0), (0, 0), (0, 150)])
    >>> line2 = LineString([(10, 10), (10, 150), (130, 10)])
    >>> hausdorff_distance(line1, line2)  # doctest: +ELLIPSIS
    14.14...
    >>> hausdorff_distance(line1, line2, densify=0.5)
    70.0
    >>> hausdorff_distance(line1, LineString())
    nan
    >>> hausdorff_distance(line1, None)
    nan
    """
    ...
@overload
def hausdorff_distance(a: OptGeoArrayLike, b: OptGeoArrayLike, densify: ArrayLikeSeq[float], **kwargs) -> NDArray[np.float64]:
    """
    Compute the discrete Hausdorff distance between two geometries.

    The Hausdorff distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(130, 0), (0, 0), (0, 150)])
    >>> line2 = LineString([(10, 10), (10, 150), (130, 10)])
    >>> hausdorff_distance(line1, line2)  # doctest: +ELLIPSIS
    14.14...
    >>> hausdorff_distance(line1, line2, densify=0.5)
    70.0
    >>> hausdorff_distance(line1, LineString())
    nan
    >>> hausdorff_distance(line1, None)
    nan
    """
    ...
@overload
def hausdorff_distance(
    a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, densify: ArrayLike[float] | None = None, **kwargs
) -> NDArray[np.float64]:
    """
    Compute the discrete Hausdorff distance between two geometries.

    The Hausdorff distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(130, 0), (0, 0), (0, 150)])
    >>> line2 = LineString([(10, 10), (10, 150), (130, 10)])
    >>> hausdorff_distance(line1, line2)  # doctest: +ELLIPSIS
    14.14...
    >>> hausdorff_distance(line1, line2, densify=0.5)
    70.0
    >>> hausdorff_distance(line1, LineString())
    nan
    >>> hausdorff_distance(line1, None)
    nan
    """
    ...
@overload
def hausdorff_distance(
    a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, densify: ArrayLike[float] | None = None, **kwargs
) -> NDArray[np.float64]:
    """
    Compute the discrete Hausdorff distance between two geometries.

    The Hausdorff distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(130, 0), (0, 0), (0, 150)])
    >>> line2 = LineString([(10, 10), (10, 150), (130, 10)])
    >>> hausdorff_distance(line1, line2)  # doctest: +ELLIPSIS
    14.14...
    >>> hausdorff_distance(line1, line2, densify=0.5)
    70.0
    >>> hausdorff_distance(line1, LineString())
    nan
    >>> hausdorff_distance(line1, None)
    nan
    """
    ...
@overload
def frechet_distance(a: Geometry | None, b: Geometry | None, densify: float | None = None, **kwargs) -> float:
    """
    Compute the discrete Fréchet distance between two geometries.

    The Fréchet distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Fréchet distance sweep continuously along their respective curves
    and the direction of curves is significant. This makes it a better measure
    of similarity than Hausdorff distance for curve or surface matching.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (100, 0)])
    >>> line2 = LineString([(0, 0), (50, 50), (100, 0)])
    >>> frechet_distance(line1, line2)  # doctest: +ELLIPSIS
    70.71...
    >>> frechet_distance(line1, line2, densify=0.5)
    50.0
    >>> frechet_distance(line1, LineString())
    nan
    >>> frechet_distance(line1, None)
    nan
    """
    ...
@overload
def frechet_distance(a: OptGeoArrayLike, b: OptGeoArrayLike, densify: ArrayLikeSeq[float], **kwargs) -> NDArray[np.float64]:
    """
    Compute the discrete Fréchet distance between two geometries.

    The Fréchet distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Fréchet distance sweep continuously along their respective curves
    and the direction of curves is significant. This makes it a better measure
    of similarity than Hausdorff distance for curve or surface matching.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (100, 0)])
    >>> line2 = LineString([(0, 0), (50, 50), (100, 0)])
    >>> frechet_distance(line1, line2)  # doctest: +ELLIPSIS
    70.71...
    >>> frechet_distance(line1, line2, densify=0.5)
    50.0
    >>> frechet_distance(line1, LineString())
    nan
    >>> frechet_distance(line1, None)
    nan
    """
    ...
@overload
def frechet_distance(
    a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, densify: ArrayLike[float] | None = None, **kwargs
) -> NDArray[np.float64]:
    """
    Compute the discrete Fréchet distance between two geometries.

    The Fréchet distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Fréchet distance sweep continuously along their respective curves
    and the direction of curves is significant. This makes it a better measure
    of similarity than Hausdorff distance for curve or surface matching.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (100, 0)])
    >>> line2 = LineString([(0, 0), (50, 50), (100, 0)])
    >>> frechet_distance(line1, line2)  # doctest: +ELLIPSIS
    70.71...
    >>> frechet_distance(line1, line2, densify=0.5)
    50.0
    >>> frechet_distance(line1, LineString())
    nan
    >>> frechet_distance(line1, None)
    nan
    """
    ...
@overload
def frechet_distance(
    a: OptGeoArrayLike, b: OptGeoArrayLikeSeq, densify: ArrayLike[float] | None = None, **kwargs
) -> NDArray[np.float64]:
    """
    Compute the discrete Fréchet distance between two geometries.

    The Fréchet distance is a measure of similarity: it is the greatest
    distance between any point in A and the closest point in B. The discrete
    distance is an approximation of this metric: only vertices are considered.
    The parameter 'densify' makes this approximation less coarse by splitting
    the line segments between vertices before computing the distance.

    Fréchet distance sweep continuously along their respective curves
    and the direction of curves is significant. This makes it a better measure
    of similarity than Hausdorff distance for curve or surface matching.

    Parameters
    ----------
    a, b : Geometry or array_like
    densify : float or array_like, optional
        The value of densify is required to be between 0 and 1.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (100, 0)])
    >>> line2 = LineString([(0, 0), (50, 50), (100, 0)])
    >>> frechet_distance(line1, line2)  # doctest: +ELLIPSIS
    70.71...
    >>> frechet_distance(line1, line2, densify=0.5)
    50.0
    >>> frechet_distance(line1, LineString())
    nan
    >>> frechet_distance(line1, None)
    nan
    """
    ...
@overload
def minimum_clearance(geometry: Geometry | None, **kwargs) -> float:
    """
    Computes the Minimum Clearance distance.

    A geometry's "minimum clearance" is the smallest distance by which
    a vertex of the geometry could be moved to produce an invalid geometry.

    If no minimum clearance exists for a geometry (for example, a single
    point, or an empty geometry), infinity is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Polygon
    >>> polygon = Polygon([(0, 0), (0, 10), (5, 6), (10, 10), (10, 0), (5, 4), (0, 0)])
    >>> minimum_clearance(polygon)
    2.0
    >>> minimum_clearance(Polygon())
    inf
    >>> minimum_clearance(None)
    nan
    """
    ...
@overload
def minimum_clearance(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Computes the Minimum Clearance distance.

    A geometry's "minimum clearance" is the smallest distance by which
    a vertex of the geometry could be moved to produce an invalid geometry.

    If no minimum clearance exists for a geometry (for example, a single
    point, or an empty geometry), infinity is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import Polygon
    >>> polygon = Polygon([(0, 0), (0, 10), (5, 6), (10, 10), (10, 0), (5, 4), (0, 0)])
    >>> minimum_clearance(polygon)
    2.0
    >>> minimum_clearance(Polygon())
    inf
    >>> minimum_clearance(None)
    nan
    """
    ...
@overload
def minimum_bounding_radius(geometry: Geometry | None, **kwargs) -> float:
    """
    Computes the radius of the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.


    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_radius(Polygon([(0, 5), (5, 10), (10, 5), (5, 0), (0, 5)]))
    5.0
    >>> minimum_bounding_radius(LineString([(1, 1), (1, 10)]))
    4.5
    >>> minimum_bounding_radius(MultiPoint([(2, 2), (4, 2)]))
    1.0
    >>> minimum_bounding_radius(Point(0, 1))
    0.0
    >>> minimum_bounding_radius(GeometryCollection())
    0.0

    See also
    --------
    minimum_bounding_circle
    """
    ...
@overload
def minimum_bounding_radius(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Computes the radius of the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.


    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_radius(Polygon([(0, 5), (5, 10), (10, 5), (5, 0), (0, 5)]))
    5.0
    >>> minimum_bounding_radius(LineString([(1, 1), (1, 10)]))
    4.5
    >>> minimum_bounding_radius(MultiPoint([(2, 2), (4, 2)]))
    1.0
    >>> minimum_bounding_radius(Point(0, 1))
    0.0
    >>> minimum_bounding_radius(GeometryCollection())
    0.0

    See also
    --------
    minimum_bounding_circle
    """
    ...
