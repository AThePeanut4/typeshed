from _typeshed import StrPath, Unused
from collections.abc import Iterable
from re import Pattern
from typing import Literal, overload

# class is entirely undocumented
class FileList:
    """
    A list of files built by on exploring the filesystem and filtered by
    applying various patterns to what we find there.

    Instance attributes:
      dir
        directory from which files will be taken -- only used if
        'allfiles' not supplied to constructor
      files
        list of filenames currently being built/filtered/manipulated
      allfiles
        complete list of files under consideration (ie. without any
        filtering applied)
    """
    allfiles: Iterable[str] | None
    files: list[str]
    def __init__(self, warn: Unused = None, debug_print: Unused = None) -> None: ...
    def set_allfiles(self, allfiles: Iterable[str]) -> None: ...
    def findall(self, dir: StrPath = ...) -> None: ...
    def debug_print(self, msg: object) -> None: ...
    def append(self, item: str) -> None: ...
    def extend(self, items: Iterable[str]) -> None: ...
    def sort(self) -> None: ...
    def remove_duplicates(self) -> None: ...
    def process_template_line(self, line: str) -> None: ...
    @overload
    def include_pattern(
        self, pattern: str, anchor: bool = True, prefix: str | None = None, is_regex: Literal[False] = False
    ) -> bool: ...
    @overload
    def include_pattern(
        self, pattern: str | Pattern[str], anchor: bool = True, prefix: str | None = None, *, is_regex: Literal[True]
    ) -> bool: ...
    @overload
    def include_pattern(self, pattern: str | Pattern[str], anchor: bool, prefix: str | None, is_regex: Literal[True]) -> bool: ...
    @overload
    def exclude_pattern(
        self, pattern: str, anchor: bool = True, prefix: str | None = None, is_regex: Literal[False] = False
    ) -> bool: ...
    @overload
    def exclude_pattern(
        self, pattern: str | Pattern[str], anchor: bool = True, prefix: str | None = None, *, is_regex: Literal[True]
    ) -> bool: ...
    @overload
    def exclude_pattern(self, pattern: str | Pattern[str], anchor: bool, prefix: str | None, is_regex: Literal[True]) -> bool: ...
