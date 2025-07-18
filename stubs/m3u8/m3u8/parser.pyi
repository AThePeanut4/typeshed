from collections.abc import Callable
from datetime import date, datetime, time
from itertools import repeat
from re import Pattern
from typing import Any, overload
from typing_extensions import TypeAlias

_CustomTagsParser: TypeAlias = Callable[[str, int, dict[str, Any], dict[str, Any]], object]

ATTRIBUTELISTPATTERN: Pattern[str]

def cast_date_time(value: str) -> datetime: ...
@overload
def format_date_time(value: time, *, timespec: str = ...) -> str: ...
@overload
def format_date_time(value: datetime, *, sep: str = ..., timespec: str = ...) -> str: ...
@overload
def format_date_time(value: date) -> str: ...

class ParseError(Exception):
    lineno: int
    line: str
    def __init__(self, lineno: int, line: str) -> None: ...

def parse(content: str, strict: bool = False, custom_tags_parser: _CustomTagsParser | None = None) -> dict[str, Any]:
    """Given a M3U8 playlist content returns a dictionary with all data found"""
    ...
def string_to_lines(string: str) -> list[str]: ...
def remove_quotes_parser(*attrs: repeat[Callable[[str], str]]) -> dict[repeat[Callable[[str], str]], Callable[[str], str]]: ...
def remove_quotes(string: str) -> str:
    """
    Remove quotes from string.

    Ex.:
      "foo" -> foo
      'foo' -> foo
      'foo  -> 'foo
    """
    ...
def normalize_attribute(attribute: str) -> str: ...
