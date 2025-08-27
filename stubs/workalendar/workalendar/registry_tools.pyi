"""Tools to update the ISO registry."""

from collections.abc import Callable
from typing import TypeVar

_T = TypeVar("_T", bound=type)

def iso_register(iso_code: str) -> Callable[[_T], _T]:
    """
    Registers Calendar class as country or region in IsoRegistry.

    Registered country must set class variables ``iso`` using this decorator.

    >>> from workalendar.core import Calendar
    >>> @iso_register('MC-MR')
    >>> class MyRegion(Calendar):
    >>>     'My Region'

    Region calendar is then retrievable from registry:

    >>> calendar = registry.get('MC-MR')
    """
    ...
