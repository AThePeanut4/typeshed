"""LaTeX2e document tree Writer."""

from _typeshed import Incomplete
from typing import ClassVar

from docutils.utils import Reporter

class Babel:
    """Language specifics for LaTeX."""
    language_codes: ClassVar[dict[str, str]]
    warn_msg: ClassVar[str]
    active_chars: ClassVar[dict[str, str]]

    reporter: Reporter | None
    language: str
    otherlanguages: dict[str, str]

    def __init__(self, language_code: str, reporter: Reporter | None = None) -> None: ...
    def __call__(self) -> str:
        """Return the babel call with correct options and settings"""
        ...
    def language_name(self, language_code: str) -> str:
        """Return TeX language name for `language_code`"""
        ...
    def get_language(self) -> str: ...

def __getattr__(name: str) -> Incomplete: ...
