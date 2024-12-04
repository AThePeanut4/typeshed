from typing import Any

from . import base

SPACES_REGEX: Any

class Filter(base.Filter):
    """Collapses whitespace except in pre, textarea, and script elements"""
    spacePreserveElements: Any
    def __iter__(self): ...

def collapse_spaces(text): ...
