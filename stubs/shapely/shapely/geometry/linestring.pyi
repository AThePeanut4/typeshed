"""Line strings and related utilities"""

from collections.abc import Iterable
from typing import Literal, SupportsFloat, SupportsIndex
from typing_extensions import Self, TypeAlias

from .._typing import ArrayLikeSeq
from ..constructive import BufferJoinStyle
from .base import BaseGeometry
from .multilinestring import MultiLineString
from .multipoint import MultiPoint
from .point import Point
from .polygon import Polygon

__all__ = ["LineString"]

_ConvertibleToLineString: TypeAlias = LineString | ArrayLikeSeq[float] | Iterable[Point | Iterable[SupportsFloat]]

class LineString(BaseGeometry):
    """
    A geometry type composed of one or more line segments.

    A LineString is a one-dimensional feature and has a non-zero length but
    zero area. It may approximate a curve and need not be straight. Unlike a
    LinearRing, a LineString is not closed.

    Parameters
    ----------
    coordinates : sequence
        A sequence of (x, y, [,z]) numeric coordinate pairs or triples, or
        an array-like with shape (N, 2) or (N, 3).
        Also can be a sequence of Point objects.

    Examples
    --------
    Create a LineString with two segments

    >>> a = LineString([[0, 0], [1, 0], [1, 1]])
    >>> a.length
    2.0
    """
    def __new__(self, coordinates: _ConvertibleToLineString | None = None) -> Self: ...
    def svg(self, scale_factor: float = 1.0, stroke_color: str | None = None, opacity: float | None = None) -> str:
        """
        Returns SVG polyline element for the LineString geometry.

        Parameters
        ==========
        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        stroke_color : str, optional
            Hex string for stroke color. Default is to use "#66cc99" if
            geometry is valid, and "#ff3333" if invalid.
        opacity : float
            Float number between 0 and 1 for color opacity. Default value is 0.8
        """
        ...
    def offset_curve(
        self,
        distance: float,
        quad_segs: SupportsIndex = 16,
        join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = ...,
        mitre_limit: float = 5.0,
    ) -> LineString | MultiLineString:
        """
        Returns a LineString or MultiLineString geometry at a distance from
        the object on its right or its left side.

        The side is determined by the sign of the `distance` parameter
        (negative for right side offset, positive for left side offset). The
        resolution of the buffer around each vertex of the object increases
        by increasing the `quad_segs` keyword parameter.

        The join style is for outside corners between line segments. Accepted
        values are JOIN_STYLE.round (1), JOIN_STYLE.mitre (2), and
        JOIN_STYLE.bevel (3).

        The mitre ratio limit is used for very sharp corners. It is the ratio
        of the distance from the corner to the end of the mitred offset corner.
        When two line segments meet at a sharp angle, a miter join will extend
        far beyond the original geometry. To prevent unreasonable geometry, the
        mitre limit allows controlling the maximum length of the join corner.
        Corners with a ratio which exceed the limit will be beveled.

        Note: the behaviour regarding orientation of the resulting line
        depends on the GEOS version. With GEOS < 3.11, the line retains the
        same direction for a left offset (positive distance) or has reverse
        direction for a right offset (negative distance), and this behaviour
        was documented as such in previous Shapely versions. Starting with
        GEOS 3.11, the function tries to preserve the orientation of the
        original line.
        """
        ...
    def parallel_offset(  # to be deprecated
        self,
        distance: float,
        side: str = "right",
        resolution: SupportsIndex = 16,
        join_style: BufferJoinStyle | Literal["round", "mitre", "bevel"] = ...,
        mitre_limit: float = 5.0,
    ) -> LineString | MultiLineString:
        """
        Alternative method to :meth:`offset_curve` method.

        Older alternative method to the :meth:`offset_curve` method, but uses
        ``resolution`` instead of ``quad_segs`` and a ``side`` keyword
        ('left' or 'right') instead of sign of the distance. This method is
        kept for backwards compatibility for now, but is is recommended to
        use :meth:`offset_curve` instead.
        """
        ...
    # more precise base overrides
    @property
    def boundary(self) -> MultiPoint:
        """
        Returns a lower dimension geometry that bounds the object

        The boundary of a polygon is a line, the boundary of a line is a
        collection of points. The boundary of a point is an empty (null)
        collection.
        """
        ...
    @property
    def convex_hull(self) -> LineString:
        """
        Imagine an elastic band stretched around the geometry: that's a
        convex hull, more or less

        The convex hull of a three member multipoint, for example, is a
        triangular polygon.
        """
        ...
    @property
    def envelope(self) -> Polygon:
        """A figure that envelopes the geometry"""
        ...
    @property
    def oriented_envelope(self) -> LineString:
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
    def minimum_rotated_rectangle(self) -> LineString:
        """
        Returns the oriented envelope (minimum rotated rectangle) that
        encloses the geometry.

        Unlike `envelope` this rectangle is not constrained to be parallel to the
        coordinate axes. If the convex hull of the object is a degenerate (line
        or point) this degenerate is returned.

        Alias of `oriented_envelope`.
        """
        ...
