from _typeshed import Incomplete
from collections.abc import Iterable, Iterator

from pygments.lexer import Lexer
from pygments.token import _TokenType

def apply_filters(stream, filters, lexer=None):
    """
    Use this method to apply an iterable of filters to
    a stream. If lexer is given it's forwarded to the
    filter, otherwise the filter receives `None`.
    """
    ...
def simplefilter(f):
    """
    Decorator that converts a function into a filter::

        @simplefilter
        def lowercase(self, lexer, stream, options):
            for ttype, value in stream:
                yield ttype, value.lower()
    """
    ...

class Filter:
    options: Incomplete
    def __init__(self, **options) -> None: ...
    def filter(self, lexer: Lexer, stream: Iterable[tuple[_TokenType, str]]) -> Iterator[tuple[_TokenType, str]]: ...

class FunctionFilter(Filter):
    function: Incomplete
    def __init__(self, **options) -> None: ...
    def filter(self, lexer: Lexer, stream: Iterable[tuple[_TokenType, str]]) -> Iterator[tuple[_TokenType, str]]: ...
