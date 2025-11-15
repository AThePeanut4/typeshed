from _typeshed import Incomplete
from collections.abc import Iterable

from . import base

class Filter(base.Filter[dict[str, Incomplete]]):
    """Injects ``<meta charset=ENCODING>`` tag into head of document"""
    encoding: str | None
    def __init__(self, source: Iterable[dict[str, Incomplete]], encoding: str | None) -> None:
        """
        Creates a Filter

        :arg source: the source token stream

        :arg encoding: the encoding to set
        """
        ...
