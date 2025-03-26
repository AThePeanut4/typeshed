import re
from builtins import list as _list  # conflicts with a method named "list"
from typing import Any, Final, Literal, overload

from commonmark.node import Node
from commonmark.render.renderer import Renderer

reUnsafeProtocol: Final[re.Pattern[str]]
reSafeDataProtocol: Final[re.Pattern[str]]

def potentially_unsafe(url: str) -> bool | None: ...

class HtmlRenderer(Renderer):
    disable_tags: int
    last_out: str
    options: dict[str, Any]
    def __init__(self, options: dict[str, Any] = {}) -> None: ...
    @overload
    def escape(self, text: None) -> Literal[""]: ...
    @overload
    def escape(self, text: str) -> str: ...
    def tag(self, name: str, attrs: _list[_list[str]] | None = None, selfclosing: bool | None = None) -> None:
        """Helper function to produce an HTML tag."""
        ...
    def text(self, node: Node, entering: bool | None = None) -> None: ...
    def softbreak(self, node: Node | None = None, entering: bool | None = None) -> None: ...
    def linebreak(self, node: Node | None = None, entering: bool | None = None) -> None: ...
    def link(self, node: Node, entering: bool | None) -> None: ...
    def image(self, node: Node, entering: bool | None) -> None: ...
    def emph(self, node: Node, entering: bool | None) -> None: ...
    def strong(self, node: Node, entering: bool | None) -> None: ...
    def paragraph(self, node: Node, entering: bool | None) -> None: ...
    def heading(self, node: Node, entering: bool | None) -> None: ...
    def code(self, node: Node, entering: bool | None) -> None: ...
    def code_block(self, node: Node, entering: bool | None) -> None: ...
    def thematic_break(self, node: Node, entering: bool | None) -> None: ...
    def block_quote(self, node: Node, entering: bool | None) -> None: ...
    def list(self, node: Node, entering: bool | None) -> None: ...
    def item(self, node: Node, entering: bool | None) -> None: ...
    def html_inline(self, node: Node, entering: bool | None) -> None: ...
    def html_block(self, node: Node, entering: bool | None) -> None: ...
    def custom_inline(self, node: Node, entering: bool | None) -> None: ...
    def custom_block(self, node: Node, entering: bool | None) -> None: ...
    def out(self, s: str | None) -> None: ...
    def attrs(self, node: Node) -> _list[_list[str]]: ...
