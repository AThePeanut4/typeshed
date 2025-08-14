"""
A Docutils-XML parser.

Provisional:
  The API is not fixed yet.
  Defined objects may be renamed or changed
  in any Docutils release without prior notice.
"""

import xml.etree.ElementTree as ET
from typing import ClassVar, Final

from docutils import nodes, parsers

__docformat__: Final = "reStructuredText"

class Parser(parsers.Parser):
    """A Docutils-XML parser."""
    config_section_dependencies: ClassVar[tuple[str, ...]]
    settings_default_overrides: ClassVar[dict[str, bool]]

class Unknown(nodes.Special, nodes.Inline, nodes.Element):
    """An unknown element found by the XML parser."""
    ...

def parse_element(inputstring: str, document: nodes.document | None = None) -> nodes.Element:
    """
    Parse `inputstring` as "Docutils XML", return `nodes.Element` instance.

    :inputstring: XML source.
    :document: `nodes.document` instance (default: a new dummy instance).
               Provides settings and reporter.
               Populated and returned, if the inputstring's root element
               is <document>.

    Caution:
      The function does not detect invalid XML.

      To check the validity of the returned node,
      you may use its `validate()` method::

        node = parse_element('<tip><hint>text</hint></tip>')
        node.validate()

    Provisional.
    """
    ...
def element2node(element: ET.Element | None, document: nodes.document | None = None, unindent: bool = True) -> nodes.Element:
    """
    Convert an `etree` element and its children to Docutils doctree nodes.

    :element:  `xml.etree` element
    :document: see `parse_element()`
    :unindent: Remove formatting indentation of follow-up text lines?
               Cf. `append_text()`.
               TODO: do we need an "unindent" configuration setting?

    Return a `docutils.nodes.Element` instance.

    Internal.
    """
    ...
def append_text(node: nodes.Element, text: str | None, unindent: bool | None) -> None: ...
