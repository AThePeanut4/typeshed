from _typeshed import ConvertibleToInt, Incomplete, Unused
from collections.abc import Iterable, Iterator
from typing import ClassVar, Literal

from openpyxl.descriptors.base import Bool, Integer, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.sequence import Sequence
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import Border
from openpyxl.styles.cell_style import CellStyle, StyleArray
from openpyxl.styles.fills import Fill
from openpyxl.styles.fonts import Font
from openpyxl.styles.protection import Protection
from openpyxl.workbook.workbook import Workbook

class NamedStyle(Serialisable):
    """Named and editable styles"""
    font: Typed[Font, Literal[False]]
    fill: Typed[Fill, Literal[False]]
    border: Typed[Border, Literal[False]]
    alignment: Typed[Alignment, Literal[False]]
    number_format: Incomplete
    protection: Typed[Protection, Literal[False]]
    builtinId: Integer[Literal[True]]
    hidden: Bool[Literal[True]]
    name: String[Literal[False]]
    def __init__(
        self,
        name: str = "Normal",
        font: Font | None = None,
        fill: Fill | None = None,
        border: Border | None = None,
        alignment: Alignment | None = None,
        number_format=None,
        protection: Protection | None = None,
        builtinId: ConvertibleToInt | None = None,
        hidden: _ConvertibleToBool | None = False,
    ) -> None: ...
    def __setattr__(self, attr: str, value) -> None: ...
    def __iter__(self) -> Iterator[tuple[str, str]]: ...
    def bind(self, wb: Workbook) -> None:
        """Bind a named style to a workbook"""
        ...
    def as_tuple(self) -> StyleArray:
        """Return a style array representing the current style"""
        ...
    def as_xf(self) -> CellStyle:
        """Return equivalent XfStyle"""
        ...
    def as_name(self) -> _NamedCellStyle:
        """Return relevant named style"""
        ...

class NamedStyleList(list[NamedStyle]):
    """
    Named styles are editable and can be applied to multiple objects

    As only the index is stored in referencing objects the order mus
    be preserved.

    Returns a list of NamedStyles
    """
    def __init__(self, iterable: Iterable[NamedStyle] = ()) -> None:
        """Allow a list of named styles to be passed in and index them."""
        ...
    @property
    def names(self) -> list[str]: ...
    def __getitem__(self, key: int | str) -> NamedStyle: ...  # type: ignore[override]
    def append(self, style: NamedStyle) -> None: ...

class _NamedCellStyle(Serialisable):
    """
    Pointer-based representation of named styles in XML
    xfId refers to the corresponding CellStyleXfs

    Not used in client code.
    """
    tagname: ClassVar[str]
    name: String[Literal[False]]
    xfId: Integer[Literal[False]]
    builtinId: Integer[Literal[True]]
    iLevel: Integer[Literal[True]]
    hidden: Bool[Literal[True]]
    customBuiltin: Bool[Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(
        self,
        name: str,
        xfId: ConvertibleToInt,
        builtinId: ConvertibleToInt | None = None,
        iLevel: ConvertibleToInt | None = None,
        hidden: _ConvertibleToBool | None = None,
        customBuiltin: _ConvertibleToBool | None = None,
        extLst: Unused = None,
    ) -> None: ...

class _NamedCellStyleList(Serialisable):
    """
    Container for named cell style objects

    Not used in client code
    """
    tagname: ClassVar[str]
    # Overwritten by property below
    # count: Integer[Literal[True]]
    cellStyle: Sequence[list[_NamedCellStyle]]
    __attrs__: ClassVar[tuple[str, ...]]
    def __init__(self, count: Unused = None, cellStyle: list[_NamedCellStyle] | tuple[_NamedCellStyle, ...] = ()) -> None: ...
    @property
    def count(self) -> int: ...
    def remove_duplicates(self) -> list[_NamedCellStyle]:
        """
        Some applications contain duplicate definitions either by name or
        referenced style.

        As the references are 0-based indices, styles are sorted by
        index.

        Returns a list of style references with duplicates removed
        """
        ...
