"""This package contains modules for language-dependent features of Docutils."""

from _typeshed import Incomplete
from typing import Protocol

from docutils.utils import Reporter

class _LanguageModule(Protocol):
    labels: dict[str, str]
    author_separators: list[str]
    bibliographic_fields: list[str]

class LanguageImporter:
    """
    Import language modules.

    When called with a BCP 47 language tag, instances return a module
    with localisations from `docutils.languages` or the PYTHONPATH.

    If there is no matching module, warn (if a `reporter` is passed)
    and fall back to English.
    """
    def __call__(self, language_code: str, reporter: Reporter | None = None) -> _LanguageModule: ...
    def __getattr__(self, name: str, /) -> Incomplete: ...

get_language: LanguageImporter
