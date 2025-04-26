from _typeshed import Incomplete, SupportsItems
from collections.abc import Iterable
from dataclasses import dataclass
from io import BytesIO
from typing import Literal, overload

from PIL import Image

from .drawing import DeviceGray, DeviceRGB
from .enums import (
    Align,
    CellBordersLayout,
    TableBordersLayout,
    TableCellFillMode,
    TableHeadingsDisplay,
    TableSpan,
    VAlign,
    WrapMode,
)
from .fonts import FontFace
from .fpdf import FPDF
from .image_datastructures import _TextAlign
from .util import Padding

DEFAULT_HEADINGS_STYLE: FontFace

class Table:
    """
    Object that `fpdf.FPDF.table()` yields, used to build a table in the document.
    Detailed usage documentation: https://py-pdf.github.io/fpdf2/Tables.html
    """
    rows: list[Row]

    def __init__(
        self,
        fpdf: FPDF,
        rows: Iterable[str] = (),
        *,
        # Keep in sync with `fpdf.fpdf.FPDF.table`:
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
        min_row_height: Incomplete | None = None,
    ) -> None: ...
    def row(
        self,
        cells: Iterable[str] = (),
        style: FontFace | None = None,
        v_align: VAlign | str | None = None,
        min_height: Incomplete | None = None,
    ) -> Row: ...
    def render(self) -> None: ...
    def get_cell_border(self, i: int, j: int, cell: Cell) -> str | Literal[0, 1]: ...

class Row:
    """Object that `Table.row()` yields, used to build a row in a table"""
    cells: list[Cell]
    style: FontFace
    v_align: VAlign | None
    min_height: Incomplete | None
    def __init__(
        self,
        table: Table,
        style: FontFace | None = None,
        v_align: VAlign | str | None = None,
        min_height: Incomplete | None = None,
    ) -> None: ...
    @property
    def cols_count(self) -> int: ...
    @property
    def max_rowspan(self) -> int: ...
    def convert_spans(self, active_rowspans: SupportsItems[int, int]) -> tuple[dict[int, int], list[int]]: ...
    @overload
    def cell(
        self,
        text: str = "",
        align: str | Align | None = None,
        v_align: str | VAlign | None = None,
        style: FontFace | None = None,
        img: str | Image.Image | BytesIO | None = None,
        img_fill_width: bool = False,
        colspan: int = 1,
        rowspan: int = 1,
        padding: tuple[float, ...] | None = None,
        link: str | int | None = None,
        border: CellBordersLayout | int = ...,
    ) -> str:
        """
        Adds a cell to the row.

        Args:
            text (str): string content, can contain several lines.
                In that case, the row height will grow proportionally.
            align (str, fpdf.enums.Align): optional text alignment.
            v_align (str, fpdf.enums.AlignV): optional vertical text alignment.
            style (fpdf.fonts.FontFace): optional text style.
            img: optional. Either a string representing a file path to an image,
                an URL to an image, an io.BytesIO, or a instance of `PIL.Image.Image`.
            img_fill_width (bool): optional, defaults to False. Indicates to render the image
                using the full width of the current table column.
            colspan (int): optional number of columns this cell should span.
            rowspan (int): optional number of rows this cell should span.
            padding (tuple): optional padding (left, top, right, bottom) for the cell.
            link (str, int): optional link, either an URL or an integer returned by `FPDF.add_link`, defining an internal link to a page
            border (fpdf.enums.CellBordersLayout): optional cell borders, defaults to `CellBordersLayout.INHERIT`
        """
        ...
    @overload
    def cell(
        self,
        text: TableSpan,
        align: str | Align | None = None,
        v_align: str | VAlign | None = None,
        style: FontFace | None = None,
        img: str | Image.Image | BytesIO | None = None,
        img_fill_width: bool = False,
        colspan: int = 1,
        rowspan: int = 1,
        padding: tuple[float, ...] | None = None,
        link: str | int | None = None,
        border: CellBordersLayout | int = ...,
    ) -> TableSpan:
        """
        Adds a cell to the row.

        Args:
            text (str): string content, can contain several lines.
                In that case, the row height will grow proportionally.
            align (str, fpdf.enums.Align): optional text alignment.
            v_align (str, fpdf.enums.AlignV): optional vertical text alignment.
            style (fpdf.fonts.FontFace): optional text style.
            img: optional. Either a string representing a file path to an image,
                an URL to an image, an io.BytesIO, or a instance of `PIL.Image.Image`.
            img_fill_width (bool): optional, defaults to False. Indicates to render the image
                using the full width of the current table column.
            colspan (int): optional number of columns this cell should span.
            rowspan (int): optional number of rows this cell should span.
            padding (tuple): optional padding (left, top, right, bottom) for the cell.
            link (str, int): optional link, either an URL or an integer returned by `FPDF.add_link`, defining an internal link to a page
            border (fpdf.enums.CellBordersLayout): optional cell borders, defaults to `CellBordersLayout.INHERIT`
        """
        ...

@dataclass
class Cell:
    """Internal representation of a table cell"""
    text: str
    align: str | Align | None
    v_align: str | VAlign | None
    style: FontFace | None
    img: str | None
    img_fill_width: bool
    colspan: int
    rowspan: int
    padding: int | tuple[float, ...] | None
    link: str | int | None
    border: CellBordersLayout | None

    def write(self, text, align: Incomplete | None = None): ...

@dataclass(frozen=True)
class RowLayoutInfo:
    """RowLayoutInfo(height: float, pagebreak_height: float, rendered_heights: dict, merged_heights: list)"""
    height: int
    pagebreak_height: float
    rendered_heights: dict[Incomplete, Incomplete]
    merged_heights: list[Incomplete]

@dataclass(frozen=True)
class RowSpanLayoutInfo:
    """RowSpanLayoutInfo(column: int, start: int, length: int, contents_height: float)"""
    column: int
    start: int
    length: int
    contents_height: float

    def row_range(self) -> range: ...

def draw_box_borders(pdf: FPDF, x1, y1, x2, y2, border: str | Literal[0, 1], fill_color: Incomplete | None = None) -> None:
    """
    Draws a box using the provided style - private helper used by table for drawing the cell and table borders.
    Difference between this and rect() is that border can be defined as "L,R,T,B" to draw only some of the four borders;
    compatible with get_border(i,k)

    See Also: rect()
    """
    ...
