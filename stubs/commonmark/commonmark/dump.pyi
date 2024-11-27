def prepare(obj, topnode: bool = ...):
    """
    Walk the complete AST, only returning needed data.

    This removes circular references and allows us to output
    JSON.
    """
    ...
def dumpJSON(obj):
    """Output AST in JSON form, this is destructive of block."""
    ...
def dumpAST(obj, ind: int = ..., topnode: bool = ...) -> None:
    """Print out a block/entire AST."""
    ...
