from collections.abc import Iterable, Iterator
from typing import Any

from pygments.lexer import Lexer
from pygments.token import _TokenType

def apply_filters(stream, filters, lexer=None): ...
def simplefilter(f): ...

class Filter:
    """
    Default filter. Subclass this class or use the `simplefilter`
    decorator to create own filters.
    """
    options: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer: Lexer, stream: Iterable[tuple[_TokenType, str]]) -> Iterator[tuple[_TokenType, str]]: ...

class FunctionFilter(Filter):
    """
    Abstract class used by `simplefilter` to create simple
    function filters on the fly. The `simplefilter` decorator
    automatically creates subclasses of this class for
    functions passed to it.
    """
    function: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer: Lexer, stream: Iterable[tuple[_TokenType, str]]) -> Iterator[tuple[_TokenType, str]]: ...
