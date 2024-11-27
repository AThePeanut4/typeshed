"""
Base geometry class and utilities

Note: a third, z, coordinate value may be used when constructing
geometry objects, but has no effect on geometric analysis. All
operations are performed in the x-y plane. Thus, geometries with
different z values may intersect or be equal.
"""

from array import array
from collections.abc import Iterator
from typing import Any, Generic, Literal, NoReturn, overload
from typing_extensions import Self, TypeVar, deprecated

import numpy as np
from numpy.typing import NDArray

from .._typing import ArrayLikeSeq, GeoArray, GeoT, OptGeoArrayLike, OptGeoArrayLikeSeq
from ..constructive import BufferCapStyle, BufferJoinStyle
from ..coords import CoordinateSequence
from ..lib import Geometry
from .collection import GeometryCollection
from .point import Point
from .polygon import Polygon

GEOMETRY_TYPES: list[str]

@deprecated("Function 'geom_factory' is deprecated.")
def geom_factory(g: int, parent: object | None = None) -> Any:
    """
    Creates a Shapely geometry instance from a pointer to a GEOS geometry.

    .. warning::
        The GEOS library used to create the the GEOS geometry pointer
        and the GEOS library used by Shapely must be exactly the same, or
        unexpected results or segfaults may occur.

    .. deprecated:: 2.0
        Deprecated in Shapely 2.0, and will be removed in a future version.
    """
    ...
def dump_coords(geom: Geometry) -> list[tuple[float, float] | list[tuple[float, float]]]:
    """Dump coordinates of a geometry in the same order as data packing"""
    ...

class CAP_STYLE:
    round: Literal[BufferCapStyle.round]
    flat: Literal[BufferCapStyle.flat]
    square: Literal[BufferCapStyle.square]

class JOIN_STYLE:
    round: Literal[BufferJoinStyle.round]
    mitre: Literal[BufferJoinStyle.mitre]
    bevel: Literal[BufferJoinStyle.bevel]

class BaseGeometry(Geometry):
    """Provides GEOS spatial predicates and topological operations."""
    @deprecated(
        "Directly calling 'BaseGeometry()' is deprecated. To create an empty geometry, "
        "use one of the subclasses instead, for example 'GeometryCollection()'."
    )
    def __new__(self) -> GeometryCollection: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __format__(self, format_spec: str) -> str:
        """Format a geometry using a format specification."""
        ...
    @overload
    def __and__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __and__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __and__(self, other: None) -> None: ...
    @overload
    def __or__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __or__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __or__(self, other: None) -> None: ...
    @overload
    def __sub__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __sub__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __sub__(self, other: None) -> None: ...
    @overload
    def __xor__(self, other: Geometry) -> BaseGeometry: ...
    @overload
    def __xor__(self, other: OptGeoArrayLikeSeq) -> GeoArray: ...
    @overload
    def __xor__(self, other: None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def coords(self) -> CoordinateSequence:
        """Access to geometry's coordinates (CoordinateSequence)"""
        ...
    @property
    def xy(self) -> tuple[array[float], array[float]]:
        """Separate arrays of X and Y coordinate values"""
        ...
    @property
    def __geo_interface__(self) -> dict[str, Any]:
        """Dictionary representation of the geometry"""
        ...
    @deprecated("Method 'geometryType()' is deprecated. Use attribute 'geom_type' instead.")
    def geometryType(self) -> str: ...
    @property
    @deprecated("Attribute 'type' is deprecated. Use attribute 'geom_type' instead.")
    def type(self) -> str: ...
    @property
    def wkt(self) -> str:
        """WKT representation of the geometry"""
        ...
    @property
    def wkb(self) -> bytes:
        """WKB representation of the geometry"""
        ...
    @property
    def wkb_hex(self) -> str:
        """WKB hex representation of the geometry"""
        ...
    def svg(self, scale_factor: float = 1.0, **kwargs) -> str:
        """Raises NotImplementedError"""
        ...
    def _repr_svg_(self) -> str:
        """SVG representation for iPython notebook"""
        ...
    @property
    def geom_type(self) -> str:
        """Name of the geometry's type, such as 'Point'"""
        ...
    @property
    def area(self) -> float:
        """Unitless area of the geometry (float)"""
        ...
    @overload
    def distance(self, other: Geometry | None) -> float:
        """Unitless distance to other geometry (float)"""
        ...
    @overload
    def distance(self, other: OptGeoArrayLikeSeq) -> NDArray[np.float64]:
        """Unitless distance to other geometry (float)"""
        ...
    @overload
    def hausdorff_distance(self, other: Geometry | None) -> float:
        """Unitless hausdorff distance to other geometry (float)"""
        ...
    @overload
    def hausdorff_distance(self, other: OptGeoArrayLikeSeq) -> NDArray[np.float64]:
        """Unitless hausdorff distance to other geometry (float)"""
        ...
    @property
    def length(self) -> float:
        """Unitless length of the geometry (float)"""
        ...
    @property
    def minimum_clearance(self) -> float:
        """Unitless distance by which a node could be moved to produce an invalid geometry (float)"""
        ...
    @property
    def boundary(self) -> BaseMultipartGeometry | Any:
        """
        Returns a lower dimension geometry that bounds the object

        The boundary of a polygon is a line, the boundary of a line is a
        collection of points. The boundary of a point is an empty (null)
        collection.
        """
        ...
    @property
    def bounds(self) -> tuple[float, float, float, float]:
        """Returns minimum bounding region (minx, miny, maxx, maxy)"""
        ...
    @property
    def centroid(self) -> Point:
        """Returns the geometric center of the object"""
        ...
    def point_on_surface(self) -> Point:
        """
        Returns a point guaranteed to be within the object, cheaply.

        Alias of `representative_point`.
        """
        ...
    def representative_point(self) -> Point:
        """
        Returns a point guaranteed to be within the object, cheaply.

        Alias of `point_on_surface`.
        """
        ...
    @property
    def convex_hull(self) -> BaseGeometry:
        """
        Imagine an elastic band stretched around the geometry: that's a
        convex hull, more or less

        The convex hull of a three member multipoint, for example, is a
        triangular polygon.
        """
        ...
    @property
    def envelope(self) -> BaseGeometry:
        """A figure that envelopes the geometry"""
        ...
    @property
    def oriented_envelope(self) -> BaseGeometry:
        """
        Returns the oriented envelope (minimum rotated rectangle) that
        encloses the geometry.

        Unlike envelope this rectangle is not constrained to be parallel to the
        coordinate axes. If the convex hull of the object is a degenerate (line
        or point) this degenerate is returned.

        Alias of `minimum_rotated_rectangle`.
        """
        ...
    @property
    def minimum_rotated_rectangle(self) -> BaseGeometry:
        """
        Returns the oriented envelope (minimum rotated rectangle) that
        encloses the geometry.

        Unlike `envelope` this rectangle is not constrained to be parallel to the
        coordinate axes. If the convex hull of the object is a degenerate (line
        or point) this degenerate is returned.

        Alias of `oriented_envelope`.
        """
        ...
    def buffer(
        self,
        distance: float,
        quad_segs: int = 16,
        cap_style: BufferCapStyle | Literal["round", "square", "flat"] = "round",
        join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = "round",
        mitre_limit: float = 5.0,
        single_sided: bool = False,
        *,
        quadsegs: int | None = None,  # deprecated
        resolution: int | None = None,  # to be deprecated
    ) -> Polygon:
        """
        Get a geometry that represents all points within a distance
        of this geometry.

        A positive distance produces a dilation, a negative distance an
        erosion. A very small or zero distance may sometimes be used to
        "tidy" a polygon.

        Parameters
        ----------
        distance : float
            The distance to buffer around the object.
        resolution : int, optional
            The resolution of the buffer around each vertex of the
            object.
        quad_segs : int, optional
            Sets the number of line segments used to approximate an
            angle fillet.
        cap_style : shapely.BufferCapStyle or {'round', 'square', 'flat'}, default 'round'
            Specifies the shape of buffered line endings. BufferCapStyle.round ('round')
            results in circular line endings (see ``quad_segs``). Both BufferCapStyle.square
            ('square') and BufferCapStyle.flat ('flat') result in rectangular line endings,
            only BufferCapStyle.flat ('flat') will end at the original vertex,
            while BufferCapStyle.square ('square') involves adding the buffer width.
        join_style : shapely.BufferJoinStyle or {'round', 'mitre', 'bevel'}, default 'round'
            Specifies the shape of buffered line midpoints. BufferJoinStyle.ROUND ('round')
            results in rounded shapes. BufferJoinStyle.bevel ('bevel') results in a beveled
            edge that touches the original vertex. BufferJoinStyle.mitre ('mitre') results
            in a single vertex that is beveled depending on the ``mitre_limit`` parameter.
        mitre_limit : float, optional
            The mitre limit ratio is used for very sharp corners. The
            mitre ratio is the ratio of the distance from the corner to
            the end of the mitred offset corner. When two line segments
            meet at a sharp angle, a miter join will extend the original
            geometry. To prevent unreasonable geometry, the mitre limit
            allows controlling the maximum length of the join corner.
            Corners with a ratio which exceed the limit will be beveled.
        single_side : bool, optional
            The side used is determined by the sign of the buffer
            distance:

                a positive distance indicates the left-hand side
                a negative distance indicates the right-hand side

            The single-sided buffer of point geometries is the same as
            the regular buffer.  The End Cap Style for single-sided
            buffers is always ignored, and forced to the equivalent of
            CAP_FLAT.
        quadsegs : int, optional
            Deprecated alias for `quad_segs`.

        Returns
        -------
        Geometry

        Notes
        -----
        The return value is a strictly two-dimensional geometry. All
        Z coordinates of the original geometry will be ignored.

        Examples
        --------
        >>> from shapely.wkt import loads
        >>> g = loads('POINT (0.0 0.0)')

        16-gon approx of a unit radius circle:

        >>> g.buffer(1.0).area  # doctest: +ELLIPSIS
        3.1365484905459...

        128-gon approximation:

        >>> g.buffer(1.0, 128).area  # doctest: +ELLIPSIS
        3.141513801144...

        triangle approximation:

        >>> g.buffer(1.0, 3).area
        3.0
        >>> list(g.buffer(1.0, cap_style=BufferCapStyle.square).exterior.coords)
        [(1.0, 1.0), (1.0, -1.0), (-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0)]
        >>> g.buffer(1.0, cap_style=BufferCapStyle.square).area
        4.0
        """
        ...
    def simplify(self, tolerance: float, preserve_topology: bool = True) -> BaseGeometry:
        """
        Returns a simplified geometry produced by the Douglas-Peucker
        algorithm

        Coordinates of the simplified geometry will be no more than the
        tolerance distance from the original. Unless the topology preserving
        option is used, the algorithm may produce self-intersecting or
        otherwise invalid geometries.
        """
        ...
    def normalize(self) -> BaseGeometry:
        """
        Converts geometry to normal form (or canonical form).

        This method orders the coordinates, rings of a polygon and parts of
        multi geometries consistently. Typically useful for testing purposes
        (for example in combination with `equals_exact`).

        Examples
        --------
        >>> from shapely import MultiLineString
        >>> line = MultiLineString([[(0, 0), (1, 1)], [(3, 3), (2, 2)]])
        >>> line.normalize()
        <MULTILINESTRING ((2 2, 3 3), (0 0, 1 1))>
        """
        ...
    @overload
    def difference(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry:
        """
        Returns the difference of the geometries.

        Refer to `shapely.difference` for full documentation.
        """
        ...
    @overload
    def difference(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray:
        """
        Returns the difference of the geometries.

        Refer to `shapely.difference` for full documentation.
        """
        ...
    @overload
    def difference(self, other: None, grid_size: float | None = None) -> None:
        """
        Returns the difference of the geometries.

        Refer to `shapely.difference` for full documentation.
        """
        ...
    @overload
    def intersection(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry:
        """
        Returns the intersection of the geometries.

        Refer to `shapely.intersection` for full documentation.
        """
        ...
    @overload
    def intersection(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray:
        """
        Returns the intersection of the geometries.

        Refer to `shapely.intersection` for full documentation.
        """
        ...
    @overload
    def intersection(self, other: None, grid_size: float | None = None) -> None:
        """
        Returns the intersection of the geometries.

        Refer to `shapely.intersection` for full documentation.
        """
        ...
    @overload
    def symmetric_difference(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry:
        """
        Returns the symmetric difference of the geometries.

        Refer to `shapely.symmetric_difference` for full documentation.
        """
        ...
    @overload
    def symmetric_difference(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray:
        """
        Returns the symmetric difference of the geometries.

        Refer to `shapely.symmetric_difference` for full documentation.
        """
        ...
    @overload
    def symmetric_difference(self, other: None, grid_size: float | None = None) -> None:
        """
        Returns the symmetric difference of the geometries.

        Refer to `shapely.symmetric_difference` for full documentation.
        """
        ...
    @overload
    def union(self, other: Geometry, grid_size: float | None = None) -> BaseGeometry:
        """
        Returns the union of the geometries.

        Refer to `shapely.union` for full documentation.
        """
        ...
    @overload
    def union(self, other: OptGeoArrayLikeSeq, grid_size: float | None = None) -> GeoArray:
        """
        Returns the union of the geometries.

        Refer to `shapely.union` for full documentation.
        """
        ...
    @overload
    def union(self, other: None, grid_size: float | None = None) -> None:
        """
        Returns the union of the geometries.

        Refer to `shapely.union` for full documentation.
        """
        ...
    @property
    def has_z(self) -> bool:
        """
        True if the geometry's coordinate sequence(s) have z values (are
        3-dimensional)
        """
        ...
    @property
    def is_empty(self) -> bool:
        """True if the set of points in this geometry is empty, else False"""
        ...
    @property
    def is_ring(self) -> bool:
        """True if the geometry is a closed ring, else False"""
        ...
    @property
    def is_closed(self) -> bool:
        """
        True if the geometry is closed, else False

        Applicable only to 1-D geometries.
        """
        ...
    @property
    def is_simple(self) -> bool:
        """
        True if the geometry is simple, meaning that any self-intersections
        are only at boundary points, else False
        """
        ...
    @property
    def is_valid(self) -> bool:
        """
        True if the geometry is valid (definition depends on sub-class),
        else False
        """
        ...
    @overload
    def relate(self, other: Geometry) -> str:
        """
        Returns the DE-9IM intersection matrix for the two geometries
        (string)
        """
        ...
    @overload
    def relate(self, other: OptGeoArrayLikeSeq) -> NDArray[np.str_]:
        """
        Returns the DE-9IM intersection matrix for the two geometries
        (string)
        """
        ...
    @overload
    def relate(self, other: None) -> None:
        """
        Returns the DE-9IM intersection matrix for the two geometries
        (string)
        """
        ...
    @overload
    def covers(self, other: Geometry | None) -> bool:
        """Returns True if the geometry covers the other, else False"""
        ...
    @overload
    def covers(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if the geometry covers the other, else False"""
        ...
    @overload
    def covered_by(self, other: Geometry | None) -> bool:
        """Returns True if the geometry is covered by the other, else False"""
        ...
    @overload
    def covered_by(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if the geometry is covered by the other, else False"""
        ...
    @overload
    def contains(self, other: Geometry | None) -> bool:
        """Returns True if the geometry contains the other, else False"""
        ...
    @overload
    def contains(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if the geometry contains the other, else False"""
        ...
    @overload
    def contains_properly(self, other: Geometry | None) -> bool:
        """
        Returns True if the geometry completely contains the other, with no
        common boundary points, else False

        Refer to `shapely.contains_properly` for full documentation.
        """
        ...
    @overload
    def contains_properly(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """
        Returns True if the geometry completely contains the other, with no
        common boundary points, else False

        Refer to `shapely.contains_properly` for full documentation.
        """
        ...
    @overload
    def crosses(self, other: Geometry | None) -> bool:
        """Returns True if the geometries cross, else False"""
        ...
    @overload
    def crosses(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if the geometries cross, else False"""
        ...
    @overload
    def disjoint(self, other: Geometry | None) -> bool:
        """Returns True if geometries are disjoint, else False"""
        ...
    @overload
    def disjoint(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if geometries are disjoint, else False"""
        ...
    @overload
    def equals(self, other: Geometry | None) -> bool:
        """
        Returns True if geometries are equal, else False.

        This method considers point-set equality (or topological
        equality), and is equivalent to (self.within(other) &
        self.contains(other)).

        Examples
        --------
        >>> LineString(
        ...     [(0, 0), (2, 2)]
        ... ).equals(
        ...     LineString([(0, 0), (1, 1), (2, 2)])
        ... )
        True

        Returns
        -------
        bool
        """
        ...
    @overload
    def equals(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """
        Returns True if geometries are equal, else False.

        This method considers point-set equality (or topological
        equality), and is equivalent to (self.within(other) &
        self.contains(other)).

        Examples
        --------
        >>> LineString(
        ...     [(0, 0), (2, 2)]
        ... ).equals(
        ...     LineString([(0, 0), (1, 1), (2, 2)])
        ... )
        True

        Returns
        -------
        bool
        """
        ...
    @overload
    def intersects(self, other: Geometry | None) -> bool:
        """Returns True if geometries intersect, else False"""
        ...
    @overload
    def intersects(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if geometries intersect, else False"""
        ...
    @overload
    def overlaps(self, other: Geometry | None) -> bool:
        """Returns True if geometries overlap, else False"""
        ...
    @overload
    def overlaps(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if geometries overlap, else False"""
        ...
    @overload
    def touches(self, other: Geometry | None) -> bool:
        """Returns True if geometries touch, else False"""
        ...
    @overload
    def touches(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if geometries touch, else False"""
        ...
    @overload
    def within(self, other: Geometry | None) -> bool:
        """Returns True if geometry is within the other, else False"""
        ...
    @overload
    def within(self, other: OptGeoArrayLikeSeq) -> NDArray[np.bool_]:
        """Returns True if geometry is within the other, else False"""
        ...
    @overload
    def dwithin(self, other: Geometry | None, distance: float) -> bool:
        """
        Returns True if geometry is within a given distance from the other, else False.

        Refer to `shapely.dwithin` for full documentation.
        """
        ...
    @overload
    def dwithin(self, other: OptGeoArrayLikeSeq, distance: float) -> NDArray[np.bool_]:
        """
        Returns True if geometry is within a given distance from the other, else False.

        Refer to `shapely.dwithin` for full documentation.
        """
        ...
    @overload
    def dwithin(self, other: OptGeoArrayLike, distance: ArrayLikeSeq[float]) -> NDArray[np.bool_]:
        """
        Returns True if geometry is within a given distance from the other, else False.

        Refer to `shapely.dwithin` for full documentation.
        """
        ...
    @overload
    def equals_exact(self, other: Geometry | None, tolerance: float) -> bool:
        """
        True if geometries are equal to within a specified
        tolerance.

        Parameters
        ----------
        other : BaseGeometry
            The other geometry object in this comparison.
        tolerance : float
            Absolute tolerance in the same units as coordinates.

        This method considers coordinate equality, which requires
        coordinates to be equal and in the same order for all components
        of a geometry.

        Because of this it is possible for "equals()" to be True for two
        geometries and "equals_exact()" to be False.

        Examples
        --------
        >>> LineString(
        ...     [(0, 0), (2, 2)]
        ... ).equals_exact(
        ...     LineString([(0, 0), (1, 1), (2, 2)]),
        ...     1e-6
        ... )
        False

        Returns
        -------
        bool
        """
        ...
    @overload
    def equals_exact(self, other: OptGeoArrayLikeSeq, tolerance: float) -> NDArray[np.bool_]:
        """
        True if geometries are equal to within a specified
        tolerance.

        Parameters
        ----------
        other : BaseGeometry
            The other geometry object in this comparison.
        tolerance : float
            Absolute tolerance in the same units as coordinates.

        This method considers coordinate equality, which requires
        coordinates to be equal and in the same order for all components
        of a geometry.

        Because of this it is possible for "equals()" to be True for two
        geometries and "equals_exact()" to be False.

        Examples
        --------
        >>> LineString(
        ...     [(0, 0), (2, 2)]
        ... ).equals_exact(
        ...     LineString([(0, 0), (1, 1), (2, 2)]),
        ...     1e-6
        ... )
        False

        Returns
        -------
        bool
        """
        ...
    @overload
    def equals_exact(self, other: OptGeoArrayLike, tolerance: ArrayLikeSeq[float]) -> NDArray[np.bool_]:
        """
        True if geometries are equal to within a specified
        tolerance.

        Parameters
        ----------
        other : BaseGeometry
            The other geometry object in this comparison.
        tolerance : float
            Absolute tolerance in the same units as coordinates.

        This method considers coordinate equality, which requires
        coordinates to be equal and in the same order for all components
        of a geometry.

        Because of this it is possible for "equals()" to be True for two
        geometries and "equals_exact()" to be False.

        Examples
        --------
        >>> LineString(
        ...     [(0, 0), (2, 2)]
        ... ).equals_exact(
        ...     LineString([(0, 0), (1, 1), (2, 2)]),
        ...     1e-6
        ... )
        False

        Returns
        -------
        bool
        """
        ...
    @deprecated("Method 'almost_equals()' is deprecated. Use method 'equals_exact()' instead.")
    def almost_equals(self, other: OptGeoArrayLike, decimal: int = 6) -> bool | NDArray[np.bool_]:
        """
        True if geometries are equal at all coordinates to a
        specified decimal place.

        .. deprecated:: 1.8.0
            The 'almost_equals()' method is deprecated
            and will be removed in Shapely 2.1 because the name is
            confusing. The 'equals_exact()' method should be used
            instead.

        Refers to approximate coordinate equality, which requires
        coordinates to be approximately equal and in the same order for
        all components of a geometry.

        Because of this it is possible for "equals()" to be True for two
        geometries and "almost_equals()" to be False.

        Examples
        --------
        >>> LineString(
        ...     [(0, 0), (2, 2)]
        ... ).equals_exact(
        ...     LineString([(0, 0), (1, 1), (2, 2)]),
        ...     1e-6
        ... )
        False

        Returns
        -------
        bool
        """
        ...
    @overload
    def relate_pattern(self, other: Geometry | None, pattern: str) -> bool:
        """
        Returns True if the DE-9IM string code for the relationship between
        the geometries satisfies the pattern, else False
        """
        ...
    @overload
    def relate_pattern(self, other: OptGeoArrayLikeSeq, pattern: str) -> NDArray[np.bool_]:
        """
        Returns True if the DE-9IM string code for the relationship between
        the geometries satisfies the pattern, else False
        """
        ...
    @overload
    def line_locate_point(self, other: Point | None, normalized: bool = False) -> float:
        """
        Returns the distance along this geometry to a point nearest the
        specified point

        If the normalized arg is True, return the distance normalized to the
        length of the linear geometry.

        Alias of `project`.
        """
        ...
    @overload
    def line_locate_point(self, other: OptGeoArrayLikeSeq, normalized: bool = False) -> NDArray[np.float64]:
        """
        Returns the distance along this geometry to a point nearest the
        specified point

        If the normalized arg is True, return the distance normalized to the
        length of the linear geometry.

        Alias of `project`.
        """
        ...
    @overload
    def project(self, other: Point | None, normalized: bool = False) -> float:
        """
        Returns the distance along this geometry to a point nearest the
        specified point

        If the normalized arg is True, return the distance normalized to the
        length of the linear geometry.

        Alias of `line_locate_point`.
        """
        ...
    @overload
    def project(self, other: OptGeoArrayLikeSeq, normalized: bool = False) -> NDArray[np.float64]:
        """
        Returns the distance along this geometry to a point nearest the
        specified point

        If the normalized arg is True, return the distance normalized to the
        length of the linear geometry.

        Alias of `line_locate_point`.
        """
        ...
    @overload
    def line_interpolate_point(self, distance: float, normalized: bool = False) -> Point:
        """
        Return a point at the specified distance along a linear geometry

        Negative length values are taken as measured in the reverse
        direction from the end of the geometry. Out-of-range index
        values are handled by clamping them to the valid range of values.
        If the normalized arg is True, the distance will be interpreted as a
        fraction of the geometry's length.

        Alias of `interpolate`.
        """
        ...
    @overload
    def line_interpolate_point(self, distance: ArrayLikeSeq[float], normalized: bool = False) -> GeoArray:
        """
        Return a point at the specified distance along a linear geometry

        Negative length values are taken as measured in the reverse
        direction from the end of the geometry. Out-of-range index
        values are handled by clamping them to the valid range of values.
        If the normalized arg is True, the distance will be interpreted as a
        fraction of the geometry's length.

        Alias of `interpolate`.
        """
        ...
    @overload
    def interpolate(self, distance: float, normalized: bool = False) -> Point:
        """
        Return a point at the specified distance along a linear geometry

        Negative length values are taken as measured in the reverse
        direction from the end of the geometry. Out-of-range index
        values are handled by clamping them to the valid range of values.
        If the normalized arg is True, the distance will be interpreted as a
        fraction of the geometry's length.

        Alias of `line_interpolate_point`.
        """
        ...
    @overload
    def interpolate(self, distance: ArrayLikeSeq[float], normalized: bool = False) -> GeoArray:
        """
        Return a point at the specified distance along a linear geometry

        Negative length values are taken as measured in the reverse
        direction from the end of the geometry. Out-of-range index
        values are handled by clamping them to the valid range of values.
        If the normalized arg is True, the distance will be interpreted as a
        fraction of the geometry's length.

        Alias of `line_interpolate_point`.
        """
        ...
    @overload
    def segmentize(self, max_segment_length: float) -> Self:
        """
        Adds vertices to line segments based on maximum segment length.

        Additional vertices will be added to every line segment in an input geometry
        so that segments are no longer than the provided maximum segment length. New
        vertices will evenly subdivide each segment.

        Only linear components of input geometries are densified; other geometries
        are returned unmodified.

        Parameters
        ----------
        max_segment_length : float or array_like
            Additional vertices will be added so that all line segments are no
            longer this value.  Must be greater than 0.

        Examples
        --------
        >>> from shapely import LineString, Polygon
        >>> LineString([(0, 0), (0, 10)]).segmentize(max_segment_length=5)
        <LINESTRING (0 0, 0 5, 0 10)>
        >>> Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]).segmentize(max_segment_length=5)
        <POLYGON ((0 0, 5 0, 10 0, 10 5, 10 10, 5 10, 0 10, 0 5, 0 0))>
        """
        ...
    @overload
    def segmentize(self, max_segment_length: ArrayLikeSeq[float]) -> GeoArray:
        """
        Adds vertices to line segments based on maximum segment length.

        Additional vertices will be added to every line segment in an input geometry
        so that segments are no longer than the provided maximum segment length. New
        vertices will evenly subdivide each segment.

        Only linear components of input geometries are densified; other geometries
        are returned unmodified.

        Parameters
        ----------
        max_segment_length : float or array_like
            Additional vertices will be added so that all line segments are no
            longer this value.  Must be greater than 0.

        Examples
        --------
        >>> from shapely import LineString, Polygon
        >>> LineString([(0, 0), (0, 10)]).segmentize(max_segment_length=5)
        <LINESTRING (0 0, 0 5, 0 10)>
        >>> Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]).segmentize(max_segment_length=5)
        <POLYGON ((0 0, 5 0, 10 0, 10 5, 10 10, 5 10, 0 10, 0 5, 0 0))>
        """
        ...
    def reverse(self) -> Self:
        """
        Returns a copy of this geometry with the order of coordinates reversed.

        If the geometry is a polygon with interior rings, the interior rings are also
        reversed.

        Points are unchanged.

        See also
        --------
        is_ccw : Checks if a geometry is clockwise.

        Examples
        --------
        >>> from shapely import LineString, Polygon
        >>> LineString([(0, 0), (1, 2)]).reverse()
        <LINESTRING (1 2, 0 0)>
        >>> Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]).reverse()
        <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
        """
        ...

_GeoT_co = TypeVar("_GeoT_co", bound=Geometry, default=BaseGeometry, covariant=True)

class BaseMultipartGeometry(BaseGeometry, Generic[_GeoT_co]):
    @property
    def coords(self) -> NoReturn: ...
    @property
    def geoms(self) -> GeometrySequence[Self]: ...
    def svg(self, scale_factor: float = 1.0, color: str | None = None) -> str:
        """
        Returns a group of SVG elements for the multipart geometry.

        Parameters
        ==========
        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        color : str, optional
            Hex string for stroke or fill color. Default is to use "#66cc99"
            if geometry is valid, and "#ff3333" if invalid.
        """
        ...

_P_co = TypeVar("_P_co", covariant=True, bound=BaseMultipartGeometry[Geometry])

class GeometrySequence(Generic[_P_co]):
    """Iterative access to members of a homogeneous multipart geometry."""
    def __init__(self, parent: _P_co) -> None: ...
    def __iter__(self: GeometrySequence[BaseMultipartGeometry[GeoT]]) -> Iterator[GeoT]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self: GeometrySequence[BaseMultipartGeometry[GeoT]], key: int | np.integer[Any]) -> GeoT: ...
    @overload
    def __getitem__(self, key: slice) -> _P_co: ...

class EmptyGeometry(BaseGeometry):
    @deprecated(
        "The 'EmptyGeometry()' constructor is deprecated. Use one of the "
        "geometry subclasses instead, for example 'GeometryCollection()'."
    )
    def __new__(self) -> GeometryCollection:
        """Create an empty geometry."""
        ...
