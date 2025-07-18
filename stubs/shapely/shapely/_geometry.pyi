from enum import IntEnum
from typing import Any, Literal, SupportsIndex, overload
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from ._enum import ParamEnum
from ._typing import ArrayLike, ArrayLikeSeq, GeoArray, OptGeoArrayLike, OptGeoArrayLikeSeq, OptGeoT
from .geometry import LinearRing, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
from .geometry.base import BaseGeometry, BaseMultipartGeometry
from .lib import Geometry

__all__ = [
    "GeometryType",
    "force_2d",
    "force_3d",
    "get_coordinate_dimension",
    "get_dimensions",
    "get_exterior_ring",
    "get_geometry",
    "get_interior_ring",
    "get_m",
    "get_num_coordinates",
    "get_num_geometries",
    "get_num_interior_rings",
    "get_num_points",
    "get_parts",
    "get_point",
    "get_precision",
    "get_rings",
    "get_srid",
    "get_type_id",
    "get_x",
    "get_y",
    "get_z",
    "set_precision",
    "set_srid",
]

_PrecisionMode: TypeAlias = Literal["valid_output", "pointwise", "keep_collapsed", 0, 1, 2]

class GeometryType(IntEnum):
    """The enumeration of GEOS geometry types."""
    MISSING = -1
    POINT = 0
    LINESTRING = 1
    LINEARRING = 2
    POLYGON = 3
    MULTIPOINT = 4
    MULTILINESTRING = 5
    MULTIPOLYGON = 6
    GEOMETRYCOLLECTION = 7

@overload
def get_type_id(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return the type ID of a geometry.

    Possible values are:

    - None (missing) is -1
    - POINT is 0
    - LINESTRING is 1
    - LINEARRING is 2
    - POLYGON is 3
    - MULTIPOINT is 4
    - MULTILINESTRING is 5
    - MULTIPOLYGON is 6
    - GEOMETRYCOLLECTION is 7

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the type ID of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    GeometryType

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.get_type_id(LineString([(0, 0), (1, 1), (2, 2), (3, 3)]))
    1
    >>> shapely.get_type_id([Point(1, 2), Point(2, 3)]).tolist()
    [0, 0]
    """
    ...
@overload
def get_type_id(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return the type ID of a geometry.

    Possible values are:

    - None (missing) is -1
    - POINT is 0
    - LINESTRING is 1
    - LINEARRING is 2
    - POLYGON is 3
    - MULTIPOINT is 4
    - MULTILINESTRING is 5
    - MULTIPOLYGON is 6
    - GEOMETRYCOLLECTION is 7

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the type ID of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    GeometryType

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.get_type_id(LineString([(0, 0), (1, 1), (2, 2), (3, 3)]))
    1
    >>> shapely.get_type_id([Point(1, 2), Point(2, 3)]).tolist()
    [0, 0]
    """
    ...
@overload
def get_dimensions(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return the inherent dimensionality of a geometry.

    The inherent dimension is 0 for points, 1 for linestrings and linearrings,
    and 2 for polygons. For geometrycollections it is the max of the containing
    elements. Empty collections and None values return -1.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the dimensionality of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import GeometryCollection, Point, Polygon
    >>> point = Point(0, 0)
    >>> shapely.get_dimensions(point)
    0
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_dimensions(polygon)
    2
    >>> shapely.get_dimensions(GeometryCollection([point, polygon]))
    2
    >>> shapely.get_dimensions(GeometryCollection([]))
    -1
    >>> shapely.get_dimensions(None)
    -1
    """
    ...
@overload
def get_dimensions(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return the inherent dimensionality of a geometry.

    The inherent dimension is 0 for points, 1 for linestrings and linearrings,
    and 2 for polygons. For geometrycollections it is the max of the containing
    elements. Empty collections and None values return -1.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the dimensionality of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import GeometryCollection, Point, Polygon
    >>> point = Point(0, 0)
    >>> shapely.get_dimensions(point)
    0
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_dimensions(polygon)
    2
    >>> shapely.get_dimensions(GeometryCollection([point, polygon]))
    2
    >>> shapely.get_dimensions(GeometryCollection([]))
    -1
    >>> shapely.get_dimensions(None)
    -1
    """
    ...
@overload
def get_coordinate_dimension(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return the dimensionality of the coordinates in a geometry (2, 3 or 4).

    The return value can be one of the following:

    * Return 2 for geometries with XY coordinate types,
    * Return 3 for XYZ or XYM coordinate types
      (distinguished by :meth:`has_z` or :meth:`has_m`),
    * Return 4 for XYZM coordinate types,
    * Return -1 for missing geometries (``None`` values).

    Note that with GEOS < 3.12, if the first Z coordinate equals ``nan``, this function
    will return ``2``. Geometries with M coordinates are supported with GEOS >= 3.12.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the coordinate dimension of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> shapely.get_coordinate_dimension(Point(0, 0))
    2
    >>> shapely.get_coordinate_dimension(Point(0, 0, 1))
    3
    >>> shapely.get_coordinate_dimension(None)
    -1
    """
    ...
@overload
def get_coordinate_dimension(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return the dimensionality of the coordinates in a geometry (2, 3 or 4).

    The return value can be one of the following:

    * Return 2 for geometries with XY coordinate types,
    * Return 3 for XYZ or XYM coordinate types
      (distinguished by :meth:`has_z` or :meth:`has_m`),
    * Return 4 for XYZM coordinate types,
    * Return -1 for missing geometries (``None`` values).

    Note that with GEOS < 3.12, if the first Z coordinate equals ``nan``, this function
    will return ``2``. Geometries with M coordinates are supported with GEOS >= 3.12.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the coordinate dimension of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> shapely.get_coordinate_dimension(Point(0, 0))
    2
    >>> shapely.get_coordinate_dimension(Point(0, 0, 1))
    3
    >>> shapely.get_coordinate_dimension(None)
    -1
    """
    ...
@overload
def get_num_coordinates(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return the total number of coordinates in a geometry.

    Returns 0 for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of coordinates of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import GeometryCollection, LineString, Point
    >>> point = Point(0, 0)
    >>> shapely.get_num_coordinates(point)
    1
    >>> shapely.get_num_coordinates(Point(0, 0, 0))
    1
    >>> line = LineString([(0, 0), (1, 1)])
    >>> shapely.get_num_coordinates(line)
    2
    >>> shapely.get_num_coordinates(GeometryCollection([point, line]))
    3
    >>> shapely.get_num_coordinates(None)
    0
    """
    ...
@overload
def get_num_coordinates(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return the total number of coordinates in a geometry.

    Returns 0 for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of coordinates of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import GeometryCollection, LineString, Point
    >>> point = Point(0, 0)
    >>> shapely.get_num_coordinates(point)
    1
    >>> shapely.get_num_coordinates(Point(0, 0, 0))
    1
    >>> line = LineString([(0, 0), (1, 1)])
    >>> shapely.get_num_coordinates(line)
    2
    >>> shapely.get_num_coordinates(GeometryCollection([point, line]))
    3
    >>> shapely.get_num_coordinates(None)
    0
    """
    ...
@overload
def get_srid(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return the SRID of a geometry.

    Returns -1 for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the SRID of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    set_srid

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(0, 0)
    >>> shapely.get_srid(point)
    0
    >>> with_srid = shapely.set_srid(point, 4326)
    >>> shapely.get_srid(with_srid)
    4326
    """
    ...
@overload
def get_srid(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return the SRID of a geometry.

    Returns -1 for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the SRID of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    set_srid

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(0, 0)
    >>> shapely.get_srid(point)
    0
    >>> with_srid = shapely.set_srid(point, 4326)
    >>> shapely.get_srid(with_srid)
    4326
    """
    ...
@overload
def set_srid(geometry: OptGeoT, srid: SupportsIndex, **kwargs) -> OptGeoT:
    """
    Return a geometry with its SRID set.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to set the SRID of.
    srid : int
        The SRID to set on the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_srid

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(0, 0)
    >>> shapely.get_srid(point)
    0
    >>> with_srid = shapely.set_srid(point, 4326)
    >>> shapely.get_srid(with_srid)
    4326
    """
    ...
@overload
def set_srid(geometry: OptGeoArrayLikeSeq, srid: ArrayLike[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return a geometry with its SRID set.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to set the SRID of.
    srid : int
        The SRID to set on the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_srid

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(0, 0)
    >>> shapely.get_srid(point)
    0
    >>> with_srid = shapely.set_srid(point, 4326)
    >>> shapely.get_srid(with_srid)
    4326
    """
    ...
@overload
def set_srid(geometry: OptGeoArrayLike, srid: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return a geometry with its SRID set.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to set the SRID of.
    srid : int
        The SRID to set on the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_srid

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(0, 0)
    >>> shapely.get_srid(point)
    0
    >>> with_srid = shapely.set_srid(point, 4326)
    >>> shapely.get_srid(with_srid)
    4326
    """
    ...
@overload
def get_x(point: Geometry | None, **kwargs) -> np.float64:
    """
    Return the x-coordinate of a point.

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries will result in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_y, get_z, get_m

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_x(Point(1, 2))
    1.0
    >>> shapely.get_x(MultiPoint([(1, 1), (1, 2)]))
    nan
    """
    ...
@overload
def get_x(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Return the x-coordinate of a point.

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries will result in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_y, get_z, get_m

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_x(Point(1, 2))
    1.0
    >>> shapely.get_x(MultiPoint([(1, 1), (1, 2)]))
    nan
    """
    ...
@overload
def get_y(point: Geometry | None, **kwargs) -> np.float64:
    """
    Return the y-coordinate of a point.

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries will result in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_x, get_z, get_m

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_y(Point(1, 2))
    2.0
    >>> shapely.get_y(MultiPoint([(1, 1), (1, 2)]))
    nan
    """
    ...
@overload
def get_y(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Return the y-coordinate of a point.

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries will result in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_x, get_z, get_m

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_y(Point(1, 2))
    2.0
    >>> shapely.get_y(MultiPoint([(1, 1), (1, 2)]))
    nan
    """
    ...
@overload
def get_z(point: Geometry | None, **kwargs) -> np.float64:
    """
    Return the z-coordinate of a point.

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries or geometries without Z dimension will result
        in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_x, get_y, get_m

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_z(Point(1, 2, 3))
    3.0
    >>> shapely.get_z(Point(1, 2))
    nan
    >>> shapely.get_z(MultiPoint([(1, 1, 1), (2, 2, 2)]))
    nan
    """
    ...
@overload
def get_z(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Return the z-coordinate of a point.

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries or geometries without Z dimension will result
        in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_x, get_y, get_m

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_z(Point(1, 2, 3))
    3.0
    >>> shapely.get_z(Point(1, 2))
    nan
    >>> shapely.get_z(MultiPoint([(1, 1, 1), (2, 2, 2)]))
    nan
    """
    ...
@overload
def get_m(point: Geometry | None, **kwargs) -> np.float64:
    """
    Return the m-coordinate of a point.

    .. versionadded:: 2.1.0

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries or geometries without M dimension will result
        in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_x, get_y, get_z

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, from_wkt
    >>> shapely.get_m(from_wkt("POINT ZM (1 2 3 4)"))
    4.0
    >>> shapely.get_m(from_wkt("POINT M (1 2 4)"))
    4.0
    >>> shapely.get_m(Point(1, 2, 3))
    nan
    >>> shapely.get_m(from_wkt("MULTIPOINT M ((1 1 1), (2 2 2))"))
    nan
    """
    ...
@overload
def get_m(point: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Return the m-coordinate of a point.

    .. versionadded:: 2.1.0

    Parameters
    ----------
    point : Geometry or array_like
        Non-point geometries or geometries without M dimension will result
        in NaN being returned.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_x, get_y, get_z

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, from_wkt
    >>> shapely.get_m(from_wkt("POINT ZM (1 2 3 4)"))
    4.0
    >>> shapely.get_m(from_wkt("POINT M (1 2 4)"))
    4.0
    >>> shapely.get_m(Point(1, 2, 3))
    nan
    >>> shapely.get_m(from_wkt("MULTIPOINT M ((1 1 1), (2 2 2))"))
    nan
    """
    ...
@overload
def get_point(geometry: LineString, index: SupportsIndex, **kwargs) -> Point | Any:
    """
    Return the nth point of a linestring or linearring.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the point of.
    index : int or array_like
        Negative values count from the end of the linestring backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points

    Examples
    --------
    >>> import shapely
    >>> from shapely import LinearRing, LineString, MultiPoint, Point
    >>> line = LineString([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_point(line, 1)
    <POINT (1 1)>
    >>> shapely.get_point(line, -2)
    <POINT (2 2)>
    >>> shapely.get_point(line, [0, 3]).tolist()
    [<POINT (0 0)>, <POINT (3 3)>]

    The function works the same for LinearRing input:

    >>> shapely.get_point(LinearRing([(0, 0), (1, 1), (2, 2), (0, 0)]), 1)
    <POINT (1 1)>

    For non-linear geometries it returns None:

    >>> shapely.get_point(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]), 1) is None
    True
    >>> shapely.get_point(Point(1, 1), 0) is None
    True
    """
    ...
@overload
def get_point(geometry: Point | Polygon | BaseMultipartGeometry | None, index: SupportsIndex, **kwargs) -> None:
    """
    Return the nth point of a linestring or linearring.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the point of.
    index : int or array_like
        Negative values count from the end of the linestring backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points

    Examples
    --------
    >>> import shapely
    >>> from shapely import LinearRing, LineString, MultiPoint, Point
    >>> line = LineString([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_point(line, 1)
    <POINT (1 1)>
    >>> shapely.get_point(line, -2)
    <POINT (2 2)>
    >>> shapely.get_point(line, [0, 3]).tolist()
    [<POINT (0 0)>, <POINT (3 3)>]

    The function works the same for LinearRing input:

    >>> shapely.get_point(LinearRing([(0, 0), (1, 1), (2, 2), (0, 0)]), 1)
    <POINT (1 1)>

    For non-linear geometries it returns None:

    >>> shapely.get_point(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]), 1) is None
    True
    >>> shapely.get_point(Point(1, 1), 0) is None
    True
    """
    ...
@overload
def get_point(geometry: Geometry, index: SupportsIndex, **kwargs) -> Point | None:
    """
    Return the nth point of a linestring or linearring.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the point of.
    index : int or array_like
        Negative values count from the end of the linestring backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points

    Examples
    --------
    >>> import shapely
    >>> from shapely import LinearRing, LineString, MultiPoint, Point
    >>> line = LineString([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_point(line, 1)
    <POINT (1 1)>
    >>> shapely.get_point(line, -2)
    <POINT (2 2)>
    >>> shapely.get_point(line, [0, 3]).tolist()
    [<POINT (0 0)>, <POINT (3 3)>]

    The function works the same for LinearRing input:

    >>> shapely.get_point(LinearRing([(0, 0), (1, 1), (2, 2), (0, 0)]), 1)
    <POINT (1 1)>

    For non-linear geometries it returns None:

    >>> shapely.get_point(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]), 1) is None
    True
    >>> shapely.get_point(Point(1, 1), 0) is None
    True
    """
    ...
@overload
def get_point(geometry: OptGeoArrayLikeSeq, index: ArrayLike[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return the nth point of a linestring or linearring.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the point of.
    index : int or array_like
        Negative values count from the end of the linestring backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points

    Examples
    --------
    >>> import shapely
    >>> from shapely import LinearRing, LineString, MultiPoint, Point
    >>> line = LineString([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_point(line, 1)
    <POINT (1 1)>
    >>> shapely.get_point(line, -2)
    <POINT (2 2)>
    >>> shapely.get_point(line, [0, 3]).tolist()
    [<POINT (0 0)>, <POINT (3 3)>]

    The function works the same for LinearRing input:

    >>> shapely.get_point(LinearRing([(0, 0), (1, 1), (2, 2), (0, 0)]), 1)
    <POINT (1 1)>

    For non-linear geometries it returns None:

    >>> shapely.get_point(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]), 1) is None
    True
    >>> shapely.get_point(Point(1, 1), 0) is None
    True
    """
    ...
@overload
def get_point(geometry: OptGeoArrayLike, index: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return the nth point of a linestring or linearring.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the point of.
    index : int or array_like
        Negative values count from the end of the linestring backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points

    Examples
    --------
    >>> import shapely
    >>> from shapely import LinearRing, LineString, MultiPoint, Point
    >>> line = LineString([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_point(line, 1)
    <POINT (1 1)>
    >>> shapely.get_point(line, -2)
    <POINT (2 2)>
    >>> shapely.get_point(line, [0, 3]).tolist()
    [<POINT (0 0)>, <POINT (3 3)>]

    The function works the same for LinearRing input:

    >>> shapely.get_point(LinearRing([(0, 0), (1, 1), (2, 2), (0, 0)]), 1)
    <POINT (1 1)>

    For non-linear geometries it returns None:

    >>> shapely.get_point(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]), 1) is None
    True
    >>> shapely.get_point(Point(1, 1), 0) is None
    True
    """
    ...
@overload
def get_num_points(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return the number of points in a linestring or linearring.

    Returns 0 for not-a-geometry values. The number of points in geometries
    other than linestring or linearring equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of points of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_point
    get_num_geometries

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, MultiPoint
    >>> shapely.get_num_points(LineString([(0, 0), (1, 1), (2, 2), (3, 3)]))
    4
    >>> shapely.get_num_points(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]))
    0
    >>> shapely.get_num_points(None)
    0
    """
    ...
@overload
def get_num_points(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return the number of points in a linestring or linearring.

    Returns 0 for not-a-geometry values. The number of points in geometries
    other than linestring or linearring equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of points of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_point
    get_num_geometries

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, MultiPoint
    >>> shapely.get_num_points(LineString([(0, 0), (1, 1), (2, 2), (3, 3)]))
    4
    >>> shapely.get_num_points(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]))
    0
    >>> shapely.get_num_points(None)
    0
    """
    ...
@overload
def get_exterior_ring(geometry: Polygon, **kwargs) -> LinearRing:
    """
    Return the exterior ring of a polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the exterior ring of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_interior_ring

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> shapely.get_exterior_ring(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>
    >>> shapely.get_exterior_ring(Point(1, 1)) is None
    True
    """
    ...
@overload
def get_exterior_ring(geometry: Point | LineString | BaseMultipartGeometry | None, **kwargs) -> None:
    """
    Return the exterior ring of a polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the exterior ring of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_interior_ring

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> shapely.get_exterior_ring(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>
    >>> shapely.get_exterior_ring(Point(1, 1)) is None
    True
    """
    ...
@overload
def get_exterior_ring(geometry: Geometry, **kwargs) -> LinearRing | None:
    """
    Return the exterior ring of a polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the exterior ring of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_interior_ring

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> shapely.get_exterior_ring(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>
    >>> shapely.get_exterior_ring(Point(1, 1)) is None
    True
    """
    ...
@overload
def get_exterior_ring(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Return the exterior ring of a polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the exterior ring of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_interior_ring

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> shapely.get_exterior_ring(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>
    >>> shapely.get_exterior_ring(Point(1, 1)) is None
    True
    """
    ...
@overload
def get_interior_ring(geometry: Polygon, index: SupportsIndex, **kwargs) -> LinearRing | Any:
    """
    Return the nth interior ring of a polygon.

    The number of interior rings in non-polygons equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the interior ring of.
    index : int or array_like
        Negative values count from the end of the interior rings backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_num_interior_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_interior_ring(polygon_with_hole, 0)
    <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>
    >>> shapely.get_interior_ring(polygon_with_hole, 1) is None
    True
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_interior_ring(polygon, 0) is None
    True
    >>> shapely.get_interior_ring(Point(0, 0), 0) is None
    True
    """
    ...
@overload
def get_interior_ring(geometry: Point | LineString | BaseMultipartGeometry | None, index: SupportsIndex, **kwargs) -> None:
    """
    Return the nth interior ring of a polygon.

    The number of interior rings in non-polygons equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the interior ring of.
    index : int or array_like
        Negative values count from the end of the interior rings backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_num_interior_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_interior_ring(polygon_with_hole, 0)
    <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>
    >>> shapely.get_interior_ring(polygon_with_hole, 1) is None
    True
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_interior_ring(polygon, 0) is None
    True
    >>> shapely.get_interior_ring(Point(0, 0), 0) is None
    True
    """
    ...
@overload
def get_interior_ring(geometry: Geometry, index: SupportsIndex, **kwargs) -> LinearRing | None:
    """
    Return the nth interior ring of a polygon.

    The number of interior rings in non-polygons equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the interior ring of.
    index : int or array_like
        Negative values count from the end of the interior rings backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_num_interior_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_interior_ring(polygon_with_hole, 0)
    <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>
    >>> shapely.get_interior_ring(polygon_with_hole, 1) is None
    True
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_interior_ring(polygon, 0) is None
    True
    >>> shapely.get_interior_ring(Point(0, 0), 0) is None
    True
    """
    ...
@overload
def get_interior_ring(geometry: OptGeoArrayLikeSeq, index: ArrayLike[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return the nth interior ring of a polygon.

    The number of interior rings in non-polygons equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the interior ring of.
    index : int or array_like
        Negative values count from the end of the interior rings backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_num_interior_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_interior_ring(polygon_with_hole, 0)
    <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>
    >>> shapely.get_interior_ring(polygon_with_hole, 1) is None
    True
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_interior_ring(polygon, 0) is None
    True
    >>> shapely.get_interior_ring(Point(0, 0), 0) is None
    True
    """
    ...
@overload
def get_interior_ring(geometry: OptGeoArrayLike, index: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return the nth interior ring of a polygon.

    The number of interior rings in non-polygons equals zero.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the interior ring of.
    index : int or array_like
        Negative values count from the end of the interior rings backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_num_interior_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_interior_ring(polygon_with_hole, 0)
    <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>
    >>> shapely.get_interior_ring(polygon_with_hole, 1) is None
    True
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_interior_ring(polygon, 0) is None
    True
    >>> shapely.get_interior_ring(Point(0, 0), 0) is None
    True
    """
    ...
@overload
def get_num_interior_rings(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return number of internal rings in a polygon.

    Returns 0 for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of interior rings of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_interior_ring

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_num_interior_rings(polygon)
    0
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_num_interior_rings(polygon_with_hole)
    1
    >>> shapely.get_num_interior_rings(Point(0, 0))
    0
    >>> shapely.get_num_interior_rings(None)
    0
    """
    ...
@overload
def get_num_interior_rings(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return number of internal rings in a polygon.

    Returns 0 for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of interior rings of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_exterior_ring
    get_interior_ring

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, Polygon
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> shapely.get_num_interior_rings(polygon)
    0
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_num_interior_rings(polygon_with_hole)
    1
    >>> shapely.get_num_interior_rings(Point(0, 0))
    0
    >>> shapely.get_num_interior_rings(None)
    0
    """
    ...
@overload
def get_geometry(geometry: MultiPoint, index: SupportsIndex, **kwargs) -> Point | Any:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: MultiLineString, index: SupportsIndex, **kwargs) -> LineString | Any:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: MultiPolygon, index: SupportsIndex, **kwargs) -> Polygon | Any:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: BaseMultipartGeometry, index: SupportsIndex, **kwargs) -> BaseGeometry | Any:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: None, index: SupportsIndex, **kwargs) -> None:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: Geometry | None, index: SupportsIndex, **kwargs) -> BaseGeometry | None:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: OptGeoArrayLikeSeq, index: ArrayLike[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_geometry(geometry: OptGeoArrayLike, index: ArrayLikeSeq[SupportsIndex], **kwargs) -> GeoArray:
    """
    Return the nth geometry from a collection of geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the nth geometry of.
    index : int or array_like
        Negative values count from the end of the collection backwards.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Notes
    -----
    - simple geometries act as length-1 collections
    - out-of-range values return None

    See Also
    --------
    get_num_geometries, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point, MultiPoint
    >>> multipoint = MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)])
    >>> shapely.get_geometry(multipoint, 1)
    <POINT (1 1)>
    >>> shapely.get_geometry(multipoint, -1)
    <POINT (3 3)>
    >>> shapely.get_geometry(multipoint, 5) is None
    True
    >>> shapely.get_geometry(Point(1, 1), 0)
    <POINT (1 1)>
    >>> shapely.get_geometry(Point(1, 1), 1) is None
    True
    """
    ...
@overload
def get_parts(geometry: OptGeoArrayLike, return_index: Literal[False] = False) -> GeoArray:
    """
    Get parts of each GeometryCollection or Multi* geometry object.

    A copy of each geometry in the GeometryCollection or Multi* geometry object
    is returned.

    Note: This does not return the individual parts of Multi* geometry objects
    in a GeometryCollection. You may need to call this function multiple times
    to return individual parts of Multi* geometry objects in a
    GeometryCollection.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the parts of.
    return_index : bool, default False
        If True, will return a tuple of ndarrays of (parts, indexes), where
        indexes are the indexes of the original geometries in the source array.

    Notes
    -----

    .. deprecated:: 2.1.0
        A deprecation warning is shown if ``return_index`` is specified as
        a positional argument. This will need to be specified as a keyword
        argument in a future release.

    Returns
    -------
    ndarray of parts or tuple of (parts, indexes)

    See Also
    --------
    get_geometry, get_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint
    >>> shapely.get_parts(MultiPoint([(0, 1), (2, 3)])).tolist()
    [<POINT (0 1)>, <POINT (2 3)>]
    >>> parts, index = shapely.get_parts([MultiPoint([(0, 1)]), MultiPoint([(4, 5), (6, 7)])], return_index=True)
    >>> parts.tolist()
    [<POINT (0 1)>, <POINT (4 5)>, <POINT (6 7)>]
    >>> index.tolist()
    [0, 1, 1]
    """
    ...
@overload
def get_parts(geometry: OptGeoArrayLike, return_index: Literal[True]) -> tuple[GeoArray, NDArray[np.int64]]:
    """
    Get parts of each GeometryCollection or Multi* geometry object.

    A copy of each geometry in the GeometryCollection or Multi* geometry object
    is returned.

    Note: This does not return the individual parts of Multi* geometry objects
    in a GeometryCollection. You may need to call this function multiple times
    to return individual parts of Multi* geometry objects in a
    GeometryCollection.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the parts of.
    return_index : bool, default False
        If True, will return a tuple of ndarrays of (parts, indexes), where
        indexes are the indexes of the original geometries in the source array.

    Notes
    -----

    .. deprecated:: 2.1.0
        A deprecation warning is shown if ``return_index`` is specified as
        a positional argument. This will need to be specified as a keyword
        argument in a future release.

    Returns
    -------
    ndarray of parts or tuple of (parts, indexes)

    See Also
    --------
    get_geometry, get_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint
    >>> shapely.get_parts(MultiPoint([(0, 1), (2, 3)])).tolist()
    [<POINT (0 1)>, <POINT (2 3)>]
    >>> parts, index = shapely.get_parts([MultiPoint([(0, 1)]), MultiPoint([(4, 5), (6, 7)])], return_index=True)
    >>> parts.tolist()
    [<POINT (0 1)>, <POINT (4 5)>, <POINT (6 7)>]
    >>> index.tolist()
    [0, 1, 1]
    """
    ...
@overload
def get_parts(geometry: OptGeoArrayLike, return_index: bool) -> GeoArray | tuple[GeoArray, NDArray[np.int64]]:
    """
    Get parts of each GeometryCollection or Multi* geometry object.

    A copy of each geometry in the GeometryCollection or Multi* geometry object
    is returned.

    Note: This does not return the individual parts of Multi* geometry objects
    in a GeometryCollection. You may need to call this function multiple times
    to return individual parts of Multi* geometry objects in a
    GeometryCollection.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the parts of.
    return_index : bool, default False
        If True, will return a tuple of ndarrays of (parts, indexes), where
        indexes are the indexes of the original geometries in the source array.

    Notes
    -----

    .. deprecated:: 2.1.0
        A deprecation warning is shown if ``return_index`` is specified as
        a positional argument. This will need to be specified as a keyword
        argument in a future release.

    Returns
    -------
    ndarray of parts or tuple of (parts, indexes)

    See Also
    --------
    get_geometry, get_rings

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint
    >>> shapely.get_parts(MultiPoint([(0, 1), (2, 3)])).tolist()
    [<POINT (0 1)>, <POINT (2 3)>]
    >>> parts, index = shapely.get_parts([MultiPoint([(0, 1)]), MultiPoint([(4, 5), (6, 7)])], return_index=True)
    >>> parts.tolist()
    [<POINT (0 1)>, <POINT (4 5)>, <POINT (6 7)>]
    >>> index.tolist()
    [0, 1, 1]
    """
    ...
@overload
def get_rings(geometry: OptGeoArrayLike, return_index: Literal[False] = False) -> GeoArray:
    """
    Get rings of Polygon geometry object.

    For each Polygon, the first returned ring is always the exterior ring
    and potential subsequent rings are interior rings.

    If the geometry is not a Polygon, nothing is returned (empty array for
    scalar geometry input or no element in output array for array input).

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the rings of.
    return_index : bool, default False
        If True, will return a tuple of ndarrays of (rings, indexes), where
        indexes are the indexes of the original geometries in the source array.

    Notes
    -----

    .. deprecated:: 2.1.0
        A deprecation warning is shown if ``return_index`` is specified as
        a positional argument. This will need to be specified as a keyword
        argument in a future release.

    Returns
    -------
    ndarray of rings or tuple of (rings, indexes)

    See Also
    --------
    get_exterior_ring, get_interior_ring, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_rings(polygon_with_hole).tolist()
    [<LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>,
     <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>]

    With ``return_index=True``:

    >>> polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)])
    >>> rings, index = shapely.get_rings(
    ...     [polygon, polygon_with_hole],
    ...     return_index=True
    ... )
    >>> rings.tolist()
    [<LINEARRING (0 0, 2 0, 2 2, 0 2, 0 0)>,
     <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>,
     <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>]
    >>> index.tolist()
    [0, 1, 1]
    """
    ...
@overload
def get_rings(geometry: OptGeoArrayLike, return_index: Literal[True]) -> tuple[GeoArray, NDArray[np.int64]]:
    """
    Get rings of Polygon geometry object.

    For each Polygon, the first returned ring is always the exterior ring
    and potential subsequent rings are interior rings.

    If the geometry is not a Polygon, nothing is returned (empty array for
    scalar geometry input or no element in output array for array input).

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the rings of.
    return_index : bool, default False
        If True, will return a tuple of ndarrays of (rings, indexes), where
        indexes are the indexes of the original geometries in the source array.

    Notes
    -----

    .. deprecated:: 2.1.0
        A deprecation warning is shown if ``return_index`` is specified as
        a positional argument. This will need to be specified as a keyword
        argument in a future release.

    Returns
    -------
    ndarray of rings or tuple of (rings, indexes)

    See Also
    --------
    get_exterior_ring, get_interior_ring, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_rings(polygon_with_hole).tolist()
    [<LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>,
     <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>]

    With ``return_index=True``:

    >>> polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)])
    >>> rings, index = shapely.get_rings(
    ...     [polygon, polygon_with_hole],
    ...     return_index=True
    ... )
    >>> rings.tolist()
    [<LINEARRING (0 0, 2 0, 2 2, 0 2, 0 0)>,
     <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>,
     <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>]
    >>> index.tolist()
    [0, 1, 1]
    """
    ...
@overload
def get_rings(geometry: OptGeoArrayLike, return_index: bool) -> GeoArray | tuple[GeoArray, NDArray[np.int64]]:
    """
    Get rings of Polygon geometry object.

    For each Polygon, the first returned ring is always the exterior ring
    and potential subsequent rings are interior rings.

    If the geometry is not a Polygon, nothing is returned (empty array for
    scalar geometry input or no element in output array for array input).

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the rings of.
    return_index : bool, default False
        If True, will return a tuple of ndarrays of (rings, indexes), where
        indexes are the indexes of the original geometries in the source array.

    Notes
    -----

    .. deprecated:: 2.1.0
        A deprecation warning is shown if ``return_index`` is specified as
        a positional argument. This will need to be specified as a keyword
        argument in a future release.

    Returns
    -------
    ndarray of rings or tuple of (rings, indexes)

    See Also
    --------
    get_exterior_ring, get_interior_ring, get_parts

    Examples
    --------
    >>> import shapely
    >>> from shapely import Polygon
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> shapely.get_rings(polygon_with_hole).tolist()
    [<LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>,
     <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>]

    With ``return_index=True``:

    >>> polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)])
    >>> rings, index = shapely.get_rings(
    ...     [polygon, polygon_with_hole],
    ...     return_index=True
    ... )
    >>> rings.tolist()
    [<LINEARRING (0 0, 2 0, 2 2, 0 2, 0 0)>,
     <LINEARRING (0 0, 0 10, 10 10, 10 0, 0 0)>,
     <LINEARRING (2 2, 2 4, 4 4, 4 2, 2 2)>]
    >>> index.tolist()
    [0, 1, 1]
    """
    ...
@overload
def get_num_geometries(geometry: Geometry | None, **kwargs) -> np.int32:
    """
    Return number of geometries in a collection.

    Returns 0 for not-a-geometry values. The number of geometries in points,
    linestrings, linearrings and polygons equals one.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of geometries of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points
    get_geometry

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_num_geometries(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]))
    4
    >>> shapely.get_num_geometries(Point(1, 1))
    1
    >>> shapely.get_num_geometries(None)
    0
    """
    ...
@overload
def get_num_geometries(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.int64]:
    """
    Return number of geometries in a collection.

    Returns 0 for not-a-geometry values. The number of geometries in points,
    linestrings, linearrings and polygons equals one.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the number of geometries of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_num_points
    get_geometry

    Examples
    --------
    >>> import shapely
    >>> from shapely import MultiPoint, Point
    >>> shapely.get_num_geometries(MultiPoint([(0, 0), (1, 1), (2, 2), (3, 3)]))
    4
    >>> shapely.get_num_geometries(Point(1, 1))
    1
    >>> shapely.get_num_geometries(None)
    0
    """
    ...
@overload
def get_precision(geometry: Geometry | None, **kwargs) -> np.float64:
    """
    Get the precision of a geometry.

    If a precision has not been previously set, it will be 0 (double
    precision). Otherwise, it will return the precision grid size that was
    set on a geometry.

    Returns NaN for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the precision of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    set_precision

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> shapely.get_precision(point)
    0.0
    >>> geometry = shapely.set_precision(point, 1.0)
    >>> shapely.get_precision(geometry)
    1.0
    >>> shapely.get_precision(None)
    nan
    """
    ...
@overload
def get_precision(geometry: OptGeoArrayLikeSeq, **kwargs) -> NDArray[np.float64]:
    """
    Get the precision of a geometry.

    If a precision has not been previously set, it will be 0 (double
    precision). Otherwise, it will return the precision grid size that was
    set on a geometry.

    Returns NaN for not-a-geometry values.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to get the precision of.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    set_precision

    Examples
    --------
    >>> import shapely
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> shapely.get_precision(point)
    0.0
    >>> geometry = shapely.set_precision(point, 1.0)
    >>> shapely.get_precision(geometry)
    1.0
    >>> shapely.get_precision(None)
    nan
    """
    ...

class SetPrecisionMode(ParamEnum):
    """An enumeration."""
    valid_output = 0
    pointwise = 1
    keep_collapsed = 2

@overload
def set_precision(geometry: OptGeoT, grid_size: float, mode: _PrecisionMode = "valid_output", **kwargs) -> OptGeoT:
    """
    Return geometry with the precision set to a precision grid size.

    By default, geometries use double precision coordinates (grid_size = 0).

    Coordinates will be rounded if the precision grid specified is less precise
    than the input geometry. Duplicated vertices will be dropped from lines and
    polygons for grid sizes greater than 0. Line and polygon geometries may
    collapse to empty geometries if all vertices are closer together than
    ``grid_size`` or if a polygon becomes significantly narrower than
    ``grid_size``. Spikes or sections in polygons narrower than ``grid_size``
    after rounding the vertices will be removed, which can lead to multipolygons
    or empty geometries. Z values, if present, will not be modified.

    Notes
    -----
    * subsequent operations will always be performed in the precision of the
      geometry with higher precision (smaller "grid_size"). That same precision
      will be attached to the operation outputs.
    * input geometries should be geometrically valid; unexpected results may
      occur if input geometries are not.
    * the geometry returned will be in
      :ref:`mild canonical form <canonical-form>`, and the order of vertices can
      change and should not be relied upon.
    * returns None if geometry is None.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to set the precision of.
    grid_size : float
        Precision grid size. If 0, will use double precision (will not modify
        geometry if precision grid size was not previously set). If this
        value is more precise than input geometry, the input geometry will
        not be modified.
    mode : {'valid_output', 'pointwise', 'keep_collapsed'}, default 'valid_output'
        This parameter determines the way a precision reduction is applied on
        the geometry. There are three modes:

        1. `'valid_output'` (default):  The output is always valid. Collapsed
           geometry elements (including both polygons and lines) are removed.
           Duplicate vertices are removed.
        2. `'pointwise'`: Precision reduction is performed pointwise. Output
           geometry may be invalid due to collapse or self-intersection.
           Duplicate vertices are not removed. In GEOS this option is called
           NO_TOPO.

           .. note::

             'pointwise' mode requires at least GEOS 3.10. It is accepted in
             earlier versions, but the results may be unexpected.
        3. `'keep_collapsed'`: Like the default mode, except that collapsed
           linear geometry elements are preserved. Collapsed polygonal input
           elements are removed. Duplicate vertices are removed.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_precision

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.set_precision(Point(0.9, 0.9), 1.0)
    <POINT (1 1)>
    >>> shapely.set_precision(Point(0.9, 0.9, 0.9), 1.0)
    <POINT Z (1 1 0.9)>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0, 1), (1, 1)]), 1.0)
    <LINESTRING (0 0, 0 1, 1 1)>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0.1, 0.1)]), 1.0, mode="valid_output")
    <LINESTRING EMPTY>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0.1, 0.1)]), 1.0, mode="pointwise")
    <LINESTRING (0 0, 0 0, 0 0)>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0.1, 0.1)]), 1.0, mode="keep_collapsed")
    <LINESTRING (0 0, 0 0)>
    >>> shapely.set_precision(None, 1.0) is None
    True
    """
    ...
@overload
def set_precision(
    geometry: OptGeoArrayLikeSeq, grid_size: float, mode: _PrecisionMode = "valid_output", **kwargs
) -> GeoArray:
    """
    Return geometry with the precision set to a precision grid size.

    By default, geometries use double precision coordinates (grid_size = 0).

    Coordinates will be rounded if the precision grid specified is less precise
    than the input geometry. Duplicated vertices will be dropped from lines and
    polygons for grid sizes greater than 0. Line and polygon geometries may
    collapse to empty geometries if all vertices are closer together than
    ``grid_size`` or if a polygon becomes significantly narrower than
    ``grid_size``. Spikes or sections in polygons narrower than ``grid_size``
    after rounding the vertices will be removed, which can lead to multipolygons
    or empty geometries. Z values, if present, will not be modified.

    Notes
    -----
    * subsequent operations will always be performed in the precision of the
      geometry with higher precision (smaller "grid_size"). That same precision
      will be attached to the operation outputs.
    * input geometries should be geometrically valid; unexpected results may
      occur if input geometries are not.
    * the geometry returned will be in
      :ref:`mild canonical form <canonical-form>`, and the order of vertices can
      change and should not be relied upon.
    * returns None if geometry is None.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to set the precision of.
    grid_size : float
        Precision grid size. If 0, will use double precision (will not modify
        geometry if precision grid size was not previously set). If this
        value is more precise than input geometry, the input geometry will
        not be modified.
    mode : {'valid_output', 'pointwise', 'keep_collapsed'}, default 'valid_output'
        This parameter determines the way a precision reduction is applied on
        the geometry. There are three modes:

        1. `'valid_output'` (default):  The output is always valid. Collapsed
           geometry elements (including both polygons and lines) are removed.
           Duplicate vertices are removed.
        2. `'pointwise'`: Precision reduction is performed pointwise. Output
           geometry may be invalid due to collapse or self-intersection.
           Duplicate vertices are not removed. In GEOS this option is called
           NO_TOPO.

           .. note::

             'pointwise' mode requires at least GEOS 3.10. It is accepted in
             earlier versions, but the results may be unexpected.
        3. `'keep_collapsed'`: Like the default mode, except that collapsed
           linear geometry elements are preserved. Collapsed polygonal input
           elements are removed. Duplicate vertices are removed.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    See Also
    --------
    get_precision

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.set_precision(Point(0.9, 0.9), 1.0)
    <POINT (1 1)>
    >>> shapely.set_precision(Point(0.9, 0.9, 0.9), 1.0)
    <POINT Z (1 1 0.9)>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0, 1), (1, 1)]), 1.0)
    <LINESTRING (0 0, 0 1, 1 1)>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0.1, 0.1)]), 1.0, mode="valid_output")
    <LINESTRING EMPTY>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0.1, 0.1)]), 1.0, mode="pointwise")
    <LINESTRING (0 0, 0 0, 0 0)>
    >>> shapely.set_precision(LineString([(0, 0), (0, 0.1), (0.1, 0.1)]), 1.0, mode="keep_collapsed")
    <LINESTRING (0 0, 0 0)>
    >>> shapely.set_precision(None, 1.0) is None
    True
    """
    ...
@overload
def force_2d(geometry: OptGeoT, **kwargs) -> OptGeoT:
    """
    Force the dimensionality of a geometry to 2D.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to force to 2D.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point, Polygon, from_wkt
    >>> shapely.force_2d(Point(0, 0, 1))
    <POINT (0 0)>
    >>> shapely.force_2d(Point(0, 0))
    <POINT (0 0)>
    >>> shapely.force_2d(LineString([(0, 0, 0), (0, 1, 1), (1, 1, 2)]))
    <LINESTRING (0 0, 0 1, 1 1)>
    >>> shapely.force_2d(from_wkt("POLYGON Z EMPTY"))
    <POLYGON EMPTY>
    >>> shapely.force_2d(None) is None
    True
    """
    ...
@overload
def force_2d(geometry: OptGeoArrayLikeSeq, **kwargs) -> GeoArray:
    """
    Force the dimensionality of a geometry to 2D.

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to force to 2D.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point, Polygon, from_wkt
    >>> shapely.force_2d(Point(0, 0, 1))
    <POINT (0 0)>
    >>> shapely.force_2d(Point(0, 0))
    <POINT (0 0)>
    >>> shapely.force_2d(LineString([(0, 0, 0), (0, 1, 1), (1, 1, 2)]))
    <LINESTRING (0 0, 0 1, 1 1)>
    >>> shapely.force_2d(from_wkt("POLYGON Z EMPTY"))
    <POLYGON EMPTY>
    >>> shapely.force_2d(None) is None
    True
    """
    ...
@overload
def force_3d(geometry: OptGeoT, z: float = 0.0, **kwargs) -> OptGeoT:
    """
    Force the dimensionality of a geometry to 3D.

    2D geometries will get the provided Z coordinate; Z coordinates of 3D geometries
    are unchanged (unless they are nan).

    Note that for empty geometries, 3D is only supported since GEOS 3.9 and then
    still only for simple geometries (non-collections).

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to force to 3D.
    z : float or array_like, default 0.0
        The Z coordinate value to set on the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.force_3d(Point(0, 0), z=3)
    <POINT Z (0 0 3)>
    >>> shapely.force_3d(Point(0, 0, 0), z=3)
    <POINT Z (0 0 0)>
    >>> shapely.force_3d(LineString([(0, 0), (0, 1), (1, 1)]))
    <LINESTRING Z (0 0 0, 0 1 0, 1 1 0)>
    >>> shapely.force_3d(None) is None
    True
    """
    ...
@overload
def force_3d(geometry: OptGeoArrayLikeSeq, z: ArrayLike[float] = 0.0, **kwargs) -> GeoArray:
    """
    Force the dimensionality of a geometry to 3D.

    2D geometries will get the provided Z coordinate; Z coordinates of 3D geometries
    are unchanged (unless they are nan).

    Note that for empty geometries, 3D is only supported since GEOS 3.9 and then
    still only for simple geometries (non-collections).

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to force to 3D.
    z : float or array_like, default 0.0
        The Z coordinate value to set on the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.force_3d(Point(0, 0), z=3)
    <POINT Z (0 0 3)>
    >>> shapely.force_3d(Point(0, 0, 0), z=3)
    <POINT Z (0 0 0)>
    >>> shapely.force_3d(LineString([(0, 0), (0, 1), (1, 1)]))
    <LINESTRING Z (0 0 0, 0 1 0, 1 1 0)>
    >>> shapely.force_3d(None) is None
    True
    """
    ...
@overload
def force_3d(geometry: OptGeoArrayLike, z: ArrayLikeSeq[float], **kwargs) -> GeoArray:
    """
    Force the dimensionality of a geometry to 3D.

    2D geometries will get the provided Z coordinate; Z coordinates of 3D geometries
    are unchanged (unless they are nan).

    Note that for empty geometries, 3D is only supported since GEOS 3.9 and then
    still only for simple geometries (non-collections).

    Parameters
    ----------
    geometry : Geometry or array_like
        Geometry or geometries to force to 3D.
    z : float or array_like, default 0.0
        The Z coordinate value to set on the geometry.
    **kwargs
        See :ref:`NumPy ufunc docs <ufuncs.kwargs>` for other keyword arguments.

    Examples
    --------
    >>> import shapely
    >>> from shapely import LineString, Point
    >>> shapely.force_3d(Point(0, 0), z=3)
    <POINT Z (0 0 3)>
    >>> shapely.force_3d(Point(0, 0, 0), z=3)
    <POINT Z (0 0 0)>
    >>> shapely.force_3d(LineString([(0, 0), (0, 1), (1, 1)]))
    <LINESTRING Z (0 0 0, 0 1 0, 1 1 0)>
    >>> shapely.force_3d(None) is None
    True
    """
    ...
