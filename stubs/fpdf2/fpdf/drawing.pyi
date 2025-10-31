"""
Vector drawing: managing colors, graphics states, paths, transforms...

The contents of this module are internal to fpdf2, and not part of the public API.
They may change at any time without prior warning or any deprecation period,
in non-backward-compatible ways.

Usage documentation at: <https://py-pdf.github.io/fpdf2/Drawing.html>
"""

import decimal
import sys
from _typeshed import Incomplete, SupportsWrite
from collections import OrderedDict
from collections.abc import Callable, Generator, Iterable, Sequence
from contextlib import contextmanager
from re import Pattern
from typing import Any, ClassVar, Literal, NamedTuple, Protocol, TypeVar, overload, type_check_only
from typing_extensions import Self, TypeAlias

if sys.version_info >= (3, 10):
    from types import EllipsisType
else:
    # Rely on builtins.ellipsis
    from builtins import ellipsis as EllipsisType

from .enums import PathPaintRule
from .syntax import Name, Raw

__pdoc__: dict[str, bool]

_T = TypeVar("_T")
_CallableT = TypeVar("_CallableT", bound=Callable[..., Any])

@type_check_only
class _SupportsSerialize(Protocol):
    def serialize(self) -> str: ...

@type_check_only
class _SupportsEndPoint(Protocol):
    @property
    def end_point(self) -> Point: ...

def force_nodocument(item: _CallableT) -> _CallableT: ...
def force_document(item: _CallableT) -> _CallableT: ...

Number: TypeAlias = int | float | decimal.Decimal
NumberClass: tuple[type, ...]
WHITESPACE: frozenset[str]
EOL_CHARS: frozenset[str]
DELIMITERS: frozenset[str]
STR_ESC: Pattern[str]
STR_ESC_MAP: dict[str, str]
_Primitive: TypeAlias = (
    _SupportsSerialize
    | Number
    | str
    | bytes
    | bool
    | Raw
    | list[_Primitive]
    | tuple[_Primitive, ...]
    | dict[Name, _Primitive]
    | None
)

class GraphicsStateDictRegistry(OrderedDict[Raw, Name]):
    """A container providing deduplication of graphics state dictionaries across a PDF."""
    def register_style(self, style: GraphicsStyle) -> Name | None: ...

def number_to_str(number: Number) -> str: ...
def render_pdf_primitive(primitive: _Primitive) -> Raw: ...

class _DeviceRGBBase(NamedTuple):
    r: Number
    g: Number
    b: Number
    a: Number | None

class DeviceRGB(_DeviceRGBBase):
    """A class representing a PDF DeviceRGB color."""
    OPERATOR: ClassVar[str]
    def __new__(cls, r: Number, g: Number, b: Number, a: Number | None = None) -> Self: ...
    @property
    def colors(self) -> tuple[Number, Number, Number]:
        """The color components as a tuple in order `(r, g, b)` with alpha omitted, in range 0-1."""
        ...
    @property
    def colors255(self) -> tuple[Number, Number, Number]:
        """The color components as a tuple in order `(r, g, b)` with alpha omitted, in range 0-255."""
        ...
    def serialize(self) -> str: ...

class _DeviceGrayBase(NamedTuple):
    g: Number
    a: Number | None

class DeviceGray(_DeviceGrayBase):
    """A class representing a PDF DeviceGray color."""
    OPERATOR: ClassVar[str]
    def __new__(cls, g: Number, a: Number | None = None) -> Self: ...
    @property
    def colors(self) -> tuple[Number, Number, Number]:
        """The color components as a tuple in order (r, g, b) with alpha omitted, in range 0-1."""
        ...
    @property
    def colors255(self) -> tuple[Number, Number, Number]:
        """The color components as a tuple in order `(r, g, b)` with alpha omitted, in range 0-255."""
        ...
    def serialize(self) -> str: ...

class _DeviceCMYKBase(NamedTuple):
    c: Number
    m: Number
    y: Number
    k: Number
    a: Number | None

class DeviceCMYK(_DeviceCMYKBase):
    """A class representing a PDF DeviceCMYK color."""
    OPERATOR: ClassVar[str]
    def __new__(cls, c: Number, m: Number, y: Number, k: Number, a: Number | None = None) -> Self: ...
    @property
    def colors(self) -> tuple[Number, Number, Number, Number]:
        """The color components as a tuple in order (c, m, y, k) with alpha omitted, in range 0-1."""
        ...
    def serialize(self) -> str: ...

def rgb8(r: Number, g: Number, b: Number, a: Number | None = None) -> DeviceRGB: ...
def gray8(g: Number, a: Number | None = None) -> DeviceGray: ...
@overload
def convert_to_device_color(r: DeviceCMYK) -> DeviceCMYK: ...
@overload
def convert_to_device_color(r: DeviceGray) -> DeviceGray: ...
@overload
def convert_to_device_color(r: DeviceRGB) -> DeviceRGB: ...
@overload
def convert_to_device_color(r: str) -> DeviceRGB: ...
@overload
def convert_to_device_color(r: int, g: Literal[-1] = -1, b: Literal[-1] = -1) -> DeviceGray: ...
@overload
def convert_to_device_color(r: Sequence[int] | int, g: int, b: int) -> DeviceGray | DeviceRGB: ...
def cmyk8(c, m, y, k, a=None) -> DeviceCMYK: ...
def color_from_hex_string(hexstr: str) -> DeviceRGB: ...
def color_from_rgb_string(rgbstr: str) -> DeviceRGB: ...

class Point(NamedTuple):
    """An x-y coordinate pair within the two-dimensional coordinate frame."""
    x: Number
    y: Number
    def render(self) -> str: ...
    def dot(self, other: Point) -> Number: ...
    def angle(self, other: Point) -> float: ...
    def mag(self) -> Number: ...
    def __add__(self, other: Point) -> Point: ...  # type: ignore[override]
    def __sub__(self, other: Point) -> Point: ...
    def __neg__(self) -> Point: ...
    def __mul__(self, other: Number) -> Point: ...  # type: ignore[override]
    def __rmul__(self, other: Number) -> Point: ...  # type: ignore[override]
    def __truediv__(self, other: Number) -> Point: ...
    def __floordiv__(self, other: Number) -> Point: ...
    def __matmul__(self, other: Transform) -> Point: ...

class Transform(NamedTuple):
    """
    A representation of an affine transformation matrix for 2D shapes.

    The actual matrix is:

    ```
                        [ a b 0 ]
    [x' y' 1] = [x y 1] [ c d 0 ]
                        [ e f 1 ]
    ```

    Complex transformation operations can be composed via a sequence of simple
    transformations by performing successive matrix multiplication of the simple
    transformations.

    For example, scaling a set of points around a specific center point can be
    represented by a translation-scale-translation sequence, where the first
    translation translates the center to the origin, the scale transform scales the
    points relative to the origin, and the second translation translates the points
    back to the specified center point. Transform multiplication is performed using
    python's dedicated matrix multiplication operator, `@`

    The semantics of this representation mean composed transformations are specified
    left-to-right in order of application (some other systems provide transposed
    representations, in which case the application order is right-to-left).

    For example, to rotate the square `(1,1) (1,3) (3,3) (3,1)` 45 degrees clockwise
    about its center point (which is `(2,2)`) , the translate-rotate-translate
    process described above may be applied:

    ```python
    rotate_centered = (
        Transform.translation(-2, -2)
        @ Transform.rotation_d(45)
        @ Transform.translation(2, 2)
    )
    ```

    Instances of this class provide a chaining API, so the above transform could also be
    constructed as follows:

    ```python
    rotate_centered = Transform.translation(-2, -2).rotate_d(45).translate(2, 2)
    ```

    Or, because the particular operation of performing some transformations about a
    specific point is pretty common,

    ```python
    rotate_centered = Transform.rotation_d(45).about(2, 2)
    ```

    By convention, this class provides class method constructors following noun-ish
    naming (`translation`, `scaling`, `rotation`, `shearing`) and instance method
    manipulations following verb-ish naming (`translate`, `scale`, `rotate`, `shear`).
    """
    a: Number
    b: Number
    c: Number
    d: Number
    e: Number
    f: Number
    @classmethod
    def identity(cls) -> Self: ...
    @classmethod
    def translation(cls, x: Number, y: Number) -> Self: ...
    @classmethod
    def scaling(cls, x: Number, y: Number | None = None) -> Self: ...
    @classmethod
    def rotation(cls, theta: Number) -> Self: ...
    @classmethod
    def rotation_d(cls, theta_d: Number) -> Self: ...
    @classmethod
    def shearing(cls, x: Number, y: Number | None = None) -> Self: ...
    def translate(self, x: Number, y: Number) -> Self: ...
    def scale(self, x: Number, y: Number | None = None) -> Self: ...
    def rotate(self, theta: Number) -> Self: ...
    def rotate_d(self, theta_d: Number) -> Self: ...
    def shear(self, x: Number, y: Number | None = None) -> Self: ...
    def about(self, x: Number, y: Number) -> Transform: ...
    def __mul__(self, other: Number) -> Transform: ...  # type: ignore[override]
    def __rmul__(self, other: Number) -> Transform: ...  # type: ignore[override]
    def __matmul__(self, other: Transform) -> Self: ...
    def render(self, last_item: _T) -> tuple[str, _T]: ...

class GraphicsStyle:
    INHERIT: ClassVar[EllipsisType]
    MERGE_PROPERTIES: ClassVar[tuple[str, ...]]
    TRANSPARENCY_KEYS: ClassVar[tuple[Name, ...]]
    PDF_STYLE_KEYS: ClassVar[tuple[Name, ...]]
    @classmethod
    def merge(cls, parent, child) -> Self: ...
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def allow_transparency(self): ...
    @allow_transparency.setter
    def allow_transparency(self, new): ...
    @property
    def paint_rule(self) -> PathPaintRule | EllipsisType: ...
    @paint_rule.setter
    def paint_rule(self, new: PathPaintRule | str | EllipsisType | None) -> None: ...
    @property
    def auto_close(self) -> bool | EllipsisType: ...
    @auto_close.setter
    def auto_close(self, new: bool | EllipsisType) -> None: ...
    @property
    def intersection_rule(self):
        """The desired intersection rule for this path/group."""
        ...
    @intersection_rule.setter
    def intersection_rule(self, new) -> None:
        """The desired intersection rule for this path/group."""
        ...
    @property
    def fill_color(self):
        """
        The desired fill color for this path/group.

        When setting this property, if the color specifies an opacity value, that will
        be used to set the fill_opacity property as well.
        """
        ...
    @fill_color.setter
    def fill_color(self, color) -> None:
        """
        The desired fill color for this path/group.

        When setting this property, if the color specifies an opacity value, that will
        be used to set the fill_opacity property as well.
        """
        ...
    @property
    def fill_opacity(self):
        """The desired fill opacity for this path/group."""
        ...
    @fill_opacity.setter
    def fill_opacity(self, new) -> None:
        """The desired fill opacity for this path/group."""
        ...
    @property
    def stroke_color(self):
        """
        The desired stroke color for this path/group.

        When setting this property, if the color specifies an opacity value, that will
        be used to set the fill_opacity property as well.
        """
        ...
    @stroke_color.setter
    def stroke_color(self, color: str | DeviceRGB | DeviceGray | DeviceCMYK | EllipsisType | None) -> None: ...
    @property
    def stroke_opacity(self):
        """The desired stroke opacity for this path/group."""
        ...
    @stroke_opacity.setter
    def stroke_opacity(self, new) -> None:
        """The desired stroke opacity for this path/group."""
        ...
    @property
    def blend_mode(self):
        """The desired blend mode for this path/group."""
        ...
    @blend_mode.setter
    def blend_mode(self, value) -> None:
        """The desired blend mode for this path/group."""
        ...
    @property
    def stroke_width(self):
        """The desired stroke width for this path/group."""
        ...
    @stroke_width.setter
    def stroke_width(self, width: Number | EllipsisType | None) -> None: ...
    @property
    def stroke_cap_style(self):
        """The desired stroke cap style for this path/group."""
        ...
    @stroke_cap_style.setter
    def stroke_cap_style(self, value) -> None:
        """The desired stroke cap style for this path/group."""
        ...
    @property
    def stroke_join_style(self):
        """The desired stroke join style for this path/group."""
        ...
    @stroke_join_style.setter
    def stroke_join_style(self, value) -> None:
        """The desired stroke join style for this path/group."""
        ...
    @property
    def stroke_miter_limit(self):
        """The desired stroke miter limit for this path/group."""
        ...
    @stroke_miter_limit.setter
    def stroke_miter_limit(self, value: Number | EllipsisType) -> None: ...
    @property
    def stroke_dash_pattern(self):
        """The desired stroke dash pattern for this path/group."""
        ...
    @stroke_dash_pattern.setter
    def stroke_dash_pattern(self, value: Number | Iterable[Number] | EllipsisType | None) -> None: ...
    @property
    def stroke_dash_phase(self):
        """The desired stroke dash pattern phase offset for this path/group."""
        ...
    @stroke_dash_phase.setter
    def stroke_dash_phase(self, value: Number | EllipsisType): ...
    def serialize(self) -> Raw | None: ...
    def resolve_paint_rule(self) -> PathPaintRule: ...

class Move(NamedTuple):
    """
    A path move element.

    If a path has been created but not yet painted, this will create a new subpath.

    See: `PaintedPath.move_to`
    """
    pt: Point
    @property
    def end_point(self) -> Point: ...
    def render(
        self, gsd_registry: GraphicsStateDictRegistry, style: GraphicsStyle, last_item: _SupportsEndPoint, initial_point: Point
    ) -> tuple[str, Self, Point]: ...
    def render_debug(
        self,
        gsd_registry: GraphicsStateDictRegistry,
        style: GraphicsStyle,
        last_item: _SupportsEndPoint,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Self, Point]: ...

class RelativeMove(NamedTuple):
    """
    A path move element with an end point relative to the end of the previous path
    element.

    If a path has been created but not yet painted, this will create a new subpath.

    See: `PaintedPath.move_relative`
    """
    pt: Point
    def render(
        self, gsd_registry: GraphicsStateDictRegistry, style: GraphicsStyle, last_item: _SupportsEndPoint, initial_point: Point
    ) -> tuple[str, Move, Point]: ...
    def render_debug(
        self,
        gsd_registry: GraphicsStateDictRegistry,
        style: GraphicsStyle,
        last_item: _SupportsEndPoint,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Move, Point]: ...

class Line(NamedTuple):
    """
    A path line element.

    This draws a straight line from the end point of the previous path element to the
    point specified by `pt`.

    See: `PaintedPath.line_to`
    """
    pt: Point
    @property
    def end_point(self) -> Point: ...
    def render(
        self, gsd_registry: GraphicsStateDictRegistry, style: GraphicsStyle, last_item: _SupportsEndPoint, initial_point: Point
    ) -> tuple[str, Self, Point]: ...
    def render_debug(
        self,
        gsd_registry: GraphicsStateDictRegistry,
        style: GraphicsStyle,
        last_item: _SupportsEndPoint,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Self, Point]: ...

class RelativeLine(NamedTuple):
    """
    A path line element with an endpoint relative to the end of the previous element.

    This draws a straight line from the end point of the previous path element to the
    point specified by `last_item.end_point + pt`. The absolute coordinates of the end
    point are resolved during the rendering process.

    See: `PaintedPath.line_relative`
    """
    pt: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `Line`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RelativeLine.render`.
        """
        ...

class HorizontalLine(NamedTuple):
    """
    A path line element that takes its ordinate from the end of the previous element.

    See: `PaintedPath.horizontal_line_to`
    """
    x: Number
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `Line`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `HorizontalLine.render`.
        """
        ...

class RelativeHorizontalLine(NamedTuple):
    """
    A path line element that takes its ordinate from the end of the previous element and
    computes its abscissa offset from the end of that element.

    See: `PaintedPath.horizontal_line_relative`
    """
    x: Number
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `Line`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RelativeHorizontalLine.render`.
        """
        ...

class VerticalLine(NamedTuple):
    """
    A path line element that takes its abscissa from the end of the previous element.

    See: `PaintedPath.vertical_line_to`
    """
    y: Number
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `Line`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `VerticalLine.render`.
        """
        ...

class RelativeVerticalLine(NamedTuple):
    """
    A path line element that takes its abscissa from the end of the previous element and
    computes its ordinate offset from the end of that element.

    See: `PaintedPath.vertical_line_relative`
    """
    y: Number
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `Line`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RelativeVerticalLine.render`.
        """
        ...

class BezierCurve(NamedTuple):
    """
    A cubic Bézier curve path element.

    This draws a Bézier curve parameterized by the end point of the previous path
    element, two off-curve control points, and an end point.

    See: `PaintedPath.curve_to`
    """
    c1: Point
    c2: Point
    end: Point
    @property
    def end_point(self) -> Point: ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeBezierCurve(NamedTuple):
    """
    A cubic Bézier curve path element whose points are specified relative to the end
    point of the previous path element.

    See: `PaintedPath.curve_relative`
    """
    c1: Point
    c2: Point
    end: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `BezierCurve`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RelativeBezierCurve.render`.
        """
        ...

class QuadraticBezierCurve(NamedTuple):
    """
    A quadratic Bézier curve path element.

    This draws a Bézier curve parameterized by the end point of the previous path
    element, one off-curve control point, and an end point.

    See: `PaintedPath.quadratic_curve_to`
    """
    ctrl: Point
    end: Point
    @property
    def end_point(self) -> Point: ...
    def to_cubic_curve(self, start_point): ...
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is `self`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `QuadraticBezierCurve.render`.
        """
        ...

class RelativeQuadraticBezierCurve(NamedTuple):
    """
    A quadratic Bézier curve path element whose points are specified relative to the end
    point of the previous path element.

    See: `PaintedPath.quadratic_curve_relative`
    """
    ctrl: Point
    end: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is the resolved
            `QuadraticBezierCurve`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RelativeQuadraticBezierCurve.render`.
        """
        ...

class Arc(NamedTuple):
    """
    An elliptical arc path element.

    The arc is drawn from the end of the current path element to its specified end point
    using a number of parameters to determine how it is constructed.

    See: `PaintedPath.arc_to`
    """
    radii: Point
    rotation: Number
    large: bool
    sweep: bool
    end: Point
    @staticmethod
    def subdivde_sweep(sweep_angle: Number) -> Generator[tuple[Point, Point, Point]]: ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeArc(NamedTuple):
    """
    An elliptical arc path element.

    The arc is drawn from the end of the current path element to its specified end point
    using a number of parameters to determine how it is constructed.

    See: `PaintedPath.arc_relative`
    """
    radii: Point
    rotation: Number
    large: bool
    sweep: bool
    end: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is a resolved
            `BezierCurve`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RelativeArc.render`.
        """
        ...

class Rectangle(NamedTuple):
    """A pdf primitive rectangle."""
    org: Point
    size: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is a `Line` back to
            the rectangle's origin.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `Rectangle.render`.
        """
        ...

class RoundedRectangle(NamedTuple):
    """
    A rectangle with rounded corners.

    See: `PaintedPath.rectangle`
    """
    org: Point
    size: Point
    corner_radii: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is a resolved
            `Line`.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `RoundedRectangle.render`.
        """
        ...

class Ellipse(NamedTuple):
    """
    An ellipse.

    See: `PaintedPath.ellipse`
    """
    radii: Point
    center: Point
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is a resolved
            `Move` to the center of the ellipse.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `Ellipse.render`.
        """
        ...

class ImplicitClose(NamedTuple):
    """
    A path close element that is conditionally rendered depending on the value of
    `GraphicsStyle.auto_close`.
    """
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is whatever the old
            last_item was.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `ImplicitClose.render`.
        """
        ...

class Close(NamedTuple):
    """
    A path close element.

    Instructs the renderer to draw a straight line from the end of the last path element
    to the start of the current path.

    See: `PaintedPath.close`
    """
    def render(self, gsd_registry, style, last_item, initial_point):
        """
        Render this path element to its PDF representation.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command

        Returns:
            a tuple of `(str, new_last_item)`, where `new_last_item` is whatever the old
            last_item was.
        """
        ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `Close.render`.
        """
        ...

class DrawingContext:
    """
    Base context for a drawing in a PDF

    This context is not stylable and is mainly responsible for transforming path
    drawing coordinates into user coordinates (i.e. it ensures that the output drawing
    is correctly scaled).
    """
    def __init__(self) -> None: ...
    def add_item(self, item, _copy: bool = True) -> None:
        """
        Append an item to this drawing context

        Args:
            item (GraphicsContext, PaintedPath): the item to be appended.
            _copy (bool): if true (the default), the item will be copied before being
                appended. This prevents modifications to a referenced object from
                "retroactively" altering its style/shape and should be disabled with
                caution.
        """
        ...
    def render(self, gsd_registry, first_point, scale, height, starting_style):
        """
        Render the drawing context to PDF format.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the parent document's graphics
                state registry.
            first_point (Point): the starting point to use if the first path element is
                a relative element.
            scale (Number): the scale factor to convert from PDF pt units into the
                document's semantic units (e.g. mm or in).
            height (Number): the page height. This is used to remap the coordinates to
                be from the top-left corner of the page (matching fpdf's behavior)
                instead of the PDF native behavior of bottom-left.
            starting_style (GraphicsStyle): the base style for this drawing context,
                derived from the document's current style defaults.

        Returns:
            A string composed of the PDF representation of all the paths and groups in
            this context (an empty string is returned if there are no paths or groups)
        """
        ...
    def render_debug(self, gsd_registry, first_point, scale, height, starting_style, debug_stream):
        """
        Render the drawing context to PDF format.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the parent document's graphics
                state registry.
            first_point (Point): the starting point to use if the first path element is
                a relative element.
            scale (Number): the scale factor to convert from PDF pt units into the
                document's semantic units (e.g. mm or in).
            height (Number): the page height. This is used to remap the coordinates to
                be from the top-left corner of the page (matching fpdf's behavior)
                instead of the PDF native behavior of bottom-left.
            starting_style (GraphicsStyle): the base style for this drawing context,
                derived from the document's current style defaults.
            debug_stream (TextIO): a text stream to which a debug representation of the
                drawing structure will be written.

        Returns:
            A string composed of the PDF representation of all the paths and groups in
            this context (an empty string is returned if there are no paths or groups)
        """
        ...

class PaintedPath:
    def __init__(self, x: Number = 0, y: Number = 0) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def style(self) -> GraphicsStyle: ...
    @property
    def transform(self):
        """The `Transform` that applies to all of the elements of this path."""
        ...
    @transform.setter
    def transform(self, tf) -> None:
        """The `Transform` that applies to all of the elements of this path."""
        ...
    @property
    def auto_close(self):
        """If true, the path should automatically close itself before painting."""
        ...
    @auto_close.setter
    def auto_close(self, should) -> None:
        """If true, the path should automatically close itself before painting."""
        ...
    @property
    def paint_rule(self):
        """Manually specify the `PathPaintRule` to use for rendering the path."""
        ...
    @paint_rule.setter
    def paint_rule(self, style) -> None:
        """Manually specify the `PathPaintRule` to use for rendering the path."""
        ...
    @property
    def clipping_path(self):
        """Set the clipping path for this path."""
        ...
    @clipping_path.setter
    def clipping_path(self, new_clipath) -> None:
        """Set the clipping path for this path."""
        ...
    @contextmanager
    def transform_group(self, transform) -> Generator[Self]:
        """Apply the provided `Transform` to all points added within this context."""
        ...
    def add_path_element(self, item, _copy: bool = True) -> None:
        """
        Add the given element as a path item of this path.

        Args:
            item: the item to add to this path.
            _copy (bool): if true (the default), the item will be copied before being
                appended. This prevents modifications to a referenced object from
                "retroactively" altering its style/shape and should be disabled with
                caution.
        """
        ...
    def remove_last_path_element(self) -> None: ...
    def rectangle(self, x: Number, y: Number, w: Number, h: Number, rx: Number = 0, ry: Number = 0) -> Self: ...
    def circle(self, cx: Number, cy: Number, r: Number) -> Self: ...
    def ellipse(self, cx: Number, cy: Number, rx: Number, ry: Number) -> Self: ...
    def move_to(self, x: Number, y: Number) -> Self: ...
    def move_relative(self, x: Number, y: Number) -> Self: ...
    def line_to(self, x: Number, y: Number) -> Self: ...
    def line_relative(self, dx: Number, dy: Number) -> Self: ...
    def horizontal_line_to(self, x: Number) -> Self: ...
    def horizontal_line_relative(self, dx: Number) -> Self: ...
    def vertical_line_to(self, y: Number) -> Self: ...
    def vertical_line_relative(self, dy: Number) -> Self: ...
    def curve_to(self, x1: Number, y1: Number, x2: Number, y2: Number, x3: Number, y3: Number) -> Self: ...
    def curve_relative(self, dx1: Number, dy1: Number, dx2: Number, dy2: Number, dx3: Number, dy3: Number) -> Self: ...
    def quadratic_curve_to(self, x1: Number, y1: Number, x2: Number, y2: Number) -> Self: ...
    def quadratic_curve_relative(self, dx1: Number, dy1: Number, dx2: Number, dy2: Number) -> Self: ...
    def arc_to(
        self, rx: Number, ry: Number, rotation: Number, large_arc: bool, positive_sweep: bool, x: Number, y: Number
    ) -> Self: ...
    def arc_relative(
        self, rx: Number, ry: Number, rotation: Number, large_arc: bool, positive_sweep: bool, dx: Number, dy: Number
    ) -> Self: ...
    def close(self) -> None: ...
    def render(self, gsd_registry, style, last_item, initial_point, debug_stream=None, pfx=None): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `PaintedPath.render`.
        """
        ...

class ClippingPath(PaintedPath):
    paint_rule: PathPaintRule
    def __init__(self, x: Number = 0, y: Number = 0) -> None: ...
    def render(self, gsd_registry, style, last_item, initial_point, debug_stream=None, pfx=None): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx):
        """
        Render this path element to its PDF representation and produce debug
        information.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).

        Returns:
            The same tuple as `ClippingPath.render`.
        """
        ...

class GraphicsContext:
    style: GraphicsStyle
    path_items: list[Incomplete]
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def transform(self) -> Transform | None: ...
    @transform.setter
    def transform(self, tf) -> None: ...
    @property
    def clipping_path(self) -> ClippingPath | None:
        """The `ClippingPath` for this graphics context."""
        ...
    @clipping_path.setter
    def clipping_path(self, new_clipath) -> None:
        """The `ClippingPath` for this graphics context."""
        ...
    def add_item(self, item, _copy: bool = True) -> None:
        """
        Add a path element to this graphics context.

        Args:
            item: the path element to add. May be a primitive element or another
                `GraphicsContext` or a `PaintedPath`.
            _copy (bool): if true (the default), the item will be copied before being
                appended. This prevents modifications to a referenced object from
                "retroactively" altering its style/shape and should be disabled with
                caution.
        """
        ...
    def remove_last_item(self) -> None: ...
    def merge(self, other_context) -> None:
        """Copy another `GraphicsContext`'s path items into this one."""
        ...
    def build_render_list(
        self, gsd_registry, style, last_item, initial_point, debug_stream=None, pfx=None, _push_stack: bool = True
    ):
        """
        Build a list composed of all all the individual elements rendered.

        This is used by `PaintedPath` and `ClippingPath` to reuse the `GraphicsContext`
        rendering process while still being able to inject some path specific items
        (e.g. the painting directive) before the render is collapsed into a single
        string.

        Args:
            gsd_registry (GraphicsStateDictRegistry): the owner's graphics state
                dictionary registry.
            style (GraphicsStyle): the current resolved graphics style
            last_item: the previous path element.
            initial_point: last position set by a "M" or "m" command
            debug_stream (io.TextIO): the stream to which the debug output should be
                written. This is not guaranteed to be seekable (e.g. it may be stdout or
                stderr).
            pfx (str): the current debug output prefix string (only needed if emitting
                more than one line).
            _push_stack (bool): if True, wrap the resulting render list in a push/pop
                graphics stack directive pair.

        Returns:
            `tuple[list[str], last_item]` where `last_item` is the past path element in
            this `GraphicsContext`
        """
        ...
    def render(
        self, gsd_registry, style: DrawingContext, last_item, initial_point, debug_stream=None, pfx=None, _push_stack: bool = True
    ): ...
    def render_debug(
        self, gsd_registry, style: DrawingContext, last_item, initial_point, debug_stream, pfx, _push_stack: bool = True
    ): ...
