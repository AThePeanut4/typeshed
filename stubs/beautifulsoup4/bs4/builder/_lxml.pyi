from typing import Any

from bs4.builder import HTMLTreeBuilder, TreeBuilder

class LXMLTreeBuilderForXML(TreeBuilder):
    DEFAULT_PARSER_CLASS: Any
    is_xml: bool
    processing_instruction_class: Any
    NAME: str
    ALTERNATE_NAMES: Any
    features: Any
    CHUNK_SIZE: int
    DEFAULT_NSMAPS: Any
    DEFAULT_NSMAPS_INVERTED: Any
    def initialize_soup(self, soup) -> None:
        """
        Let the BeautifulSoup object know about the standard namespace
        mapping.

        :param soup: A `BeautifulSoup`.
        """
        ...
    def default_parser(self, encoding):
        """
        Find the default parser for the given encoding.

        :param encoding: A string.
        :return: Either a parser object or a class, which
          will be instantiated with default arguments.
        """
        ...
    def parser_for(self, encoding):
        """
        Instantiate an appropriate parser for the given encoding.

        :param encoding: A string.
        :return: A parser object such as an `etree.XMLParser`.
        """
        ...
    empty_element_tags: Any
    soup: Any
    nsmaps: Any
    def __init__(self, parser=None, empty_element_tags=None, **kwargs) -> None: ...
    def prepare_markup(  # type: ignore[override]  # the order of the parameters is different
        self, markup, user_specified_encoding=None, exclude_encodings=None, document_declared_encoding=None
    ) -> None: ...
    parser: Any
    def feed(self, markup) -> None: ...
    def close(self) -> None: ...
    def start(self, name, attrs, nsmap={}) -> None: ...
    def end(self, name) -> None: ...
    def pi(self, target, data) -> None: ...
    def data(self, content) -> None: ...
    def doctype(self, name, pubid, system) -> None: ...
    def comment(self, content) -> None:
        """Handle comments as Comment objects."""
        ...
    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
        ...

class LXMLTreeBuilder(HTMLTreeBuilder, LXMLTreeBuilderForXML):
    NAME: Any
    ALTERNATE_NAMES: Any
    features: Any
    is_xml: bool
    processing_instruction_class: Any
    def default_parser(self, encoding): ...
    parser: Any
    def feed(self, markup) -> None: ...
    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
        ...
