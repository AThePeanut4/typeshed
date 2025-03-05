"""
pygments.plugin
~~~~~~~~~~~~~~~

Pygments plugin interface.

lexer plugins::

    [pygments.lexers]
    yourlexer = yourmodule:YourLexer

formatter plugins::

    [pygments.formatters]
    yourformatter = yourformatter:YourFormatter
    /.ext = yourformatter:YourFormatter

As you can see, you can define extensions for the formatter
with a leading slash.

syntax plugins::

    [pygments.styles]
    yourstyle = yourstyle:YourStyle

filter plugin::

    [pygments.filter]
    yourfilter = yourfilter:YourFilter


:copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
"""

import sys
from collections.abc import Generator
from typing import Any

from pygments.filter import Filter
from pygments.formatter import Formatter
from pygments.lexer import Lexer
from pygments.style import Style

LEXER_ENTRY_POINT: str
FORMATTER_ENTRY_POINT: str
STYLE_ENTRY_POINT: str
FILTER_ENTRY_POINT: str

if sys.version_info >= (3, 10):
    from importlib.metadata import EntryPoints
    def iter_entry_points(group_name: str) -> EntryPoints: ...

else:
    from importlib.metadata import EntryPoint

    def iter_entry_points(group_name: str) -> tuple[EntryPoint, ...] | list[EntryPoint]: ...

def find_plugin_lexers() -> Generator[type[Lexer], None, None]: ...
def find_plugin_formatters() -> Generator[tuple[str, type[Formatter[Any]]], None, None]: ...
def find_plugin_styles() -> Generator[tuple[str, type[Style]], None, None]: ...
def find_plugin_filters() -> Generator[tuple[str, type[Filter]], None, None]: ...
