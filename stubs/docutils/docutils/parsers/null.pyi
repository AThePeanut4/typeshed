"""A do-nothing parser."""

from typing import ClassVar, Final

from docutils import parsers

__docformat__: Final = "reStructuredText"

class Parser(parsers.Parser):
    """A do-nothing parser."""
    supported: ClassVar[tuple[str, ...]]
    config_section_dependencies: ClassVar[tuple[str, ...]]
