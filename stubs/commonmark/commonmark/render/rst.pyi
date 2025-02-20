from typing import Any

from commonmark.render.renderer import Renderer

class ReStructuredTextRenderer(Renderer):
    """
    Render reStructuredText from Markdown

    Example:

    .. code:: python

        import commonmark

        parser = commonmark.Parser()
        ast = parser.parse('Hello `inline code` example')

        renderer = commonmark.ReStructuredTextRenderer()
        rst = renderer.render(ast)
        print(rst)  # Hello ``inline code`` example
    """
    indent_char: Any
    indent_length: int
    def __init__(self, indent_char: str = ...) -> None: ...
    def lit(self, s): ...
    def cr(self) -> None: ...
    def indent_lines(self, literal, indent_length: int = ...): ...
    def document(self, node, entering) -> None: ...
    def softbreak(self, node, entering) -> None: ...
    def linebreak(self, node, entering) -> None: ...
    def text(self, node, entering) -> None: ...
    def emph(self, node, entering) -> None: ...
    def strong(self, node, entering) -> None: ...
    def paragraph(self, node, entering) -> None: ...
    def link(self, node, entering) -> None: ...
    def image(self, node, entering) -> None: ...
    def code(self, node, entering) -> None: ...
    def code_block(self, node, entering) -> None: ...
    def list(self, node, entering) -> None: ...
    def item(self, node, entering) -> None: ...
    def block_quote(self, node, entering) -> None: ...
    def heading(self, node, entering) -> None: ...
