"""Linear geometry functions."""

from typing import overload

import numpy as np
from numpy.typing import NDArray

from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq
from .geometry import GeometryCollection, LineString, MultiLineString, Point
from .lib import Geometry

__all__ = ["line_interpolate_point", "line_locate_point", "line_merge", "shared_paths", "shortest_line"]

@overload
def line_interpolate_point(line: None, distance: float, normalized: bool = False, **kwargs) -> None:
    """
    Return a point interpolated at given distance on a line.

    Parameters
    ----------
    line : Geometry or array_like
        For multilinestrings or geometrycollections, the first geometry is taken
        and the rest is ignored. This function raises a TypeError for non-linear
        geometries. For empty linear geometries, empty points are returned.
    distance : float or array_like
        Negative values measure distance from the end of the line. Out-of-range
        values will be clipped to the line endings.
    normalized : bool, default False
        If True, the distance is a fraction of the total
        line length instead of the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line = LineString([(0, 2), (0, 10)])
    >>> shapely.line_interpolate_point(line, 2)
    <POINT (0 4)>
    >>> shapely.line_interpolate_point(line, 100)
    <POINT (0 10)>
    >>> shapely.line_interpolate_point(line, -2)
    <POINT (0 8)>
    >>> shapely.line_interpolate_point(line, [0.25, -0.25], normalized=True).tolist()
    [<POINT (0 4)>, <POINT (0 8)>]
    >>> shapely.line_interpolate_point(LineString(), 1)
    <POINT EMPTY>
    """
    ...
@overload
def line_interpolate_point(
    line: None, distance: ArrayLikeSeq[float], normalized: bool = False, **kwargs
) -> NDArray[np.object_]:
    """
    Return a point interpolated at given distance on a line.

    Parameters
    ----------
    line : Geometry or array_like
        For multilinestrings or geometrycollections, the first geometry is taken
        and the rest is ignored. This function raises a TypeError for non-linear
        geometries. For empty linear geometries, empty points are returned.
    distance : float or array_like
        Negative values measure distance from the end of the line. Out-of-range
        values will be clipped to the line endings.
    normalized : bool, default False
        If True, the distance is a fraction of the total
        line length instead of the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line = LineString([(0, 2), (0, 10)])
    >>> shapely.line_interpolate_point(line, 2)
    <POINT (0 4)>
    >>> shapely.line_interpolate_point(line, 100)
    <POINT (0 10)>
    >>> shapely.line_interpolate_point(line, -2)
    <POINT (0 8)>
    >>> shapely.line_interpolate_point(line, [0.25, -0.25], normalized=True).tolist()
    [<POINT (0 4)>, <POINT (0 8)>]
    >>> shapely.line_interpolate_point(LineString(), 1)
    <POINT EMPTY>
    """
    ...
@overload
def line_interpolate_point(
    line: LineString | MultiLineString | GeometryCollection, distance: float, normalized: bool = False, **kwargs
) -> Point:
    """
    Return a point interpolated at given distance on a line.

    Parameters
    ----------
    line : Geometry or array_like
        For multilinestrings or geometrycollections, the first geometry is taken
        and the rest is ignored. This function raises a TypeError for non-linear
        geometries. For empty linear geometries, empty points are returned.
    distance : float or array_like
        Negative values measure distance from the end of the line. Out-of-range
        values will be clipped to the line endings.
    normalized : bool, default False
        If True, the distance is a fraction of the total
        line length instead of the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line = LineString([(0, 2), (0, 10)])
    >>> shapely.line_interpolate_point(line, 2)
    <POINT (0 4)>
    >>> shapely.line_interpolate_point(line, 100)
    <POINT (0 10)>
    >>> shapely.line_interpolate_point(line, -2)
    <POINT (0 8)>
    >>> shapely.line_interpolate_point(line, [0.25, -0.25], normalized=True).tolist()
    [<POINT (0 4)>, <POINT (0 8)>]
    >>> shapely.line_interpolate_point(LineString(), 1)
    <POINT EMPTY>
    """
    ...
@overload
def line_interpolate_point(
    line: LineString | MultiLineString | GeometryCollection, distance: ArrayLikeSeq[float], normalized: bool = False, **kwargs
) -> GeoArray:
    """
    Return a point interpolated at given distance on a line.

    Parameters
    ----------
    line : Geometry or array_like
        For multilinestrings or geometrycollections, the first geometry is taken
        and the rest is ignored. This function raises a TypeError for non-linear
        geometries. For empty linear geometries, empty points are returned.
    distance : float or array_like
        Negative values measure distance from the end of the line. Out-of-range
        values will be clipped to the line endings.
    normalized : bool, default False
        If True, the distance is a fraction of the total
        line length instead of the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line = LineString([(0, 2), (0, 10)])
    >>> shapely.line_interpolate_point(line, 2)
    <POINT (0 4)>
    >>> shapely.line_interpolate_point(line, 100)
    <POINT (0 10)>
    >>> shapely.line_interpolate_point(line, -2)
    <POINT (0 8)>
    >>> shapely.line_interpolate_point(line, [0.25, -0.25], normalized=True).tolist()
    [<POINT (0 4)>, <POINT (0 8)>]
    >>> shapely.line_interpolate_point(LineString(), 1)
    <POINT EMPTY>
    """
    ...
@overload
def line_interpolate_point(
    line: OptGeoArrayLikeSeq, distance: ArrayLike[float], normalized: bool = False, **kwargs
) -> GeoArray:
    """
    Return a point interpolated at given distance on a line.

    Parameters
    ----------
    line : Geometry or array_like
        For multilinestrings or geometrycollections, the first geometry is taken
        and the rest is ignored. This function raises a TypeError for non-linear
        geometries. For empty linear geometries, empty points are returned.
    distance : float or array_like
        Negative values measure distance from the end of the line. Out-of-range
        values will be clipped to the line endings.
    normalized : bool, default False
        If True, the distance is a fraction of the total
        line length instead of the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line = LineString([(0, 2), (0, 10)])
    >>> shapely.line_interpolate_point(line, 2)
    <POINT (0 4)>
    >>> shapely.line_interpolate_point(line, 100)
    <POINT (0 10)>
    >>> shapely.line_interpolate_point(line, -2)
    <POINT (0 8)>
    >>> shapely.line_interpolate_point(line, [0.25, -0.25], normalized=True).tolist()
    [<POINT (0 4)>, <POINT (0 8)>]
    >>> shapely.line_interpolate_point(LineString(), 1)
    <POINT EMPTY>
    """
    ...
@overload
def line_locate_point(
    line: LineString | MultiLineString | GeometryCollection | None, other: Point | None, normalized: bool = False, **kwargs
) -> np.float64:
    """
    Return the distance to the line origin of given point.

    If given point does not intersect with the line, the point will first be
    projected onto the line after which the distance is taken.

    Parameters
    ----------
    line : Geometry or array_like
        Line or lines to calculate the distance to.
    other : Geometry or array_like
        Point or points to calculate the distance from.
    normalized : bool, default False
        If True, the distance is a fraction of the total line length instead of
        the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 2), (0, 10)])
    >>> point = Point(4, 4)
    >>> shapely.line_locate_point(line, point)
    2.0
    >>> shapely.line_locate_point(line, point, normalized=True)
    0.25
    >>> shapely.line_locate_point(line, Point(0, 18))
    8.0
    >>> shapely.line_locate_point(LineString(), point)
    nan
    """
    ...
@overload
def line_locate_point(
    line: LineString | MultiLineString | GeometryCollection | None, other: OptGeoArrayLikeSeq, normalized: bool = False, **kwargs
) -> NDArray[np.float64]:
    """
    Return the distance to the line origin of given point.

    If given point does not intersect with the line, the point will first be
    projected onto the line after which the distance is taken.

    Parameters
    ----------
    line : Geometry or array_like
        Line or lines to calculate the distance to.
    other : Geometry or array_like
        Point or points to calculate the distance from.
    normalized : bool, default False
        If True, the distance is a fraction of the total line length instead of
        the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 2), (0, 10)])
    >>> point = Point(4, 4)
    >>> shapely.line_locate_point(line, point)
    2.0
    >>> shapely.line_locate_point(line, point, normalized=True)
    0.25
    >>> shapely.line_locate_point(line, Point(0, 18))
    8.0
    >>> shapely.line_locate_point(LineString(), point)
    nan
    """
    ...
@overload
def line_locate_point(
    line: OptGeoArrayLikeSeq, other: OptGeoArrayLike, normalized: bool = False, **kwargs
) -> NDArray[np.float64]:
    """
    Return the distance to the line origin of given point.

    If given point does not intersect with the line, the point will first be
    projected onto the line after which the distance is taken.

    Parameters
    ----------
    line : Geometry or array_like
        Line or lines to calculate the distance to.
    other : Geometry or array_like
        Point or points to calculate the distance from.
    normalized : bool, default False
        If True, the distance is a fraction of the total line length instead of
        the absolute distance.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 2), (0, 10)])
    >>> point = Point(4, 4)
    >>> shapely.line_locate_point(line, point)
    2.0
    >>> shapely.line_locate_point(line, point, normalized=True)
    0.25
    >>> shapely.line_locate_point(line, Point(0, 18))
    8.0
    >>> shapely.line_locate_point(LineString(), point)
    nan
    """
    ...
@overload
def line_merge(line: None, directed: bool = False, **kwargs) -> None:
    """
    Return (Multi)LineStrings formed by combining the lines in a MultiLineString.

    Lines are joined together at their endpoints in case two lines are
    intersecting. Lines are not joined when 3 or more lines are intersecting at
    the endpoints. Line elements that cannot be joined are kept as is in the
    resulting MultiLineString.

    The direction of each merged LineString will be that of the majority of the
    LineStrings from which it was derived. Except if ``directed=True`` is
    specified, then the operation will not change the order of points within
    lines and so only lines which can be joined with no change in direction
    are merged.

    Parameters
    ----------
    line : Geometry or array_like
        Linear geometry or geometries to merge.
    directed : bool, default False
        Only combine lines if possible without changing point order.
        Requires GEOS >= 3.11.0
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiLineString
    >>> shapely.line_merge(MultiLineString([[(0, 2), (0, 10)], [(0, 10), (5, 10)]]))
    <LINESTRING (0 2, 0 10, 5 10)>
    >>> shapely.line_merge(MultiLineString([[(0, 2), (0, 10)], [(0, 11), (5, 10)]]))
    <MULTILINESTRING ((0 2, 0 10), (0 11, 5 10))>
    >>> shapely.line_merge(MultiLineString())
    <GEOMETRYCOLLECTION EMPTY>
    >>> shapely.line_merge(MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]))
    <LINESTRING (1 0, 0 0, 3 0)>
    >>> shapely.line_merge(MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]), directed=True)
    <MULTILINESTRING ((0 0, 1 0), (0 0, 3 0))>
    """
    ...
@overload
def line_merge(line: Geometry, directed: bool = False, **kwargs) -> LineString | MultiLineString | GeometryCollection:
    """
    Return (Multi)LineStrings formed by combining the lines in a MultiLineString.

    Lines are joined together at their endpoints in case two lines are
    intersecting. Lines are not joined when 3 or more lines are intersecting at
    the endpoints. Line elements that cannot be joined are kept as is in the
    resulting MultiLineString.

    The direction of each merged LineString will be that of the majority of the
    LineStrings from which it was derived. Except if ``directed=True`` is
    specified, then the operation will not change the order of points within
    lines and so only lines which can be joined with no change in direction
    are merged.

    Parameters
    ----------
    line : Geometry or array_like
        Linear geometry or geometries to merge.
    directed : bool, default False
        Only combine lines if possible without changing point order.
        Requires GEOS >= 3.11.0
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiLineString
    >>> shapely.line_merge(MultiLineString([[(0, 2), (0, 10)], [(0, 10), (5, 10)]]))
    <LINESTRING (0 2, 0 10, 5 10)>
    >>> shapely.line_merge(MultiLineString([[(0, 2), (0, 10)], [(0, 11), (5, 10)]]))
    <MULTILINESTRING ((0 2, 0 10), (0 11, 5 10))>
    >>> shapely.line_merge(MultiLineString())
    <GEOMETRYCOLLECTION EMPTY>
    >>> shapely.line_merge(MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]))
    <LINESTRING (1 0, 0 0, 3 0)>
    >>> shapely.line_merge(MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]), directed=True)
    <MULTILINESTRING ((0 0, 1 0), (0 0, 3 0))>
    """
    ...
@overload
def line_merge(line: OptGeoArrayLikeSeq, directed: bool = False, **kwargs) -> GeoArray:
    """
    Return (Multi)LineStrings formed by combining the lines in a MultiLineString.

    Lines are joined together at their endpoints in case two lines are
    intersecting. Lines are not joined when 3 or more lines are intersecting at
    the endpoints. Line elements that cannot be joined are kept as is in the
    resulting MultiLineString.

    The direction of each merged LineString will be that of the majority of the
    LineStrings from which it was derived. Except if ``directed=True`` is
    specified, then the operation will not change the order of points within
    lines and so only lines which can be joined with no change in direction
    are merged.

    Parameters
    ----------
    line : Geometry or array_like
        Linear geometry or geometries to merge.
    directed : bool, default False
        Only combine lines if possible without changing point order.
        Requires GEOS >= 3.11.0
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiLineString
    >>> shapely.line_merge(MultiLineString([[(0, 2), (0, 10)], [(0, 10), (5, 10)]]))
    <LINESTRING (0 2, 0 10, 5 10)>
    >>> shapely.line_merge(MultiLineString([[(0, 2), (0, 10)], [(0, 11), (5, 10)]]))
    <MULTILINESTRING ((0 2, 0 10), (0 11, 5 10))>
    >>> shapely.line_merge(MultiLineString())
    <GEOMETRYCOLLECTION EMPTY>
    >>> shapely.line_merge(MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]))
    <LINESTRING (1 0, 0 0, 3 0)>
    >>> shapely.line_merge(MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]), directed=True)
    <MULTILINESTRING ((0 0, 1 0), (0 0, 3 0))>
    """
    ...
@overload
def shared_paths(a: LineString | MultiLineString | None, b: None, **kwargs) -> None:
    """
    Return the shared paths between a and b.

    Both geometries should be linestrings or arrays of linestrings.
    A geometrycollection or array of geometrycollections is returned
    with two elements in each geometrycollection. The first element is a
    multilinestring containing shared paths with the same direction
    for both inputs. The second element is a multilinestring containing
    shared paths with the opposite direction for the two inputs.

    Parameters
    ----------
    a, b : Geometry or array_like
        Linestring or linestrings to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)])
    >>> shapely.shared_paths(line1, line2).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MULTILINESTRING ((1 0, 1 1)))'
    >>> line3 = LineString([(1, 1), (0, 1)])
    >>> shapely.shared_paths(line1, line3).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1)), MULTILINESTRING EMPTY)'
    """
    ...
@overload
def shared_paths(a: None, b: LineString | MultiLineString | None, **kwargs) -> None:
    """
    Return the shared paths between a and b.

    Both geometries should be linestrings or arrays of linestrings.
    A geometrycollection or array of geometrycollections is returned
    with two elements in each geometrycollection. The first element is a
    multilinestring containing shared paths with the same direction
    for both inputs. The second element is a multilinestring containing
    shared paths with the opposite direction for the two inputs.

    Parameters
    ----------
    a, b : Geometry or array_like
        Linestring or linestrings to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)])
    >>> shapely.shared_paths(line1, line2).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MULTILINESTRING ((1 0, 1 1)))'
    >>> line3 = LineString([(1, 1), (0, 1)])
    >>> shapely.shared_paths(line1, line3).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1)), MULTILINESTRING EMPTY)'
    """
    ...
@overload
def shared_paths(
    a: LineString | MultiLineString, b: LineString | MultiLineString, **kwargs
) -> GeometryCollection[MultiLineString]:
    """
    Return the shared paths between a and b.

    Both geometries should be linestrings or arrays of linestrings.
    A geometrycollection or array of geometrycollections is returned
    with two elements in each geometrycollection. The first element is a
    multilinestring containing shared paths with the same direction
    for both inputs. The second element is a multilinestring containing
    shared paths with the opposite direction for the two inputs.

    Parameters
    ----------
    a, b : Geometry or array_like
        Linestring or linestrings to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)])
    >>> shapely.shared_paths(line1, line2).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MULTILINESTRING ((1 0, 1 1)))'
    >>> line3 = LineString([(1, 1), (0, 1)])
    >>> shapely.shared_paths(line1, line3).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1)), MULTILINESTRING EMPTY)'
    """
    ...
@overload
def shared_paths(a: LineString | MultiLineString | None, b: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Return the shared paths between a and b.

    Both geometries should be linestrings or arrays of linestrings.
    A geometrycollection or array of geometrycollections is returned
    with two elements in each geometrycollection. The first element is a
    multilinestring containing shared paths with the same direction
    for both inputs. The second element is a multilinestring containing
    shared paths with the opposite direction for the two inputs.

    Parameters
    ----------
    a, b : Geometry or array_like
        Linestring or linestrings to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)])
    >>> shapely.shared_paths(line1, line2).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MULTILINESTRING ((1 0, 1 1)))'
    >>> line3 = LineString([(1, 1), (0, 1)])
    >>> shapely.shared_paths(line1, line3).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1)), MULTILINESTRING EMPTY)'
    """
    ...
@overload
def shared_paths(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> GeoArray:
    """
    Return the shared paths between a and b.

    Both geometries should be linestrings or arrays of linestrings.
    A geometrycollection or array of geometrycollections is returned
    with two elements in each geometrycollection. The first element is a
    multilinestring containing shared paths with the same direction
    for both inputs. The second element is a multilinestring containing
    shared paths with the opposite direction for the two inputs.

    Parameters
    ----------
    a, b : Geometry or array_like
        Linestring or linestrings to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)])
    >>> shapely.shared_paths(line1, line2).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MULTILINESTRING ((1 0, 1 1)))'
    >>> line3 = LineString([(1, 1), (0, 1)])
    >>> shapely.shared_paths(line1, line3).wkt
    'GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1)), MULTILINESTRING EMPTY)'
    """
    ...
@overload
def shortest_line(a: Geometry | None, b: None, **kwargs) -> None:
    """
    Return the shortest line between two geometries.

    The resulting line consists of two points, representing the nearest
    points between the geometry pair. The line always starts in the first
    geometry `a` and ends in the second geometry `b`. The endpoints of the
    line will not necessarily be existing vertices of the input geometries
    `a` and `b`, but can also be a point along a line segment.

    Parameters
    ----------
    a, b : Geometry or array_like
        Geometry or geometries to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    prepare : improve performance by preparing ``a`` (the first argument)

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(0, 3), (3, 0), (5, 3)])
    >>> shapely.shortest_line(line1, line2)
    <LINESTRING (1 1, 1.5 1.5)>
    """
    ...
@overload
def shortest_line(a: None, b: Geometry | None, **kwargs) -> None:
    """
    Return the shortest line between two geometries.

    The resulting line consists of two points, representing the nearest
    points between the geometry pair. The line always starts in the first
    geometry `a` and ends in the second geometry `b`. The endpoints of the
    line will not necessarily be existing vertices of the input geometries
    `a` and `b`, but can also be a point along a line segment.

    Parameters
    ----------
    a, b : Geometry or array_like
        Geometry or geometries to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    prepare : improve performance by preparing ``a`` (the first argument)

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(0, 3), (3, 0), (5, 3)])
    >>> shapely.shortest_line(line1, line2)
    <LINESTRING (1 1, 1.5 1.5)>
    """
    ...
@overload
def shortest_line(a: Geometry, b: Geometry, **kwargs) -> LineString:
    """
    Return the shortest line between two geometries.

    The resulting line consists of two points, representing the nearest
    points between the geometry pair. The line always starts in the first
    geometry `a` and ends in the second geometry `b`. The endpoints of the
    line will not necessarily be existing vertices of the input geometries
    `a` and `b`, but can also be a point along a line segment.

    Parameters
    ----------
    a, b : Geometry or array_like
        Geometry or geometries to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    prepare : improve performance by preparing ``a`` (the first argument)

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(0, 3), (3, 0), (5, 3)])
    >>> shapely.shortest_line(line1, line2)
    <LINESTRING (1 1, 1.5 1.5)>
    """
    ...
@overload
def shortest_line(a: Geometry | None, b: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Return the shortest line between two geometries.

    The resulting line consists of two points, representing the nearest
    points between the geometry pair. The line always starts in the first
    geometry `a` and ends in the second geometry `b`. The endpoints of the
    line will not necessarily be existing vertices of the input geometries
    `a` and `b`, but can also be a point along a line segment.

    Parameters
    ----------
    a, b : Geometry or array_like
        Geometry or geometries to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    prepare : improve performance by preparing ``a`` (the first argument)

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(0, 3), (3, 0), (5, 3)])
    >>> shapely.shortest_line(line1, line2)
    <LINESTRING (1 1, 1.5 1.5)>
    """
    ...
@overload
def shortest_line(a: OptGeoArrayLikeSeq, b: OptGeoArrayLike, **kwargs) -> GeoArray:
    """
    Return the shortest line between two geometries.

    The resulting line consists of two points, representing the nearest
    points between the geometry pair. The line always starts in the first
    geometry `a` and ends in the second geometry `b`. The endpoints of the
    line will not necessarily be existing vertices of the input geometries
    `a` and `b`, but can also be a point along a line segment.

    Parameters
    ----------
    a, b : Geometry or array_like
        Geometry or geometries to compare.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    prepare : improve performance by preparing ``a`` (the first argument)

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString
    >>> line1 = LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    >>> line2 = LineString([(0, 3), (3, 0), (5, 3)])
    >>> shapely.shortest_line(line1, line2)
    <LINESTRING (1 1, 1.5 1.5)>
    """
    ...
