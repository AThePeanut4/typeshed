"""
An implementation of [PHP Markdown Extra](http://michelf.com/projects/php-markdown/extra/)'s
parsing of Markdown syntax in raw HTML.

See the [documentation](https://Python-Markdown.github.io/extensions/raw_html)
for details.
"""

from xml.etree.ElementTree import Element

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.postprocessors import RawHtmlPostprocessor

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
