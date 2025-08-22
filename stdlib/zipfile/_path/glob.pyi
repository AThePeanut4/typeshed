import sys
from collections.abc import Iterator
from re import Match

if sys.version_info >= (3, 13):
    class Translator:
        if sys.platform == "win32":
            def __init__(self, seps: str = "\\/") -> None: ...
        else:
            def __init__(self, seps: str = "/") -> None: ...

        def translate(self, pattern: str) -> str: ...
        def extend(self, pattern: str) -> str: ...
        def match_dirs(self, pattern: str) -> str: ...
        def translate_core(self, pattern: str) -> str: ...
        def replace(self, match: Match[str]) -> str: ...
        def restrict_rglob(self, pattern: str) -> None: ...
        def star_not_empty(self, pattern: str) -> str: ...

else:
    def translate(pattern: str) -> str: ...
    def match_dirs(pattern: str) -> str:
        """
        Ensure that zipfile.Path directory names are matched.

        zipfile.Path directory names always end in a slash.
        """
        ...
    def translate_core(pattern: str) -> str:
        r"""
        Given a glob pattern, produce a regex that matches it.

        >>> translate('*.txt')
        '[^/]*\\.txt'
        >>> translate('a?txt')
        'a.txt'
        >>> translate('**/*')
        '.*/[^/]*'
        """
        ...
    def replace(match: Match[str]) -> str:
        """Perform the replacements for a match from :func:`separate`."""
        ...

def separate(pattern: str) -> Iterator[Match[str]]:
    """
    Separate out character sets to avoid translating their contents.

    >>> [m.group(0) for m in separate('*.txt')]
    ['*.txt']
    >>> [m.group(0) for m in separate('a[?]txt')]
    ['a', '[?]', 'txt']
    """
    ...
