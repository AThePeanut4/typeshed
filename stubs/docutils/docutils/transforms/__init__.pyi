"""
This package contains modules for standard tree transforms available
to Docutils components. Tree transforms serve a variety of purposes:

- To tie up certain syntax-specific "loose ends" that remain after the
  initial parsing of the input plaintext. These transforms are used to
  supplement a limited syntax.

- To automate the internal linking of the document tree (hyperlink
  references, footnote references, etc.).

- To extract useful information from the document tree. These
  transforms may be used to construct (for example) indexes and tables
  of contents.

Each transform is an optional step that a Docutils component may
choose to perform on the parsed document.
"""

from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from typing import Any, ClassVar, Final
from typing_extensions import TypeAlias

from docutils import ApplicationError, TransformSpec, nodes
from docutils.languages import LanguageImporter

_TransformTuple: TypeAlias = tuple[str, type[Transform], nodes.Node | None, dict[str, Any]]

__docformat__: Final = "reStructuredText"

class TransformError(ApplicationError): ...

class Transform:
    default_priority: ClassVar[int | None]
    document: nodes.document
    startnode: nodes.Node | None
    language: LanguageImporter
    def __init__(self, document: nodes.document, startnode: nodes.Node | None = None) -> None: ...
    def __getattr__(self, name: str, /) -> Incomplete: ...  # method apply is not implemented

class Transformer(TransformSpec):
    transforms: list[_TransformTuple]
    document: nodes.document
    applied: list[_TransformTuple]
    sorted: bool
    components: Mapping[str, TransformSpec]
    serialno: int
    def __init__(self, document: nodes.document): ...
    def add_transform(self, transform_class: type[Transform], priority: int | None = None, **kwargs) -> None: ...
    def add_transforms(self, transform_list: Iterable[type[Transform]]) -> None: ...
    def add_pending(self, pending: nodes.pending, priority: int | None = None) -> None: ...
    def get_priority_string(self, priority: int) -> str: ...
    def populate_from_components(self, components: Iterable[TransformSpec]) -> None: ...
    def apply_transforms(self) -> None: ...
