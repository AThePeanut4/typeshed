"""Points and related utilities."""

from collections.abc import Iterable
from typing import overload
from typing_extensions import Self, TypeAlias

from .._typing import ArrayLikeSeq
from .base import BaseGeometry
from .collection import GeometryCollection

__all__ = ["Point"]

_PointLike: TypeAlias = Point | Iterable[float] | ArrayLikeSeq[float]

class Point(BaseGeometry):
    __slots__: list[str] = []
    @overload  # no args: empty point
    def __new__(self) -> Self:
        """Create a new Point geometry."""
        ...
    @overload  # one arg: (x, y[, z]) tuple or a Point instance
    def __new__(self, coords: _PointLike, /) -> Self:
        """Create a new Point geometry."""
        ...
    @overload  # two args: (x, y) tuple
    def __new__(self, x: float, y: float, /) -> Self:
        """Create a new Point geometry."""
        ...
    @overload  # three args: (x, y, z) tuple
    def __new__(self, x: float, y: float, z: float, /) -> Self:
        """Create a new Point geometry."""
        ...
    @property
    def x(self) -> float:
        """Return x coordinate."""
        ...
    @property
    def y(self) -> float:
        """Return y coordinate."""
        ...
    @property
    def z(self) -> float:
        """Return z coordinate."""
        ...
    @property
    def m(self) -> float:
        """
        Return m coordinate.

        .. versionadded:: 2.1.0
           Also requires GEOS 3.12.0 or later.
        """
        ...
    def svg(self, scale_factor: float = 1.0, fill_color: str | None = None, opacity: float | None = None) -> str:
        """
        Return SVG circle element for the Point geometry.

        Parameters
        ----------
        scale_factor : float
            Multiplication factor for the SVG circle diameter.  Default is 1.
        fill_color : str, optional
            Hex string for fill color. Default is to use "#66cc99" if
            geometry is valid, and "#ff3333" if invalid.
        opacity : float
            Float number between 0 and 1 for color opacity. Default value is 0.6
        """
        ...
    # more precise base overrides
    @property
    def boundary(self) -> GeometryCollection:
        """
        Return a lower dimension geometry that bounds the object.

        The boundary of a polygon is a line, the boundary of a line is a
        collection of points. The boundary of a point is an empty (null)
        collection.
        """
        ...
    @property
    def convex_hull(self) -> Point:
        """
        Return the convex hull of the geometry.

        Imagine an elastic band stretched around the geometry: that's a convex
        hull, more or less.

        The convex hull of a three member multipoint, for example, is a
        triangular polygon.
        """
        ...
    @property
    def envelope(self) -> Point:
        """A figure that envelopes the geometry."""
        ...
    @property
    def oriented_envelope(self) -> Point:
        """
        Return the oriented envelope (minimum rotated rectangle) of a geometry.

        The oriented envelope encloses an input geometry, such that the resulting
        rectangle has minimum area.

        Unlike envelope this rectangle is not constrained to be parallel to the
        coordinate axes. If the convex hull of the object is a degenerate (line
        or point) this degenerate is returned.

        The starting point of the rectangle is not fixed. You can use
        :func:`~shapely.normalize` to reorganize the rectangle to
        :ref:`strict canonical form <canonical-form>` so the starting point is
        always the lower left point.

        Alias of `minimum_rotated_rectangle`.
        """
        ...
    @property
    def minimum_rotated_rectangle(self) -> Point:
        """
        Return the oriented envelope (minimum rotated rectangle) of the geometry.

        The oriented envelope encloses an input geometry, such that the resulting
        rectangle has minimum area.

        Unlike `envelope` this rectangle is not constrained to be parallel to the
        coordinate axes. If the convex hull of the object is a degenerate (line
        or point) this degenerate is returned.

        The starting point of the rectangle is not fixed. You can use
        :func:`~shapely.normalize` to reorganize the rectangle to
        :ref:`strict canonical form <canonical-form>` so the starting point is
        always the lower left point.

        Alias of `oriented_envelope`.
        """
        ...
