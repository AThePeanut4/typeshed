"""This package contains Docutils parser modules."""

from typing import Any, ClassVar

from docutils import Component
from docutils.nodes import document as _document

class Parser(Component):
    component_type: ClassVar[str]
    config_section: ClassVar[str]
    inputstring: Any  # defined after call to setup_parse()
    document: Any  # defined after call to setup_parse()
    def parse(self, inputstring: str, document: _document) -> None:
        """Override to parse `inputstring` into document tree `document`."""
        ...
    def setup_parse(self, inputstring: str, document: _document) -> None:
        """Initial parse setup.  Call at start of `self.parse()`."""
        ...
    def finish_parse(self) -> None:
        """Finalize parse details.  Call at end of `self.parse()`."""
        ...

_parser_aliases: dict[str, str]

def get_parser_class(parser_name: str) -> type[Parser]:
    """Return the Parser class from the `parser_name` module."""
    ...
