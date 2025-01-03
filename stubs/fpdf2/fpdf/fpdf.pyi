import datetime
from _typeshed import Incomplete, StrPath, Unused
from collections.abc import Callable, Generator, Iterable, Sequence
from contextlib import _GeneratorContextManager
from io import BytesIO
from pathlib import PurePath
from re import Pattern
from typing import Any, ClassVar, Final, Literal, NamedTuple, overload
from typing_extensions import TypeAlias, deprecated

from fpdf import ViewerPreferences
from fpdf.outline import OutlineSection
from PIL import Image

from .annotations import AnnotationDict, PDFEmbeddedFile
from .drawing import DeviceGray, DeviceRGB, DrawingContext, PaintedPath
from .enums import (
    AccessPermission,
    Align,
    AnnotationFlag,
    AnnotationName,
    Corner,
    EncryptionMethod,
    FileAttachmentAnnotationName,
    MethodReturnValue,
    PageLabelStyle,
    PageLayout,
    PageMode,
    PageOrientation,
    PathPaintRule,
    RenderStyle,
    TableBordersLayout,
    TableCellFillMode,
    TableHeadingsDisplay,
    TextDirection,
    TextEmphasis,
    TextMarkupType,
    TextMode as TextMode,
    VAlign,
    WrapMode as WrapMode,
    XPos as XPos,
    YPos as YPos,
    _Align,
)
from .errors import FPDFException as FPDFException
from .fonts import CoreFont, FontFace, TextStyle, TitleStyle as TitleStyle, TTFFont
from .graphics_state import GraphicsStateMixin
from .html import HTML2FPDF
from .image_datastructures import (
    ImageCache,
    ImageInfo as ImageInfo,
    RasterImageInfo as RasterImageInfo,
    VectorImageInfo as VectorImageInfo,
    _TextAlign,
)
from .output import OutputProducer, PDFPage
from .recorder import FPDFRecorder
from .structure_tree import StructureTreeBuilder
from .syntax import DestinationXYZ
from .table import Table
from .transitions import Transition
from .util import Padding, _Unit

__all__ = [
    "FPDF",
    "XPos",
    "YPos",
    "get_page_format",
    "ImageInfo",
    "RasterImageInfo",
    "VectorImageInfo",
    "TextMode",
    "TitleStyle",
    "PAGE_FORMATS",
]

_Orientation: TypeAlias = Literal["", "portrait", "p", "P", "landscape", "l", "L"]
_Format: TypeAlias = Literal["", "a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"]
_FontStyle: TypeAlias = Literal["", "B", "I", "BI"]
_FontStyles: TypeAlias = Literal["", "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB"]

FPDF_VERSION: Final[str]
PAGE_FORMATS: dict[_Format, tuple[float, float]]

class ToCPlaceholder(NamedTuple):
    render_function: Callable[[FPDF, list[OutlineSection]], object]
    start_page: int
    y: int
    page_orientation: str
    pages: int = 1

def get_page_format(format: _Format | tuple[float, float], k: float | None = None) -> tuple[float, float]:
    """
    Return page width and height size in points.

    Throws FPDFPageFormatException

    `format` can be either a 2-tuple or one of 'a3', 'a4', 'a5', 'letter', or
    'legal'.

    If format is a tuple, then the return value is the tuple's values
    given in the units specified on this document in the constructor,
    multiplied by the corresponding scale factor `k`, taken from instance
    variable `self.k`.

    If format is a string, the (width, height) tuple returned is in points.
    For a width and height of 8.5 * 11, 72 dpi is assumed, so the value
    returned is (8.5 * 72, 11 * 72), or (612, 792). Additional formats can be
    added by adding fields to the `PAGE_FORMATS` dictionary with a
    case insensitive key (the name of the new format) and 2-tuple value of
    (width, height) in dots per inch with a 72 dpi resolution.
    """
    ...

class FPDF(GraphicsStateMixin):
    """PDF Generation class"""
    MARKDOWN_BOLD_MARKER: ClassVar[str]
    MARKDOWN_ITALICS_MARKER: ClassVar[str]
    MARKDOWN_UNDERLINE_MARKER: ClassVar[str]
    MARKDOWN_ESCAPE_CHARACTER: ClassVar[str]
    MARKDOWN_LINK_REGEX: ClassVar[Pattern[str]]
    MARKDOWN_LINK_COLOR: ClassVar[Incomplete | None]
    MARKDOWN_LINK_UNDERLINE: ClassVar[bool]

    HTML2FPDF_CLASS: ClassVar[type[HTML2FPDF]]

    page: int
    pages: dict[int, PDFPage]
    fonts: dict[str, CoreFont | TTFFont]
    fonts_used_per_page_number: dict[int, set[int]]
    links: dict[int, DestinationXYZ]
    embedded_files: list[PDFEmbeddedFile]
    image_cache: ImageCache
    images_used_per_page_number: dict[int, set[int]]

    in_footer: bool
    str_alias_nb_pages: str

    xmp_metadata: str | None
    page_duration: int
    page_transition: Incomplete | None
    allow_images_transparency: bool
    oversized_images: Incomplete | None
    oversized_images_ratio: float
    struct_builder: StructureTreeBuilder
    toc_placeholder: ToCPlaceholder | None
    in_toc_rendering: bool
    title: str | None
    section_title_styles: dict[int, TextStyle]

    core_fonts: dict[str, str]
    core_fonts_encoding: str
    font_aliases: dict[str, str]
    k: float

    page_background: Incomplete | None

    dw_pt: float
    dh_pt: float
    def_orientation: Literal["P", "L"]
    x: float
    y: float
    l_margin: float
    t_margin: float
    c_margin: float
    viewer_preferences: ViewerPreferences | None
    compress: bool
    pdf_version: str
    creation_date: datetime.datetime
    graphics_style_names_per_page_number: dict[int, set[str]]

    buffer: bytearray | None

    # Set during call to _set_orientation(), called from __init__().
    cur_orientation: PageOrientation
    w_pt: float
    h_pt: float
    w: float
    h: float

    def __init__(
        self,
        orientation: _Orientation = "portrait",
        unit: _Unit | float = "mm",
        format: _Format | tuple[float, float] = "A4",
        font_cache_dir: Literal["DEPRECATED"] = "DEPRECATED",
    ) -> None:
        """
        Args:
            orientation (str): possible values are "portrait" (can be abbreviated "P")
                or "landscape" (can be abbreviated "L"). Default to "portrait".
            unit (str, int, float): possible values are "pt", "mm", "cm", "in", or a number.
                A point equals 1/72 of an inch, that is to say about 0.35 mm (an inch being 2.54 cm).
                This is a very common unit in typography; font sizes are expressed in this unit.
                If given a number, then it will be treated as the number of points per unit.  (eg. 72 = 1 in)
                Default to "mm".
            format (str): possible values are "a3", "a4", "a5", "letter", "legal" or a tuple
                (width, height) expressed in the given unit. Default to "a4".
            font_cache_dir (Path or str): [**DEPRECATED since v2.5.1**] unused
        """
        ...
    def set_encryption(
        self,
        owner_password: str,
        user_password: str | None = None,
        encryption_method: EncryptionMethod | str = ...,
        permissions: AccessPermission = ...,
        encrypt_metadata: bool = False,
    ) -> None:
        """
        Activate encryption of the document content.

        Args:
            owner_password (str): mandatory. The owner password allows to perform any change on the document,
                including removing all encryption and access permissions.
            user_password (str): optional. If a user password is set, the content of the document will be encrypted
                and a password prompt displayed when a user opens the document.
                The document will only be displayed after either the user or owner password is entered.
            encryption_method (fpdf.enums.EncryptionMethod, str): algorithm to be used to encrypt the document.
                Defaults to RC4.
            permissions (fpdf.enums.AccessPermission): specify access permissions granted
                when the document is opened with user access. Defaults to ALL.
            encrypt_metadata (bool): whether to also encrypt document metadata (author, creation date, etc.).
                Defaults to False.
        """
        ...
    # args and kwargs are passed to HTML2FPDF_CLASS constructor.
    def write_html(self, text: str, *args: Any, **kwargs: Any) -> None:
        """
        Parse HTML and convert it to PDF.
        cf. https://py-pdf.github.io/fpdf2/HTML.html

        Args:
            text (str): HTML content to render
            image_map (function): an optional one-argument function that map `<img>` "src" to new image URLs
            li_tag_indent (int): [**DEPRECATED since v2.7.9**]
                numeric indentation of `<li>` elements - Set `tag_styles` instead
            dd_tag_indent (int): [**DEPRECATED since v2.7.9**]
                numeric indentation of `<dd>` elements - Set `tag_styles` instead
            table_line_separators (bool): enable horizontal line separators in `<table>`. Defaults to `False`.
            ul_bullet_char (str): bullet character preceding `<li>` items in `<ul>` lists.
                Can also be configured using the HTML `type` attribute of `<ul>` tags.
            li_prefix_color (tuple, str, fpdf.drawing.DeviceCMYK, fpdf.drawing.DeviceGray, fpdf.drawing.DeviceRGB): color for bullets
                or numbers preceding `<li>` tags. This applies to both `<ul>` & `<ol>` lists.
            heading_sizes (dict): [**DEPRECATED since v2.7.9**]
                font size per heading level names ("h1", "h2"...) - Set `tag_styles` instead
            pre_code_font (str): [**DEPRECATED since v2.7.9**]
                font to use for `<pre>` & `<code>` blocks - Set `tag_styles` instead
            warn_on_tags_not_matching (bool): control warnings production for unmatched HTML tags. Defaults to `True`.
            tag_indents (dict): [**DEPRECATED since v2.7.10**]
                mapping of HTML tag names to numeric values representing their horizontal left identation. - Set `tag_styles` instead
            tag_styles (dict[str, fpdf.fonts.TextStyle]): mapping of HTML tag names to `fpdf.TextStyle` or `fpdf.FontFace` instances
        """
        ...
    @property
    def emphasis(self) -> TextEmphasis:
        """The current text emphasis: bold, italics and/or underlined."""
        ...
    @property
    def is_ttf_font(self) -> bool: ...
    @property
    def page_mode(self) -> PageMode: ...
    @property
    def epw(self) -> float:
        """Effective page width: the page width minus its horizontal margins."""
        ...
    @property
    def eph(self) -> float:
        """Effective page height: the page height minus its vertical margins."""
        ...
    @property
    def pages_count(self) -> int:
        """Returns the total pages of the document."""
        ...
    def set_margin(self, margin: float) -> None:
        """
        Sets the document right, left, top & bottom margins to the same value.

        Args:
            margin (float): margin in the unit specified to FPDF constructor
        """
        ...
    def set_margins(self, left: float, top: float, right: float = -1) -> None:
        """
        Sets the document left, top & optionaly right margins to the same value.
        By default, they equal 1 cm.
        Also sets the current FPDF.y on the page to this minimum vertical position.

        Args:
            left (float): left margin in the unit specified to FPDF constructor
            top (float): top margin in the unit specified to FPDF constructor
            right (float): optional right margin in the unit specified to FPDF constructor
        """
        ...
    def set_left_margin(self, margin: float) -> None:
        """
        Sets the document left margin.
        Also sets the current FPDF.x on the page to this minimum horizontal position.

        Args:
            margin (float): margin in the unit specified to FPDF constructor
        """
        ...
    def set_top_margin(self, margin: float) -> None:
        """
        Sets the document top margin.

        Args:
            margin (float): margin in the unit specified to FPDF constructor
        """
        ...
    r_margin: float
    def set_right_margin(self, margin: float) -> None:
        """
        Sets the document right margin.

        Args:
            margin (float): margin in the unit specified to FPDF constructor
        """
        ...
    auto_page_break: bool
    b_margin: float
    page_break_trigger: float
    def set_auto_page_break(self, auto: bool, margin: float = 0) -> None:
        """
        Set auto page break mode and triggering bottom margin.
        By default, the mode is on and the bottom margin is 2 cm.

        Args:
            auto (bool): enable or disable this mode
            margin (float): optional bottom margin (distance from the bottom of the page)
                in the unit specified to FPDF constructor
        """
        ...
    @property
    def default_page_dimensions(self) -> tuple[float, float]:
        """Return a pair (width, height) in the unit specified to FPDF constructor"""
        ...
    zoom_mode: Literal["fullpage", "fullwidth", "real", "default"] | float
    page_layout: PageLayout | None
    def set_display_mode(
        self,
        zoom: Literal["fullpage", "fullwidth", "real", "default"] | float,
        layout: Literal["single", "continuous", "two", "default"] = "continuous",
    ) -> None:
        """
        Defines the way the document is to be displayed by the viewer.

        It allows to set the zoom level: pages can be displayed entirely on screen,
        occupy the full width of the window, use the real size,
        be scaled by a specific zooming factor or use the viewer default (configured in its Preferences menu).

        The page layout can also be specified: single page at a time, continuous display, two columns or viewer default.

        Args:
            zoom: either "fullpage", "fullwidth", "real", "default",
                or a number indicating the zooming factor to use, interpreted as a percentage.
                The zoom level set by default is "default".
            layout (fpdf.enums.PageLayout, str): allowed layout aliases are "single", "continuous", "two" or "default",
                meaning to use the viewer default mode.
                The layout set by default is "continuous".
        """
        ...
    def set_text_shaping(
        self,
        use_shaping_engine: bool = True,
        features: dict[str, bool] | None = None,
        direction: Literal["ltr", "rtl"] | TextDirection | None = None,
        script: str | None = None,
        language: str | None = None,
    ) -> None: ...
    def set_compression(self, compress: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    lang: str
    def set_lang(self, lang: str) -> None:
        """
        A language identifier specifying the natural language for all text in the document
        except where overridden by language specifications for structure elements or marked content.
        A language identifier can either be the empty text string, to indicate that the language is unknown,
        or a Language-Tag as defined in RFC 3066, "Tags for the Identification of Languages".

        Args:
            lang (str): the document main language
        """
        ...
    subject: str
    def set_subject(self, subject: str) -> None:
        """
        Defines the subject of the document.

        Args:
            subject (str): the document main subject
        """
        ...
    author: str
    def set_author(self, author: str) -> None:
        """
        Defines the author of the document.

        Args:
            author(str): the name of the author
        """
        ...
    keywords: str
    def set_keywords(self, keywords: str) -> None:
        """
        Associate keywords with the document

        Args:
            keywords (str): a space-separated list of words
        """
        ...
    creator: str
    def set_creator(self, creator: str) -> None:
        """
        Defines the creator of the document.
        This is typically the name of the application that generates the PDF.

        Args:
            creator (str): name of the PDF creator
        """
        ...
    producer: str
    def set_producer(self, producer: str) -> None:
        """Producer of document"""
        ...
    def set_creation_date(self, date: datetime.datetime) -> None:
        """Sets Creation of Date time, or current time if None given."""
        ...
    def set_xmp_metadata(self, xmp_metadata: str) -> None: ...
    def set_doc_option(self, opt: str, value: str) -> None: ...
    def set_image_filter(self, image_filter: str) -> None: ...
    def alias_nb_pages(self, alias: str = "{nb}") -> None: ...
    def set_page_label(
        self, label_style: PageLabelStyle | str | None = None, label_prefix: str | None = None, label_start: int | None = None
    ) -> None: ...
    def add_page(
        self,
        orientation: _Orientation = "",
        format: _Format | tuple[float, float] = "",
        same: bool = False,
        duration: float = 0,
        transition: Transition | None = None,
        label_style: PageLabelStyle | str | None = None,
        label_prefix: str | None = None,
        label_start: int | None = None,
    ) -> None: ...
    def header(self) -> None: ...
    def footer(self) -> None: ...
    def page_no(self) -> int: ...
    def get_page_label(self) -> str: ...
    def set_draw_color(self, r: int, g: int = -1, b: int = -1) -> None: ...
    def set_fill_color(self, r: int, g: int = -1, b: int = -1) -> None: ...
    def set_text_color(self, r: int, g: int = -1, b: int = -1) -> None: ...
    def get_string_width(self, s: str, normalized: bool = False, markdown: bool = False) -> float: ...
    def set_line_width(self, width: float) -> None: ...
    def set_page_background(self, background) -> None: ...
    def drawing_context(self, debug_stream: Incomplete | None = None) -> _GeneratorContextManager[DrawingContext]: ...
    def new_path(
        self, x: float = 0, y: float = 0, paint_rule: PathPaintRule = ..., debug_stream: Incomplete | None = None
    ) -> _GeneratorContextManager[PaintedPath]:
        """
        Create a path for appending lines and curves to.

        Args:
            x (float): Abscissa of the path starting point
            y (float): Ordinate of the path starting point
            paint_rule (PathPaintRule): Optional choice of how the path should
                be painted. The default (AUTO) automatically selects stroke/fill based
                on the path style settings.
            debug_stream (TextIO): print a pretty tree of all items to be rendered
                to the provided stream. To store the output in a string, use
                `io.StringIO`.
        """
        ...
    def draw_path(self, path: PaintedPath, debug_stream: Incomplete | None = None) -> None:
        """
        Add a pre-constructed path to the document.

        Args:
            path (drawing.PaintedPath): the path to be drawn.
            debug_stream (TextIO): print a pretty tree of all items to be rendered
                to the provided stream. To store the output in a string, use
                `io.StringIO`.
        """
        ...
    def set_dash_pattern(self, dash: float = 0, gap: float = 0, phase: float = 0) -> None:
        """
        Set the current dash pattern for lines and curves.

        Args:
            dash (float): The length of the dashes in current units.

            gap (float): The length of the gaps between dashes in current units.
                If omitted, the dash length will be used.

            phase (float): Where in the sequence to start drawing.

        Omitting 'dash' (= 0) resets the pattern to a solid line.
        """
        ...
    def line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        Draw a line between two points.

        Args:
            x1 (float): Abscissa of first point
            y1 (float): Ordinate of first point
            x2 (float): Abscissa of second point
            y2 (float): Ordinate of second point
        """
        ...
    def polyline(
        self,
        point_list: list[tuple[float, float]],
        fill: bool = False,
        polygon: bool = False,
        style: RenderStyle | str | None = None,
    ) -> None:
        """
        Draws lines between two or more points.

        Args:
            point_list (list of tuples): List of Abscissa and Ordinate of
                                        segments that should be drawn
            fill (bool): [**DEPRECATED since v2.5.4**] Use `style="F"` or `style="DF"` instead
            polygon (bool): If true, close path before stroking, to fill the inside of the polyline
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Possible values are:

            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def polygon(
        self, point_list: list[tuple[float, float]], fill: bool = False, style: RenderStyle | str | None = None
    ) -> None:
        """
        Outputs a polygon defined by three or more points.

        Args:
            point_list (list of tuples): List of coordinates defining the polygon to draw
            fill (bool): [**DEPRECATED since v2.5.4**] Use `style="F"` or `style="DF"` instead
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Possible values are:

            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def dashed_line(self, x1, y1, x2, y2, dash_length: int = 1, space_length: int = 1) -> None:
        """
        Draw a dashed line between two points.

        Args:
            x1 (float): Abscissa of first point
            y1 (float): Ordinate of first point
            x2 (float): Abscissa of second point
            y2 (float): Ordinate of second point
            dash_length (float): Length of the dash
            space_length (float): Length of the space between 2 dashes

        .. deprecated:: 2.4.6
            Use `FPDF.set_dash_pattern()` and the normal drawing operations instead.
        """
        ...
    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        style: RenderStyle | str | None = None,
        round_corners: tuple[str, ...] | tuple[Corner, ...] | bool = False,
        corner_radius: float = 0,
    ) -> None:
        """
        Outputs a rectangle.
        It can be drawn (border only), filled (with no border) or both.

        Args:
            x (float): Abscissa of upper-left bounding box.
            y (float): Ordinate of upper-left bounding box.
            w (float): Width.
            h (float): Height.
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Possible values are:

            * `D` or empty string: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill

            round_corners (tuple of str, tuple of fpdf.enums.Corner, bool): Optional draw a rectangle with round corners.
            Possible values are:

            *`TOP_LEFT`: a rectangle with round top left corner
            *`TOP_RIGHT`: a rectangle with round top right corner
            *`BOTTOM_LEFT`: a rectangle with round bottom left corner
            *`BOTTOM_RIGHT`: a rectangle with round bottom right corner
            *`True`: a rectangle with all round corners
            *`False`: a rectangle with no round corners

            corner_radius: Optional radius of the corners
        """
        ...
    def ellipse(self, x: float, y: float, w: float, h: float, style: RenderStyle | str | None = None) -> None:
        """
        Outputs an ellipse.
        It can be drawn (border only), filled (with no border) or both.

        Args:
            x (float): Abscissa of upper-left bounding box.
            y (float): Ordinate of upper-left bounding box.
            w (float): Width
            h (float): Height
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Possible values are:

            * `D` or empty string: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def circle(self, x: float, y: float, radius: float, style: RenderStyle | str | None = None) -> None:
        """
        Outputs a circle.
        It can be drawn (border only), filled (with no border) or both.

        WARNING: This method changed parameters in [release 2.8.0](https://github.com/py-pdf/fpdf2/releases/tag/2.8.0)

        Args:
            x (float): Abscissa of upper-left bounding box.
            y (float): Ordinate of upper-left bounding box.
            radius (float): Radius of the circle.
            style (str): Style of rendering. Possible values are:

            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def regular_polygon(
        self,
        x: float,
        y: float,
        numSides: int,
        polyWidth: float,
        rotateDegrees: float = 0,
        style: RenderStyle | str | None = None,
    ):
        """
        Outputs a regular polygon with n sides
        It can be rotated
        Style can also be applied (fill, border...)

        Args:
            x (float): Abscissa of upper-left bounding box.
            y (float): Ordinate of upper-left bounding box.
            numSides (int): Number of sides for polygon.
            polyWidth (float): Width of the polygon.
            rotateDegrees (float): Optional degree amount to rotate polygon.
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Possible values are:

            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def star(
        self,
        x: float,
        y: float,
        r_in: float,
        r_out: float,
        corners: int,
        rotate_degrees: float = 0,
        style: RenderStyle | str | None = None,
    ):
        """
        Outputs a regular star with n corners.
        It can be rotated.
        It can be drawn (border only), filled (with no border) or both.

        Args:
            x (float): Abscissa of star's centre.
            y (float): Ordinate of star's centre.
            r_in (float): radius of internal circle.
            r_out (float): radius of external circle.
            corners (int): number of star's corners.
            rotate_degrees (float): Optional degree amount to rotate star clockwise.

            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Possible values are:
            * `D`: draw border. This is the default value.
            * `F`: fill.
            * `DF` or `FD`: draw and fill.
        """
        ...
    def arc(
        self,
        x: float,
        y: float,
        a: float,
        start_angle: float,
        end_angle: float,
        b: float | None = None,
        inclination: float = 0,
        clockwise: bool = False,
        start_from_center: bool = False,
        end_at_center: bool = False,
        style: RenderStyle | str | None = None,
    ) -> None:
        """
        Outputs an arc.
        It can be drawn (border only), filled (with no border) or both.

        Args:
            a (float): Semi-major axis diameter.
            b (float): Semi-minor axis diameter, if None, equals to a (default: None).
            start_angle (float): Start angle of the arc (in degrees).
            end_angle (float): End angle of the arc (in degrees).
            inclination (float): Inclination of the arc in respect of the x-axis (default: 0).
            clockwise (bool): Way of drawing the arc (True: clockwise, False: counterclockwise) (default: False).
            start_from_center (bool): Start drawing from the center of the circle (default: False).
            end_at_center (bool): End drawing at the center of the circle (default: False).
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Allowed values are:

            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def solid_arc(
        self,
        x: float,
        y: float,
        a: float,
        start_angle: float,
        end_angle: float,
        b: float | None = None,
        inclination: float = 0,
        clockwise: bool = False,
        style: RenderStyle | str | None = None,
    ) -> None:
        """
        Outputs a solid arc. A solid arc combines an arc and a triangle to form a pie slice
        It can be drawn (border only), filled (with no border) or both.

        Args:
            x (float): Abscissa of upper-left bounding box.
            y (float): Ordinate of upper-left bounding box.
            a (float): Semi-major axis.
            b (float): Semi-minor axis, if None, equals to a (default: None).
            start_angle (float): Start angle of the arc (in degrees).
            end_angle (float): End angle of the arc (in degrees).
            inclination (float): Inclination of the arc in respect of the x-axis (default: 0).
            clockwise (bool): Way of drawing the arc (True: clockwise, False: counterclockwise) (default: False).
            style (str): Style of rendering. Possible values are:

            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def bezier(
        self,
        point_list: Sequence[tuple[int, int]],
        closed: bool = False,
        style: RenderStyle | Literal["D", "F", "DF", "FD"] | None = None,
    ) -> None:
        """
        Outputs a quadratic or cubic Bézier curve, defined by three or four coordinates.

        Args:
            point_list (list of tuples): List of Abscissa and Ordinate of
                                        segments that should be drawn. Should be
                                        three or four tuples. The first and last
                                        points are the start and end point. The
                                        middle point(s) are the control point(s).
            closed (bool): True to draw the curve as a closed path, False (default)
                                        for it to be drawn as an open path.
            style (fpdf.enums.RenderStyle, str): Optional style of rendering. Allowed values are:
            * `D` or None: draw border. This is the default value.
            * `F`: fill
            * `DF` or `FD`: draw and fill
        """
        ...
    def add_font(
        self,
        family: str | None = None,
        style: _FontStyle = "",
        fname: str | PurePath | None = None,
        uni: bool | Literal["DEPRECATED"] = "DEPRECATED",
    ) -> None:
        """
        Imports a TrueType or OpenType font and makes it available
        for later calls to the `FPDF.set_font()` method.

        You will find more information on the "Unicode" documentation page.

        Args:
            family (str): optional name of the font family. Used as a reference for `FPDF.set_font()`.
                If not provided, use the base name of the `fname` font path, without extension.
            style (str): font style. "" for regular, include 'B' for bold, and/or 'I' for italic.
            fname (str): font file name. You can specify a relative or full path.
                If the file is not found, it will be searched in `FPDF_FONT_DIR`.
            uni (bool): [**DEPRECATED since 2.5.1**] unused
        """
        ...
    def set_font(self, family: str | None = None, style: _FontStyles = "", size: int = 0) -> None:
        """
        Sets the font used to print character strings.
        It is mandatory to call this method at least once before printing text.

        Default encoding is not specified, but all text writing methods accept only
        unicode for external fonts and one byte encoding for standard.

        Standard fonts use `Latin-1` encoding by default, but Windows
        encoding `cp1252` (Western Europe) can be used with
        `self.core_fonts_encoding = encoding`.

        The font specified is retained from page to page.
        The method can be called before the first page is created.

        Args:
            family (str): name of a font added with `FPDF.add_font`,
                or name of one of the 14 standard "PostScript" fonts:
                Courier (fixed-width), Helvetica (sans serif), Times (serif),
                Symbol (symbolic) or ZapfDingbats (symbolic)
                If an empty string is provided, the current family is retained.
            style (str): empty string (by default) or a combination
                of one or several letters among B (bold), I (italic) and U (underline).
                Bold and italic styles do not apply to Symbol and ZapfDingbats fonts.
            size (float): in points. The default value is the current size.
        """
        ...
    def set_font_size(self, size: float) -> None:
        """
        Configure the font size in points

        Args:
            size (float): font size in points
        """
        ...
    def set_char_spacing(self, spacing: float) -> None:
        """
        Sets horizontal character spacing.
        A positive value increases the space between characters, a negative value
        reduces it (which may result in glyph overlap).
        By default, no spacing is set (which is equivalent to a value of 0).

        Args:
            spacing (float): horizontal spacing in document units
        """
        ...
    def set_stretching(self, stretching: float) -> None:
        """
        Sets horizontal font stretching.
        By default, no stretching is set (which is equivalent to a value of 100).

        Args:
            stretching (float): horizontal stretching (scaling) in percents.
        """
        ...
    def set_fallback_fonts(self, fallback_fonts: Iterable[str], exact_match: bool = True) -> None:
        """
        Allows you to specify a list of fonts to be used if any character is not available on the font currently set.
        Detailed documentation: https://py-pdf.github.io/fpdf2/Unicode.html#fallback-fonts

        Args:
            fallback_fonts: sequence of fallback font IDs
            exact_match (bool): when a glyph cannot be rendered uing the current font,
                fpdf2 will look for a fallback font matching the current character emphasis (bold/italics).
                If it does not find such matching font, and `exact_match` is True, no fallback font will be used.
                If it does not find such matching font, and `exact_match` is False, a fallback font will still be used.
                To get even more control over this logic, you can also override `FPDF.get_fallback_font()`
        """
        ...
    def add_link(self, y: float = 0, x: float = 0, page: int = -1, zoom: float | Literal["null"] = "null") -> int:
        """
        Creates a new internal link and returns its identifier.
        An internal link is a clickable area which directs to another place within the document.

        The identifier can then be passed to the `FPDF.cell()`, `FPDF.write()`, `FPDF.image()`
        or `FPDF.link()` methods.

        Args:
            y (float): optional ordinate of target position.
                The default value is 0 (top of page).
            x (float): optional abscissa of target position.
                The default value is 0 (top of page).
            page (int): optional number of target page.
                -1 indicates the current page, which is the default value.
            zoom (float): optional new zoom level after following the link.
                Currently ignored by Sumatra PDF Reader, but observed by Adobe Acrobat reader.
        """
        ...
    def set_link(self, link, y: float = 0, x: float = 0, page: int = -1, zoom: float | Literal["null"] = "null") -> None:
        """
        Defines the page and position a link points to.

        Args:
            link (int): a link identifier returned by `FPDF.add_link()`.
            y (float): optional ordinate of target position.
                The default value is 0 (top of page).
            x (float): optional abscissa of target position.
                The default value is 0 (top of page).
            page (int): optional number of target page.
                -1 indicates the current page, which is the default value.
            zoom (float): optional new zoom level after following the link.
                Currently ignored by Sumatra PDF Reader, but observed by Adobe Acrobat reader.
        """
        ...
    def link(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        link: str | int,
        alt_text: str | None = None,
        *,
        border_width: int = 0,
        **kwargs,  # accepts AnnotationDict arguments
    ) -> AnnotationDict: ...
    def embed_file(
        self,
        file_path: StrPath | None = None,
        bytes: bytes | None = None,
        basename: str | None = None,
        modification_date: datetime.datetime | None = None,
        *,
        creation_date: datetime.datetime | None = ...,
        desc: str = ...,
        compress: bool = ...,
        checksum: bool = ...,
    ) -> str:
        """
        Embed a file into the PDF document

        Args:
            file_path (str or Path): filesystem path to the existing file to embed
            bytes (bytes): optional, as an alternative to file_path, bytes content of the file to embed
            basename (str): optional, required if bytes is provided, file base name
            creation_date (datetime): date and time when the file was created
            modification_date (datetime): date and time when the file was last modified
            desc (str): optional description of the file
            compress (bool): enabled zlib compression of the file - False by default
            checksum (bool): insert a MD5 checksum of the file content - False by default

        Returns: a PDFEmbeddedFile instance, with a .basename string attribute representing the internal file name
        """
        ...
    def file_attachment_annotation(
        self,
        file_path: StrPath,
        x: float,
        y: float,
        w: float = 1,
        h: float = 1,
        name: FileAttachmentAnnotationName | str | None = None,
        flags: Iterable[AnnotationFlag | str] = ...,
        *,
        bytes: bytes | None = ...,
        basename: str | None = ...,
        creation_date: datetime.datetime | None = ...,
        modification_date: datetime.datetime | None = ...,
        desc: str = ...,
        compress: bool = ...,
        checksum: bool = ...,
    ) -> AnnotationDict:
        """
        Puts a file attachment annotation on a rectangular area of the page.

        Args:
            file_path (str or Path): filesystem path to the existing file to embed
            x (float): horizontal position (from the left) to the left side of the link rectangle
            y (float): vertical position (from the top) to the bottom side of the link rectangle
            w (float): optional width of the link rectangle
            h (float): optional height of the link rectangle
            name (fpdf.enums.FileAttachmentAnnotationName, str): optional icon that shall be used in displaying the annotation
            flags (Tuple[fpdf.enums.AnnotationFlag], Tuple[str]): optional list of flags defining annotation properties
            bytes (bytes): optional, as an alternative to file_path, bytes content of the file to embed
            basename (str): optional, required if bytes is provided, file base name
            creation_date (datetime): date and time when the file was created
            modification_date (datetime): date and time when the file was last modified
            desc (str): optional description of the file
            compress (bool): enabled zlib compression of the file - False by default
            checksum (bool): insert a MD5 checksum of the file content - False by default
        """
        ...
    def text_annotation(
        self,
        x: float,
        y: float,
        text: str,
        w: float = 1,
        h: float = 1,
        name: AnnotationName | str | None = None,
        *,
        flags: tuple[AnnotationFlag, ...] | tuple[str, ...] = ...,
        **kwargs,  # accepts AnnotationDict arguments
    ) -> AnnotationDict: ...
    def free_text_annotation(
        self,
        text: str,
        x: float | None = None,
        y: float | None = None,
        w: float | None = None,
        h: float | None = None,
        *,
        flags: tuple[AnnotationFlag, ...] | tuple[str, ...] = ...,
        **kwargs,  # accepts AnnotationDict arguments
    ) -> AnnotationDict: ...
    def add_action(
        self, action, x: float, y: float, w: float, h: float, **kwargs  # accepts AnnotationDict arguments
    ) -> AnnotationDict: ...
    def highlight(
        self,
        text: str,
        type: TextMarkupType | str = "Highlight",
        color: tuple[float, float, float] = (1, 1, 0),
        modification_time: datetime.datetime | None = None,
        *,
        title: str | None = None,
        **kwargs,  # accepts AnnotationDict arguments
    ) -> _GeneratorContextManager[None]: ...
    add_highlight = highlight
    def add_text_markup_annotation(
        self,
        type: str,
        text: str,
        quad_points: Sequence[int],
        color: tuple[float, float, float] = (1, 1, 0),
        modification_time: datetime.datetime | None = None,
        page: int | None = None,
        *,
        title: str | None = None,
        **kwargs,  # accepts AnnotationDict arguments
    ) -> AnnotationDict: ...
    def ink_annotation(
        self,
        coords: Iterable[Incomplete],
        text: str = "",
        color: Sequence[float] = (1, 1, 0),
        border_width: float = 1,
        *,
        title: str | None = None,
        **kwargs,  # accepts AnnotationDict arguments
    ) -> AnnotationDict: ...
    def text(self, x: float, y: float, text: str = "") -> None: ...
    def rotate(self, angle: float, x: float | None = None, y: float | None = None) -> None: ...
    def rotation(self, angle: float, x: float | None = None, y: float | None = None) -> _GeneratorContextManager[None]: ...
    def skew(
        self, ax: float = 0, ay: float = 0, x: float | None = None, y: float | None = None
    ) -> _GeneratorContextManager[None]:
        """
        Method to perform a skew transformation originating from a given center.
        It must be used as a context-manager using `with`:

            with skew(ax=15, ay=15, x=x, y=y):
                pdf.something()

        The skew transformation affects all elements which are printed inside the indented
        context (with the exception of clickable areas).

        Args:
            ax (float): angle of skew in the horizontal direction in degrees
            ay (float): angle of skew in the vertical direction in degrees
            x (float): abscissa of the center of the skew transformation
            y (float): ordinate of the center of the skew transformation
        """
        ...
    def mirror(self, origin, angle) -> Generator[None]:
        """
        Method to perform a reflection transformation over a given mirror line.
        It must be used as a context-manager using `with`:

            with mirror(origin=(15,15), angle="SOUTH"):
                pdf.something()

        The mirror transformation affects all elements which are rendered inside the indented
        context (with the exception of clickable areas).

        Args:
            origin (float, Sequence(float, float)): a point on the mirror line
            angle: (fpdf.enums.Angle): the direction of the mirror line
        """
        ...
    def local_context(
        self,
        *,
        font_family: Incomplete | None = None,
        font_style: Incomplete | None = None,
        font_size_pt: Incomplete | None = None,
        line_width: Incomplete | None = None,
        draw_color: Incomplete | None = None,
        fill_color: Incomplete | None = None,
        text_color: Incomplete | None = None,
        dash_pattern: Incomplete | None = None,
        font_size=...,  # semi-deprecated, prefer font_size_pt
        char_vpos=...,
        char_spacing=...,
        current_font=...,
        denom_lift=...,
        denom_scale=...,
        font_stretching=...,
        nom_lift=...,
        nom_scale=...,
        sub_lift=...,
        sub_scale=...,
        sup_lift=...,
        sup_scale=...,
        text_mode=...,
        text_shaping=...,
        underline=...,
        paint_rule=...,
        allow_transparency=...,
        auto_close=...,
        intersection_rule=...,
        fill_opacity=...,
        stroke_color=...,
        stroke_opacity=...,
        blend_mode=...,
        stroke_width=...,
        stroke_cap_style=...,
        stroke_join_style=...,
        stroke_miter_limit=...,
        stroke_dash_pattern=...,
        stroke_dash_phase=...,
    ) -> _GeneratorContextManager[None]:
        """
        Creates a local graphics state, which won't affect the surrounding code.
        This method must be used as a context manager using `with`:

            with pdf.local_context():
                set_some_state()
                draw_some_stuff()

        The affected settings are those controlled by GraphicsStateMixin and drawing.GraphicsStyle:
            allow_transparency
            auto_close
            blend_mode
            char_vpos
            char_spacing
            dash_pattern
            denom_lift
            denom_scale
            draw_color
            fill_color
            fill_opacity
            font_family
            font_size
            font_size_pt
            font_style
            font_stretching
            intersection_rule
            line_width
            nom_lift
            nom_scale
            paint_rule
            stroke_cap_style
            stroke_join_style
            stroke_miter_limit
            stroke_opacity
            sub_lift
            sub_scale
            sup_lift
            sup_scale
            text_color
            text_mode
            text_shaping
            underline

        Args:
            **kwargs: key-values settings to set at the beggining of this context.
        """
        ...
    @property
    def accept_page_break(self) -> bool:
        """
        Whenever a page break condition is met, this method is called,
        and the break is issued or not depending on the returned value.

        The default implementation returns a value according to the mode selected by `FPDF.set_auto_page_break()`.
        This method is called automatically and should not be called directly by the application.
        """
        ...
    def cell(
        self,
        w: float | None = None,
        h: float | None = None,
        text: str = "",
        border: bool | Literal[0, 1] | str = 0,
        ln: int | Literal["DEPRECATED"] = "DEPRECATED",
        align: str | Align = ...,
        fill: bool = False,
        link: str | int = "",
        center: bool = False,
        markdown: bool = False,
        new_x: XPos | str = ...,
        new_y: YPos | str = ...,
    ) -> bool:
        r"""
        Prints a cell (rectangular area) with optional borders, background color and
        character string. The upper-left corner of the cell corresponds to the current
        position. The text can be aligned or centered. After the call, the current
        position moves to the selected `new_x`/`new_y` position. It is possible to put a link
        on the text. A cell has an horizontal padding, on the left & right sides, defined by
        the.c_margin property.

        If automatic page breaking is enabled and the cell goes beyond the limit, a
        page break is performed before outputting.

        Args:
            w (float): Cell width. Default value: None, meaning to fit text width.
                If 0, the cell extends up to the right margin.
            h (float): Cell height. Default value: None, meaning an height equal
                to the current font size.
            text (str): String to print. Default value: empty string.
            border: Indicates if borders must be drawn around the cell.
                The value can be either a number (`0`: no border ; `1`: frame)
                or a string containing some or all of the following characters
                (in any order):
                `L`: left ; `T`: top ; `R`: right ; `B`: bottom. Default value: 0.
            new_x (fpdf.enums.XPos, str): New current position in x after the call. Default: RIGHT
            new_y (fpdf.enums.YPos, str): New current position in y after the call. Default: TOP
            ln (int): **DEPRECATED since 2.5.1**: Use `new_x` and `new_y` instead.
            align (fpdf.enums.Align, str): Set text alignment inside the cell.
                Possible values are: `L` or empty string: left align (default value) ;
                `C`: center; `X`: center around current x position; `R`: right align
            fill (bool): Indicates if the cell background must be painted (`True`)
                or transparent (`False`). Default value: False.
            link (str): optional link to add on the cell, internal
                (identifier returned by `FPDF.add_link`) or external URL.
            center (bool): center the cell horizontally on the page.
            markdown (bool): enable minimal markdown-like markup to render part
                of text as bold / italics / underlined. Supports `\` as escape character. Default to False.
            txt (str): [**DEPRECATED since v2.7.6**] String to print. Default value: empty string.

        Returns: a boolean indicating if page break was triggered
        """
        ...
    def get_fallback_font(self, char: str, style: str = "") -> str | None:
        """
        Returns which fallback font has the requested glyph.
        This method can be overriden to provide more control than the `select_mode` parameter
        of `FPDF.set_fallback_fonts()` provides.
        """
        ...
    def will_page_break(self, height: float) -> bool:
        """
        Let you know if adding an element will trigger a page break,
        based on its height and the current ordinate (`y` position).

        Args:
            height (float): height of the section that would be added, e.g. a cell

        Returns: a boolean indicating if a page break would occur
        """
        ...
    def multi_cell(
        self,
        w: float,
        h: float | None = None,
        text: str = "",
        border: bool | Literal[0, 1] | str = 0,
        align: str | Align = ...,
        fill: bool = False,
        split_only: bool = False,
        link: str | int = "",
        ln: int | Literal["DEPRECATED"] = "DEPRECATED",
        max_line_height: float | None = None,
        markdown: bool = False,
        print_sh: bool = False,
        new_x: XPos | str = ...,
        new_y: YPos | str = ...,
        wrapmode: WrapMode = ...,
        dry_run: bool = False,
        output: MethodReturnValue | str | int = ...,
        center: bool = False,
        padding: int = 0,
    ):
        r"""
        This method allows printing text with line breaks. They can be automatic
        (breaking at the most recent space or soft-hyphen character) as soon as the text
        reaches the right border of the cell, or explicit (via the `\n` character).
        As many cells as necessary are stacked, one below the other.
        Text can be aligned, centered or justified. The cell block can be framed and
        the background painted. A cell has an horizontal padding, on the left & right sides,
        defined by the.c_margin property.

        Args:
            w (float): cell width. If 0, they extend up to the right margin of the page.
            h (float): height of a single line of text.  Default value: None, meaning to use the current font size.
            text (str): string to print.
            border: Indicates if borders must be drawn around the cell.
                The value can be either a number (`0`: no border ; `1`: frame)
                or a string containing some or all of the following characters
                (in any order):
                `L`: left ; `T`: top ; `R`: right ; `B`: bottom. Default value: 0.
            align (fpdf.enums.Align, str): Set text alignment inside the cell.
                Possible values are:
                `J`: justify (default value); `L` or empty string: left align;
                `C`: center; `X`: center around current x position; `R`: right align
            fill (bool): Indicates if the cell background must be painted (`True`)
                or transparent (`False`). Default value: False.
            split_only (bool): **DEPRECATED since 2.7.4**:
                Use `dry_run=True` and `output=("LINES",)` instead.
            link (str): optional link to add on the cell, internal
                (identifier returned by `add_link`) or external URL.
            new_x (fpdf.enums.XPos, str): New current position in x after the call. Default: RIGHT
            new_y (fpdf.enums.YPos, str): New current position in y after the call. Default: NEXT
            ln (int): **DEPRECATED since 2.5.1**: Use `new_x` and `new_y` instead.
            max_line_height (float): optional maximum height of each sub-cell generated
            markdown (bool): enable minimal markdown-like markup to render part
                of text as bold / italics / underlined. Supports `\` as escape character. Default to False.
            print_sh (bool): Treat a soft-hyphen (\u00ad) as a normal printable
                character, instead of a line breaking opportunity. Default value: False
            wrapmode (fpdf.enums.WrapMode): "WORD" for word based line wrapping (default),
                "CHAR" for character based line wrapping.
            dry_run (bool): if `True`, does not output anything in the document.
                Can be useful when combined with `output`.
            output (fpdf.enums.MethodReturnValue): defines what this method returns.
                If several enum values are joined, the result will be a tuple.
            txt (str): [**DEPRECATED since v2.7.6**] string to print.
            center (bool): center the cell horizontally on the page.
            padding (float or Sequence): padding to apply around the text. Default value: 0.
                When one value is specified, it applies the same padding to all four sides.
                When two values are specified, the first padding applies to the top and bottom, the second to
                the left and right. When three values are specified, the first padding applies to the top,
                the second to the right and left, the third to the bottom. When four values are specified,
                the paddings apply to the top, right, bottom, and left in that order (clockwise)
                If padding for left or right ends up being non-zero then respective c_margin is ignored.

        Center overrides values for horizontal padding

        Using `new_x=XPos.RIGHT, new_y=XPos.TOP, maximum height=pdf.font_size` is
        useful to build tables with multiline text in cells.

        Returns: a single value or a tuple, depending on the `output` parameter value
        """
        ...
    def write(
        self, h: float | None = None, text: str = "", link: str | int = "", print_sh: bool = False, wrapmode: WrapMode = ...
    ) -> bool:
        r"""
        Prints text from the current position.
        When the right margin is reached, a line break occurs at the most recent
        space or soft-hyphen character, and text continues from the left margin.
        A manual break happens any time the \n character is met,
        Upon method exit, the current position is left just at the end of the text.

        Args:
            h (float): line height. Default value: None, meaning to use the current font size.
            text (str): text content
            link (str): optional link to add on the text, internal
                (identifier returned by `FPDF.add_link`) or external URL.
            print_sh (bool): Treat a soft-hyphen (\u00ad) as a normal printable
                character, instead of a line breaking opportunity. Default value: False
            wrapmode (fpdf.enums.WrapMode): "WORD" for word based line wrapping (default),
                "CHAR" for character based line wrapping.
            txt (str): [**DEPRECATED since v2.7.6**] text content
        """
        ...
    def text_columns(
        self,
        text: str | None = None,
        img: str | None = None,
        img_fill_width: bool = False,
        ncols: int = 1,
        gutter: float = 10,
        balance: bool = False,
        text_align: str | _TextAlign | tuple[_TextAlign | str, ...] = "LEFT",
        line_height: float = 1,
        l_margin: float | None = None,
        r_margin: float | None = None,
        print_sh: bool = False,
        wrapmode: WrapMode = ...,
        skip_leading_spaces: bool = False,
    ):
        r"""
        Establish a layout with multiple columns to fill with text.
        Args:
            text (str, optional): A first piece of text to insert.
            ncols (int, optional): the number of columns to create. (Default: 1).
            gutter (float, optional): The distance between the columns. (Default: 10).
            balance: (bool, optional): Specify whether multiple columns should end at approximately
                the same height, if they don't fill the page. (Default: False)
            text_align (Align or str, optional): The alignment of the text within the region.
                (Default: "LEFT")
            line_height (float, optional): A multiplier relative to the font size changing the
                vertical space occupied by a line of text. (Default: 1.0).
            l_margin (float, optional): Override the current left page margin.
            r_margin (float, optional): Override the current right page margin.
            print_sh (bool, optional): Treat a soft-hyphen (\u00ad) as a printable character,
                instead of a line breaking opportunity. (Default: False)
            wrapmode (fpdf.enums.WrapMode, optional): "WORD" for word based line wrapping,
                "CHAR" for character based line wrapping. (Default: "WORD")
            skip_leading_spaces (bool, optional): On each line, any space characters at the
                beginning will be skipped if True. (Default: False)
        """
        ...
    def image(
        self,
        name: str | Image.Image | BytesIO | StrPath,
        x: float | Align | None = None,
        y: float | None = None,
        w: float = 0,
        h: float = 0,
        type: str = "",
        link: str | int = "",
        title: str | None = None,
        alt_text: str | None = None,
        dims: tuple[float, float] | None = None,
        keep_aspect_ratio: bool = False,
    ) -> RasterImageInfo | VectorImageInfo:
        """
        Put an image on the page.

        The size of the image on the page can be specified in different ways:
        * explicit width and height (expressed in user units)
        * one explicit dimension, the other being calculated automatically
          in order to keep the original proportions
        * no explicit dimension, in which case the image is put at 72 dpi.
        * explicit width and height (expressed in user units) and `keep_aspect_ratio=True`

        **Remarks**:
        * if an image is used several times, only one copy is embedded in the file.
        * when using an animated GIF, only the first frame is used.

        Args:
            name: either a string representing a file path to an image, an URL to an image,
                bytes, an io.BytesIO, or a instance of `PIL.Image.Image`
            x (float, fpdf.enums.Align): optional horizontal position where to put the image on the page.
                If not specified or equal to None, the current abscissa is used.
                `Align.C` can also be passed to center the image horizontally;
                and `Align.R` to place it along the right page margin
            y (float): optional vertical position where to put the image on the page.
                If not specified or equal to None, the current ordinate is used.
                After the call, the current ordinate is moved to the bottom of the image
            w (float): optional width of the image. If not specified or equal to zero,
                it is automatically calculated from the image size.
                Pass `pdf.epw` to scale horizontally to the full page width.
            h (float): optional height of the image. If not specified or equal to zero,
                it is automatically calculated from the image size.
                Pass `pdf.eph` to scale horizontally to the full page height.
            type (str): [**DEPRECATED since 2.2.0**] unused, will be removed in a later version.
            link (str): optional link to add on the image, internal
                (identifier returned by `FPDF.add_link`) or external URL.
            title (str): optional. Currently, never seem rendered by PDF readers.
            alt_text (str): optional alternative text describing the image,
                for accessibility purposes. Displayed by some PDF readers on hover.
            dims (Tuple[float]): optional dimensions as a tuple (width, height) to resize the image
                before storing it in the PDF. Note that those are the **intrinsic** image dimensions,
                but the image will still be rendered on the page with the width (`w`) and height (`h`)
                provided as parameters. Note also that the `.oversized_images` attribute of FPDF
                provides an automated way to auto-adjust those intrinsic image dimensions.
            keep_aspect_ratio (bool): ensure the image fits in the rectangle defined by `x`, `y`, `w` & `h`
                while preserving its original aspect ratio. Defaults to False.
                Only meaningful if both `w` & `h` are provided.

        If `y` is provided, this method will not trigger any page break;
        otherwise, auto page break detection will be performed.

        Returns: an instance of a subclass of `ImageInfo`.
        """
        ...
    def x_by_align(self, x: _Align, w: int, h: int, img_info: ImageInfo, keep_aspect_ratio: bool) -> int: ...
    @deprecated("Deprecated since 2.7.7; use fpdf.image_parsing.preload_image() instead")
    def preload_image(
        self, name: str | Image.Image | BytesIO, dims: tuple[float, float] | None = None
    ) -> tuple[str, Any, ImageInfo]:
        """
        Read an image and load it into memory.

        .. deprecated:: 2.7.7
            Use `fpdf.image_parsing.preload_image` instead.
        """
        ...
    def ln(self, h: float | None = None) -> None:
        """
        Line Feed.
        The current abscissa goes back to the left margin and the ordinate increases by
        the amount passed as parameter.

        Args:
            h (float): The height of the break.
                By default, the value equals the height of the last printed text line
                (except when written by `.text()`). If no text has been written yet to
                the document, then the current font height is used.
        """
        ...
    def get_x(self) -> float:
        """Returns the abscissa of the current position."""
        ...
    def set_x(self, x: float) -> None:
        """
        Defines the abscissa of the current position.
        If the value provided is negative, it is relative to the right of the page.

        Args:
            x (float): the new current abscissa
        """
        ...
    def get_y(self) -> float:
        """Returns the ordinate of the current position."""
        ...
    def set_y(self, y: float) -> None:
        """
        Moves the current abscissa back to the left margin and sets the ordinate.
        If the value provided is negative, it is relative to the bottom of the page.

        Args:
            y (float): the new current ordinate
        """
        ...
    def set_xy(self, x: float, y: float) -> None:
        """
        Defines the abscissa and ordinate of the current position.
        If the values provided are negative, they are relative respectively to the right and bottom of the page.

        Args:
            x (float): the new current abscissa
            y (float): the new current ordinate
        """
        ...
    def normalize_text(self, text: str) -> str:
        """Check that text input is in the correct format/encoding"""
        ...
    def sign_pkcs12(
        self,
        pkcs_filepath: str,
        password: bytes | None = None,
        hashalgo: str = "sha256",
        contact_info: str | None = None,
        location: str | None = None,
        signing_time: datetime.datetime | None = None,
        reason: str | None = None,
        flags: tuple[AnnotationFlag, ...] = ...,
    ) -> None:
        """
        Args:
            pkcs_filepath (str): file path to a .pfx or .p12 PKCS12,
                in the binary format described by RFC 7292
            password (bytes-like): the password to use to decrypt the data.
                `None` if the PKCS12 is not encrypted.
            hashalgo (str): hashing algorithm used, passed to `hashlib.new`
            contact_info (str): optional information provided by the signer to enable
                a recipient to contact the signer to verify the signature
            location (str): optional CPU host name or physical location of the signing
            signing_time (datetime): optional time of signing
            reason (str): optional signing reason
            flags (Tuple[fpdf.enums.AnnotationFlag], Tuple[str]): optional list of flags defining annotation properties
        """
        ...
    def sign(
        self,
        key,
        cert,
        extra_certs: Sequence[Incomplete] = (),
        hashalgo: str = "sha256",
        contact_info: str | None = None,
        location: str | None = None,
        signing_time: datetime.datetime | None = None,
        reason: str | None = None,
        flags: tuple[AnnotationFlag, ...] = ...,
    ) -> None: ...
    def file_id(self) -> str: ...
    def interleaved2of5(self, text, x: float, y: float, w: float = 1, h: float = 10) -> None: ...
    def code39(self, text, x: float, y: float, w: float = 1.5, h: float = 5) -> None: ...
    def rect_clip(self, x: float, y: float, w: float, h: float) -> _GeneratorContextManager[None]: ...
    def elliptic_clip(self, x: float, y: float, w: float, h: float) -> _GeneratorContextManager[None]: ...
    def round_clip(self, x: float, y: float, r: float) -> _GeneratorContextManager[None]: ...
    def unbreakable(self) -> _GeneratorContextManager[FPDFRecorder]: ...
    def offset_rendering(self) -> _GeneratorContextManager[FPDFRecorder]: ...
    def insert_toc_placeholder(
        self, render_toc_function: Callable[[FPDF, list[OutlineSection]], object], pages: int = 1, allow_extra_pages: bool = False
    ) -> None: ...
    def set_section_title_styles(
        self,
        level0: TextStyle,
        level1: TextStyle | None = None,
        level2: TextStyle | None = None,
        level3: TextStyle | None = None,
        level4: TextStyle | None = None,
        level5: TextStyle | None = None,
        level6: TextStyle | None = None,
    ) -> None: ...
    def start_section(self, name: str, level: int = 0, strict: bool = True) -> None: ...
    def use_text_style(self, text_style: TextStyle) -> _GeneratorContextManager[None]: ...
    def use_font_face(self, font_face: FontFace) -> _GeneratorContextManager[None]: ...
    def table(
        self,
        rows: Iterable[Incomplete] = (),
        *,
        # Keep in sync with `fpdf.table.Table`:
        align: str | _TextAlign = "CENTER",
        v_align: str | VAlign = "MIDDLE",
        borders_layout: str | TableBordersLayout = ...,
        cell_fill_color: int | tuple[Incomplete, ...] | DeviceGray | DeviceRGB | None = None,
        cell_fill_mode: str | TableCellFillMode = ...,
        col_widths: int | tuple[int, ...] | None = None,
        first_row_as_headings: bool = True,
        gutter_height: float = 0,
        gutter_width: float = 0,
        headings_style: FontFace = ...,
        line_height: int | None = None,
        markdown: bool = False,
        text_align: str | _TextAlign | tuple[str | _TextAlign, ...] = "JUSTIFY",
        width: int | None = None,
        wrapmode: WrapMode = ...,
        padding: float | Padding | None = None,
        outer_border_width: float | None = None,
        num_heading_rows: int = 1,
        repeat_headings: TableHeadingsDisplay | int = 1,
    ) -> _GeneratorContextManager[Table]:
        """
        Inserts a table, that can be built using the `fpdf.table.Table` object yield.
        Detailed usage documentation: https://py-pdf.github.io/fpdf2/Tables.html

        Args:
            rows: optional. Sequence of rows (iterable) of str to initiate the table cells with text content.
            align (str, fpdf.enums.Align): optional, default to CENTER. Sets the table horizontal position
                relative to the page, when it's not using the full page width.
            borders_layout (str, fpdf.enums.TableBordersLayout): optional, default to ALL. Control what cell
                borders are drawn.
            cell_fill_color (int, tuple, fpdf.drawing.DeviceCMYK, fpdf.drawing.DeviceGray, fpdf.drawing.DeviceRGB): optional.
                Defines the cells background color.
            cell_fill_mode (str, fpdf.enums.TableCellFillMode): optional. Defines which cells are filled
                with color in the background.
            col_widths (int, tuple): optional. Sets column width. Can be a single number or a sequence of numbers.
            first_row_as_headings (bool): optional, default to True. If False, the first row of the table
                is not styled differently from the others.
            gutter_height (float): optional vertical space between rows.
            gutter_width (float): optional horizontal space between columns.
            headings_style (fpdf.fonts.FontFace): optional, default to bold.
                Defines the visual style of the top headings row: size, color, emphasis...
            line_height (number): optional. Defines how much vertical space a line of text will occupy.
            markdown (bool): optional, default to False. Enable markdown interpretation of cells textual content.
            text_align (str, fpdf.enums.Align): optional, default to JUSTIFY. Control text alignment inside cells.
            v_align (str, fpdf.enums.AlignV): optional, default to CENTER. Control vertical alignment of cells content.
            width (number): optional. Sets the table width.
            wrapmode (fpdf.enums.WrapMode): "WORD" for word based line wrapping (default),
                "CHAR" for character based line wrapping.
            padding (number, tuple, Padding): optional. Sets the cell padding. Can be a single number or a sequence
                of numbers, default:0
                If padding for left or right ends up being non-zero then the respective c_margin is ignored.
            outer_border_width (number): optional. The outer_border_width will trigger rendering of the outer
                border of the table with the given width regardless of any other defined border styles.
            num_heading_rows (number): optional. Sets the number of heading rows, default value is 1. If this value is not 1,
                first_row_as_headings needs to be True if num_heading_rows>1 and False if num_heading_rows=0. For backwards compatibility,
                first_row_as_headings is used in case num_heading_rows is 1.
            repeat_headings (fpdf.enums.TableHeadingsDisplay): optional, indicates whether to print table headings on every page, default to 1.
        """
        ...
    @overload
    def output(  # type: ignore[overload-overlap]
        self,
        name: Literal[""] | None = "",
        dest: Unused = "",
        linearize: bool = False,
        output_producer_class: Callable[[FPDF], OutputProducer] = ...,
    ) -> bytearray:
        """
        Output PDF to some destination.
        The method first calls [close](close.md) if necessary to terminate the document.
        After calling this method, content cannot be added to the document anymore.

        By default the bytearray buffer is returned.
        If a `name` is given, the PDF is written to a new file.

        Args:
            name (str): optional File object or file path where to save the PDF under
            dest (str): [**DEPRECATED since 2.3.0**] unused, will be removed in a later version
            output_producer_class (class): use a custom class for PDF file generation
        """
        ...
    @overload
    def output(
        self, name: str, dest: Unused = "", linearize: bool = False, output_producer_class: Callable[[FPDF], OutputProducer] = ...
    ) -> None:
        """
        Output PDF to some destination.
        The method first calls [close](close.md) if necessary to terminate the document.
        After calling this method, content cannot be added to the document anymore.

        By default the bytearray buffer is returned.
        If a `name` is given, the PDF is written to a new file.

        Args:
            name (str): optional File object or file path where to save the PDF under
            dest (str): [**DEPRECATED since 2.3.0**] unused, will be removed in a later version
            output_producer_class (class): use a custom class for PDF file generation
        """
        ...
