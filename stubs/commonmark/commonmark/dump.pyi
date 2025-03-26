from typing import Any

from .node import Node

def prepare(obj: Node, topnode: bool = ...) -> list[dict[str, Any]]:
    """
    Walk the complete AST, only returning needed data.

    This removes circular references and allows us to output
    JSON.
    """
    ...
def dumpJSON(obj: Node) -> str:
    """Output AST in JSON form, this is destructive of block."""
    ...
def dumpAST(obj: Node, ind: int = ..., topnode: bool = ...) -> None:
    """Print out a block/entire AST."""
    ...
