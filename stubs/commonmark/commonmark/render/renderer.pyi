from commonmark.node import Node

class Renderer:
    buf: str
    last_out: str
    def render(self, ast: Node) -> str:
        """
        Walks the AST and calls member methods for each Node type.

        @param ast {Node} The root of the abstract syntax tree.
        """
        ...
    def lit(self, s: str) -> None:
        """
        Concatenate a literal string to the buffer.

        @param str {String} The string to concatenate.
        """
        ...
    def cr(self) -> None: ...
    def out(self, s: str) -> None:
        """
        Concatenate a string to the buffer possibly escaping the content.

        Concrete renderer implementations should override this method.

        @param str {String} The string to concatenate.
        """
        ...
