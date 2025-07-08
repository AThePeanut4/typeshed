from collections.abc import Iterable, Mapping
from typing import Literal
from xml.etree.ElementTree import Element, TreeBuilder

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.htmlparser import HTMLExtractor
from markdown.postprocessors import RawHtmlPostprocessor
from markdown.preprocessors import Preprocessor

class HTMLExtractorExtra(HTMLExtractor):
    block_level_tags: set[str]
    span_tags: set[str]
    raw_tags: set[str]
    block_tags: set[str]
    span_and_blocks_tags: set[str]
    mdstack: list[str]
    treebuilder: TreeBuilder
    mdstate: list[Literal["block", "span", "off"] | None]
    mdstarted: list[bool]
    def get_element(self) -> Element: ...
    def get_state(self, tag: str, attrs: Mapping[str, str]) -> Literal["block", "span", "off"] | None: ...
    def handle_starttag(self, tag: str, attrs: Iterable[tuple[str, str | None]]) -> None: ...
    def handle_endtag(self, tag: str) -> None: ...
    def handle_startendtag(self, tag: str, attrs: Iterable[tuple[str, str | None]]) -> None: ...
    def handle_data(self, data: str) -> None: ...
    def handle_empty_tag(self, data: str, is_block: bool) -> None: ...
    def parse_pi(self, i: int) -> int: ...
    def parse_html_declaration(self, i: int) -> int: ...

class HtmlBlockPreprocessor(Preprocessor): ...

class MarkdownInHtmlProcessor(BlockProcessor):
    """Process Markdown Inside HTML Blocks which have been stored in the `HtmlStash`."""
    def parse_element_content(self, element: Element) -> None:
        """
        Recursively parse the text content of an `etree` Element as Markdown.

        Any block level elements generated from the Markdown will be inserted as children of the element in place
        of the text content. All `markdown` attributes are removed. For any elements in which Markdown parsing has
        been disabled, the text content of it and its children are wrapped in an `AtomicString`.
        """
        ...

class MarkdownInHTMLPostprocessor(RawHtmlPostprocessor):
    def stash_to_string(self, text: str | Element) -> str:
        """Override default to handle any `etree` elements still in the stash. """
        ...

class MarkdownInHtmlExtension(Extension):
    """Add Markdown parsing in HTML to Markdown class."""
    ...

def makeExtension(**kwargs) -> MarkdownInHtmlExtension: ...
