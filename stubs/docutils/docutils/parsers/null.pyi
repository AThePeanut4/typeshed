"""A do-nothing parser."""

from typing import ClassVar

from docutils import parsers

class Parser(parsers.Parser):
    """A do-nothing parser."""
    config_section_dependencies: ClassVar[tuple[str, ...]]
