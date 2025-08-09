from typing import Final

from .filters import *
from .filterset import FilterSet as FilterSet, UnknownFieldBehavior as UnknownFieldBehavior

__version__: Final[str]

def parse_version(version: str) -> tuple[str | int]:
    """
    '0.1.2.dev1' -> (0, 1, 2, 'dev1')
    '0.1.2' -> (0, 1, 2)
    """
    ...

VERSION: tuple[str | int, ...]
