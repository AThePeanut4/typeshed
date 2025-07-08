from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Callable, Collection, Hashable, Iterable, Mapping, Sequence
from typing import Any, Literal, Protocol, SupportsIndex, overload, type_check_only
from typing_extensions import Self, TypeAlias, deprecated

import numpy as np
import pandas as pd
from numpy.random import BitGenerator, Generator as RandomGenerator, SeedSequence
from numpy.typing import ArrayLike, NDArray
from pandas._typing import ListLikeU
from pandas.core.base import IndexOpsMixin
from pyproj import CRS
from shapely import Geometry, MultiPolygon, Point, Polygon
from shapely.geometry.base import BaseGeometry

from .array import GeometryArray, _Array1D
from .geodataframe import GeoDataFrame
from .geoseries import GeoSeries
from .sindex import SpatialIndex

@type_check_only
class _SupportsToWkt(Protocol):
    def to_wkt(self) -> str: ...

@type_check_only
class _SupportsGeoInterface(Protocol):  # noqa: Y046
    @property
    def __geo_interface__(self) -> dict[str, Any]: ...  # values are arbitrary

_ConvertibleToCRS: TypeAlias = str | int | tuple[str, str] | list[str] | dict[str, Incomplete] | _SupportsToWkt
_AffinityOrigin: TypeAlias = Literal["center", "centroid"] | Point | tuple[float, float] | tuple[float, float, float]
_ClipMask: TypeAlias = GeoDataFrame | GeoSeries | Polygon | MultiPolygon | tuple[float, float, float, float]  # noqa: Y047
# np.floating[Any] because precision is not important
_BboxLike: TypeAlias = Sequence[float] | NDArray[np.floating[Any]] | Geometry | GeoDataFrame | GeoSeries  # noqa: Y047
_MaskLike: TypeAlias = dict[str, Incomplete] | Geometry | GeoDataFrame | GeoSeries  # noqa: Y047

# Cannot use IndexOpsMixin[Geometry] because of IndexOpsMixin type variable bounds
_GeoListLike: TypeAlias = ArrayLike | Sequence[Geometry] | IndexOpsMixin[Any]
_ConvertibleToGeoSeries: TypeAlias = Geometry | Mapping[int, Geometry] | Mapping[str, Geometry] | _GeoListLike  # noqa: Y047

# Cannot use pd.Series[Geometry] because of pd.Series type variable bounds
_GeomSeq: TypeAlias = Sequence[Geometry] | NDArray[np.object_] | pd.Series[Any] | GeometryArray | GeoSeries
_GeomCol: TypeAlias = Hashable | _GeomSeq  # name of column or column values  # noqa: Y047
# dict[Any, Any] because of variance issues
_ConvertibleToDataFrame: TypeAlias = (  # noqa: Y047
    ListLikeU | pd.DataFrame | dict[Any, Any] | Iterable[ListLikeU | tuple[Hashable, ListLikeU] | dict[Any, Any]]
)

def is_geometry_type(data: object) -> bool:
    """
    Check if the data is of geometry dtype.

    Does not include object array of shapely scalars.
    """
    ...

class GeoPandasBase:
    @property
    def area(self) -> pd.Series[float]:
        """
        Returns a ``Series`` containing the area of each geometry in the
        ``GeoSeries`` expressed in the units of the CRS.

        Examples
        --------

        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         Polygon([(10, 0), (10, 5), (0, 0)]),
        ...         Polygon([(0, 0), (2, 2), (2, 0)]),
        ...         LineString([(0, 0), (1, 1), (0, 1)]),
        ...         Point(0, 1)
        ...     ]
        ... )
        >>> s
        0       POLYGON ((0 0, 1 1, 0 1, 0 0))
        1    POLYGON ((10 0, 10 5, 0 0, 10 0))
        2       POLYGON ((0 0, 2 2, 2 0, 0 0))
        3           LINESTRING (0 0, 1 1, 0 1)
        4                          POINT (0 1)
        dtype: geometry

        >>> s.area
        0     0.5
        1    25.0
        2     2.0
        3     0.0
        4     0.0
        dtype: float64

        See also
        --------
        GeoSeries.length : measure length

        Notes
        -----
        Area may be invalid for a geographic CRS using degrees as units;
        use :meth:`GeoSeries.to_crs` to project geometries to a planar
        CRS before using this function.

        Every operation in GeoPandas is planar, i.e. the potential third
        dimension is not taken into account.
        """
        ...
    @property
    def crs(self) -> CRS | None:
        """
        The Coordinate Reference System (CRS) represented as a ``pyproj.CRS``
        object.

        Returns None if the CRS is not set, and to set the value it
        :getter: Returns a ``pyproj.CRS`` or None. When setting, the value
        can be anything accepted by
        :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
        such as an authority string (eg "EPSG:4326") or a WKT string.

        Examples
        --------

        >>> s.crs  # doctest: +SKIP
        <Geographic 2D CRS: EPSG:4326>
        Name: WGS 84
        Axis Info [ellipsoidal]:
        - Lat[north]: Geodetic latitude (degree)
        - Lon[east]: Geodetic longitude (degree)
        Area of Use:
        - name: World
        - bounds: (-180.0, -90.0, 180.0, 90.0)
        Datum: World Geodetic System 1984
        - Ellipsoid: WGS 84
        - Prime Meridian: Greenwich

        See also
        --------
        GeoSeries.set_crs : assign CRS
        GeoSeries.to_crs : re-project to another CRS
        """
        ...
    @crs.setter
    def crs(self, value: _ConvertibleToCRS | None) -> None:
        """
        The Coordinate Reference System (CRS) represented as a ``pyproj.CRS``
        object.

        Returns None if the CRS is not set, and to set the value it
        :getter: Returns a ``pyproj.CRS`` or None. When setting, the value
        can be anything accepted by
        :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
        such as an authority string (eg "EPSG:4326") or a WKT string.

        Examples
        --------

        >>> s.crs  # doctest: +SKIP
        <Geographic 2D CRS: EPSG:4326>
        Name: WGS 84
        Axis Info [ellipsoidal]:
        - Lat[north]: Geodetic latitude (degree)
        - Lon[east]: Geodetic longitude (degree)
        Area of Use:
        - name: World
        - bounds: (-180.0, -90.0, 180.0, 90.0)
        Datum: World Geodetic System 1984
        - Ellipsoid: WGS 84
        - Prime Meridian: Greenwich

        See also
        --------
        GeoSeries.set_crs : assign CRS
        GeoSeries.to_crs : re-project to another CRS
        """
        ...
    @property
    def geom_type(self) -> pd.Series[str]:
        """
        Returns a ``Series`` of strings specifying the `Geometry Type` of each
        object.

        Examples
        --------
        >>> from shapely.geometry import Point, Polygon, LineString
        >>> d = {'geometry': [Point(2, 1), Polygon([(0, 0), (1, 1), (1, 0)]),
        ... LineString([(0, 0), (1, 1)])]}
        >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326")
        >>> gdf.geom_type
        0         Point
        1       Polygon
        2    LineString
        dtype: object
        """
        ...
    @property
    def type(self) -> pd.Series[str]:
        """Return the geometry type of each geometry in the GeoSeries"""
        ...
    @property
    def length(self) -> pd.Series[float]:
        """
        Returns a ``Series`` containing the length of each geometry
        expressed in the units of the CRS.

        In the case of a (Multi)Polygon it measures the length
        of its exterior (i.e. perimeter).

        Examples
        --------

        >>> from shapely.geometry import Polygon, LineString, MultiLineString, Point, GeometryCollection
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(10, 0), (10, 5), (0, 0)]),
        ...         MultiLineString([((0, 0), (1, 0)), ((-1, 0), (1, 0))]),
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         Point(0, 1),
        ...         GeometryCollection([Point(1, 0), LineString([(10, 0), (10, 5), (0, 0)])])
        ...     ]
        ... )
        >>> s
        0                           LINESTRING (0 0, 1 1, 0 1)
        1                         LINESTRING (10 0, 10 5, 0 0)
        2            MULTILINESTRING ((0 0, 1 0), (-1 0, 1 0))
        3                       POLYGON ((0 0, 1 1, 0 1, 0 0))
        4                                          POINT (0 1)
        5    GEOMETRYCOLLECTION (POINT (1 0), LINESTRING (1...
        dtype: geometry

        >>> s.length
        0     2.414214
        1    16.180340
        2     3.000000
        3     3.414214
        4     0.000000
        5    16.180340
        dtype: float64

        See also
        --------
        GeoSeries.area : measure area of a polygon

        Notes
        -----
        Length may be invalid for a geographic CRS using degrees as units;
        use :meth:`GeoSeries.to_crs` to project geometries to a planar
        CRS before using this function.

        Every operation in GeoPandas is planar, i.e. the potential third
        dimension is not taken into account.
        """
        ...
    @property
    def is_valid(self) -> pd.Series[bool]: ...
    def is_valid_reason(self) -> pd.Series[str]: ...
    def is_valid_coverage(self, *, gap_width: float = 0.0) -> bool: ...
    def invalid_coverage_edges(self, *, gap_width: float = 0.0) -> GeoSeries: ...
    @property
    def is_empty(self) -> pd.Series[bool]:
        """
        Returns a ``Series`` of ``dtype('bool')`` with value ``True`` for
        empty geometries.

        Examples
        --------
        An example of a GeoDataFrame with one empty point, one point and one missing
        value:

        >>> from shapely.geometry import Point
        >>> d = {'geometry': [Point(), Point(2, 1), None]}
        >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326")
        >>> gdf
            geometry
        0  POINT EMPTY
        1  POINT (2 1)
        2         None

        >>> gdf.is_empty
        0     True
        1    False
        2    False
        dtype: bool

        See Also
        --------
        GeoSeries.isna : detect missing values
        """
        ...
    def count_coordinates(self) -> pd.Series[int]:
        """
        Returns a ``Series`` containing the count of the number of coordinate pairs
        in each geometry.

        Examples
        --------
        An example of a GeoDataFrame with two line strings, one point and one None
        value:

        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (1, 1), (1, -1), (0, 1)]),
        ...         LineString([(0, 0), (1, 1), (1, -1)]),
        ...         Point(0, 0),
        ...         Polygon([(10, 10), (10, 20), (20, 20), (20, 10), (10, 10)]),
        ...         None
        ...     ]
        ... )
        >>> s
        0                 LINESTRING (0 0, 1 1, 1 -1, 0 1)
        1                      LINESTRING (0 0, 1 1, 1 -1)
        2                                      POINT (0 0)
        3    POLYGON ((10 10, 10 20, 20 20, 20 10, 10 10))
        4                                             None
        dtype: geometry

        >>> s.count_coordinates()
        0    4
        1    3
        2    1
        3    5
        4    0
        dtype: int32

        See also
        --------
        GeoSeries.get_coordinates : extract coordinates as a :class:`~pandas.DataFrame`
        GoSeries.count_geometries : count the number of geometries in a collection
        """
        ...
    def count_geometries(self) -> pd.Series[int]:
        """
        Returns a ``Series`` containing the count of geometries in each multi-part
        geometry.

        For single-part geometry objects, this is always 1. For multi-part geometries,
        like ``MultiPoint`` or ``MultiLineString``, it is the number of parts in the
        geometry. For ``GeometryCollection``, it is the number of geometries direct
        parts of the collection (the method does not recurse into collections within
        collections).


        Examples
        --------
        >>> from shapely.geometry import Point, MultiPoint, LineString, MultiLineString
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         MultiPoint([(0, 0), (1, 1), (1, -1), (0, 1)]),
        ...         MultiLineString([((0, 0), (1, 1)), ((-1, 0), (1, 0))]),
        ...         LineString([(0, 0), (1, 1), (1, -1)]),
        ...         Point(0, 0),
        ...     ]
        ... )
        >>> s
        0     MULTIPOINT ((0 0), (1 1), (1 -1), (0 1))
        1    MULTILINESTRING ((0 0, 1 1), (-1 0, 1 0))
        2                  LINESTRING (0 0, 1 1, 1 -1)
        3                                  POINT (0 0)
        dtype: geometry

        >>> s.count_geometries()
        0    4
        1    2
        2    1
        3    1
        dtype: int32

        See also
        --------
        GeoSeries.count_coordinates : count the number of coordinates in a geometry
        GeoSeries.count_interior_rings : count the number of interior rings
        """
        ...
    def count_interior_rings(self) -> pd.Series[int]:
        """
        Returns a ``Series`` containing the count of the number of interior rings
        in a polygonal geometry.

        For non-polygonal geometries, this is always 0.

        Examples
        --------
        >>> from shapely.geometry import Polygon, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon(
        ...             [(0, 0), (0, 5), (5, 5), (5, 0)],
        ...             [[(1, 1), (1, 4), (4, 4), (4, 1)]],
        ...         ),
        ...         Polygon(
        ...             [(0, 0), (0, 5), (5, 5), (5, 0)],
        ...             [
        ...                 [(1, 1), (1, 2), (2, 2), (2, 1)],
        ...                 [(3, 2), (3, 3), (4, 3), (4, 2)],
        ...             ],
        ...         ),
        ...         Point(0, 1),
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0 0, 0 5, 5 5, 5 0, 0 0), (1 1, 1 4,...
        1    POLYGON ((0 0, 0 5, 5 5, 5 0, 0 0), (1 1, 1 2,...
        2                                          POINT (0 1)
        dtype: geometry

        >>> s.count_interior_rings()
        0    1
        1    2
        2    0
        dtype: int32

        See also
        --------
        GeoSeries.count_coordinates : count the number of coordinates in a geometry
        GeoSeries.count_geometries : count the number of geometries in a collection
        """
        ...
    @property
    def is_simple(self) -> pd.Series[bool]:
        """
        Returns a ``Series`` of ``dtype('bool')`` with value ``True`` for
        geometries that do not cross themselves.

        This is meaningful only for `LineStrings` and `LinearRings`.

        Examples
        --------
        >>> from shapely.geometry import LineString
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (1, 1), (1, -1), (0, 1)]),
        ...         LineString([(0, 0), (1, 1), (1, -1)]),
        ...     ]
        ... )
        >>> s
        0    LINESTRING (0 0, 1 1, 1 -1, 0 1)
        1         LINESTRING (0 0, 1 1, 1 -1)
        dtype: geometry

        >>> s.is_simple
        0    False
        1     True
        dtype: bool
        """
        ...
    @property
    def is_ring(self) -> pd.Series[bool]:
        """
        Returns a ``Series`` of ``dtype('bool')`` with value ``True`` for
        features that are closed.

        When constructing a LinearRing, the sequence of coordinates may be
        explicitly closed by passing identical values in the first and last indices.
        Otherwise, the sequence will be implicitly closed by copying the first tuple
        to the last index.

        Examples
        --------
        >>> from shapely.geometry import LineString, LinearRing
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (1, 1), (1, -1)]),
        ...         LineString([(0, 0), (1, 1), (1, -1), (0, 0)]),
        ...         LinearRing([(0, 0), (1, 1), (1, -1)]),
        ...     ]
        ... )
        >>> s
        0         LINESTRING (0 0, 1 1, 1 -1)
        1    LINESTRING (0 0, 1 1, 1 -1, 0 0)
        2    LINEARRING (0 0, 1 1, 1 -1, 0 0)
        dtype: geometry

        >>> s.is_ring
        0    False
        1     True
        2     True
        dtype: bool
        """
        ...
    @property
    def is_ccw(self) -> pd.Series[bool]:
        """
        Returns a ``Series`` of ``dtype('bool')`` with value ``True``
        if a LineString or LinearRing is counterclockwise.

        Note that there are no checks on whether lines are actually
        closed and not self-intersecting, while this is a requirement
        for ``is_ccw``. The recommended usage of this property for
        LineStrings is ``GeoSeries.is_ccw & GeoSeries.is_simple`` and for
        LinearRings ``GeoSeries.is_ccw & GeoSeries.is_valid``.

        This property will return False for non-linear geometries and for
        lines with fewer than 4 points (including the closing point).

        Examples
        --------
        >>> from shapely.geometry import LineString, LinearRing, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LinearRing([(0, 0), (0, 1), (1, 1), (0, 0)]),
        ...         LinearRing([(0, 0), (1, 1), (0, 1), (0, 0)]),
        ...         LineString([(0, 0), (1, 1), (0, 1)]),
        ...         Point(3, 3)
        ...     ]
        ... )
        >>> s
        0    LINEARRING (0 0, 0 1, 1 1, 0 0)
        1    LINEARRING (0 0, 1 1, 0 1, 0 0)
        2         LINESTRING (0 0, 1 1, 0 1)
        3                        POINT (3 3)
        dtype: geometry

        >>> s.is_ccw
        0    False
        1     True
        2    False
        3    False
        dtype: bool
        """
        ...
    @property
    def is_closed(self) -> pd.Series[bool]:
        """
        Returns a ``Series`` of ``dtype('bool')`` with value ``True``
        if a LineString's or LinearRing's first and last points are equal.

        Returns False for any other geometry type.

        Examples
        --------
        >>> from shapely.geometry import LineString, Point, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (1, 1), (0, 1), (0, 0)]),
        ...         LineString([(0, 0), (1, 1), (0, 1)]),
        ...         Polygon([(0, 0), (0, 1), (1, 1), (0, 0)]),
        ...         Point(3, 3)
        ...     ]
        ... )
        >>> s
        0    LINESTRING (0 0, 1 1, 0 1, 0 0)
        1         LINESTRING (0 0, 1 1, 0 1)
        2     POLYGON ((0 0, 0 1, 1 1, 0 0))
        3                        POINT (3 3)
        dtype: geometry

        >>> s.is_closed
        0     True
        1    False
        2    False
        3    False
        dtype: bool
        """
        ...
    @property
    def has_z(self) -> pd.Series[bool]: ...
    @property
    def has_m(self) -> pd.Series[bool]: ...
    def get_precision(self) -> pd.Series[float]: ...
    def get_geometry(self, index: SupportsIndex | ArrayLike) -> GeoSeries: ...
    @property
    def boundary(self) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of lower dimensional objects representing
        each geometry's set-theoretic `boundary`.

        Examples
        --------

        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(0, 0), (1, 1), (1, 0)]),
        ...         Point(0, 0),
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0 0, 1 1, 0 1, 0 0))
        1        LINESTRING (0 0, 1 1, 1 0)
        2                       POINT (0 0)
        dtype: geometry

        >>> s.boundary
        0    LINESTRING (0 0, 1 1, 0 1, 0 0)
        1          MULTIPOINT ((0 0), (1 0))
        2           GEOMETRYCOLLECTION EMPTY
        dtype: geometry

        See also
        --------
        GeoSeries.exterior : outer boundary (without interior rings)
        """
        ...
    @property
    def centroid(self) -> GeoSeries: ...
    def concave_hull(self, ratio: float = 0.0, allow_holes: bool = False) -> GeoSeries: ...
    def constrained_delaunay_triangles(self) -> GeoSeries: ...
    @property
    def convex_hull(self) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of geometries representing the convex hull
        of each geometry.

        The convex hull of a geometry is the smallest convex `Polygon`
        containing all the points in each geometry, unless the number of points
        in the geometric object is less than three. For two points, the convex
        hull collapses to a `LineString`; for 1, a `Point`.

        Examples
        --------

        >>> from shapely.geometry import Polygon, LineString, Point, MultiPoint
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(0, 0), (1, 1), (1, 0)]),
        ...         MultiPoint([(0, 0), (1, 1), (0, 1), (1, 0), (0.5, 0.5)]),
        ...         MultiPoint([(0, 0), (1, 1)]),
        ...         Point(0, 0),
        ...     ]
        ... )
        >>> s
        0                       POLYGON ((0 0, 1 1, 0 1, 0 0))
        1                           LINESTRING (0 0, 1 1, 1 0)
        2    MULTIPOINT ((0 0), (1 1), (0 1), (1 0), (0.5 0...
        3                            MULTIPOINT ((0 0), (1 1))
        4                                          POINT (0 0)
        dtype: geometry

        >>> s.convex_hull
        0         POLYGON ((0 0, 0 1, 1 1, 0 0))
        1         POLYGON ((0 0, 1 1, 1 0, 0 0))
        2    POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))
        3                  LINESTRING (0 0, 1 1)
        4                            POINT (0 0)
        dtype: geometry

        See also
        --------
        GeoSeries.concave_hull : concave hull geometry
        GeoSeries.envelope : bounding rectangle geometry
        """
        ...
    def delaunay_triangles(self, tolerance: float | ArrayLike = 0.0, only_edges: bool | ArrayLike = False) -> GeoSeries:
        """
        Returns a ``GeoSeries`` consisting of objects representing
        the computed Delaunay triangulation between the vertices of
        an input geometry.

        All geometries within the GeoSeries are considered together within a single
        Delaunay triangulation. The resulting geometries therefore do not map 1:1
        to input geometries. Note that each vertex of a geometry is considered a site
        for the triangulation, so the triangles will be constructed between the vertices
        of each geometry.

        Notes
        -----
        If you want to generate Delaunay triangles for each geometry separately, use
        :func:`shapely.delaunay_triangles` instead.

        Parameters
        ----------
        tolerance : float, default 0.0
            Snap input vertices together if their distance is less than this value.
        only_edges : bool (optional, default False)
            If set to True, the triangulation will return linestrings instead of
            polygons.

        Examples
        --------

        >>> from shapely import LineString, MultiPoint, Point, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(1, 1),
        ...         Point(2, 2),
        ...         Point(1, 3),
        ...         Point(0, 2),
        ...     ]
        ... )
        >>> s
        0    POINT (1 1)
        1    POINT (2 2)
        2    POINT (1 3)
        3    POINT (0 2)
        dtype: geometry

        >>> s.delaunay_triangles()
        0    POLYGON ((0 2, 1 1, 1 3, 0 2))
        1    POLYGON ((1 3, 1 1, 2 2, 1 3))
        dtype: geometry

        >>> s.delaunay_triangles(only_edges=True)
        0    LINESTRING (1 3, 2 2)
        1    LINESTRING (0 2, 1 3)
        2    LINESTRING (0 2, 1 1)
        3    LINESTRING (1 1, 2 2)
        4    LINESTRING (1 1, 1 3)
        dtype: geometry

        The method supports any geometry type but keep in mind that the underlying
        algorithm is based on the vertices of the input geometries only and does not
        consider edge segments between vertices.

        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(1, 0), (2, 1), (1, 2)]),
        ...         MultiPoint([(2, 3), (2, 0), (3, 1)]),
        ...     ]
        ... )
        >>> s2
        0      POLYGON ((0 0, 1 1, 0 1, 0 0))
        1          LINESTRING (1 0, 2 1, 1 2)
        2    MULTIPOINT ((2 3), (2 0), (3 1))
        dtype: geometry

        >>> s2.delaunay_triangles()
        0    POLYGON ((0 1, 0 0, 1 0, 0 1))
        1    POLYGON ((0 1, 1 0, 1 1, 0 1))
        2    POLYGON ((0 1, 1 1, 1 2, 0 1))
        3    POLYGON ((1 2, 1 1, 2 1, 1 2))
        4    POLYGON ((1 2, 2 1, 2 3, 1 2))
        5    POLYGON ((2 3, 2 1, 3 1, 2 3))
        6    POLYGON ((3 1, 2 1, 2 0, 3 1))
        7    POLYGON ((2 0, 2 1, 1 1, 2 0))
        8    POLYGON ((2 0, 1 1, 1 0, 2 0))
        dtype: geometry

        See also
        --------
        GeoSeries.voronoi_polygons : Voronoi diagram around vertices
        """
        ...
    def voronoi_polygons(
        self, tolerance: float | ArrayLike = 0.0, extend_to: Geometry | None = None, only_edges: bool = False
    ) -> GeoSeries:
        """
        Returns a ``GeoSeries`` consisting of objects representing
        the computed Voronoi diagram around the vertices of an input geometry.

        All geometries within the GeoSeries are considered together within a single
        Voronoi diagram. The resulting geometries therefore do not necessarily map 1:1
        to input geometries. Note that each vertex of a geometry is considered a site
        for the Voronoi diagram, so the diagram will be constructed around the vertices
        of each geometry.

        Notes
        -----
        The order of polygons in the output currently does not correspond to the order
        of input vertices.

        If you want to generate a Voronoi diagram for each geometry separately, use
        :func:`shapely.voronoi_polygons` instead.

        Parameters
        ----------
        tolerance : float, default 0.0
            Snap input vertices together if their distance is less than this value.
        extend_to : shapely.Geometry, default None
            If set, the Voronoi diagram will be extended to cover the
            envelope of this geometry (unless this envelope is smaller than the input
            geometry).
        only_edges : bool (optional, default False)
            If set to True, the diagram will return LineStrings instead
            of Polygons.

        Examples
        --------
        The most common use case is to generate polygons representing the Voronoi
        diagram around a set of points:

        >>> from shapely import LineString, MultiPoint, Point, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(1, 1),
        ...         Point(2, 2),
        ...         Point(1, 3),
        ...         Point(0, 2),
        ...     ]
        ... )
        >>> s
        0    POINT (1 1)
        1    POINT (2 2)
        2    POINT (1 3)
        3    POINT (0 2)
        dtype: geometry

        By default, you get back a GeoSeries of polygons:

        >>> s.voronoi_polygons()
        0     POLYGON ((-2 5, 1 2, -2 -1, -2 5))
        1        POLYGON ((4 5, 1 2, -2 5, 4 5))
        2    POLYGON ((-2 -1, 1 2, 4 -1, -2 -1))
        3       POLYGON ((4 -1, 1 2, 4 5, 4 -1))
        dtype: geometry

        If you set only_edges to True, you get back LineStrings representing the
        edges of the Voronoi diagram:

        >>> s.voronoi_polygons(only_edges=True)
        0     LINESTRING (-2 5, 1 2)
        1    LINESTRING (1 2, -2 -1)
        2      LINESTRING (4 5, 1 2)
        3     LINESTRING (1 2, 4 -1)
        dtype: geometry

        You can also extend each diagram to a given geometry:

        >>> limit = Polygon([(-10, -10), (0, 15), (15, 15), (15, 0)])
        >>> s.voronoi_polygons(extend_to=limit)
        0              POLYGON ((-10 13, 1 2, -10 -9, -10 13))
        1    POLYGON ((15 15, 15 -10, 13 -10, 1 2, 14 15, 1...
        2    POLYGON ((-10 -10, -10 -9, 1 2, 13 -10, -10 -10))
        3       POLYGON ((-10 15, 14 15, 1 2, -10 13, -10 15))
        dtype: geometry

        The method supports any geometry type but keep in mind that the underlying
        algorithm is based on the vertices of the input geometries only and does not
        consider edge segments between vertices.

        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(1, 0), (2, 1), (1, 2)]),
        ...         MultiPoint([(2, 3), (2, 0), (3, 1)]),
        ...     ]
        ... )
        >>> s2
        0      POLYGON ((0 0, 1 1, 0 1, 0 0))
        1          LINESTRING (1 0, 2 1, 1 2)
        2    MULTIPOINT ((2 3), (2 0), (3 1))
        dtype: geometry

        >>> s2.voronoi_polygons()
        0    POLYGON ((1.5 1.5, 1.5 0.5, 0.5 0.5, 0.5 1.5, ...
        1    POLYGON ((1.5 0.5, 1.5 1.5, 2 2, 2.5 2, 2.5 0....
        2    POLYGON ((-3 -3, -3 0.5, 0.5 0.5, 0.5 -3, -3 -3))
        3    POLYGON ((0.5 -3, 0.5 0.5, 1.5 0.5, 1.5 -3, 0....
        4     POLYGON ((-3 5, 0.5 1.5, 0.5 0.5, -3 0.5, -3 5))
        5    POLYGON ((-3 6, -2 6, 2 2, 1.5 1.5, 0.5 1.5, -...
        6    POLYGON ((1.5 -3, 1.5 0.5, 2.5 0.5, 6 -3, 1.5 ...
        7       POLYGON ((6 6, 6 3.75, 2.5 2, 2 2, -2 6, 6 6))
        8       POLYGON ((6 -3, 2.5 0.5, 2.5 2, 6 3.75, 6 -3))
        dtype: geometry

        See also
        --------
        GeoSeries.delaunay_triangles : Delaunay triangulation around vertices
        """
        ...
    @property
    def envelope(self) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of geometries representing the envelope of
        each geometry.

        The envelope of a geometry is the bounding rectangle. That is, the
        point or smallest rectangular polygon (with sides parallel to the
        coordinate axes) that contains the geometry.

        Examples
        --------

        >>> from shapely.geometry import Polygon, LineString, Point, MultiPoint
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(0, 0), (1, 1), (1, 0)]),
        ...         MultiPoint([(0, 0), (1, 1)]),
        ...         Point(0, 0),
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0 0, 1 1, 0 1, 0 0))
        1        LINESTRING (0 0, 1 1, 1 0)
        2         MULTIPOINT ((0 0), (1 1))
        3                       POINT (0 0)
        dtype: geometry

        >>> s.envelope
        0    POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))
        1    POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))
        2    POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))
        3                            POINT (0 0)
        dtype: geometry

        See also
        --------
        GeoSeries.convex_hull : convex hull geometry
        """
        ...
    def minimum_rotated_rectangle(self) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of the general minimum bounding rectangle
        that contains the object.

        Unlike envelope this rectangle is not constrained to be parallel
        to the coordinate axes. If the convex hull of the object is a
        degenerate (line or point) this degenerate is returned.

        Examples
        --------

        >>> from shapely.geometry import Polygon, LineString, Point, MultiPoint
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(0, 0), (1, 1), (1, 0)]),
        ...         MultiPoint([(0, 0), (1, 1)]),
        ...         Point(0, 0),
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0 0, 1 1, 0 1, 0 0))
        1        LINESTRING (0 0, 1 1, 1 0)
        2         MULTIPOINT ((0 0), (1 1))
        3                       POINT (0 0)
        dtype: geometry

        >>> s.minimum_rotated_rectangle()
        0    POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))
        1    POLYGON ((1 1, 1 0, 0 0, 0 1, 1 1))
        2                  LINESTRING (0 0, 1 1)
        3                            POINT (0 0)
        dtype: geometry

        See also
        --------
        GeoSeries.envelope : bounding rectangle
        """
        ...
    @property
    def exterior(self) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of LinearRings representing the outer
        boundary of each polygon in the GeoSeries.

        Applies to GeoSeries containing only Polygons. Returns ``None``` for
        other geometry types.

        Examples
        --------

        >>> from shapely.geometry import Polygon, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         Polygon([(1, 0), (2, 1), (0, 0)]),
        ...         Point(0, 1)
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0 0, 1 1, 0 1, 0 0))
        1    POLYGON ((1 0, 2 1, 0 0, 1 0))
        2                       POINT (0 1)
        dtype: geometry

        >>> s.exterior
        0    LINEARRING (0 0, 1 1, 0 1, 0 0)
        1    LINEARRING (1 0, 2 1, 0 0, 1 0)
        2                               None
        dtype: geometry

        See also
        --------
        GeoSeries.boundary : complete set-theoretic boundary
        GeoSeries.interiors : list of inner rings of each polygon
        """
        ...
    def extract_unique_points(self) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of MultiPoints representing all
        distinct vertices of an input geometry.

        Examples
        --------

        >>> from shapely import LineString, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (0, 0), (1, 1), (1, 1)]),
        ...         Polygon([(0, 0), (0, 0), (1, 1), (1, 1)])
        ...     ],
        ... )
        >>> s
        0        LINESTRING (0 0, 0 0, 1 1, 1 1)
        1    POLYGON ((0 0, 0 0, 1 1, 1 1, 0 0))
        dtype: geometry

        >>> s.extract_unique_points()
        0    MULTIPOINT ((0 0), (1 1))
        1    MULTIPOINT ((0 0), (1 1))
        dtype: geometry

        See also
        --------

        GeoSeries.get_coordinates : extract coordinates as a :class:`~pandas.DataFrame`
        """
        ...
    def offset_curve(
        self,
        distance: float | ArrayLike,
        quad_segs: int = 8,
        join_style: Literal["round", "bevel", "mitre"] = "round",
        mitre_limit: float = 5.0,
    ) -> GeoSeries:
        """
        Returns a ``LineString`` or ``MultiLineString`` geometry at a
        distance from the object on its right or its left side.

        Parameters
        ----------
        distance : float | array-like
            Specifies the offset distance from the input geometry. Negative
            for right side offset, positive for left side offset.
        quad_segs : int (optional, default 8)
            Specifies the number of linear segments in a quarter circle in the
            approximation of circular arcs.
        join_style : {'round', 'bevel', 'mitre'}, (optional, default 'round')
            Specifies the shape of outside corners. 'round' results in
            rounded shapes. 'bevel' results in a beveled edge that touches the
            original vertex. 'mitre' results in a single vertex that is beveled
            depending on the ``mitre_limit`` parameter.
        mitre_limit : float (optional, default 5.0)
            Crops of 'mitre'-style joins if the point is displaced from the
            buffered vertex by more than this limit.

        See http://shapely.readthedocs.io/en/latest/manual.html#object.offset_curve
        for details.

        Examples
        --------

        >>> from shapely.geometry import LineString
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (0, 1), (1, 1)]),
        ...     ],
        ...     crs=3857
        ... )
        >>> s
        0    LINESTRING (0 0, 0 1, 1 1)
        dtype: geometry

        >>> s.offset_curve(1)
        0    LINESTRING (-1 0, -1 1, -0.981 1.195, -0.924 1...
        dtype: geometry
        """
        ...
    @property
    def interiors(self) -> pd.Series[Any]:
        """
        Returns a ``Series`` of List representing the
        inner rings of each polygon in the GeoSeries.

        Applies to GeoSeries containing only Polygons.

        Returns
        -------
        inner_rings: Series of List
            Inner rings of each polygon in the GeoSeries.

        Examples
        --------

        >>> from shapely.geometry import Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon(
        ...             [(0, 0), (0, 5), (5, 5), (5, 0)],
        ...             [[(1, 1), (2, 1), (1, 2)], [(1, 4), (2, 4), (2, 3)]],
        ...         ),
        ...         Polygon([(1, 0), (2, 1), (0, 0)]),
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0 0, 0 5, 5 5, 5 0, 0 0), (1 1, 2 1,...
        1                       POLYGON ((1 0, 2 1, 0 0, 1 0))
        dtype: geometry

        >>> s.interiors
        0    [LINEARRING (1 1, 2 1, 1 2, 1 1), LINEARRING (...
        1                                                   []
        dtype: object

        See also
        --------
        GeoSeries.exterior : outer boundary
        """
        ...
    def remove_repeated_points(self, tolerance: float = 0.0) -> GeoSeries:
        """
        Returns a ``GeoSeries`` containing a copy of the input geometry
        with repeated points removed.

        From the start of the coordinate sequence, each next point within the
        tolerance is removed.

        Removing repeated points with a non-zero tolerance may result in an invalid
        geometry being returned.

        Parameters
        ----------
        tolerance : float, default 0.0
            Remove all points within this distance of each other. Use 0.0
            to remove only exactly repeated points (the default).

        Examples
        --------

        >>> from shapely import LineString, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...        LineString([(0, 0), (0, 0), (1, 0)]),
        ...        Polygon([(0, 0), (0, 0.5), (0, 1), (0.5, 1), (0,0)]),
        ...     ],
        ... )
        >>> s
        0                 LINESTRING (0 0, 0 0, 1 0)
        1    POLYGON ((0 0, 0 0.5, 0 1, 0.5 1, 0 0))
        dtype: geometry

        >>> s.remove_repeated_points(tolerance=0.0)
        0                      LINESTRING (0 0, 1 0)
        1    POLYGON ((0 0, 0 0.5, 0 1, 0.5 1, 0 0))
        dtype: geometry
        """
        ...
    def set_precision(
        self, grid_size: float, mode: Literal["valid_output", "pointwise", "keep_collapsed"] = "valid_output"
    ) -> GeoSeries: ...
    def representative_point(self) -> GeoSeries: ...
    def minimum_bounding_circle(self) -> GeoSeries: ...
    def maximum_inscribed_circle(self, *, tolerance: float | ArrayLike | None = None) -> GeoSeries: ...
    def minimum_bounding_radius(self) -> pd.Series[float]: ...
    def minimum_clearance(self) -> pd.Series[float]: ...
    def minimum_clearance_line(self) -> GeoSeries: ...
    def normalize(self) -> GeoSeries: ...
    def orient_polygons(self, *, exterior_cw: bool = False) -> GeoSeries: ...
    def make_valid(self, *, method: Literal["linework", "structure"] = "linework", keep_collapsed: bool = True) -> GeoSeries: ...
    def reverse(self) -> GeoSeries: ...
    def segmentize(self, max_segment_length: float | ArrayLike) -> GeoSeries: ...
    def transform(
        self, transformation: Callable[[NDArray[np.float64]], NDArray[np.float64]], include_z: bool = False
    ) -> GeoSeries:
        """
        Returns a ``GeoSeries`` with the transformation function
        applied to the geometry coordinates.

        Parameters
        ----------
        transformation : Callable
            A function that transforms a (N, 2) or (N, 3) ndarray of float64
            to another (N,2) or (N, 3) ndarray of float64
        include_z : bool, default False
            If True include the third dimension in the coordinates array that
            is passed to the ``transformation`` function. If a geometry has no third
            dimension, the z-coordinates passed to the function will be NaN.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely import Point, Polygon
        >>> s = geopandas.GeoSeries([Point(0, 0)])
        >>> s.transform(lambda x: x + 1)
        0    POINT (1 1)
        dtype: geometry

        >>> s = geopandas.GeoSeries([Polygon([(0, 0), (1, 1), (0, 1)])])
        >>> s.transform(lambda x: x * [2, 3])
        0    POLYGON ((0 0, 2 3, 0 3, 0 0))
        dtype: geometry

        By default the third dimension is ignored and you need explicitly include it:

        >>> s = geopandas.GeoSeries([Point(0, 0, 0)])
        >>> s.transform(lambda x: x + 1, include_z=True)
        0    POINT Z (1 1 1)
        dtype: geometry
        """
        ...
    def force_2d(self) -> GeoSeries:
        """
        Forces the dimensionality of a geometry to 2D.

        Removes the additional Z coordinate dimension from all geometries.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(0.5, 2.5, 0),
        ...         LineString([(1, 1, 1), (0, 1, 3), (1, 0, 2)]),
        ...         Polygon([(0, 0, 0), (0, 10, 0), (10, 10, 0)]),
        ...     ],
        ... )
        >>> s
        0                            POINT Z (0.5 2.5 0)
        1             LINESTRING Z (1 1 1, 0 1 3, 1 0 2)
        2    POLYGON Z ((0 0 0, 0 10 0, 10 10 0, 0 0 0))
        dtype: geometry

        >>> s.force_2d()
        0                      POINT (0.5 2.5)
        1           LINESTRING (1 1, 0 1, 1 0)
        2    POLYGON ((0 0, 0 10, 10 10, 0 0))
        dtype: geometry
        """
        ...
    def force_3d(self, z: float | ArrayLike = 0) -> GeoSeries:
        """
        Forces the dimensionality of a geometry to 3D.

        2D geometries will get the provided Z coordinate; 3D geometries
        are unchanged (unless their Z coordinate is ``np.nan``).

        Note that for empty geometries, 3D is only supported since GEOS 3.9 and then
        still only for simple geometries (non-collections).

        Parameters
        ----------
        z : float | array_like (default 0)
            Z coordinate to be assigned

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(1, 2),
        ...         Point(0.5, 2.5, 2),
        ...         LineString([(1, 1), (0, 1), (1, 0)]),
        ...         Polygon([(0, 0), (0, 10), (10, 10)]),
        ...     ],
        ... )
        >>> s
        0                          POINT (1 2)
        1                  POINT Z (0.5 2.5 2)
        2           LINESTRING (1 1, 0 1, 1 0)
        3    POLYGON ((0 0, 0 10, 10 10, 0 0))
        dtype: geometry

        >>> s.force_3d()
        0                                POINT Z (1 2 0)
        1                            POINT Z (0.5 2.5 2)
        2             LINESTRING Z (1 1 0, 0 1 0, 1 0 0)
        3    POLYGON Z ((0 0 0, 0 10 0, 10 10 0, 0 0 0))
        dtype: geometry

        Z coordinate can be specified as scalar:

        >>> s.force_3d(4)
        0                                POINT Z (1 2 4)
        1                            POINT Z (0.5 2.5 2)
        2             LINESTRING Z (1 1 4, 0 1 4, 1 0 4)
        3    POLYGON Z ((0 0 4, 0 10 4, 10 10 4, 0 0 4))
        dtype: geometry

        Or as an array-like (one value per geometry):

        >>> s.force_3d(range(4))
        0                                POINT Z (1 2 0)
        1                            POINT Z (0.5 2.5 2)
        2             LINESTRING Z (1 1 2, 0 1 2, 1 0 2)
        3    POLYGON Z ((0 0 3, 0 10 3, 10 10 3, 0 0 3))
        dtype: geometry
        """
        ...
    def line_merge(self, directed: bool = False) -> GeoSeries:
        """
        Returns (Multi)LineStrings formed by combining the lines in a
        MultiLineString.

        Lines are joined together at their endpoints in case two lines are intersecting.
        Lines are not joined when 3 or more lines are intersecting at the endpoints.
        Line elements that cannot be joined are kept as is in the resulting
        MultiLineString.

        The direction of each merged LineString will be that of the majority of the
        LineStrings from which it was derived. Except if ``directed=True`` is specified,
        then the operation will not change the order of points within lines and so only
        lines which can be joined with no change in direction are merged.

        Non-linear geometeries result in an empty GeometryCollection.

        Parameters
        ----------
        directed : bool, default False
            Only combine lines if possible without changing point order.
            Requires GEOS >= 3.11.0

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import MultiLineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         MultiLineString([[(0, 2), (0, 10)], [(0, 10), (5, 10)]]),
        ...         MultiLineString([[(0, 2), (0, 10)], [(0, 11), (5, 10)]]),
        ...         MultiLineString(),
        ...         MultiLineString([[(0, 0), (1, 0)], [(0, 0), (3, 0)]]),
        ...         Point(0, 0),
        ...     ]
        ... )
        >>> s
        0    MULTILINESTRING ((0 2, 0 10), (0 10, 5 10))
        1    MULTILINESTRING ((0 2, 0 10), (0 11, 5 10))
        2                          MULTILINESTRING EMPTY
        3       MULTILINESTRING ((0 0, 1 0), (0 0, 3 0))
        4                                    POINT (0 0)
        dtype: geometry

        >>> s.line_merge()
        0                   LINESTRING (0 2, 0 10, 5 10)
        1    MULTILINESTRING ((0 2, 0 10), (0 11, 5 10))
        2                       GEOMETRYCOLLECTION EMPTY
        3                     LINESTRING (1 0, 0 0, 3 0)
        4                       GEOMETRYCOLLECTION EMPTY
        dtype: geometry

        With ``directed=True``, you can avoid changing the order of points within lines
        and merge only lines where no change of direction is required:

        >>> s.line_merge(directed=True)
        0                   LINESTRING (0 2, 0 10, 5 10)
        1    MULTILINESTRING ((0 2, 0 10), (0 11, 5 10))
        2                       GEOMETRYCOLLECTION EMPTY
        3       MULTILINESTRING ((0 0, 1 0), (0 0, 3 0))
        4                       GEOMETRYCOLLECTION EMPTY
        dtype: geometry
        """
        ...
    @property
    @deprecated("Use method `union_all` instead.")
    def unary_union(self) -> BaseGeometry: ...
    def union_all(
        self, method: Literal["coverage", "unary", "disjoint_subset"] = "unary", *, grid_size: float | None = None
    ) -> BaseGeometry: ...
    def intersection_all(self) -> BaseGeometry: ...
    def contains(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def contains_properly(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def dwithin(self, other: GeoSeries | Geometry, distance: float | ArrayLike, align: bool | None = None) -> pd.Series[bool]: ...
    def geom_equals(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def geom_equals_exact(
        self, other: GeoSeries | Geometry, tolerance: float | ArrayLike, align: bool | None = None
    ) -> pd.Series[bool]: ...
    def geom_equals_identical(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def crosses(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def disjoint(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def intersects(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def overlaps(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def touches(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def within(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def covers(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def covered_by(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[bool]: ...
    def distance(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[float]: ...
    def hausdorff_distance(
        self, other: GeoSeries | Geometry, align: bool | None = None, densify: float | ArrayLike | None = None
    ) -> pd.Series[float]:
        """
        Returns a ``Series`` containing the Hausdorff distance to aligned `other`.

        The Hausdorff distance is the largest distance consisting of any point in `self`
        with the nearest point in `other`.

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center

        Parameters
        ----------
        other : GeoSeries or geometric object
            The Geoseries (elementwise) or geometric object to find the
            distance to.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.
        densify : float (default None)
            A value between 0 and 1, that splits each subsegment of a line string
            into equal length segments, making the approximation less coarse.
            A densify value of 0.5 will add a point halfway between each pair of
            points. A densify value of 0.25 will add a point a quarter of the way
            between each pair of points.


        Returns
        -------
        Series (float)

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 0), (1, 1)]),
        ...         Polygon([(0, 0), (-1, 0), (-1, 1)]),
        ...         LineString([(1, 1), (0, 0)]),
        ...         Point(0, 0),
        ...     ],
        ... )
        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)]),
        ...         Point(3, 1),
        ...         LineString([(1, 0), (2, 0)]),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 5),
        ... )

        >>> s
        0      POLYGON ((0 0, 1 0, 1 1, 0 0))
        1    POLYGON ((0 0, -1 0, -1 1, 0 0))
        2               LINESTRING (1 1, 0 0)
        3                         POINT (0 0)
        dtype: geometry

        >>> s2
        1    POLYGON ((0.5 0.5, 1.5 0.5, 1.5 1.5, 0.5 1.5, ...
        2                                          POINT (3 1)
        3                                LINESTRING (1 0, 2 0)
        4                                          POINT (0 1)
        dtype: geometry

        We can check the hausdorff distance of each geometry of GeoSeries
        to a single geometry:

        >>> point = Point(-1, 0)
        >>> s.hausdorff_distance(point)
        0    2.236068
        1    1.000000
        2    2.236068
        3    1.000000
        dtype: float64

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and use elements with the same index using
        ``align=True`` or ignore index and use elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.hausdorff_distance(s2, align=True)
        0         NaN
        1    2.121320
        2    3.162278
        3    2.000000
        4         NaN
        dtype: float64

        >>> s.hausdorff_distance(s2, align=False)
        0    0.707107
        1    4.123106
        2    1.414214
        3    1.000000
        dtype: float64

        We can also set a densify value, which is a float between 0 and 1 and
        signifies the fraction of the distance between each pair of points that will
        be used as the distance between the points when densifying.

        >>> l1 = geopandas.GeoSeries([LineString([(130, 0), (0, 0), (0, 150)])])
        >>> l2 = geopandas.GeoSeries([LineString([(10, 10), (10, 150), (130, 10)])])
        >>> l1.hausdorff_distance(l2)
        0    14.142136
        dtype: float64
        >>> l1.hausdorff_distance(l2, densify=0.25)
        0    70.0
        dtype: float64
        """
        ...
    def frechet_distance(
        self, other: GeoSeries | Geometry, align: bool | None = None, densify: float | ArrayLike | None = None
    ) -> pd.Series[float]:
        """
        Returns a ``Series`` containing the Frechet distance to aligned `other`.

        The Fréchet distance is a measure of similarity: it is the greatest distance
        between any point in A and the closest point in B. The discrete distance is an
        approximation of this metric: only vertices are considered. The parameter
        ``densify`` makes this approximation less coarse by splitting the line segments
        between vertices before computing the distance.

        Fréchet distance sweep continuously along their respective curves and the
        direction of curves is significant. This makes it a better measure of similarity
        than Hausdorff distance for curve or surface matching.

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center

        Parameters
        ----------
        other : GeoSeries or geometric object
            The Geoseries (elementwise) or geometric object to find the
            distance to.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.
        densify : float (default None)
            A value between 0 and 1, that splits each subsegment of a line string
            into equal length segments, making the approximation less coarse.
            A densify value of 0.5 will add a point halfway between each pair of
            points. A densify value of 0.25 will add a point every quarter of the way
            between each pair of points.

        Returns
        -------
        Series (float)

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 0), (1, 1)]),
        ...         Polygon([(0, 0), (-1, 0), (-1, 1)]),
        ...         LineString([(1, 1), (0, 0)]),
        ...         Point(0, 0),
        ...     ],
        ... )
        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)]),
        ...         Point(3, 1),
        ...         LineString([(1, 0), (2, 0)]),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 5),
        ... )

        >>> s
        0      POLYGON ((0 0, 1 0, 1 1, 0 0))
        1    POLYGON ((0 0, -1 0, -1 1, 0 0))
        2               LINESTRING (1 1, 0 0)
        3                         POINT (0 0)
        dtype: geometry

        >>> s2
        1    POLYGON ((0.5 0.5, 1.5 0.5, 1.5 1.5, 0.5 1.5, ...
        2                                          POINT (3 1)
        3                                LINESTRING (1 0, 2 0)
        4                                          POINT (0 1)
        dtype: geometry

        We can check the frechet distance of each geometry of GeoSeries
        to a single geometry:

        >>> point = Point(-1, 0)
        >>> s.frechet_distance(point)
        0    2.236068
        1    1.000000
        2    2.236068
        3    1.000000
        dtype: float64

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and use elements with the same index using
        ``align=True`` or ignore index and use elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.frechet_distance(s2, align=True)
        0         NaN
        1    2.121320
        2    3.162278
        3    2.000000
        4         NaN
        dtype: float64
        >>> s.frechet_distance(s2, align=False)
        0    0.707107
        1    4.123106
        2    2.000000
        3    1.000000
        dtype: float64

        We can also set a ``densify`` value, which is a float between 0 and 1 and
        signifies the fraction of the distance between each pair of points that will
        be used as the distance between the points when densifying.

        >>> l1 = geopandas.GeoSeries([LineString([(0, 0), (10, 0), (0, 15)])])
        >>> l2 = geopandas.GeoSeries([LineString([(0, 0), (20, 15), (9, 11)])])
        >>> l1.frechet_distance(l2)
        0    18.027756
        dtype: float64
        >>> l1.frechet_distance(l2, densify=0.25)
        0    16.77051
        dtype: float64
        """
        ...
    def difference(self, other: GeoSeries | Geometry, align: bool | None = None) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of the points in each aligned geometry that
        are not in `other`.

        .. image:: ../../../_static/binary_geo-difference.svg
           :align: center

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center

        Parameters
        ----------
        other : Geoseries or geometric object
            The Geoseries (elementwise) or geometric object to find the
            difference to.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         LineString([(0, 0), (2, 2)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(0, 1),
        ...     ],
        ... )
        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(1, 0), (1, 3)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(1, 1),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 6),
        ... )

        >>> s
        0    POLYGON ((0 0, 2 2, 0 2, 0 0))
        1    POLYGON ((0 0, 2 2, 0 2, 0 0))
        2             LINESTRING (0 0, 2 2)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (0 1)
        dtype: geometry

        >>> s2
        1    POLYGON ((0 0, 1 1, 0 1, 0 0))
        2             LINESTRING (1 0, 1 3)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (1 1)
        5                       POINT (0 1)
        dtype: geometry

        We can do difference of each geometry and a single
        shapely geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> s.difference(Polygon([(0, 0), (1, 1), (0, 1)]))
        0       POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        1         POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        2                       LINESTRING (1 1, 2 2)
        3    MULTILINESTRING ((2 0, 1 1), (1 1, 0 2))
        4                                 POINT EMPTY
        dtype: geometry

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and compare elements with the same index using
        ``align=True`` or ignore index and compare elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.difference(s2, align=True)
        0                                        None
        1         POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        2    MULTILINESTRING ((0 0, 1 1), (1 1, 2 2))
        3                            LINESTRING EMPTY
        4                                 POINT (0 1)
        5                                        None
        dtype: geometry

        >>> s.difference(s2, align=False)
        0         POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        1    POLYGON ((0 0, 0 2, 1 2, 2 2, 1 1, 0 0))
        2    MULTILINESTRING ((0 0, 1 1), (1 1, 2 2))
        3                       LINESTRING (2 0, 0 2)
        4                                 POINT EMPTY
        dtype: geometry

        See Also
        --------
        GeoSeries.symmetric_difference
        GeoSeries.union
        GeoSeries.intersection
        """
        ...
    def symmetric_difference(self, other: GeoSeries | Geometry, align: bool | None = None) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of the symmetric difference of points in
        each aligned geometry with `other`.

        For each geometry, the symmetric difference consists of points in the
        geometry not in `other`, and points in `other` not in the geometry.

        .. image:: ../../../_static/binary_geo-symm_diff.svg
           :align: center

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center


        Parameters
        ----------
        other : Geoseries or geometric object
            The Geoseries (elementwise) or geometric object to find the
            symmetric difference to.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         LineString([(0, 0), (2, 2)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(0, 1),
        ...     ],
        ... )
        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(1, 0), (1, 3)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(1, 1),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 6),
        ... )

        >>> s
        0    POLYGON ((0 0, 2 2, 0 2, 0 0))
        1    POLYGON ((0 0, 2 2, 0 2, 0 0))
        2             LINESTRING (0 0, 2 2)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (0 1)
        dtype: geometry

        >>> s2
        1    POLYGON ((0 0, 1 1, 0 1, 0 0))
        2             LINESTRING (1 0, 1 3)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (1 1)
        5                       POINT (0 1)
        dtype: geometry

        We can do symmetric difference of each geometry and a single
        shapely geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> s.symmetric_difference(Polygon([(0, 0), (1, 1), (0, 1)]))
        0                  POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        1                  POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        2    GEOMETRYCOLLECTION (POLYGON ((0 0, 0 1, 1 1, 0...
        3    GEOMETRYCOLLECTION (POLYGON ((0 0, 0 1, 1 1, 0...
        4                       POLYGON ((0 1, 1 1, 0 0, 0 1))
        dtype: geometry

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and compare elements with the same index using
        ``align=True`` or ignore index and compare elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.symmetric_difference(s2, align=True)
        0                                                 None
        1                  POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        2    MULTILINESTRING ((0 0, 1 1), (1 1, 2 2), (1 0,...
        3                                     LINESTRING EMPTY
        4                            MULTIPOINT ((0 1), (1 1))
        5                                                 None
        dtype: geometry

        >>> s.symmetric_difference(s2, align=False)
        0                  POLYGON ((0 2, 2 2, 1 1, 0 1, 0 2))
        1    GEOMETRYCOLLECTION (POLYGON ((0 0, 0 2, 1 2, 2...
        2    MULTILINESTRING ((0 0, 1 1), (1 1, 2 2), (2 0,...
        3                                LINESTRING (2 0, 0 2)
        4                                          POINT EMPTY
        dtype: geometry

        See Also
        --------
        GeoSeries.difference
        GeoSeries.union
        GeoSeries.intersection
        """
        ...
    def union(self, other: GeoSeries | Geometry, align: bool | None = None) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of the union of points in each aligned geometry with
        `other`.

        .. image:: ../../../_static/binary_geo-union.svg
           :align: center

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center


        Parameters
        ----------
        other : Geoseries or geometric object
            The Geoseries (elementwise) or geometric object to find the union
            with.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         LineString([(0, 0), (2, 2)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(0, 1),
        ...     ],
        ... )
        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(1, 0), (1, 3)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(1, 1),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 6),
        ... )

        >>> s
        0    POLYGON ((0 0, 2 2, 0 2, 0 0))
        1    POLYGON ((0 0, 2 2, 0 2, 0 0))
        2             LINESTRING (0 0, 2 2)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (0 1)
        dtype: geometry
        >>>

        >>> s2
        1    POLYGON ((0 0, 1 1, 0 1, 0 0))
        2             LINESTRING (1 0, 1 3)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (1 1)
        5                       POINT (0 1)
        dtype: geometry

        We can do union of each geometry and a single
        shapely geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> s.union(Polygon([(0, 0), (1, 1), (0, 1)]))
        0             POLYGON ((0 0, 0 1, 0 2, 2 2, 1 1, 0 0))
        1             POLYGON ((0 0, 0 1, 0 2, 2 2, 1 1, 0 0))
        2    GEOMETRYCOLLECTION (POLYGON ((0 0, 0 1, 1 1, 0...
        3    GEOMETRYCOLLECTION (POLYGON ((0 0, 0 1, 1 1, 0...
        4                       POLYGON ((0 1, 1 1, 0 0, 0 1))
        dtype: geometry

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and compare elements with the same index using
        ``align=True`` or ignore index and compare elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.union(s2, align=True)
        0                                                 None
        1             POLYGON ((0 0, 0 1, 0 2, 2 2, 1 1, 0 0))
        2    MULTILINESTRING ((0 0, 1 1), (1 1, 2 2), (1 0,...
        3                                LINESTRING (2 0, 0 2)
        4                            MULTIPOINT ((0 1), (1 1))
        5                                                 None
        dtype: geometry

        >>> s.union(s2, align=False)
        0             POLYGON ((0 0, 0 1, 0 2, 2 2, 1 1, 0 0))
        1    GEOMETRYCOLLECTION (POLYGON ((0 0, 0 2, 1 2, 2...
        2    MULTILINESTRING ((0 0, 1 1), (1 1, 2 2), (2 0,...
        3                                LINESTRING (2 0, 0 2)
        4                                          POINT (0 1)
        dtype: geometry


        See Also
        --------
        GeoSeries.symmetric_difference
        GeoSeries.difference
        GeoSeries.intersection
        """
        ...
    def intersection(self, other: GeoSeries | Geometry, align: bool | None = None) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of the intersection of points in each
        aligned geometry with `other`.

        .. image:: ../../../_static/binary_geo-intersection.svg
           :align: center

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center


        Parameters
        ----------
        other : Geoseries or geometric object
            The Geoseries (elementwise) or geometric object to find the
            intersection with.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         LineString([(0, 0), (2, 2)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(0, 1),
        ...     ],
        ... )
        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         LineString([(1, 0), (1, 3)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(1, 1),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 6),
        ... )

        >>> s
        0    POLYGON ((0 0, 2 2, 0 2, 0 0))
        1    POLYGON ((0 0, 2 2, 0 2, 0 0))
        2             LINESTRING (0 0, 2 2)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (0 1)
        dtype: geometry

        >>> s2
        1    POLYGON ((0 0, 1 1, 0 1, 0 0))
        2             LINESTRING (1 0, 1 3)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (1 1)
        5                       POINT (0 1)
        dtype: geometry

        We can also do intersection of each geometry and a single
        shapely geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> s.intersection(Polygon([(0, 0), (1, 1), (0, 1)]))
        0    POLYGON ((0 0, 0 1, 1 1, 0 0))
        1    POLYGON ((0 0, 0 1, 1 1, 0 0))
        2             LINESTRING (0 0, 1 1)
        3                       POINT (1 1)
        4                       POINT (0 1)
        dtype: geometry

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and compare elements with the same index using
        ``align=True`` or ignore index and compare elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.intersection(s2, align=True)
        0                              None
        1    POLYGON ((0 0, 0 1, 1 1, 0 0))
        2                       POINT (1 1)
        3             LINESTRING (2 0, 0 2)
        4                       POINT EMPTY
        5                              None
        dtype: geometry

        >>> s.intersection(s2, align=False)
        0    POLYGON ((0 0, 0 1, 1 1, 0 0))
        1             LINESTRING (1 1, 1 2)
        2                       POINT (1 1)
        3                       POINT (1 1)
        4                       POINT (0 1)
        dtype: geometry


        See Also
        --------
        GeoSeries.difference
        GeoSeries.symmetric_difference
        GeoSeries.union
        """
        ...
    def clip_by_rect(self, xmin: float, ymin: float, xmax: float, ymax: float) -> GeoSeries:
        """
        Returns a ``GeoSeries`` of the portions of geometry within the given
        rectangle.

        Note that the results are not exactly equal to
        :meth:`~GeoSeries.intersection()`. E.g. in edge cases,
        :meth:`~GeoSeries.clip_by_rect()` will not return a point just touching the
        rectangle. Check the examples section below for some of these exceptions.

        The geometry is clipped in a fast but possibly dirty way. The output is not
        guaranteed to be valid. No exceptions will be raised for topological errors.

        Note: empty geometries or geometries that do not overlap with the specified
        bounds will result in ``GEOMETRYCOLLECTION EMPTY``.

        Parameters
        ----------
        xmin: float
            Minimum x value of the rectangle
        ymin: float
            Minimum y value of the rectangle
        xmax: float
            Maximum x value of the rectangle
        ymax: float
            Maximum y value of the rectangle

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         LineString([(0, 0), (2, 2)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(0, 1),
        ...     ],
        ... )
        >>> bounds = (0, 0, 1, 1)
        >>> s
        0    POLYGON ((0 0, 2 2, 0 2, 0 0))
        1    POLYGON ((0 0, 2 2, 0 2, 0 0))
        2             LINESTRING (0 0, 2 2)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (0 1)
        dtype: geometry

        >>> s.clip_by_rect(*bounds)
        0    POLYGON ((0 0, 0 1, 1 1, 0 0))
        1    POLYGON ((0 0, 0 1, 1 1, 0 0))
        2             LINESTRING (0 0, 1 1)
        3          GEOMETRYCOLLECTION EMPTY
        4          GEOMETRYCOLLECTION EMPTY
        dtype: geometry

        See also
        --------
        GeoSeries.intersection
        """
        ...
    def shortest_line(self, other: GeoSeries | Geometry, align: bool | None = None) -> GeoSeries:
        """
        Returns the shortest two-point line between two geometries.

        The resulting line consists of two points, representing the nearest points
        between the geometry pair. The line always starts in the first geometry a
        and ends in he second geometry b. The endpoints of the line will not
        necessarily be existing vertices of the input geometries a and b, but
        can also be a point along a line segment.


        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
            :align: center

        Parameters
        ----------
        other : Geoseries or geometric object
            The Geoseries (elementwise) or geometric object to find the
            shortest line with.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         Polygon([(0, 0), (2, 2), (0, 2)]),
        ...         LineString([(0, 0), (2, 2)]),
        ...         LineString([(2, 0), (0, 2)]),
        ...         Point(0, 1),
        ...     ],
        ... )
        >>> s
        0    POLYGON ((0 0, 2 2, 0 2, 0 0))
        1    POLYGON ((0 0, 2 2, 0 2, 0 0))
        2             LINESTRING (0 0, 2 2)
        3             LINESTRING (2 0, 0 2)
        4                       POINT (0 1)
        dtype: geometry

        We can also do intersection of each geometry and a single
        shapely geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> p = Point(3, 3)
        >>> s.shortest_line(p)
        0    LINESTRING (2 2, 3 3)
        1    LINESTRING (2 2, 3 3)
        2    LINESTRING (2 2, 3 3)
        3    LINESTRING (1 1, 3 3)
        4    LINESTRING (0 1, 3 3)
        dtype: geometry

        We can also check two GeoSeries against each other, row by row.
        The GeoSeries above have different indices than the one below. We can either
        align both GeoSeries based on index values and compare elements with the same
        index using ``align=True`` or ignore index and compare elements based on their
        matching order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)]),
        ...         Point(3, 1),
        ...         LineString([(1, 0), (2, 0)]),
        ...         Point(10, 15),
        ...         Point(0, 1),
        ...     ],
        ...     index=range(1, 6),
        ... )

        >>> s.shortest_line(s2, align=True)
        0                             None
        1    LINESTRING (0.5 0.5, 0.5 0.5)
        2            LINESTRING (2 2, 3 1)
        3            LINESTRING (2 0, 2 0)
        4          LINESTRING (0 1, 10 15)
        5                             None
        dtype: geometry
        >>>

        >>> s.shortest_line(s2, align=False)
        0    LINESTRING (0.5 0.5, 0.5 0.5)
        1            LINESTRING (2 2, 3 1)
        2        LINESTRING (0.5 0.5, 1 0)
        3          LINESTRING (0 2, 10 15)
        4            LINESTRING (0 1, 0 1)
        dtype: geometry
        """
        ...
    def snap(self, other: GeoSeries | Geometry, tolerance: float | ArrayLike, align: bool | None = None) -> GeoSeries:
        """
        Snaps an input geometry to reference geometry's vertices.

        Vertices of the first geometry are snapped to vertices of the second. geometry,
        returning a new geometry; the input geometries are not modified. The result
        geometry is the input geometry with the vertices snapped. If no snapping occurs
        then the input geometry is returned unchanged. The tolerance is used to control
        where snapping is performed.

        Where possible, this operation tries to avoid creating invalid geometries;
        however, it does not guarantee that output geometries will be valid. It is the
        responsibility of the caller to check for and handle invalid geometries.

        Because too much snapping can result in invalid geometries being created,
        heuristics are used to determine the number and location of snapped vertices
        that are likely safe to snap. These heuristics may omit some potential snaps
        that are otherwise within the tolerance.

        The operation works in a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center

        Parameters
        ----------
        other : GeoSeries or geometric object
            The Geoseries (elementwise) or geometric object to snap to.
        tolerance : float or array like
            Maximum distance between vertices that shall be snapped
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely import Polygon, LineString, Point
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(0.5, 2.5),
        ...         LineString([(0.1, 0.1), (0.49, 0.51), (1.01, 0.89)]),
        ...         Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ...     ],
        ... )
        >>> s
        0                               POINT (0.5 2.5)
        1    LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)
        2       POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))
        dtype: geometry

        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         Point(0, 2),
        ...         LineString([(0, 0), (0.5, 0.5), (1.0, 1.0)]),
        ...         Point(8, 10),
        ...     ],
        ...     index=range(1, 4),
        ... )
        >>> s2
        1                       POINT (0 2)
        2    LINESTRING (0 0, 0.5 0.5, 1 1)
        3                      POINT (8 10)
        dtype: geometry

        We can snap each geometry to a single shapely geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> s.snap(Point(0, 2), tolerance=1)
        0                                     POINT (0 2)
        1      LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)
        2    POLYGON ((0 0, 0 2, 0 10, 10 10, 10 0, 0 0))
        dtype: geometry

        We can also snap two GeoSeries to each other, row by row.
        The GeoSeries above have different indices. We can either align both GeoSeries
        based on index values and snap elements with the same index using
        ``align=True`` or ignore index and snap elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s.snap(s2, tolerance=1, align=True)
        0                                                 None
        1           LINESTRING (0.1 0.1, 0.49 0.51, 1.01 0.89)
        2    POLYGON ((0.5 0.5, 1 1, 0 10, 10 10, 10 0, 0.5...
        3                                                 None
        dtype: geometry

        >>> s.snap(s2, tolerance=1, align=False)
        0                                      POINT (0 2)
        1                   LINESTRING (0 0, 0.5 0.5, 1 1)
        2    POLYGON ((0 0, 0 10, 8 10, 10 10, 10 0, 0 0))
        dtype: geometry
        """
        ...
    def shared_paths(self, other: GeoSeries | Geometry, align: bool | None = None):
        """
        Returns the shared paths between two geometries.

        Geometries within the GeoSeries should be only (Multi)LineStrings or
        LinearRings. A GeoSeries of GeometryCollections is returned with two elements
        in each GeometryCollection. The first element is a MultiLineString containing
        shared paths with the same direction for both inputs. The second element is a
        MultiLineString containing shared paths with the opposite direction for the two
        inputs.

        You can extract individual geometries of the resulting GeometryCollection using
        the :meth:`GeoSeries.get_geometry` method.

        The operation works on a 1-to-1 row-wise manner:

        .. image:: ../../../_static/binary_op-01.svg
           :align: center

        Parameters
        ----------
        other : Geoseries or geometric object
            The Geoseries (elementwise) or geometric object to find the shared paths
            with. Has to contain only (Multi)LineString or LinearRing geometry types.
        align : bool | None (default None)
            If True, automatically aligns GeoSeries based on their indices.
            If False, the order of elements is preserved. None defaults to True.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import LineString, MultiLineString
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]),
        ...         LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)]),
        ...         MultiLineString([[(1, 0), (2, 0)], [(2, 1), (1, 1), (1, 0)]]),
        ...     ],
        ... )
        >>> s
        0             LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)
        1             LINESTRING (1 0, 2 0, 2 1, 1 1, 1 0)
        2    MULTILINESTRING ((1 0, 2 0), (2 1, 1 1, 1 0))
        dtype: geometry

        We can find the shared paths between each geometry and a single shapely
        geometry:

        .. image:: ../../../_static/binary_op-03.svg
           :align: center

        >>> l = LineString([(1, 1), (0, 1)])
        >>> s.shared_paths(l)
        0    GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1...
        1    GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MUL...
        2    GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MUL...
        dtype: geometry

        We can also check two GeoSeries against each other, row by row. The GeoSeries
        above have different indices than the one below. We can either align both
        GeoSeries based on index values and compare elements with the same index using
        ``align=True`` or ignore index and compare elements based on their matching
        order using ``align=False``:

        .. image:: ../../../_static/binary_op-02.svg

        >>> s2 = geopandas.GeoSeries(
        ...     [
        ...         LineString([(1, 1), (0, 1)]),
        ...         LineString([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]),
        ...         LineString([(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)]),
        ...     ],
        ...     index=[1, 2, 3]
        ... )

        >>> s.shared_paths(s2, align=True)
        0                                                 None
        1    GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MUL...
        2    GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MUL...
        3                                                 None
        dtype: geometry
        >>>

        >>> s.shared_paths(s2, align=False)
        0    GEOMETRYCOLLECTION (MULTILINESTRING ((1 1, 0 1...
        1    GEOMETRYCOLLECTION (MULTILINESTRING EMPTY, MUL...
        2    GEOMETRYCOLLECTION (MULTILINESTRING ((1 0, 2 0...
        dtype: geometry

        See Also
        --------
        GeoSeries.get_geometry
        """
        ...
    @property
    def bounds(self) -> pd.DataFrame:
        """
        Returns a ``DataFrame`` with columns ``minx``, ``miny``, ``maxx``,
        ``maxy`` values containing the bounds for each geometry.

        See ``GeoSeries.total_bounds`` for the limits of the entire series.

        Examples
        --------
        >>> from shapely.geometry import Point, Polygon, LineString
        >>> d = {'geometry': [Point(2, 1), Polygon([(0, 0), (1, 1), (1, 0)]),
        ... LineString([(0, 1), (1, 2)])]}
        >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326")
        >>> gdf.bounds
           minx  miny  maxx  maxy
        0   2.0   1.0   2.0   1.0
        1   0.0   0.0   1.0   1.0
        2   0.0   1.0   1.0   2.0

        You can assign the bounds to the ``GeoDataFrame`` as:

        >>> import pandas as pd
        >>> gdf = pd.concat([gdf, gdf.bounds], axis=1)
        >>> gdf
                                geometry  minx  miny  maxx  maxy
        0                     POINT (2 1)   2.0   1.0   2.0   1.0
        1  POLYGON ((0 0, 1 1, 1 0, 0 0))   0.0   0.0   1.0   1.0
        2           LINESTRING (0 1, 1 2)   0.0   1.0   1.0   2.0
        """
        ...
    @property
    def total_bounds(self) -> _Array1D[np.float64]:
        """
        Returns a tuple containing ``minx``, ``miny``, ``maxx``, ``maxy``
        values for the bounds of the series as a whole.

        See ``GeoSeries.bounds`` for the bounds of the geometries contained in
        the series.

        Examples
        --------
        >>> from shapely.geometry import Point, Polygon, LineString
        >>> d = {'geometry': [Point(3, -1), Polygon([(0, 0), (1, 1), (1, 0)]),
        ... LineString([(0, 1), (1, 2)])]}
        >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326")
        >>> gdf.total_bounds
        array([ 0., -1.,  3.,  2.])
        """
        ...
    @property
    def sindex(self) -> SpatialIndex:
        """
        Generate the spatial index

        Creates R-tree spatial index based on ``shapely.STRtree``.

        Note that the spatial index may not be fully
        initialized until the first use.

        Examples
        --------
        >>> from shapely.geometry import box
        >>> s = geopandas.GeoSeries(geopandas.points_from_xy(range(5), range(5)))
        >>> s
        0    POINT (0 0)
        1    POINT (1 1)
        2    POINT (2 2)
        3    POINT (3 3)
        4    POINT (4 4)
        dtype: geometry

        Query the spatial index with a single geometry based on the bounding box:

        >>> s.sindex.query(box(1, 1, 3, 3))
        array([1, 2, 3])

        Query the spatial index with a single geometry based on the predicate:

        >>> s.sindex.query(box(1, 1, 3, 3), predicate="contains")
        array([2])

        Query the spatial index with an array of geometries based on the bounding
        box:

        >>> s2 = geopandas.GeoSeries([box(1, 1, 3, 3), box(4, 4, 5, 5)])
        >>> s2
        0    POLYGON ((3 1, 3 3, 1 3, 1 1, 3 1))
        1    POLYGON ((5 4, 5 5, 4 5, 4 4, 5 4))
        dtype: geometry

        >>> s.sindex.query(s2)
        array([[0, 0, 0, 1],
               [1, 2, 3, 4]])

        Query the spatial index with an array of geometries based on the predicate:

        >>> s.sindex.query(s2, predicate="contains")
        array([[0],
               [2]])
        """
        ...
    @property
    def has_sindex(self) -> bool:
        """
        Check the existence of the spatial index without generating it.

        Use the `.sindex` attribute on a GeoDataFrame or GeoSeries
        to generate a spatial index if it does not yet exist,
        which may take considerable time based on the underlying index
        implementation.

        Note that the underlying spatial index may not be fully
        initialized until the first use.

        Examples
        --------

        >>> from shapely.geometry import Point
        >>> d = {'geometry': [Point(1, 2), Point(2, 1)]}
        >>> gdf = geopandas.GeoDataFrame(d)
        >>> gdf.has_sindex
        False
        >>> index = gdf.sindex
        >>> gdf.has_sindex
        True

        Returns
        -------
        bool
            `True` if the spatial index has been generated or
            `False` if not.
        """
        ...
    def buffer(
        self,
        distance: float | ArrayLike,
        resolution: int = 16,
        cap_style: Literal["round", "square", "flat"] = "round",
        join_style: Literal["round", "mitre", "bevel"] = "round",
        mitre_limit: float = 5.0,
        single_sided: bool = False,
        **kwargs,
    ) -> GeoSeries: ...
    def simplify(self, tolerance: float | ArrayLike, preserve_topology: bool = True) -> GeoSeries: ...
    def simplify_coverage(self, tolerance: float | ArrayLike, *, simplify_boundary: bool = True) -> GeoSeries: ...
    def relate(self, other: GeoSeries | Geometry, align: bool | None = None) -> pd.Series[str]: ...
    def relate_pattern(self, other: GeoSeries | Geometry, pattern: str, align: bool | None = None) -> pd.Series[bool]: ...
    def project(self, other: GeoSeries | Geometry, normalized: bool = False, align: bool | None = None) -> pd.Series[float]: ...
    def interpolate(self, distance: float | ArrayLike, normalized: bool = False) -> GeoSeries: ...
    def affine_transform(self, matrix: Collection[float]) -> GeoSeries: ...
    def translate(self, xoff: float = 0.0, yoff: float = 0.0, zoff: float = 0.0) -> GeoSeries: ...
    def rotate(self, angle: float, origin: _AffinityOrigin = "center", use_radians: bool = False) -> GeoSeries: ...
    def scale(
        self, xfact: float = 1.0, yfact: float = 1.0, zfact: float = 1.0, origin: _AffinityOrigin = "center"
    ) -> GeoSeries:
        """
        Returns a ``GeoSeries`` with scaled geometries.

        The geometries can be scaled by different factors along each
        dimension. Negative scale factors will mirror or reflect coordinates.

        See http://shapely.readthedocs.io/en/latest/manual.html#shapely.affinity.scale
        for details.

        Parameters
        ----------
        xfact, yfact, zfact : float, float, float
            Scaling factors for the x, y, and z dimensions respectively.
        origin : string, Point, or tuple
            The point of origin can be a keyword 'center' for the 2D bounding
            box center (default), 'centroid' for the geometry's 2D centroid, a
            Point object or a coordinate tuple (x, y, z).

        Examples
        --------
        >>> from shapely.geometry import Point, LineString, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(1, 1),
        ...         LineString([(1, -1), (1, 0)]),
        ...         Polygon([(3, -1), (4, 0), (3, 1)]),
        ...     ]
        ... )
        >>> s
        0                         POINT (1 1)
        1              LINESTRING (1 -1, 1 0)
        2    POLYGON ((3 -1, 4 0, 3 1, 3 -1))
        dtype: geometry

        >>> s.scale(2, 3)
        0                                 POINT (1 1)
        1                      LINESTRING (1 -2, 1 1)
        2    POLYGON ((2.5 -3, 4.5 0, 2.5 3, 2.5 -3))
        dtype: geometry

        >>> s.scale(2, 3, origin=(0, 0))
        0                         POINT (2 3)
        1              LINESTRING (2 -3, 2 0)
        2    POLYGON ((6 -3, 8 0, 6 3, 6 -3))
        dtype: geometry
        """
        ...
    def skew(
        self, xs: float = 0.0, ys: float = 0.0, origin: _AffinityOrigin = "center", use_radians: bool = False
    ) -> GeoSeries:
        """
        Returns a ``GeoSeries`` with skewed geometries.

        The geometries are sheared by angles along the x and y dimensions.

        See http://shapely.readthedocs.io/en/latest/manual.html#shapely.affinity.skew
        for details.

        Parameters
        ----------
        xs, ys : float, float
            The shear angle(s) for the x and y axes respectively. These can be
            specified in either degrees (default) or radians by setting
            use_radians=True.
        origin : string, Point, or tuple (x, y)
            The point of origin can be a keyword 'center' for the bounding box
            center (default), 'centroid' for the geometry's centroid, a Point
            object or a coordinate tuple (x, y).
        use_radians : boolean
            Whether to interpret the shear angle(s) as degrees or radians

        Examples
        --------
        >>> from shapely.geometry import Point, LineString, Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Point(1, 1),
        ...         LineString([(1, -1), (1, 0)]),
        ...         Polygon([(3, -1), (4, 0), (3, 1)]),
        ...     ]
        ... )
        >>> s
        0                         POINT (1 1)
        1              LINESTRING (1 -1, 1 0)
        2    POLYGON ((3 -1, 4 0, 3 1, 3 -1))
        dtype: geometry

        >>> s.skew(45, 30)
        0                                          POINT (1 1)
        1                           LINESTRING (0.5 -1, 1.5 0)
        2    POLYGON ((2 -1.28868, 4 0.28868, 4 0.71132, 2 ...
        dtype: geometry

        >>> s.skew(45, 30, origin=(0, 0))
        0                                    POINT (2 1.57735)
        1                   LINESTRING (0 -0.42265, 1 0.57735)
        2    POLYGON ((2 0.73205, 4 2.3094, 4 2.73205, 2 0....
        dtype: geometry
        """
        ...
    @property
    def cx(self) -> SupportsGetItem[tuple[SupportsIndex | slice, SupportsIndex | slice], Self]: ...
    def get_coordinates(
        self, include_z: bool = False, ignore_index: bool = False, index_parts: bool = False, *, include_m: bool = False
    ) -> pd.DataFrame: ...
    def hilbert_distance(
        self, total_bounds: tuple[float, float, float, float] | Iterable[float] | None = None, level: int = 16
    ) -> pd.Series[int]:
        """
        Calculate the distance along a Hilbert curve.

        The distances are calculated for the midpoints of the geometries in the
        GeoDataFrame, and using the total bounds of the GeoDataFrame.

        The Hilbert distance can be used to spatially sort GeoPandas
        objects, by mapping two dimensional geometries along the Hilbert curve.

        Parameters
        ----------
        total_bounds : 4-element array, optional
            The spatial extent in which the curve is constructed (used to
            rescale the geometry midpoints). By default, the total bounds
            of the full GeoDataFrame or GeoSeries will be computed. If known,
            you can pass the total bounds to avoid this extra computation.
        level : int (1 - 16), default 16
            Determines the precision of the curve (points on the curve will
            have coordinates in the range [0, 2^level - 1]).

        Returns
        -------
        Series
            Series containing distance along the curve for geometry
        """
        ...
    @overload
    def sample_points(
        self,
        size: int | ArrayLike,
        method: str = "uniform",
        seed: None = None,
        rng: int | ArrayLike | SeedSequence | BitGenerator | RandomGenerator | None = None,
        **kwargs,
    ) -> GeoSeries:
        """
        Sample points from each geometry.

        Generate a MultiPoint per each geometry containing points sampled from the
        geometry. You can either sample randomly from a uniform distribution or use an
        advanced sampling algorithm from the ``pointpats`` package.

        For polygons, this samples within the area of the polygon. For lines,
        this samples along the length of the linestring. For multi-part
        geometries, the weights of each part are selected according to their relevant
        attribute (area for Polygons, length for LineStrings), and then points are
        sampled from each part.

        Any other geometry type (e.g. Point, GeometryCollection) is ignored, and an
        empty MultiPoint geometry is returned.

        Parameters
        ----------
        size : int | array-like
            The size of the sample requested. Indicates the number of samples to draw
            from each geometry.  If an array of the same length as a GeoSeries is
            passed, it denotes the size of a sample per geometry.
        method : str, default "uniform"
            The sampling method. ``uniform`` samples uniformly at random from a
            geometry using ``numpy.random.uniform``. Other allowed strings
            (e.g. ``"cluster_poisson"``) denote sampling function name from the
            ``pointpats.random`` module (see
            http://pysal.org/pointpats/api.html#random-distributions). Pointpats methods
            are implemented for (Multi)Polygons only and will return an empty MultiPoint
            for other geometry types.
        rng : {None, int, array_like[ints], SeedSequence, BitGenerator, Generator}, optional
            A random generator or seed to initialize the numpy BitGenerator. If None, then fresh,
            unpredictable entropy will be pulled from the OS.
        **kwargs : dict
            Options for the pointpats sampling algorithms.

        Returns
        -------
        GeoSeries
            Points sampled within (or along) each geometry.

        Examples
        --------
        >>> from shapely.geometry import Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(1, -1), (1, 0), (0, 0)]),
        ...         Polygon([(3, -1), (4, 0), (3, 1)]),
        ...     ]
        ... )

        >>> s.sample_points(size=10)  # doctest: +SKIP
        0    MULTIPOINT ((0.1045 -0.10294), (0.35249 -0.264...
        1    MULTIPOINT ((3.03261 -0.43069), (3.10068 0.114...
        Name: sampled_points, dtype: geometry
        """
        ...
    @overload
    @deprecated("Parameter `seed` is deprecated. Use `rng` instead.")
    def sample_points(
        self,
        size: int | ArrayLike,
        method: str = "uniform",
        *,
        seed: int | ArrayLike | SeedSequence | BitGenerator | RandomGenerator,
        rng: int | ArrayLike | SeedSequence | BitGenerator | RandomGenerator | None = None,
        **kwargs,
    ) -> GeoSeries:
        """
        Sample points from each geometry.

        Generate a MultiPoint per each geometry containing points sampled from the
        geometry. You can either sample randomly from a uniform distribution or use an
        advanced sampling algorithm from the ``pointpats`` package.

        For polygons, this samples within the area of the polygon. For lines,
        this samples along the length of the linestring. For multi-part
        geometries, the weights of each part are selected according to their relevant
        attribute (area for Polygons, length for LineStrings), and then points are
        sampled from each part.

        Any other geometry type (e.g. Point, GeometryCollection) is ignored, and an
        empty MultiPoint geometry is returned.

        Parameters
        ----------
        size : int | array-like
            The size of the sample requested. Indicates the number of samples to draw
            from each geometry.  If an array of the same length as a GeoSeries is
            passed, it denotes the size of a sample per geometry.
        method : str, default "uniform"
            The sampling method. ``uniform`` samples uniformly at random from a
            geometry using ``numpy.random.uniform``. Other allowed strings
            (e.g. ``"cluster_poisson"``) denote sampling function name from the
            ``pointpats.random`` module (see
            http://pysal.org/pointpats/api.html#random-distributions). Pointpats methods
            are implemented for (Multi)Polygons only and will return an empty MultiPoint
            for other geometry types.
        rng : {None, int, array_like[ints], SeedSequence, BitGenerator, Generator}, optional
            A random generator or seed to initialize the numpy BitGenerator. If None, then fresh,
            unpredictable entropy will be pulled from the OS.
        **kwargs : dict
            Options for the pointpats sampling algorithms.

        Returns
        -------
        GeoSeries
            Points sampled within (or along) each geometry.

        Examples
        --------
        >>> from shapely.geometry import Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(1, -1), (1, 0), (0, 0)]),
        ...         Polygon([(3, -1), (4, 0), (3, 1)]),
        ...     ]
        ... )

        >>> s.sample_points(size=10)  # doctest: +SKIP
        0    MULTIPOINT ((0.1045 -0.10294), (0.35249 -0.264...
        1    MULTIPOINT ((3.03261 -0.43069), (3.10068 0.114...
        Name: sampled_points, dtype: geometry
        """
        ...
    def build_area(self, node: bool = True) -> GeoSeries:
        """
        Creates an areal geometry formed by the constituent linework.

        Builds areas from the GeoSeries that contain linework which represents the edges
        of a planar graph. Any geometry type may be provided as input; only the
        constituent lines and rings will be used to create the output polygons. All
        geometries within the GeoSeries are considered together and the resulting
        polygons therefore do not map 1:1 to input geometries.

        This function converts inner rings into holes. To turn inner rings into polygons
        as well, use polygonize.

        Unless you know that the input GeoSeries represents a planar graph with a clean
        topology (e.g. there is a node on both lines where they intersect), it is
        recommended to use ``node=True`` which performs noding prior to building areal
        geometry. Using ``node=False`` will provide performance benefits but may result
        in incorrect polygons if the input is not of the proper topology.

        If the input linework crosses, this function may produce invalid polygons. Use
        :meth:`GeoSeries.make_valid` to ensure valid geometries.

        Parameters
        ----------
        node : bool, default True
            Perform noding prior to building the areas, by default True.

        Returns
        -------
        GeoSeries
            GeoSeries with polygons

        Examples
        --------
        >>> from shapely.geometry import LineString, Polygon
        >>> s = geopandas.GeoSeries([
        ...     LineString([(18, 4), (4, 2), (2, 9)]),
        ...     LineString([(18, 4), (16, 16)]),
        ...     LineString([(16, 16), (8, 19), (8, 12), (2, 9)]),
        ...     LineString([(8, 6), (12, 13), (15, 8)]),
        ...     LineString([(8, 6), (15, 8)]),
        ...     LineString([(0, 0), (0, 3), (3, 3), (3, 0), (0, 0)]),
        ...     Polygon([(1, 1), (2, 2), (1, 2), (1, 1)]),
        ... ])
        >>> s.build_area()
        0    POLYGON ((0 3, 3 3, 3 0, 0 0, 0 3), (1 1, 2 2,...
        1    POLYGON ((4 2, 2 9, 8 12, 8 19, 16 16, 18 4, 4...
        Name: polygons, dtype: geometry
        """
        ...
    @overload
    def polygonize(self, node: bool = True, full: Literal[False] = False) -> GeoSeries:
        """
        Creates polygons formed from the linework of a GeoSeries.

        Polygonizes the GeoSeries that contain linework which represents the
        edges of a planar graph. Any geometry type may be provided as input; only the
        constituent lines and rings will be used to create the output polygons.

        Lines or rings that when combined do not completely close a polygon will be
        ignored. Duplicate segments are ignored.

        Unless you know that the input GeoSeries represents a planar graph with a clean
        topology (e.g. there is a node on both lines where they intersect), it is
        recommended to use ``node=True`` which performs noding prior to polygonization.
        Using ``node=False`` will provide performance benefits but may result in
        incorrect polygons if the input is not of the proper topology.

        When ``full=True``, the return value is a 4-tuple containing output polygons,
        along with lines which could not be converted to polygons. The return value
        consists of 4 elements or varying lenghts:

        - GeoSeries of the valid polygons (same as with ``full=False``)
        - GeoSeries of cut edges: edges connected on both ends but not part of
          polygonal output
        - GeoSeries of dangles: edges connected on one end but not part of polygonal
          output
        - GeoSeries of invalid rings: polygons that are formed but are not valid
          (bowties, etc)

        Parameters
        ----------
        node : bool, default True
            Perform noding prior to polygonization, by default True.
        full : bool, default False
            Return the full output composed of a tuple of GeoSeries, by default False.

        Returns
        -------
        GeoSeries | tuple(GeoSeries, GeoSeries, GeoSeries, GeoSeries)
            GeoSeries with the polygons or a tuple of four GeoSeries as
            ``(polygons, cuts, dangles, invalid)``

        Examples
        --------
        >>> from shapely.geometry import LineString
        >>> s = geopandas.GeoSeries([
        ...     LineString([(0, 0), (1, 1)]),
        ...     LineString([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
        ...     LineString([(0.5, 0.2), (0.5, 0.8)]),
        ... ])
        >>> s.polygonize()
        0        POLYGON ((0 0, 0.5 0.5, 1 1, 1 0, 0 0))
        1    POLYGON ((0.5 0.5, 0 0, 0 1, 1 1, 0.5 0.5))
        Name: polygons, dtype: geometry

        >>> polygons, cuts, dangles, invalid = s.polygonize(full=True)
        """
        ...
    @overload
    def polygonize(self, node: bool = True, *, full: Literal[True]) -> tuple[GeoSeries, GeoSeries, GeoSeries, GeoSeries]:
        """
        Creates polygons formed from the linework of a GeoSeries.

        Polygonizes the GeoSeries that contain linework which represents the
        edges of a planar graph. Any geometry type may be provided as input; only the
        constituent lines and rings will be used to create the output polygons.

        Lines or rings that when combined do not completely close a polygon will be
        ignored. Duplicate segments are ignored.

        Unless you know that the input GeoSeries represents a planar graph with a clean
        topology (e.g. there is a node on both lines where they intersect), it is
        recommended to use ``node=True`` which performs noding prior to polygonization.
        Using ``node=False`` will provide performance benefits but may result in
        incorrect polygons if the input is not of the proper topology.

        When ``full=True``, the return value is a 4-tuple containing output polygons,
        along with lines which could not be converted to polygons. The return value
        consists of 4 elements or varying lenghts:

        - GeoSeries of the valid polygons (same as with ``full=False``)
        - GeoSeries of cut edges: edges connected on both ends but not part of
          polygonal output
        - GeoSeries of dangles: edges connected on one end but not part of polygonal
          output
        - GeoSeries of invalid rings: polygons that are formed but are not valid
          (bowties, etc)

        Parameters
        ----------
        node : bool, default True
            Perform noding prior to polygonization, by default True.
        full : bool, default False
            Return the full output composed of a tuple of GeoSeries, by default False.

        Returns
        -------
        GeoSeries | tuple(GeoSeries, GeoSeries, GeoSeries, GeoSeries)
            GeoSeries with the polygons or a tuple of four GeoSeries as
            ``(polygons, cuts, dangles, invalid)``

        Examples
        --------
        >>> from shapely.geometry import LineString
        >>> s = geopandas.GeoSeries([
        ...     LineString([(0, 0), (1, 1)]),
        ...     LineString([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
        ...     LineString([(0.5, 0.2), (0.5, 0.8)]),
        ... ])
        >>> s.polygonize()
        0        POLYGON ((0 0, 0.5 0.5, 1 1, 1 0, 0 0))
        1    POLYGON ((0.5 0.5, 0 0, 0 1, 1 1, 0.5 0.5))
        Name: polygons, dtype: geometry

        >>> polygons, cuts, dangles, invalid = s.polygonize(full=True)
        """
        ...
    @overload
    def polygonize(self, node: bool, full: Literal[True]) -> tuple[GeoSeries, GeoSeries, GeoSeries, GeoSeries]:
        """
        Creates polygons formed from the linework of a GeoSeries.

        Polygonizes the GeoSeries that contain linework which represents the
        edges of a planar graph. Any geometry type may be provided as input; only the
        constituent lines and rings will be used to create the output polygons.

        Lines or rings that when combined do not completely close a polygon will be
        ignored. Duplicate segments are ignored.

        Unless you know that the input GeoSeries represents a planar graph with a clean
        topology (e.g. there is a node on both lines where they intersect), it is
        recommended to use ``node=True`` which performs noding prior to polygonization.
        Using ``node=False`` will provide performance benefits but may result in
        incorrect polygons if the input is not of the proper topology.

        When ``full=True``, the return value is a 4-tuple containing output polygons,
        along with lines which could not be converted to polygons. The return value
        consists of 4 elements or varying lenghts:

        - GeoSeries of the valid polygons (same as with ``full=False``)
        - GeoSeries of cut edges: edges connected on both ends but not part of
          polygonal output
        - GeoSeries of dangles: edges connected on one end but not part of polygonal
          output
        - GeoSeries of invalid rings: polygons that are formed but are not valid
          (bowties, etc)

        Parameters
        ----------
        node : bool, default True
            Perform noding prior to polygonization, by default True.
        full : bool, default False
            Return the full output composed of a tuple of GeoSeries, by default False.

        Returns
        -------
        GeoSeries | tuple(GeoSeries, GeoSeries, GeoSeries, GeoSeries)
            GeoSeries with the polygons or a tuple of four GeoSeries as
            ``(polygons, cuts, dangles, invalid)``

        Examples
        --------
        >>> from shapely.geometry import LineString
        >>> s = geopandas.GeoSeries([
        ...     LineString([(0, 0), (1, 1)]),
        ...     LineString([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
        ...     LineString([(0.5, 0.2), (0.5, 0.8)]),
        ... ])
        >>> s.polygonize()
        0        POLYGON ((0 0, 0.5 0.5, 1 1, 1 0, 0 0))
        1    POLYGON ((0.5 0.5, 0 0, 0 1, 1 1, 0.5 0.5))
        Name: polygons, dtype: geometry

        >>> polygons, cuts, dangles, invalid = s.polygonize(full=True)
        """
        ...
