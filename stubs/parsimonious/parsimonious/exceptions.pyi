from parsimonious.expressions import Expression
from parsimonious.grammar import LazyReference
from parsimonious.nodes import Node
from parsimonious.utils import StrAndRepr

class ParsimoniousError(Exception): ...

class ParseError(StrAndRepr, ParsimoniousError):
    text: str
    pos: int
    expr: Expression | None
    def __init__(self, text: str, pos: int = -1, expr: Expression | None = None) -> None: ...
    def line(self) -> int:
        """
        Return the 1-based line number where the expression ceased to
        match.
        """
        ...
    def column(self) -> int:
        """Return the 1-based column where the expression ceased to match."""
        ...

class LeftRecursionError(ParseError): ...
class IncompleteParseError(ParseError):
    """
    A call to ``parse()`` matched a whole Expression but did not consume the
    entire text.
    """
    ...

class VisitationError(ParsimoniousError):
    original_class: type[BaseException]
    def __init__(self, exc: BaseException, exc_class: type[BaseException], node: Node) -> None: ...

class BadGrammar(StrAndRepr, ParsimoniousError): ...

class UndefinedLabel(BadGrammar):
    """
    A rule referenced in a grammar was never defined.

    Circular references and forward references are okay, but you have to define
    stuff at some point.
    """
    label: LazyReference
    def __init__(self, label: LazyReference) -> None: ...
