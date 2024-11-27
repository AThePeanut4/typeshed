from collections.abc import Sequence
from typing import Any, Literal, SupportsIndex, overload

from ._enum import ParamEnum
from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq, OptGeoT
from .geometry import GeometryCollection, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
from .geometry.base import BaseGeometry, BaseMultipartGeometry
from .lib import Geometry

__all__ = [
    "BufferCapStyle",
    "BufferJoinStyle",
    "boundary",
    "buffer",
    "offset_curve",
    "centroid",
    "clip_by_rect",
    "concave_hull",
    "convex_hull",
    "delaunay_triangles",
    "segmentize",
    "envelope",
    "extract_unique_points",
    "build_area",
    "make_valid",
    "normalize",
    "node",
    "point_on_surface",
    "polygonize",
    "polygonize_full",
    "remove_repeated_points",
    "reverse",
    "simplify",
    "snap",
    "voronoi_polygons",
    "oriented_envelope",
    "minimum_rotated_rectangle",
    "minimum_bounding_circle",
]

class BufferCapStyle(ParamEnum):
    """An enumeration."""
    round = 1
    flat = 2
    square = 3

class BufferJoinStyle(ParamEnum):
    """An enumeration."""
    round = 1
    mitre = 2
    bevel = 3

@overload
def boundary(geometry: Point | MultiPoint, **kwargs) -> GeometryCollection:
    """
    Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    ...
@overload
def boundary(geometry: LineString | MultiLineString, **kwargs) -> MultiPoint:
    """
    Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    ...
@overload
def boundary(geometry: Polygon | MultiPolygon, **kwargs) -> MultiLineString:
    """
    Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    ...
@overload
def boundary(geometry: GeometryCollection | None, **kwargs) -> None:
    """
    Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    ...
@overload
def boundary(geometry: Geometry, **kwargs) -> BaseMultipartGeometry | Any:
    """
    Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    ...
@overload
def boundary(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    ...
@overload
def buffer(
    geometry: Geometry,
    distance: float,
    quad_segs: int = 8,
    cap_style: BufferJoinStyle | Literal["round", "square", "flat"] = "round",
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    single_sided: bool = False,
    **kwargs,
) -> Polygon:
    """
    Computes the buffer of a geometry for positive and negative buffer distance.

    The buffer of a geometry is defined as the Minkowski sum (or difference,
    for negative distance) of the geometry with a circle with radius equal
    to the absolute value of the buffer distance.

    The buffer operation always returns a polygonal result. The negative
    or zero-distance buffer of lines and points is always empty.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the circle radius in the Minkowski sum (or difference).
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
        results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
        ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
        only BufferCapStyle.flat ('flat') will end at the original vertex,
        while BufferCapStyle.square ('square') involves adding the buffer width.
    join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
        Specifies the shape of buffered line midpoints. BufferJoinStyle.round ('round')
        results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
        edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
        in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    single_sided : bool, default False
        Only buffer at one side of the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon, BufferCapStyle, BufferJoinStyle
    >>> buffer(Point(10, 10), 2, quad_segs=1)
    <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>
    >>> buffer(Point(10, 10), 2, quad_segs=2)
    <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>
    >>> buffer(Point(10, 10), -2, quad_segs=1)
    <POLYGON EMPTY>
    >>> line = LineString([(10, 10), (20, 10)])
    >>> buffer(line, 2, cap_style="square")
    <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>
    >>> buffer(line, 2, cap_style="flat")
    <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>
    >>> buffer(line, 2, single_sided=True, cap_style="flat")
    <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>
    >>> line2 = LineString([(10, 10), (20, 10), (20, 20)])
    >>> buffer(line2, 2, cap_style="flat", join_style="bevel")
    <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre")
    <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
    <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>
    >>> square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> buffer(square, 2, join_style="mitre")
    <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>
    >>> buffer(square, -2, join_style="mitre")
    <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>
    >>> buffer(square, -5, join_style="mitre")
    <POLYGON EMPTY>
    >>> buffer(line, float("nan")) is None
    True
    """
    ...
@overload
def buffer(
    geometry: None,
    distance: float,
    quad_segs: int = 8,
    cap_style: BufferJoinStyle | Literal["round", "square", "flat"] = "round",
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    single_sided: bool = False,
    **kwargs,
) -> None:
    """
    Computes the buffer of a geometry for positive and negative buffer distance.

    The buffer of a geometry is defined as the Minkowski sum (or difference,
    for negative distance) of the geometry with a circle with radius equal
    to the absolute value of the buffer distance.

    The buffer operation always returns a polygonal result. The negative
    or zero-distance buffer of lines and points is always empty.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the circle radius in the Minkowski sum (or difference).
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
        results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
        ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
        only BufferCapStyle.flat ('flat') will end at the original vertex,
        while BufferCapStyle.square ('square') involves adding the buffer width.
    join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
        Specifies the shape of buffered line midpoints. BufferJoinStyle.round ('round')
        results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
        edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
        in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    single_sided : bool, default False
        Only buffer at one side of the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon, BufferCapStyle, BufferJoinStyle
    >>> buffer(Point(10, 10), 2, quad_segs=1)
    <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>
    >>> buffer(Point(10, 10), 2, quad_segs=2)
    <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>
    >>> buffer(Point(10, 10), -2, quad_segs=1)
    <POLYGON EMPTY>
    >>> line = LineString([(10, 10), (20, 10)])
    >>> buffer(line, 2, cap_style="square")
    <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>
    >>> buffer(line, 2, cap_style="flat")
    <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>
    >>> buffer(line, 2, single_sided=True, cap_style="flat")
    <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>
    >>> line2 = LineString([(10, 10), (20, 10), (20, 20)])
    >>> buffer(line2, 2, cap_style="flat", join_style="bevel")
    <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre")
    <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
    <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>
    >>> square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> buffer(square, 2, join_style="mitre")
    <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>
    >>> buffer(square, -2, join_style="mitre")
    <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>
    >>> buffer(square, -5, join_style="mitre")
    <POLYGON EMPTY>
    >>> buffer(line, float("nan")) is None
    True
    """
    ...
@overload
def buffer(
    geometry: Geometry | None,
    distance: float,
    quad_segs: int = 8,
    cap_style: BufferJoinStyle | Literal["round", "square", "flat"] = "round",
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    single_sided: bool = False,
    **kwargs,
) -> Polygon | None:
    """
    Computes the buffer of a geometry for positive and negative buffer distance.

    The buffer of a geometry is defined as the Minkowski sum (or difference,
    for negative distance) of the geometry with a circle with radius equal
    to the absolute value of the buffer distance.

    The buffer operation always returns a polygonal result. The negative
    or zero-distance buffer of lines and points is always empty.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the circle radius in the Minkowski sum (or difference).
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
        results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
        ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
        only BufferCapStyle.flat ('flat') will end at the original vertex,
        while BufferCapStyle.square ('square') involves adding the buffer width.
    join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
        Specifies the shape of buffered line midpoints. BufferJoinStyle.round ('round')
        results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
        edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
        in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    single_sided : bool, default False
        Only buffer at one side of the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon, BufferCapStyle, BufferJoinStyle
    >>> buffer(Point(10, 10), 2, quad_segs=1)
    <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>
    >>> buffer(Point(10, 10), 2, quad_segs=2)
    <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>
    >>> buffer(Point(10, 10), -2, quad_segs=1)
    <POLYGON EMPTY>
    >>> line = LineString([(10, 10), (20, 10)])
    >>> buffer(line, 2, cap_style="square")
    <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>
    >>> buffer(line, 2, cap_style="flat")
    <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>
    >>> buffer(line, 2, single_sided=True, cap_style="flat")
    <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>
    >>> line2 = LineString([(10, 10), (20, 10), (20, 20)])
    >>> buffer(line2, 2, cap_style="flat", join_style="bevel")
    <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre")
    <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
    <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>
    >>> square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> buffer(square, 2, join_style="mitre")
    <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>
    >>> buffer(square, -2, join_style="mitre")
    <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>
    >>> buffer(square, -5, join_style="mitre")
    <POLYGON EMPTY>
    >>> buffer(line, float("nan")) is None
    True
    """
    ...
@overload
def buffer(
    geometry: OptGeoArrayLike,
    distance: ArrayLikeSeq[float],
    quad_segs: int = 8,
    cap_style: BufferJoinStyle | Literal["round", "square", "flat"] = "round",
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    single_sided: bool = False,
    **kwargs,
) -> GeoArray:
    """
    Computes the buffer of a geometry for positive and negative buffer distance.

    The buffer of a geometry is defined as the Minkowski sum (or difference,
    for negative distance) of the geometry with a circle with radius equal
    to the absolute value of the buffer distance.

    The buffer operation always returns a polygonal result. The negative
    or zero-distance buffer of lines and points is always empty.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the circle radius in the Minkowski sum (or difference).
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
        results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
        ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
        only BufferCapStyle.flat ('flat') will end at the original vertex,
        while BufferCapStyle.square ('square') involves adding the buffer width.
    join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
        Specifies the shape of buffered line midpoints. BufferJoinStyle.round ('round')
        results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
        edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
        in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    single_sided : bool, default False
        Only buffer at one side of the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon, BufferCapStyle, BufferJoinStyle
    >>> buffer(Point(10, 10), 2, quad_segs=1)
    <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>
    >>> buffer(Point(10, 10), 2, quad_segs=2)
    <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>
    >>> buffer(Point(10, 10), -2, quad_segs=1)
    <POLYGON EMPTY>
    >>> line = LineString([(10, 10), (20, 10)])
    >>> buffer(line, 2, cap_style="square")
    <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>
    >>> buffer(line, 2, cap_style="flat")
    <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>
    >>> buffer(line, 2, single_sided=True, cap_style="flat")
    <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>
    >>> line2 = LineString([(10, 10), (20, 10), (20, 20)])
    >>> buffer(line2, 2, cap_style="flat", join_style="bevel")
    <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre")
    <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
    <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>
    >>> square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> buffer(square, 2, join_style="mitre")
    <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>
    >>> buffer(square, -2, join_style="mitre")
    <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>
    >>> buffer(square, -5, join_style="mitre")
    <POLYGON EMPTY>
    >>> buffer(line, float("nan")) is None
    True
    """
    ...
@overload
def buffer(
    geometry: OptGeoArrayLikeSeq,
    distance: ArrayLike[float],
    quad_segs: int = 8,
    cap_style: BufferJoinStyle | Literal["round", "square", "flat"] = "round",
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    single_sided: bool = False,
    **kwargs,
) -> GeoArray:
    """
    Computes the buffer of a geometry for positive and negative buffer distance.

    The buffer of a geometry is defined as the Minkowski sum (or difference,
    for negative distance) of the geometry with a circle with radius equal
    to the absolute value of the buffer distance.

    The buffer operation always returns a polygonal result. The negative
    or zero-distance buffer of lines and points is always empty.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the circle radius in the Minkowski sum (or difference).
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
        results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
        ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
        only BufferCapStyle.flat ('flat') will end at the original vertex,
        while BufferCapStyle.square ('square') involves adding the buffer width.
    join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
        Specifies the shape of buffered line midpoints. BufferJoinStyle.round ('round')
        results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
        edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
        in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    single_sided : bool, default False
        Only buffer at one side of the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon, BufferCapStyle, BufferJoinStyle
    >>> buffer(Point(10, 10), 2, quad_segs=1)
    <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>
    >>> buffer(Point(10, 10), 2, quad_segs=2)
    <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>
    >>> buffer(Point(10, 10), -2, quad_segs=1)
    <POLYGON EMPTY>
    >>> line = LineString([(10, 10), (20, 10)])
    >>> buffer(line, 2, cap_style="square")
    <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>
    >>> buffer(line, 2, cap_style="flat")
    <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>
    >>> buffer(line, 2, single_sided=True, cap_style="flat")
    <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>
    >>> line2 = LineString([(10, 10), (20, 10), (20, 20)])
    >>> buffer(line2, 2, cap_style="flat", join_style="bevel")
    <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre")
    <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
    <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>
    >>> square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> buffer(square, 2, join_style="mitre")
    <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>
    >>> buffer(square, -2, join_style="mitre")
    <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>
    >>> buffer(square, -5, join_style="mitre")
    <POLYGON EMPTY>
    >>> buffer(line, float("nan")) is None
    True
    """
    ...
@overload
def offset_curve(
    geometry: Geometry,
    distance: float,
    quad_segs: SupportsIndex = 8,
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    **kwargs,
) -> LineString | MultiLineString:
    """
    Returns a (Multi)LineString at a distance from the object
    on its right or its left side.

    For positive distance the offset will be at the left side of the input
    line. For a negative distance it will be at the right side. In general,
    this function tries to preserve the direction of the input.

    Note: the behaviour regarding orientation of the resulting line depends
    on the GEOS version. With GEOS < 3.11, the line retains the same
    direction for a left offset (positive distance) or has opposite direction
    for a right offset (negative distance), and this behaviour was documented
    as such in previous Shapely versions. Starting with GEOS 3.11, the
    function tries to preserve the orientation of the original line.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the offset distance from the input geometry. Negative
        for right side offset, positive for left side offset.
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of outside corners. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line = LineString([(0, 0), (0, 2)])
    >>> offset_curve(line, 2)
    <LINESTRING (-2 0, -2 2)>
    >>> offset_curve(line, -2)
    <LINESTRING (2 0, 2 2)>
    """
    ...
@overload
def offset_curve(
    geometry: None,
    distance: float,
    quad_segs: SupportsIndex = 8,
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    **kwargs,
) -> None:
    """
    Returns a (Multi)LineString at a distance from the object
    on its right or its left side.

    For positive distance the offset will be at the left side of the input
    line. For a negative distance it will be at the right side. In general,
    this function tries to preserve the direction of the input.

    Note: the behaviour regarding orientation of the resulting line depends
    on the GEOS version. With GEOS < 3.11, the line retains the same
    direction for a left offset (positive distance) or has opposite direction
    for a right offset (negative distance), and this behaviour was documented
    as such in previous Shapely versions. Starting with GEOS 3.11, the
    function tries to preserve the orientation of the original line.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the offset distance from the input geometry. Negative
        for right side offset, positive for left side offset.
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of outside corners. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line = LineString([(0, 0), (0, 2)])
    >>> offset_curve(line, 2)
    <LINESTRING (-2 0, -2 2)>
    >>> offset_curve(line, -2)
    <LINESTRING (2 0, 2 2)>
    """
    ...
@overload
def offset_curve(
    geometry: Geometry | None,
    distance: float,
    quad_segs: SupportsIndex = 8,
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    **kwargs,
) -> LineString | MultiLineString | None:
    """
    Returns a (Multi)LineString at a distance from the object
    on its right or its left side.

    For positive distance the offset will be at the left side of the input
    line. For a negative distance it will be at the right side. In general,
    this function tries to preserve the direction of the input.

    Note: the behaviour regarding orientation of the resulting line depends
    on the GEOS version. With GEOS < 3.11, the line retains the same
    direction for a left offset (positive distance) or has opposite direction
    for a right offset (negative distance), and this behaviour was documented
    as such in previous Shapely versions. Starting with GEOS 3.11, the
    function tries to preserve the orientation of the original line.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the offset distance from the input geometry. Negative
        for right side offset, positive for left side offset.
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of outside corners. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line = LineString([(0, 0), (0, 2)])
    >>> offset_curve(line, 2)
    <LINESTRING (-2 0, -2 2)>
    >>> offset_curve(line, -2)
    <LINESTRING (2 0, 2 2)>
    """
    ...
@overload
def offset_curve(
    geometry: OptGeoArrayLike,
    distance: ArrayLikeSeq[float],
    quad_segs: SupportsIndex = 8,
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    **kwargs,
) -> GeoArray:
    """
    Returns a (Multi)LineString at a distance from the object
    on its right or its left side.

    For positive distance the offset will be at the left side of the input
    line. For a negative distance it will be at the right side. In general,
    this function tries to preserve the direction of the input.

    Note: the behaviour regarding orientation of the resulting line depends
    on the GEOS version. With GEOS < 3.11, the line retains the same
    direction for a left offset (positive distance) or has opposite direction
    for a right offset (negative distance), and this behaviour was documented
    as such in previous Shapely versions. Starting with GEOS 3.11, the
    function tries to preserve the orientation of the original line.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the offset distance from the input geometry. Negative
        for right side offset, positive for left side offset.
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of outside corners. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line = LineString([(0, 0), (0, 2)])
    >>> offset_curve(line, 2)
    <LINESTRING (-2 0, -2 2)>
    >>> offset_curve(line, -2)
    <LINESTRING (2 0, 2 2)>
    """
    ...
@overload
def offset_curve(
    geometry: OptGeoArrayLikeSeq,
    distance: ArrayLike[float],
    quad_segs: SupportsIndex = 8,
    join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
    mitre_limit: float = 5.0,
    **kwargs,
) -> GeoArray:
    """
    Returns a (Multi)LineString at a distance from the object
    on its right or its left side.

    For positive distance the offset will be at the left side of the input
    line. For a negative distance it will be at the right side. In general,
    this function tries to preserve the direction of the input.

    Note: the behaviour regarding orientation of the resulting line depends
    on the GEOS version. With GEOS < 3.11, the line retains the same
    direction for a left offset (positive distance) or has opposite direction
    for a right offset (negative distance), and this behaviour was documented
    as such in previous Shapely versions. Starting with GEOS 3.11, the
    function tries to preserve the orientation of the original line.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the offset distance from the input geometry. Negative
        for right side offset, positive for left side offset.
    quad_segs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of outside corners. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString
    >>> line = LineString([(0, 0), (0, 2)])
    >>> offset_curve(line, 2)
    <LINESTRING (-2 0, -2 2)>
    >>> offset_curve(line, -2)
    <LINESTRING (2 0, 2 2)>
    """
    ...
@overload
def centroid(geometry: Geometry, **kwargs) -> Point:
    """
    Computes the geometric center (center-of-mass) of a geometry.

    For multipoints this is computed as the mean of the input coordinates.
    For multilinestrings the centroid is weighted by the length of each
    line segment. For multipolygons the centroid is weighted by the area of
    each polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> centroid(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> centroid(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(MultiPoint([(0, 0), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def centroid(geometry: None, **kwargs) -> None:
    """
    Computes the geometric center (center-of-mass) of a geometry.

    For multipoints this is computed as the mean of the input coordinates.
    For multilinestrings the centroid is weighted by the length of each
    line segment. For multipolygons the centroid is weighted by the area of
    each polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> centroid(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> centroid(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(MultiPoint([(0, 0), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def centroid(geometry: Geometry | None, **kwargs) -> Point | None:
    """
    Computes the geometric center (center-of-mass) of a geometry.

    For multipoints this is computed as the mean of the input coordinates.
    For multilinestrings the centroid is weighted by the length of each
    line segment. For multipolygons the centroid is weighted by the area of
    each polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> centroid(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> centroid(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(MultiPoint([(0, 0), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def centroid(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Computes the geometric center (center-of-mass) of a geometry.

    For multipoints this is computed as the mean of the input coordinates.
    For multilinestrings the centroid is weighted by the length of each
    line segment. For multipolygons the centroid is weighted by the area of
    each polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> centroid(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> centroid(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(MultiPoint([(0, 0), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def clip_by_rect(geometry: Geometry, xmin: float, ymin: float, xmax: float, ymax: float, **kwargs) -> BaseGeometry:
    """
    Returns the portion of a geometry within a rectangle.

    The geometry is clipped in a fast but possibly dirty way. The output is
    not guaranteed to be valid. No exceptions will be raised for topological
    errors.

    Note: empty geometries or geometries that do not overlap with the
    specified bounds will result in GEOMETRYCOLLECTION EMPTY.

    Parameters
    ----------
    geometry : Geometry or array_like
        The geometry to be clipped
    xmin : float
        Minimum x value of the rectangle
    ymin : float
        Minimum y value of the rectangle
    xmax : float
        Maximum x value of the rectangle
    ymax : float
        Maximum y value of the rectangle
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (10, 10)])
    >>> clip_by_rect(line, 0., 0., 1., 1.)
    <LINESTRING (0 0, 1 1)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> clip_by_rect(polygon, 0., 0., 1., 1.)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    ...
@overload
def clip_by_rect(geometry: None, xmin: float, ymin: float, xmax: float, ymax: float, **kwargs) -> None:
    """
    Returns the portion of a geometry within a rectangle.

    The geometry is clipped in a fast but possibly dirty way. The output is
    not guaranteed to be valid. No exceptions will be raised for topological
    errors.

    Note: empty geometries or geometries that do not overlap with the
    specified bounds will result in GEOMETRYCOLLECTION EMPTY.

    Parameters
    ----------
    geometry : Geometry or array_like
        The geometry to be clipped
    xmin : float
        Minimum x value of the rectangle
    ymin : float
        Minimum y value of the rectangle
    xmax : float
        Maximum x value of the rectangle
    ymax : float
        Maximum y value of the rectangle
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (10, 10)])
    >>> clip_by_rect(line, 0., 0., 1., 1.)
    <LINESTRING (0 0, 1 1)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> clip_by_rect(polygon, 0., 0., 1., 1.)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    ...
@overload
def clip_by_rect(
    geometry: Geometry | None, xmin: float, ymin: float, xmax: float, ymax: float, **kwargs
) -> BaseGeometry | None:
    """
    Returns the portion of a geometry within a rectangle.

    The geometry is clipped in a fast but possibly dirty way. The output is
    not guaranteed to be valid. No exceptions will be raised for topological
    errors.

    Note: empty geometries or geometries that do not overlap with the
    specified bounds will result in GEOMETRYCOLLECTION EMPTY.

    Parameters
    ----------
    geometry : Geometry or array_like
        The geometry to be clipped
    xmin : float
        Minimum x value of the rectangle
    ymin : float
        Minimum y value of the rectangle
    xmax : float
        Maximum x value of the rectangle
    ymax : float
        Maximum y value of the rectangle
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (10, 10)])
    >>> clip_by_rect(line, 0., 0., 1., 1.)
    <LINESTRING (0 0, 1 1)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> clip_by_rect(polygon, 0., 0., 1., 1.)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    ...
@overload
def clip_by_rect(geometry: OptGeoArrayLikeSeq, xmin: float, ymin: float, xmax: float, ymax: float, **kwargs) -> GeoArray:
    """
    Returns the portion of a geometry within a rectangle.

    The geometry is clipped in a fast but possibly dirty way. The output is
    not guaranteed to be valid. No exceptions will be raised for topological
    errors.

    Note: empty geometries or geometries that do not overlap with the
    specified bounds will result in GEOMETRYCOLLECTION EMPTY.

    Parameters
    ----------
    geometry : Geometry or array_like
        The geometry to be clipped
    xmin : float
        Minimum x value of the rectangle
    ymin : float
        Minimum y value of the rectangle
    xmax : float
        Maximum x value of the rectangle
    ymax : float
        Maximum y value of the rectangle
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (10, 10)])
    >>> clip_by_rect(line, 0., 0., 1., 1.)
    <LINESTRING (0 0, 1 1)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> clip_by_rect(polygon, 0., 0., 1., 1.)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    ...
@overload
def concave_hull(geometry: Geometry, ratio: float = 0.0, allow_holes: bool = False, **kwargs) -> BaseGeometry:
    """
    Computes a concave geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    ratio : float, default 0.0
        Number in the range [0, 1]. Higher numbers will include fewer vertices
        in the hull.
    allow_holes : bool, default False
        If set to True, the concave hull may have holes.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=0.1)
    <POLYGON ((0 0, 0 3, 1 1, 3 3, 3 0, 0 0))>
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=1.0)
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0))>
    >>> concave_hull(Polygon())
    <POLYGON EMPTY>
    """
    ...
@overload
def concave_hull(geometry: None, ratio: float = 0.0, allow_holes: bool = False, **kwargs) -> None:
    """
    Computes a concave geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    ratio : float, default 0.0
        Number in the range [0, 1]. Higher numbers will include fewer vertices
        in the hull.
    allow_holes : bool, default False
        If set to True, the concave hull may have holes.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=0.1)
    <POLYGON ((0 0, 0 3, 1 1, 3 3, 3 0, 0 0))>
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=1.0)
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0))>
    >>> concave_hull(Polygon())
    <POLYGON EMPTY>
    """
    ...
@overload
def concave_hull(geometry: Geometry | None, ratio: float = 0.0, allow_holes: bool = False, **kwargs) -> BaseGeometry | None:
    """
    Computes a concave geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    ratio : float, default 0.0
        Number in the range [0, 1]. Higher numbers will include fewer vertices
        in the hull.
    allow_holes : bool, default False
        If set to True, the concave hull may have holes.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=0.1)
    <POLYGON ((0 0, 0 3, 1 1, 3 3, 3 0, 0 0))>
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=1.0)
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0))>
    >>> concave_hull(Polygon())
    <POLYGON EMPTY>
    """
    ...
@overload
def concave_hull(geometry: OptGeoArrayLikeSeq, ratio: float = 0.0, allow_holes: bool = False, **kwargs) -> GeoArray:
    """
    Computes a concave geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    ratio : float, default 0.0
        Number in the range [0, 1]. Higher numbers will include fewer vertices
        in the hull.
    allow_holes : bool, default False
        If set to True, the concave hull may have holes.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=0.1)
    <POLYGON ((0 0, 0 3, 1 1, 3 3, 3 0, 0 0))>
    >>> concave_hull(MultiPoint([(0, 0), (0, 3), (1, 1), (3, 0), (3, 3)]), ratio=1.0)
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0))>
    >>> concave_hull(Polygon())
    <POLYGON EMPTY>
    """
    ...
@overload
def convex_hull(geometry: Geometry, **kwargs) -> BaseGeometry:
    """
    Computes the minimum convex geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> convex_hull(MultiPoint([(0, 0), (10, 0), (10, 10)]))
    <POLYGON ((0 0, 10 10, 10 0, 0 0))>
    >>> convex_hull(Polygon())
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def convex_hull(geometry: None, **kwargs) -> None:
    """
    Computes the minimum convex geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> convex_hull(MultiPoint([(0, 0), (10, 0), (10, 10)]))
    <POLYGON ((0 0, 10 10, 10 0, 0 0))>
    >>> convex_hull(Polygon())
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def convex_hull(geometry: Geometry | None, **kwargs) -> BaseGeometry | None:
    """
    Computes the minimum convex geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> convex_hull(MultiPoint([(0, 0), (10, 0), (10, 10)]))
    <POLYGON ((0 0, 10 10, 10 0, 0 0))>
    >>> convex_hull(Polygon())
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def convex_hull(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Computes the minimum convex geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> convex_hull(MultiPoint([(0, 0), (10, 0), (10, 10)]))
    <POLYGON ((0 0, 10 10, 10 0, 0 0))>
    >>> convex_hull(Polygon())
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: Geometry, tolerance: float = 0.0, only_edges: Literal[False] = False, **kwargs
) -> GeometryCollection:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(geometry: Geometry, tolerance: float, only_edges: Literal[True], **kwargs) -> MultiLineString:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(geometry: Geometry, tolerance: float = 0.0, *, only_edges: Literal[True], **kwargs) -> MultiLineString:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: Geometry, tolerance: float = 0.0, only_edges: bool = False, **kwargs
) -> GeometryCollection | MultiLineString:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(geometry: None, tolerance: float = 0.0, only_edges: bool = False, **kwargs) -> None:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: Geometry | None, tolerance: float = 0.0, only_edges: bool = False, **kwargs
) -> GeometryCollection | MultiLineString | None:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: OptGeoArrayLike, tolerance: ArrayLike[float], only_edges: ArrayLikeSeq[bool], **kwargs
) -> GeoArray:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: OptGeoArrayLike, tolerance: ArrayLike[float] = 0.0, *, only_edges: ArrayLikeSeq[bool], **kwargs
) -> GeoArray:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: OptGeoArrayLike, tolerance: ArrayLikeSeq[float], only_edges: ArrayLike[bool] = False, **kwargs
) -> GeoArray:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def delaunay_triangles(
    geometry: OptGeoArrayLikeSeq, tolerance: ArrayLike[float] = 0.0, only_edges: ArrayLike[bool] = False, **kwargs
) -> GeoArray:
    """
    Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), tolerance=2).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)])).normalize()
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 100 100, 60 30, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def envelope(geometry: Point, **kwargs) -> Point:
    """
    Computes the minimum bounding box that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point
    >>> envelope(LineString([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(MultiPoint([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(Point(0, 0))
    <POINT (0 0)>
    >>> envelope(GeometryCollection([]))
    <POINT EMPTY>
    """
    ...
@overload
def envelope(geometry: Geometry, **kwargs) -> BaseGeometry:
    """
    Computes the minimum bounding box that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point
    >>> envelope(LineString([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(MultiPoint([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(Point(0, 0))
    <POINT (0 0)>
    >>> envelope(GeometryCollection([]))
    <POINT EMPTY>
    """
    ...
@overload
def envelope(geometry: None, **kwargs) -> None:
    """
    Computes the minimum bounding box that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point
    >>> envelope(LineString([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(MultiPoint([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(Point(0, 0))
    <POINT (0 0)>
    >>> envelope(GeometryCollection([]))
    <POINT EMPTY>
    """
    ...
@overload
def envelope(geometry: Geometry | None, **kwargs) -> BaseGeometry | None:
    """
    Computes the minimum bounding box that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point
    >>> envelope(LineString([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(MultiPoint([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(Point(0, 0))
    <POINT (0 0)>
    >>> envelope(GeometryCollection([]))
    <POINT EMPTY>
    """
    ...
@overload
def envelope(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Computes the minimum bounding box that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point
    >>> envelope(LineString([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(MultiPoint([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(Point(0, 0))
    <POINT (0 0)>
    >>> envelope(GeometryCollection([]))
    <POINT EMPTY>
    """
    ...
@overload
def extract_unique_points(geometry: Geometry, **kwargs) -> MultiPoint:
    """
    Returns all distinct vertices of an input geometry as a multipoint.

    Note that only 2 dimensions of the vertices are considered when testing
    for equality.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Point, Polygon
    >>> extract_unique_points(Point(0, 0))
    <MULTIPOINT (0 0)>
    >>> extract_unique_points(LineString([(0, 0), (1, 1), (1, 1)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 0, 1 1, 0 1)>
    >>> extract_unique_points(MultiPoint([(0, 0), (1, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(LineString())
    <MULTIPOINT EMPTY>
    """
    ...
@overload
def extract_unique_points(geometry: None, **kwargs) -> None:
    """
    Returns all distinct vertices of an input geometry as a multipoint.

    Note that only 2 dimensions of the vertices are considered when testing
    for equality.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Point, Polygon
    >>> extract_unique_points(Point(0, 0))
    <MULTIPOINT (0 0)>
    >>> extract_unique_points(LineString([(0, 0), (1, 1), (1, 1)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 0, 1 1, 0 1)>
    >>> extract_unique_points(MultiPoint([(0, 0), (1, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(LineString())
    <MULTIPOINT EMPTY>
    """
    ...
@overload
def extract_unique_points(geometry: Geometry | None, **kwargs) -> MultiPoint | None:
    """
    Returns all distinct vertices of an input geometry as a multipoint.

    Note that only 2 dimensions of the vertices are considered when testing
    for equality.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Point, Polygon
    >>> extract_unique_points(Point(0, 0))
    <MULTIPOINT (0 0)>
    >>> extract_unique_points(LineString([(0, 0), (1, 1), (1, 1)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 0, 1 1, 0 1)>
    >>> extract_unique_points(MultiPoint([(0, 0), (1, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(LineString())
    <MULTIPOINT EMPTY>
    """
    ...
@overload
def extract_unique_points(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Returns all distinct vertices of an input geometry as a multipoint.

    Note that only 2 dimensions of the vertices are considered when testing
    for equality.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Point, Polygon
    >>> extract_unique_points(Point(0, 0))
    <MULTIPOINT (0 0)>
    >>> extract_unique_points(LineString([(0, 0), (1, 1), (1, 1)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 0, 1 1, 0 1)>
    >>> extract_unique_points(MultiPoint([(0, 0), (1, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(LineString())
    <MULTIPOINT EMPTY>
    """
    ...
@overload
def build_area(geometry: Geometry, **kwargs) -> BaseGeometry:
    """
    Creates an areal geometry formed by the constituent linework of given geometry.

    Equivalent of the PostGIS ST_BuildArea() function.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, Polygon
    >>> polygon1 = Polygon([(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])
    >>> polygon2 = Polygon([(1, 1), (1, 2), (2, 2), (1, 1)])
    >>> build_area(GeometryCollection([polygon1, polygon2]))
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0), (1 1, 2 2, 1 2, 1 1))>
    """
    ...
@overload
def build_area(geometry: None, **kwargs) -> None:
    """
    Creates an areal geometry formed by the constituent linework of given geometry.

    Equivalent of the PostGIS ST_BuildArea() function.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, Polygon
    >>> polygon1 = Polygon([(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])
    >>> polygon2 = Polygon([(1, 1), (1, 2), (2, 2), (1, 1)])
    >>> build_area(GeometryCollection([polygon1, polygon2]))
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0), (1 1, 2 2, 1 2, 1 1))>
    """
    ...
@overload
def build_area(geometry: Geometry | None, **kwargs) -> BaseGeometry | None:
    """
    Creates an areal geometry formed by the constituent linework of given geometry.

    Equivalent of the PostGIS ST_BuildArea() function.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, Polygon
    >>> polygon1 = Polygon([(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])
    >>> polygon2 = Polygon([(1, 1), (1, 2), (2, 2), (1, 1)])
    >>> build_area(GeometryCollection([polygon1, polygon2]))
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0), (1 1, 2 2, 1 2, 1 1))>
    """
    ...
@overload
def build_area(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Creates an areal geometry formed by the constituent linework of given geometry.

    Equivalent of the PostGIS ST_BuildArea() function.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, Polygon
    >>> polygon1 = Polygon([(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])
    >>> polygon2 = Polygon([(1, 1), (1, 2), (2, 2), (1, 1)])
    >>> build_area(GeometryCollection([polygon1, polygon2]))
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0), (1 1, 2 2, 1 2, 1 1))>
    """
    ...
@overload
def make_valid(geometry: Geometry, **kwargs) -> BaseGeometry:
    """
    Repairs invalid geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import is_valid, Polygon
    >>> polygon = Polygon([(0, 0), (1, 1), (1, 2), (1, 1), (0, 0)])
    >>> is_valid(polygon)
    False
    >>> make_valid(polygon)
    <MULTILINESTRING ((0 0, 1 1), (1 1, 1 2))>
    """
    ...
@overload
def make_valid(geometry: None, **kwargs) -> None:
    """
    Repairs invalid geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import is_valid, Polygon
    >>> polygon = Polygon([(0, 0), (1, 1), (1, 2), (1, 1), (0, 0)])
    >>> is_valid(polygon)
    False
    >>> make_valid(polygon)
    <MULTILINESTRING ((0 0, 1 1), (1 1, 1 2))>
    """
    ...
@overload
def make_valid(geometry: Geometry | None, **kwargs) -> BaseGeometry | None:
    """
    Repairs invalid geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import is_valid, Polygon
    >>> polygon = Polygon([(0, 0), (1, 1), (1, 2), (1, 1), (0, 0)])
    >>> is_valid(polygon)
    False
    >>> make_valid(polygon)
    <MULTILINESTRING ((0 0, 1 1), (1 1, 1 2))>
    """
    ...
@overload
def make_valid(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Repairs invalid geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import is_valid, Polygon
    >>> polygon = Polygon([(0, 0), (1, 1), (1, 2), (1, 1), (0, 0)])
    >>> is_valid(polygon)
    False
    >>> make_valid(polygon)
    <MULTILINESTRING ((0 0, 1 1), (1 1, 1 2))>
    """
    ...
@overload
def normalize(geometry: OptGeoT, **kwargs) -> OptGeoT:
    """
    Converts Geometry to strict normal form (or canonical form).

    In :ref:`strict canonical form <canonical-form>`, the coordinates, rings of a polygon and
    parts of multi geometries are ordered consistently. Typically useful for testing
    purposes (for example in combination with ``equals_exact``).

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiLineString
    >>> line = MultiLineString([[(0, 0), (1, 1)], [(2, 2), (3, 3)]])
    >>> normalize(line)
    <MULTILINESTRING ((2 2, 3 3), (0 0, 1 1))>
    """
    ...
@overload
def normalize(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Converts Geometry to strict normal form (or canonical form).

    In :ref:`strict canonical form <canonical-form>`, the coordinates, rings of a polygon and
    parts of multi geometries are ordered consistently. Typically useful for testing
    purposes (for example in combination with ``equals_exact``).

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import MultiLineString
    >>> line = MultiLineString([[(0, 0), (1, 1)], [(2, 2), (3, 3)]])
    >>> normalize(line)
    <MULTILINESTRING ((2 2, 3 3), (0 0, 1 1))>
    """
    ...
@overload
def point_on_surface(geometry: Geometry, **kwargs) -> Point:
    """
    Returns a point that intersects an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> point_on_surface(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> point_on_surface(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (2 2)>
    >>> point_on_surface(MultiPoint([(0, 0), (10, 10)]))
    <POINT (0 0)>
    >>> point_on_surface(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def point_on_surface(geometry: None, **kwargs) -> None:
    """
    Returns a point that intersects an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> point_on_surface(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> point_on_surface(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (2 2)>
    >>> point_on_surface(MultiPoint([(0, 0), (10, 10)]))
    <POINT (0 0)>
    >>> point_on_surface(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def point_on_surface(geometry: Geometry | None, **kwargs) -> Point | None:
    """
    Returns a point that intersects an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> point_on_surface(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> point_on_surface(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (2 2)>
    >>> point_on_surface(MultiPoint([(0, 0), (10, 10)]))
    <POINT (0 0)>
    >>> point_on_surface(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def point_on_surface(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Returns a point that intersects an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> point_on_surface(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> point_on_surface(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (2 2)>
    >>> point_on_surface(MultiPoint([(0, 0), (10, 10)]))
    <POINT (0 0)>
    >>> point_on_surface(Polygon())
    <POINT EMPTY>
    """
    ...
@overload
def node(geometry: Geometry, **kwargs) -> MultiLineString:
    """
    Returns the fully noded version of the linear input as MultiLineString.

    Given a linear input geometry, this function returns a new MultiLineString
    in which no lines cross each other but only touch at and points. To
    obtain this, all intersections between segments are computed and added
    to the segments, and duplicate segments are removed.

    Non-linear input (points) will result in an empty MultiLineString.

    This function can for example be used to create a fully-noded linework
    suitable to passed as input to ``polygonize``.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 0), (1,1), (0, 1), (1, 0)])
    >>> node(line)
    <MULTILINESTRING ((0 0, 0.5 0.5), (0.5 0.5, 1 1, 0 1, 0.5 0.5), (0.5 0.5, 1 0))>
    >>> node(Point(1, 1))
    <MULTILINESTRING EMPTY>
    """
    ...
@overload
def node(geometry: None, **kwargs) -> None:
    """
    Returns the fully noded version of the linear input as MultiLineString.

    Given a linear input geometry, this function returns a new MultiLineString
    in which no lines cross each other but only touch at and points. To
    obtain this, all intersections between segments are computed and added
    to the segments, and duplicate segments are removed.

    Non-linear input (points) will result in an empty MultiLineString.

    This function can for example be used to create a fully-noded linework
    suitable to passed as input to ``polygonize``.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 0), (1,1), (0, 1), (1, 0)])
    >>> node(line)
    <MULTILINESTRING ((0 0, 0.5 0.5), (0.5 0.5, 1 1, 0 1, 0.5 0.5), (0.5 0.5, 1 0))>
    >>> node(Point(1, 1))
    <MULTILINESTRING EMPTY>
    """
    ...
@overload
def node(geometry: Geometry | None, **kwargs) -> MultiLineString | None:
    """
    Returns the fully noded version of the linear input as MultiLineString.

    Given a linear input geometry, this function returns a new MultiLineString
    in which no lines cross each other but only touch at and points. To
    obtain this, all intersections between segments are computed and added
    to the segments, and duplicate segments are removed.

    Non-linear input (points) will result in an empty MultiLineString.

    This function can for example be used to create a fully-noded linework
    suitable to passed as input to ``polygonize``.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 0), (1,1), (0, 1), (1, 0)])
    >>> node(line)
    <MULTILINESTRING ((0 0, 0.5 0.5), (0.5 0.5, 1 1, 0 1, 0.5 0.5), (0.5 0.5, 1 0))>
    >>> node(Point(1, 1))
    <MULTILINESTRING EMPTY>
    """
    ...
@overload
def node(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Returns the fully noded version of the linear input as MultiLineString.

    Given a linear input geometry, this function returns a new MultiLineString
    in which no lines cross each other but only touch at and points. To
    obtain this, all intersections between segments are computed and added
    to the segments, and duplicate segments are removed.

    Non-linear input (points) will result in an empty MultiLineString.

    This function can for example be used to create a fully-noded linework
    suitable to passed as input to ``polygonize``.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Point
    >>> line = LineString([(0, 0), (1,1), (0, 1), (1, 0)])
    >>> node(line)
    <MULTILINESTRING ((0 0, 0.5 0.5), (0.5 0.5, 1 1, 0 1, 0.5 0.5), (0.5 0.5, 1 0))>
    >>> node(Point(1, 1))
    <MULTILINESTRING EMPTY>
    """
    ...
@overload
def polygonize(geometries: Sequence[Geometry | None], **kwargs) -> GeometryCollection:
    """
    Creates polygons formed from the linework of a set of Geometries.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    Lines or rings that when combined do not completely close a polygon
    will result in an empty GeometryCollection.  Duplicate segments are
    ignored.

    This function returns the polygons within a GeometryCollection.
    Individual Polygons can be obtained using ``get_geometry`` to get
    a single polygon or ``get_parts`` to get an array of polygons.
    MultiPolygons can be constructed from the output using
    ``shapely.multipolygons(shapely.get_parts(shapely.polygonize(geometries)))``.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    GeometryCollection or array of GeometryCollections

    See Also
    --------
    get_parts, get_geometry
    polygonize_full
    node

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize(lines)
    <GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>
    """
    ...
@overload
def polygonize(geometries: Sequence[Sequence[Geometry | None]], **kwargs) -> GeoArray:
    """
    Creates polygons formed from the linework of a set of Geometries.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    Lines or rings that when combined do not completely close a polygon
    will result in an empty GeometryCollection.  Duplicate segments are
    ignored.

    This function returns the polygons within a GeometryCollection.
    Individual Polygons can be obtained using ``get_geometry`` to get
    a single polygon or ``get_parts`` to get an array of polygons.
    MultiPolygons can be constructed from the output using
    ``shapely.multipolygons(shapely.get_parts(shapely.polygonize(geometries)))``.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    GeometryCollection or array of GeometryCollections

    See Also
    --------
    get_parts, get_geometry
    polygonize_full
    node

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize(lines)
    <GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>
    """
    ...
@overload
def polygonize(geometries: OptGeoArrayLikeSeq, **kwargs) -> GeometryCollection | GeoArray:
    """
    Creates polygons formed from the linework of a set of Geometries.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    Lines or rings that when combined do not completely close a polygon
    will result in an empty GeometryCollection.  Duplicate segments are
    ignored.

    This function returns the polygons within a GeometryCollection.
    Individual Polygons can be obtained using ``get_geometry`` to get
    a single polygon or ``get_parts`` to get an array of polygons.
    MultiPolygons can be constructed from the output using
    ``shapely.multipolygons(shapely.get_parts(shapely.polygonize(geometries)))``.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    GeometryCollection or array of GeometryCollections

    See Also
    --------
    get_parts, get_geometry
    polygonize_full
    node

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize(lines)
    <GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>
    """
    ...
@overload
def polygonize_full(
    geometries: Sequence[Geometry | None], **kwargs
) -> tuple[GeometryCollection, GeometryCollection, GeometryCollection, GeometryCollection]:
    """
    Creates polygons formed from the linework of a set of Geometries and
    return all extra outputs as well.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    This function performs the same polygonization as ``polygonize`` but does
    not only return the polygonal result but all extra outputs as well. The
    return value consists of 4 elements:

    * The polygonal valid output
    * **Cut edges**: edges connected on both ends but not part of polygonal output
    * **dangles**: edges connected on one end but not part of polygonal output
    * **invalid rings**: polygons formed but which are not valid

    This function returns the geometries within GeometryCollections.
    Individual geometries can be obtained using ``get_geometry`` to get
    a single geometry or ``get_parts`` to get an array of geometries.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    (polygons, cuts, dangles, invalid)
        tuple of 4 GeometryCollections or arrays of GeometryCollections

    See Also
    --------
    polygonize

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1), (1, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize_full(lines)  # doctest: +NORMALIZE_WHITESPACE
    (<GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>,
     <GEOMETRYCOLLECTION EMPTY>,
     <GEOMETRYCOLLECTION (LINESTRING (0 1, 1 1))>,
     <GEOMETRYCOLLECTION EMPTY>)
    """
    ...
@overload
def polygonize_full(
    geometries: Sequence[Sequence[Geometry | None]], **kwargs
) -> tuple[GeoArray, GeoArray, GeoArray, GeoArray]:
    """
    Creates polygons formed from the linework of a set of Geometries and
    return all extra outputs as well.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    This function performs the same polygonization as ``polygonize`` but does
    not only return the polygonal result but all extra outputs as well. The
    return value consists of 4 elements:

    * The polygonal valid output
    * **Cut edges**: edges connected on both ends but not part of polygonal output
    * **dangles**: edges connected on one end but not part of polygonal output
    * **invalid rings**: polygons formed but which are not valid

    This function returns the geometries within GeometryCollections.
    Individual geometries can be obtained using ``get_geometry`` to get
    a single geometry or ``get_parts`` to get an array of geometries.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    (polygons, cuts, dangles, invalid)
        tuple of 4 GeometryCollections or arrays of GeometryCollections

    See Also
    --------
    polygonize

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1), (1, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize_full(lines)  # doctest: +NORMALIZE_WHITESPACE
    (<GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>,
     <GEOMETRYCOLLECTION EMPTY>,
     <GEOMETRYCOLLECTION (LINESTRING (0 1, 1 1))>,
     <GEOMETRYCOLLECTION EMPTY>)
    """
    ...
@overload
def polygonize_full(
    geometries: OptGeoArrayLikeSeq, **kwargs
) -> (
    tuple[GeometryCollection, GeometryCollection, GeometryCollection, GeometryCollection]
    | tuple[GeoArray, GeoArray, GeoArray, GeoArray]
):
    """
    Creates polygons formed from the linework of a set of Geometries and
    return all extra outputs as well.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    This function performs the same polygonization as ``polygonize`` but does
    not only return the polygonal result but all extra outputs as well. The
    return value consists of 4 elements:

    * The polygonal valid output
    * **Cut edges**: edges connected on both ends but not part of polygonal output
    * **dangles**: edges connected on one end but not part of polygonal output
    * **invalid rings**: polygons formed but which are not valid

    This function returns the geometries within GeometryCollections.
    Individual geometries can be obtained using ``get_geometry`` to get
    a single geometry or ``get_parts`` to get an array of geometries.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Returns
    -------
    (polygons, cuts, dangles, invalid)
        tuple of 4 GeometryCollections or arrays of GeometryCollections

    See Also
    --------
    polygonize

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1), (1, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize_full(lines)  # doctest: +NORMALIZE_WHITESPACE
    (<GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>,
     <GEOMETRYCOLLECTION EMPTY>,
     <GEOMETRYCOLLECTION (LINESTRING (0 1, 1 1))>,
     <GEOMETRYCOLLECTION EMPTY>)
    """
    ...
@overload
def remove_repeated_points(geometry: OptGeoT, tolerance: float = 0.0, **kwargs) -> OptGeoT:
    """
    Returns a copy of a Geometry with repeated points removed.

    From the start of the coordinate sequence, each next point within the
    tolerance is removed.

    Removing repeated points with a non-zero tolerance may result in an invalid
    geometry being returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default=0.0
        Use 0.0 to remove only exactly repeated points.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> remove_repeated_points(LineString([(0,0), (0,0), (1,0)]), tolerance=0)
    <LINESTRING (0 0, 1 0)>
    >>> remove_repeated_points(Polygon([(0, 0), (0, .5), (0, 1), (.5, 1), (0,0)]), tolerance=.5)
    <POLYGON ((0 0, 0 1, 0 0, 0 0))>
    """
    ...
@overload
def remove_repeated_points(geometry: OptGeoArrayLikeSeq, tolerance: float = 0.0, **kwargs) -> GeoArray:
    """
    Returns a copy of a Geometry with repeated points removed.

    From the start of the coordinate sequence, each next point within the
    tolerance is removed.

    Removing repeated points with a non-zero tolerance may result in an invalid
    geometry being returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default=0.0
        Use 0.0 to remove only exactly repeated points.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> remove_repeated_points(LineString([(0,0), (0,0), (1,0)]), tolerance=0)
    <LINESTRING (0 0, 1 0)>
    >>> remove_repeated_points(Polygon([(0, 0), (0, .5), (0, 1), (.5, 1), (0,0)]), tolerance=.5)
    <POLYGON ((0 0, 0 1, 0 0, 0 0))>
    """
    ...
@overload
def reverse(geometry: OptGeoT, **kwargs) -> OptGeoT:
    """
    Returns a copy of a Geometry with the order of coordinates reversed.

    If a Geometry is a polygon with interior rings, the interior rings are also
    reversed.

    Points are unchanged. None is returned where Geometry is None.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    is_ccw : Checks if a Geometry is clockwise.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> reverse(LineString([(0, 0), (1, 2)]))
    <LINESTRING (1 2, 0 0)>
    >>> reverse(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    >>> reverse(None) is None
    True
    """
    ...
@overload
def reverse(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Returns a copy of a Geometry with the order of coordinates reversed.

    If a Geometry is a polygon with interior rings, the interior rings are also
    reversed.

    Points are unchanged. None is returned where Geometry is None.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See also
    --------
    is_ccw : Checks if a Geometry is clockwise.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> reverse(LineString([(0, 0), (1, 2)]))
    <LINESTRING (1 2, 0 0)>
    >>> reverse(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    >>> reverse(None) is None
    True
    """
    ...
@overload
def segmentize(geometry: OptGeoT, max_segment_length: float, **kwargs) -> OptGeoT:
    """
    Adds vertices to line segments based on maximum segment length.

    Additional vertices will be added to every line segment in an input geometry
    so that segments are no longer than the provided maximum segment length. New
    vertices will evenly subdivide each segment.

    Only linear components of input geometries are densified; other geometries
    are returned unmodified.

    Parameters
    ----------
    geometry : Geometry or array_like
    max_segment_length : float or array_like
        Additional vertices will be added so that all line segments are no
        longer than this value.  Must be greater than 0.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (0, 10)])
    >>> segmentize(line, max_segment_length=5)
    <LINESTRING (0 0, 0 5, 0 10)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> segmentize(polygon, max_segment_length=5)
    <POLYGON ((0 0, 5 0, 10 0, 10 5, 10 10, 5 10, 0 10, 0 5, 0 0))>
    >>> segmentize(None, max_segment_length=5) is None
    True
    """
    ...
@overload
def segmentize(geometry: OptGeoArrayLike, max_segment_length: ArrayLikeSeq[float], **kwargs) -> GeoArray:
    """
    Adds vertices to line segments based on maximum segment length.

    Additional vertices will be added to every line segment in an input geometry
    so that segments are no longer than the provided maximum segment length. New
    vertices will evenly subdivide each segment.

    Only linear components of input geometries are densified; other geometries
    are returned unmodified.

    Parameters
    ----------
    geometry : Geometry or array_like
    max_segment_length : float or array_like
        Additional vertices will be added so that all line segments are no
        longer than this value.  Must be greater than 0.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (0, 10)])
    >>> segmentize(line, max_segment_length=5)
    <LINESTRING (0 0, 0 5, 0 10)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> segmentize(polygon, max_segment_length=5)
    <POLYGON ((0 0, 5 0, 10 0, 10 5, 10 10, 5 10, 0 10, 0 5, 0 0))>
    >>> segmentize(None, max_segment_length=5) is None
    True
    """
    ...
@overload
def segmentize(geometry: OptGeoArrayLikeSeq, max_segment_length: ArrayLike[float], **kwargs) -> GeoArray:
    """
    Adds vertices to line segments based on maximum segment length.

    Additional vertices will be added to every line segment in an input geometry
    so that segments are no longer than the provided maximum segment length. New
    vertices will evenly subdivide each segment.

    Only linear components of input geometries are densified; other geometries
    are returned unmodified.

    Parameters
    ----------
    geometry : Geometry or array_like
    max_segment_length : float or array_like
        Additional vertices will be added so that all line segments are no
        longer than this value.  Must be greater than 0.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (0, 10)])
    >>> segmentize(line, max_segment_length=5)
    <LINESTRING (0 0, 0 5, 0 10)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> segmentize(polygon, max_segment_length=5)
    <POLYGON ((0 0, 5 0, 10 0, 10 5, 10 10, 5 10, 0 10, 0 5, 0 0))>
    >>> segmentize(None, max_segment_length=5) is None
    True
    """
    ...
@overload
def simplify(geometry: OptGeoT, tolerance: float, preserve_topology: bool = True, **kwargs) -> OptGeoT:
    """
    Returns a simplified version of an input geometry using the
    Douglas-Peucker algorithm.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like
        The maximum allowed geometry displacement. The higher this value, the
        smaller the number of vertices in the resulting geometry.
    preserve_topology : bool, default True
        By default (True), the operation will avoid creating invalid
        geometries (checking for collapses, ring-intersections, etc), but
        this is computationally more expensive.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (1, 10), (0, 20)])
    >>> simplify(line, tolerance=0.9)
    <LINESTRING (0 0, 1 10, 0 20)>
    >>> simplify(line, tolerance=1)
    <LINESTRING (0 0, 0 20)>
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=True)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 2, 2 4, 4 4, 4 2...>
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=False)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    ...
@overload
def simplify(geometry: OptGeoArrayLike, tolerance: ArrayLikeSeq[float], preserve_topology: bool = True, **kwargs) -> GeoArray:
    """
    Returns a simplified version of an input geometry using the
    Douglas-Peucker algorithm.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like
        The maximum allowed geometry displacement. The higher this value, the
        smaller the number of vertices in the resulting geometry.
    preserve_topology : bool, default True
        By default (True), the operation will avoid creating invalid
        geometries (checking for collapses, ring-intersections, etc), but
        this is computationally more expensive.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (1, 10), (0, 20)])
    >>> simplify(line, tolerance=0.9)
    <LINESTRING (0 0, 1 10, 0 20)>
    >>> simplify(line, tolerance=1)
    <LINESTRING (0 0, 0 20)>
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=True)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 2, 2 4, 4 4, 4 2...>
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=False)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    ...
@overload
def simplify(geometry: OptGeoArrayLikeSeq, tolerance: ArrayLike[float], preserve_topology: bool = True, **kwargs) -> GeoArray:
    """
    Returns a simplified version of an input geometry using the
    Douglas-Peucker algorithm.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like
        The maximum allowed geometry displacement. The higher this value, the
        smaller the number of vertices in the resulting geometry.
    preserve_topology : bool, default True
        By default (True), the operation will avoid creating invalid
        geometries (checking for collapses, ring-intersections, etc), but
        this is computationally more expensive.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (1, 10), (0, 20)])
    >>> simplify(line, tolerance=0.9)
    <LINESTRING (0 0, 1 10, 0 20)>
    >>> simplify(line, tolerance=1)
    <LINESTRING (0 0, 0 20)>
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=True)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 2, 2 4, 4 4, 4 2...>
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=False)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    ...
@overload
def snap(geometry: OptGeoT, reference: Geometry, tolerance: float, **kwargs) -> OptGeoT:
    """
    Snaps an input geometry to reference geometry's vertices.

    Vertices of the first geometry are snapped to vertices of the second.
    geometry, returning a new geometry; the input geometries are not modified.
    The result geometry is the input geometry with the vertices snapped.
    If no snapping occurs then the input geometry is returned unchanged.
    The tolerance is used to control where snapping is performed.

    Where possible, this operation tries to avoid creating invalid geometries;
    however, it does not guarantee that output geometries will be valid.  It is
    the responsibility of the caller to check for and handle invalid geometries.

    Because too much snapping can result in invalid geometries being created,
    heuristics are used to determine the number and location of snapped
    vertices that are likely safe to snap. These heuristics may omit
    some potential snaps that are otherwise within the tolerance.

    Parameters
    ----------
    geometry : Geometry or array_like
    reference : Geometry or array_like
    tolerance : float or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import snap, distance, LineString, Point, Polygon, MultiPoint, box

    >>> point = Point(0.5, 2.5)
    >>> target_point = Point(0, 2)
    >>> snap(point, target_point, tolerance=1)
    <POINT (0 2)>
    >>> snap(point, target_point, tolerance=0.49)
    <POINT (0.5 2.5)>

    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> snap(polygon, Point(8, 10), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 10 0, 0 0))>
    >>> snap(polygon, LineString([(8, 10), (8, 0)]), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 8 0, 0 0))>

    You can snap one line to another, for example to clean imprecise coordinates:

    >>> line1 = LineString([(0.1, 0.1), (0.49, 0.51), (1.01, 0.89)])
    >>> line2 = LineString([(0, 0), (0.5, 0.5), (1.0, 1.0)])
    >>> snap(line1, line2, 0.25)
    <LINESTRING (0 0, 0.5 0.5, 1 1)>

    Snapping also supports Z coordinates:

    >>> point1 = Point(0.1, 0.1, 0.5)
    >>> multipoint = MultiPoint([(0, 0, 1), (0, 0, 0)])
    >>> snap(point1, multipoint, 1)
    <POINT Z (0 0 1)>

    Snapping to an empty geometry has no effect:

    >>> snap(line1, LineString([]), 0.25)
    <LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)>

    Snapping to a non-geometry (None) will always return None:

    >>> snap(line1, None, 0.25) is None
    True

    Only one vertex of a polygon is snapped to a target point,
    even if all vertices are equidistant to it,
    in order to prevent collapse of the polygon:

    >>> poly = box(0, 0, 1, 1)
    >>> poly
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> snap(poly, Point(0.5, 0.5), 1)
    <POLYGON ((0.5 0.5, 1 1, 0 1, 0 0, 0.5 0.5))>
    """
    ...
@overload
def snap(geometry: Geometry | None, reference: None, tolerance: float, **kwargs) -> None:
    """
    Snaps an input geometry to reference geometry's vertices.

    Vertices of the first geometry are snapped to vertices of the second.
    geometry, returning a new geometry; the input geometries are not modified.
    The result geometry is the input geometry with the vertices snapped.
    If no snapping occurs then the input geometry is returned unchanged.
    The tolerance is used to control where snapping is performed.

    Where possible, this operation tries to avoid creating invalid geometries;
    however, it does not guarantee that output geometries will be valid.  It is
    the responsibility of the caller to check for and handle invalid geometries.

    Because too much snapping can result in invalid geometries being created,
    heuristics are used to determine the number and location of snapped
    vertices that are likely safe to snap. These heuristics may omit
    some potential snaps that are otherwise within the tolerance.

    Parameters
    ----------
    geometry : Geometry or array_like
    reference : Geometry or array_like
    tolerance : float or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import snap, distance, LineString, Point, Polygon, MultiPoint, box

    >>> point = Point(0.5, 2.5)
    >>> target_point = Point(0, 2)
    >>> snap(point, target_point, tolerance=1)
    <POINT (0 2)>
    >>> snap(point, target_point, tolerance=0.49)
    <POINT (0.5 2.5)>

    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> snap(polygon, Point(8, 10), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 10 0, 0 0))>
    >>> snap(polygon, LineString([(8, 10), (8, 0)]), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 8 0, 0 0))>

    You can snap one line to another, for example to clean imprecise coordinates:

    >>> line1 = LineString([(0.1, 0.1), (0.49, 0.51), (1.01, 0.89)])
    >>> line2 = LineString([(0, 0), (0.5, 0.5), (1.0, 1.0)])
    >>> snap(line1, line2, 0.25)
    <LINESTRING (0 0, 0.5 0.5, 1 1)>

    Snapping also supports Z coordinates:

    >>> point1 = Point(0.1, 0.1, 0.5)
    >>> multipoint = MultiPoint([(0, 0, 1), (0, 0, 0)])
    >>> snap(point1, multipoint, 1)
    <POINT Z (0 0 1)>

    Snapping to an empty geometry has no effect:

    >>> snap(line1, LineString([]), 0.25)
    <LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)>

    Snapping to a non-geometry (None) will always return None:

    >>> snap(line1, None, 0.25) is None
    True

    Only one vertex of a polygon is snapped to a target point,
    even if all vertices are equidistant to it,
    in order to prevent collapse of the polygon:

    >>> poly = box(0, 0, 1, 1)
    >>> poly
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> snap(poly, Point(0.5, 0.5), 1)
    <POLYGON ((0.5 0.5, 1 1, 0 1, 0 0, 0.5 0.5))>
    """
    ...
@overload
def snap(geometry: OptGeoArrayLikeSeq, reference: OptGeoArrayLike, tolerance: ArrayLike[float], **kwargs) -> GeoArray:
    """
    Snaps an input geometry to reference geometry's vertices.

    Vertices of the first geometry are snapped to vertices of the second.
    geometry, returning a new geometry; the input geometries are not modified.
    The result geometry is the input geometry with the vertices snapped.
    If no snapping occurs then the input geometry is returned unchanged.
    The tolerance is used to control where snapping is performed.

    Where possible, this operation tries to avoid creating invalid geometries;
    however, it does not guarantee that output geometries will be valid.  It is
    the responsibility of the caller to check for and handle invalid geometries.

    Because too much snapping can result in invalid geometries being created,
    heuristics are used to determine the number and location of snapped
    vertices that are likely safe to snap. These heuristics may omit
    some potential snaps that are otherwise within the tolerance.

    Parameters
    ----------
    geometry : Geometry or array_like
    reference : Geometry or array_like
    tolerance : float or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import snap, distance, LineString, Point, Polygon, MultiPoint, box

    >>> point = Point(0.5, 2.5)
    >>> target_point = Point(0, 2)
    >>> snap(point, target_point, tolerance=1)
    <POINT (0 2)>
    >>> snap(point, target_point, tolerance=0.49)
    <POINT (0.5 2.5)>

    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> snap(polygon, Point(8, 10), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 10 0, 0 0))>
    >>> snap(polygon, LineString([(8, 10), (8, 0)]), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 8 0, 0 0))>

    You can snap one line to another, for example to clean imprecise coordinates:

    >>> line1 = LineString([(0.1, 0.1), (0.49, 0.51), (1.01, 0.89)])
    >>> line2 = LineString([(0, 0), (0.5, 0.5), (1.0, 1.0)])
    >>> snap(line1, line2, 0.25)
    <LINESTRING (0 0, 0.5 0.5, 1 1)>

    Snapping also supports Z coordinates:

    >>> point1 = Point(0.1, 0.1, 0.5)
    >>> multipoint = MultiPoint([(0, 0, 1), (0, 0, 0)])
    >>> snap(point1, multipoint, 1)
    <POINT Z (0 0 1)>

    Snapping to an empty geometry has no effect:

    >>> snap(line1, LineString([]), 0.25)
    <LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)>

    Snapping to a non-geometry (None) will always return None:

    >>> snap(line1, None, 0.25) is None
    True

    Only one vertex of a polygon is snapped to a target point,
    even if all vertices are equidistant to it,
    in order to prevent collapse of the polygon:

    >>> poly = box(0, 0, 1, 1)
    >>> poly
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> snap(poly, Point(0.5, 0.5), 1)
    <POLYGON ((0.5 0.5, 1 1, 0 1, 0 0, 0.5 0.5))>
    """
    ...
@overload
def snap(geometry: OptGeoArrayLike, reference: OptGeoArrayLikeSeq, tolerance: ArrayLike[float], **kwargs) -> GeoArray:
    """
    Snaps an input geometry to reference geometry's vertices.

    Vertices of the first geometry are snapped to vertices of the second.
    geometry, returning a new geometry; the input geometries are not modified.
    The result geometry is the input geometry with the vertices snapped.
    If no snapping occurs then the input geometry is returned unchanged.
    The tolerance is used to control where snapping is performed.

    Where possible, this operation tries to avoid creating invalid geometries;
    however, it does not guarantee that output geometries will be valid.  It is
    the responsibility of the caller to check for and handle invalid geometries.

    Because too much snapping can result in invalid geometries being created,
    heuristics are used to determine the number and location of snapped
    vertices that are likely safe to snap. These heuristics may omit
    some potential snaps that are otherwise within the tolerance.

    Parameters
    ----------
    geometry : Geometry or array_like
    reference : Geometry or array_like
    tolerance : float or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import snap, distance, LineString, Point, Polygon, MultiPoint, box

    >>> point = Point(0.5, 2.5)
    >>> target_point = Point(0, 2)
    >>> snap(point, target_point, tolerance=1)
    <POINT (0 2)>
    >>> snap(point, target_point, tolerance=0.49)
    <POINT (0.5 2.5)>

    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> snap(polygon, Point(8, 10), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 10 0, 0 0))>
    >>> snap(polygon, LineString([(8, 10), (8, 0)]), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 8 0, 0 0))>

    You can snap one line to another, for example to clean imprecise coordinates:

    >>> line1 = LineString([(0.1, 0.1), (0.49, 0.51), (1.01, 0.89)])
    >>> line2 = LineString([(0, 0), (0.5, 0.5), (1.0, 1.0)])
    >>> snap(line1, line2, 0.25)
    <LINESTRING (0 0, 0.5 0.5, 1 1)>

    Snapping also supports Z coordinates:

    >>> point1 = Point(0.1, 0.1, 0.5)
    >>> multipoint = MultiPoint([(0, 0, 1), (0, 0, 0)])
    >>> snap(point1, multipoint, 1)
    <POINT Z (0 0 1)>

    Snapping to an empty geometry has no effect:

    >>> snap(line1, LineString([]), 0.25)
    <LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)>

    Snapping to a non-geometry (None) will always return None:

    >>> snap(line1, None, 0.25) is None
    True

    Only one vertex of a polygon is snapped to a target point,
    even if all vertices are equidistant to it,
    in order to prevent collapse of the polygon:

    >>> poly = box(0, 0, 1, 1)
    >>> poly
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> snap(poly, Point(0.5, 0.5), 1)
    <POLYGON ((0.5 0.5, 1 1, 0 1, 0 0, 0.5 0.5))>
    """
    ...
@overload
def snap(geometry: OptGeoArrayLike, reference: OptGeoArrayLike, tolerance: ArrayLikeSeq[float], **kwargs) -> GeoArray:
    """
    Snaps an input geometry to reference geometry's vertices.

    Vertices of the first geometry are snapped to vertices of the second.
    geometry, returning a new geometry; the input geometries are not modified.
    The result geometry is the input geometry with the vertices snapped.
    If no snapping occurs then the input geometry is returned unchanged.
    The tolerance is used to control where snapping is performed.

    Where possible, this operation tries to avoid creating invalid geometries;
    however, it does not guarantee that output geometries will be valid.  It is
    the responsibility of the caller to check for and handle invalid geometries.

    Because too much snapping can result in invalid geometries being created,
    heuristics are used to determine the number and location of snapped
    vertices that are likely safe to snap. These heuristics may omit
    some potential snaps that are otherwise within the tolerance.

    Parameters
    ----------
    geometry : Geometry or array_like
    reference : Geometry or array_like
    tolerance : float or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import snap, distance, LineString, Point, Polygon, MultiPoint, box

    >>> point = Point(0.5, 2.5)
    >>> target_point = Point(0, 2)
    >>> snap(point, target_point, tolerance=1)
    <POINT (0 2)>
    >>> snap(point, target_point, tolerance=0.49)
    <POINT (0.5 2.5)>

    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> snap(polygon, Point(8, 10), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 10 0, 0 0))>
    >>> snap(polygon, LineString([(8, 10), (8, 0)]), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 8 0, 0 0))>

    You can snap one line to another, for example to clean imprecise coordinates:

    >>> line1 = LineString([(0.1, 0.1), (0.49, 0.51), (1.01, 0.89)])
    >>> line2 = LineString([(0, 0), (0.5, 0.5), (1.0, 1.0)])
    >>> snap(line1, line2, 0.25)
    <LINESTRING (0 0, 0.5 0.5, 1 1)>

    Snapping also supports Z coordinates:

    >>> point1 = Point(0.1, 0.1, 0.5)
    >>> multipoint = MultiPoint([(0, 0, 1), (0, 0, 0)])
    >>> snap(point1, multipoint, 1)
    <POINT Z (0 0 1)>

    Snapping to an empty geometry has no effect:

    >>> snap(line1, LineString([]), 0.25)
    <LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)>

    Snapping to a non-geometry (None) will always return None:

    >>> snap(line1, None, 0.25) is None
    True

    Only one vertex of a polygon is snapped to a target point,
    even if all vertices are equidistant to it,
    in order to prevent collapse of the polygon:

    >>> poly = box(0, 0, 1, 1)
    >>> poly
    <POLYGON ((1 0, 1 1, 0 1, 0 0, 1 0))>
    >>> snap(poly, Point(0.5, 0.5), 1)
    <POLYGON ((0.5 0.5, 1 1, 0 1, 0 0, 0.5 0.5))>
    """
    ...
@overload
def voronoi_polygons(
    geometry: Geometry, tolerance: float = 0.0, extend_to: Geometry | None = None, only_edges: Literal[False] = False, **kwargs
) -> GeometryCollection[Polygon]:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: Geometry, tolerance: float, extend_to: Geometry | None, only_edges: Literal[True], **kwargs
) -> LineString | MultiLineString:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: Geometry, tolerance: float = 0.0, extend_to: Geometry | None = None, *, only_edges: Literal[True], **kwargs
) -> LineString | MultiLineString:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: Geometry, tolerance: float = 0.0, extend_to: Geometry | None = None, only_edges: bool = False, **kwargs
) -> GeometryCollection[Polygon] | LineString | MultiLineString:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: None, tolerance: float = 0.0, extend_to: Geometry | None = None, only_edges: bool = False, **kwargs
) -> None:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: Geometry | None, tolerance: float = 0.0, extend_to: Geometry | None = None, only_edges: bool = False, **kwargs
) -> GeometryCollection[Polygon] | LineString | MultiLineString | None:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: OptGeoArrayLikeSeq,
    tolerance: ArrayLike[float] = 0.0,
    extend_to: OptGeoArrayLike = None,
    only_edges: ArrayLike[bool] = False,
    **kwargs,
) -> GeoArray:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: OptGeoArrayLike,
    tolerance: ArrayLikeSeq[float],
    extend_to: OptGeoArrayLike = None,
    only_edges: ArrayLike[bool] = False,
    **kwargs,
) -> GeoArray:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: OptGeoArrayLike,
    tolerance: ArrayLike[float],
    extend_to: OptGeoArrayLikeSeq,
    only_edges: ArrayLike[bool] = False,
    **kwargs,
) -> GeoArray:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: OptGeoArrayLike,
    tolerance: ArrayLike[float] = 0.0,
    *,
    extend_to: OptGeoArrayLikeSeq,
    only_edges: ArrayLike[bool] = False,
    **kwargs,
) -> GeoArray:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: OptGeoArrayLike, tolerance: ArrayLike[float], extend_to: OptGeoArrayLike, only_edges: ArrayLikeSeq[bool], **kwargs
) -> GeoArray:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def voronoi_polygons(
    geometry: OptGeoArrayLike,
    tolerance: ArrayLike[float] = 0.0,
    extend_to: OptGeoArrayLike = None,
    *,
    only_edges: ArrayLikeSeq[bool],
    **kwargs,
) -> GeoArray:
    """
    Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    ...
@overload
def oriented_envelope(geometry: Point, **kwargs) -> Point:
    """
    Computes the oriented envelope (minimum rotated rectangle)
    that encloses an input geometry, such that the resulting rectangle has
    minimum area.

    Unlike envelope this rectangle is not constrained to be parallel to the
    coordinate axes. If the convex hull of the object is a degenerate (line
    or point) this degenerate is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> oriented_envelope(MultiPoint([(0, 0), (10, 0), (10, 10)])).normalize()
    <POLYGON ((0 0, 10 10, 15 5, 5 -5, 0 0))>
    >>> oriented_envelope(LineString([(1, 1), (5, 1), (10, 10)])).normalize()
    <POLYGON ((1 1, 10 10, 12 8, 3 -1, 1 1))>
    >>> oriented_envelope(Polygon([(1, 1), (15, 1), (5, 10), (1, 1)])).normalize()
    <POLYGON ((1 1, 1 10, 15 10, 15 1, 1 1))>
    >>> oriented_envelope(LineString([(1, 1), (10, 1)])).normalize()
    <LINESTRING (1 1, 10 1)>
    >>> oriented_envelope(Point(2, 2))
    <POINT (2 2)>
    >>> oriented_envelope(GeometryCollection([]))
    <POLYGON EMPTY>
    """
    ...
@overload
def oriented_envelope(geometry: Geometry, **kwargs) -> BaseGeometry:
    """
    Computes the oriented envelope (minimum rotated rectangle)
    that encloses an input geometry, such that the resulting rectangle has
    minimum area.

    Unlike envelope this rectangle is not constrained to be parallel to the
    coordinate axes. If the convex hull of the object is a degenerate (line
    or point) this degenerate is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> oriented_envelope(MultiPoint([(0, 0), (10, 0), (10, 10)])).normalize()
    <POLYGON ((0 0, 10 10, 15 5, 5 -5, 0 0))>
    >>> oriented_envelope(LineString([(1, 1), (5, 1), (10, 10)])).normalize()
    <POLYGON ((1 1, 10 10, 12 8, 3 -1, 1 1))>
    >>> oriented_envelope(Polygon([(1, 1), (15, 1), (5, 10), (1, 1)])).normalize()
    <POLYGON ((1 1, 1 10, 15 10, 15 1, 1 1))>
    >>> oriented_envelope(LineString([(1, 1), (10, 1)])).normalize()
    <LINESTRING (1 1, 10 1)>
    >>> oriented_envelope(Point(2, 2))
    <POINT (2 2)>
    >>> oriented_envelope(GeometryCollection([]))
    <POLYGON EMPTY>
    """
    ...
@overload
def oriented_envelope(geometry: None, **kwargs) -> None:
    """
    Computes the oriented envelope (minimum rotated rectangle)
    that encloses an input geometry, such that the resulting rectangle has
    minimum area.

    Unlike envelope this rectangle is not constrained to be parallel to the
    coordinate axes. If the convex hull of the object is a degenerate (line
    or point) this degenerate is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> oriented_envelope(MultiPoint([(0, 0), (10, 0), (10, 10)])).normalize()
    <POLYGON ((0 0, 10 10, 15 5, 5 -5, 0 0))>
    >>> oriented_envelope(LineString([(1, 1), (5, 1), (10, 10)])).normalize()
    <POLYGON ((1 1, 10 10, 12 8, 3 -1, 1 1))>
    >>> oriented_envelope(Polygon([(1, 1), (15, 1), (5, 10), (1, 1)])).normalize()
    <POLYGON ((1 1, 1 10, 15 10, 15 1, 1 1))>
    >>> oriented_envelope(LineString([(1, 1), (10, 1)])).normalize()
    <LINESTRING (1 1, 10 1)>
    >>> oriented_envelope(Point(2, 2))
    <POINT (2 2)>
    >>> oriented_envelope(GeometryCollection([]))
    <POLYGON EMPTY>
    """
    ...
@overload
def oriented_envelope(geometry: Geometry | None, **kwargs) -> BaseGeometry | None:
    """
    Computes the oriented envelope (minimum rotated rectangle)
    that encloses an input geometry, such that the resulting rectangle has
    minimum area.

    Unlike envelope this rectangle is not constrained to be parallel to the
    coordinate axes. If the convex hull of the object is a degenerate (line
    or point) this degenerate is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> oriented_envelope(MultiPoint([(0, 0), (10, 0), (10, 10)])).normalize()
    <POLYGON ((0 0, 10 10, 15 5, 5 -5, 0 0))>
    >>> oriented_envelope(LineString([(1, 1), (5, 1), (10, 10)])).normalize()
    <POLYGON ((1 1, 10 10, 12 8, 3 -1, 1 1))>
    >>> oriented_envelope(Polygon([(1, 1), (15, 1), (5, 10), (1, 1)])).normalize()
    <POLYGON ((1 1, 1 10, 15 10, 15 1, 1 1))>
    >>> oriented_envelope(LineString([(1, 1), (10, 1)])).normalize()
    <LINESTRING (1 1, 10 1)>
    >>> oriented_envelope(Point(2, 2))
    <POINT (2 2)>
    >>> oriented_envelope(GeometryCollection([]))
    <POLYGON EMPTY>
    """
    ...
@overload
def oriented_envelope(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Computes the oriented envelope (minimum rotated rectangle)
    that encloses an input geometry, such that the resulting rectangle has
    minimum area.

    Unlike envelope this rectangle is not constrained to be parallel to the
    coordinate axes. If the convex hull of the object is a degenerate (line
    or point) this degenerate is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> oriented_envelope(MultiPoint([(0, 0), (10, 0), (10, 10)])).normalize()
    <POLYGON ((0 0, 10 10, 15 5, 5 -5, 0 0))>
    >>> oriented_envelope(LineString([(1, 1), (5, 1), (10, 10)])).normalize()
    <POLYGON ((1 1, 10 10, 12 8, 3 -1, 1 1))>
    >>> oriented_envelope(Polygon([(1, 1), (15, 1), (5, 10), (1, 1)])).normalize()
    <POLYGON ((1 1, 1 10, 15 10, 15 1, 1 1))>
    >>> oriented_envelope(LineString([(1, 1), (10, 1)])).normalize()
    <LINESTRING (1 1, 10 1)>
    >>> oriented_envelope(Point(2, 2))
    <POINT (2 2)>
    >>> oriented_envelope(GeometryCollection([]))
    <POLYGON EMPTY>
    """
    ...

minimum_rotated_rectangle = oriented_envelope

@overload
def minimum_bounding_circle(geometry: Point, **kwargs) -> Point:
    """
    Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    ...
@overload
def minimum_bounding_circle(geometry: LineString | Polygon | BaseMultipartGeometry, **kwargs) -> Polygon:
    """
    Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    ...
@overload
def minimum_bounding_circle(geometry: Geometry, **kwargs) -> Polygon | Point:
    """
    Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    ...
@overload
def minimum_bounding_circle(geometry: None, **kwargs) -> None:
    """
    Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    ...
@overload
def minimum_bounding_circle(geometry: Geometry | None, **kwargs) -> Polygon | Point | None:
    """
    Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    ...
@overload
def minimum_bounding_circle(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    ...
