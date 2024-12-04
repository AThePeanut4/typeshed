"""
Quoting section 8.2.2 "Document Outline" of the 2006 PDF spec 1.7:
> The document outline consists of a tree-structured hierarchy of outline items (sometimes called bookmarks),
> which serve as a visual table of contents to display the document’s structure to the user.

The contents of this module are internal to fpdf2, and not part of the public API.
They may change at any time without prior warning or any deprecation period,
in non-backward-compatible ways.
"""

from _typeshed import Incomplete
from collections.abc import Generator, Iterable
from typing import NamedTuple

from .structure_tree import StructElem
from .syntax import Destination, PDFObject, PDFString

class OutlineSection(NamedTuple):
    """OutlineSection(name, level, page_number, dest, struct_elem)"""
    name: str
    level: int
    page_number: int
    dest: Destination
    struct_elem: StructElem | None = None

class OutlineItemDictionary(PDFObject):
    title: PDFString
    parent: Incomplete | None
    prev: Incomplete | None
    next: Incomplete | None
    first: Incomplete | None
    last: Incomplete | None
    count: int
    dest: Destination | None
    struct_elem: StructElem | None
    def __init__(self, title: str, dest: Destination | None = None, struct_elem: StructElem | None = None) -> None: ...

class OutlineDictionary(PDFObject):
    type: str
    first: Incomplete | None
    last: Incomplete | None
    count: int
    def __init__(self) -> None: ...

def build_outline_objs(
    sections: Iterable[Incomplete],
) -> Generator[Incomplete, None, list[OutlineDictionary | OutlineItemDictionary]]:
    """
    Build PDF objects constitutive of the documents outline,
    and yield them one by one, starting with the outline dictionary
    """
    ...
