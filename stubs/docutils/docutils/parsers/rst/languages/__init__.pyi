"""
This package contains modules for language-dependent features of
reStructuredText.
"""

from typing import ClassVar, Final, Protocol, type_check_only

from docutils.languages import LanguageImporter

__docformat__: Final = "reStructuredText"

@type_check_only
class _RstLanguageModule(Protocol):
    directives: dict[str, str]
    roles: dict[str, str]

class RstLanguageImporter(LanguageImporter):
    """
    Import language modules.

    When called with a BCP 47 language tag, instances return a module
    with localisations for "directive" and "role" names for  from
    `docutils.parsers.rst.languages` or the PYTHONPATH.

    If there is no matching module, warn (if a `reporter` is passed)
    and return None.
    """
    fallback: ClassVar[None]  # type: ignore[assignment]
    def check_content(self, module: _RstLanguageModule) -> None:
        """Check if we got an rST language module."""
        ...

get_language: RstLanguageImporter
