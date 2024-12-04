"""Points and related utilities"""

from collections.abc import Iterable
from typing import overload
from typing_extensions import Self, TypeAlias

from .._typing import ArrayLikeSeq
from .base import BaseGeometry
from .collection import GeometryCollection

__all__ = ["Point"]

_PointLike: TypeAlias = Point | Iterable[float] | ArrayLikeSeq[float]

class Point(BaseGeometry):
    """
    A geometry type that represents a single coordinate with
    x,y and possibly z values.

    A point is a zero-dimensional feature and has zero length and zero area.

    Parameters
    ----------
    args : float, or sequence of floats
        The coordinates can either be passed as a single parameter, or as
        individual float values using multiple parameters:

        1) 1 parameter: a sequence or array-like of with 2 or 3 values.
        2) 2 or 3 parameters (float): x, y, and possibly z.

    Attributes
    ----------
    x, y, z : float
        Coordinate values

    Examples
    --------
    Constructing the Point using separate parameters for x and y:

    >>> p = Point(1.0, -1.0)

    Constructing the Point using a list of x, y coordinates:

    >>> p = Point([1.0, -1.0])
    >>> print(p)
    POINT (1 -1)
    >>> p.y
    -1.0
    >>> p.x
    1.0
    """
    @overload  # no args: empty point
    def __new__(self) -> Self: ...
    @overload  # one arg: (x, y[, z]) tuple or a Point instance
    def __new__(self, coords: _PointLike, /) -> Self: ...
    @overload  # two args: (x, y) tuple
    def __new__(self, x: float, y: float, /) -> Self: ...
    @overload  # three args: (x, y, z) tuple
    def __new__(self, x: float, y: float, z: float, /) -> Self: ...
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
    def svg(self, scale_factor: float = 1.0, fill_color: str | None = None, opacity: float | None = None) -> str:
        """
        Returns SVG circle element for the Point geometry.

        Parameters
        ==========
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
        Returns a lower dimension geometry that bounds the object

        The boundary of a polygon is a line, the boundary of a line is a
        collection of points. The boundary of a point is an empty (null)
        collection.
        """
        ...
    @property
    def convex_hull(self) -> Point:
        """
        Imagine an elastic band stretched around the geometry: that's a
        convex hull, more or less

        The convex hull of a three member multipoint, for example, is a
        triangular polygon.
        """
        ...
    @property
    def envelope(self) -> Point:
        """A figure that envelopes the geometry"""
        ...
    @property
    def oriented_envelope(self) -> Point:
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
    def minimum_rotated_rectangle(self) -> Point:
        """
        Returns the oriented envelope (minimum rotated rectangle) that
        encloses the geometry.

        Unlike `envelope` this rectangle is not constrained to be parallel to the
        coordinate axes. If the convex hull of the object is a degenerate (line
        or point) this degenerate is returned.

        Alias of `oriented_envelope`.
        """
        ...
