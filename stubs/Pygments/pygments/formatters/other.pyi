"""
pygments.formatters.other
~~~~~~~~~~~~~~~~~~~~~~~~~

Other formatters: NullFormatter, RawTokenFormatter.

:copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
"""

from typing import Any, TypeVar

from pygments.formatter import Formatter

_T = TypeVar("_T", str, bytes)

class NullFormatter(Formatter[_T]):
    """Output the text unchanged without any formatting."""
    name: str
    aliases: Any
    filenames: Any
    def format(self, tokensource, outfile) -> None: ...

class RawTokenFormatter(Formatter[bytes]):
    name: str
    aliases: Any
    filenames: Any
    unicodeoutput: bool
    encoding: str
    compress: Any
    error_color: Any
    def format(self, tokensource, outfile) -> None: ...

class TestcaseFormatter(Formatter[_T]):
    """
    Format tokens as appropriate for a new testcase.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Any
    def format(self, tokensource, outfile) -> None: ...
