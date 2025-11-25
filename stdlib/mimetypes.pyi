"""
Guess the MIME type of a file.

This module defines two useful functions:

guess_type(url, strict=True) -- guess the MIME type and encoding of a URL.

guess_extension(type, strict=True) -- guess the extension for a given MIME type.

It also contains the following, for tuning the behavior:

Data:

knownfiles -- list of files to parse
inited -- flag set when init() has been called
suffix_map -- dictionary mapping suffixes to suffixes
encodings_map -- dictionary mapping suffixes to encodings
types_map -- dictionary mapping suffixes to types

Functions:

init([files]) -- parse a list of files, default knownfiles (on Windows, the
  default values are taken from the registry)
read_mime_types(file) -- parse one file, return a dictionary or None
"""

import sys
from _typeshed import StrPath
from collections.abc import Iterable
from typing import IO

__all__ = [
    "knownfiles",
    "inited",
    "MimeTypes",
    "guess_type",
    "guess_all_extensions",
    "guess_extension",
    "add_type",
    "init",
    "read_mime_types",
    "suffix_map",
    "encodings_map",
    "types_map",
    "common_types",
]

if sys.version_info >= (3, 13):
    __all__ += ["guess_file_type"]

def guess_type(url: StrPath, strict: bool = True) -> tuple[str | None, str | None]: ...
def guess_all_extensions(type: str, strict: bool = True) -> list[str]: ...
def guess_extension(type: str, strict: bool = True) -> str | None: ...
def init(files: Iterable[StrPath] | None = None) -> None: ...
def read_mime_types(file: StrPath) -> dict[str, str] | None: ...
def add_type(type: str, ext: str, strict: bool = True) -> None: ...

if sys.version_info >= (3, 13):
    def guess_file_type(path: StrPath, *, strict: bool = True) -> tuple[str | None, str | None]:
        """
        Guess the type of a file based on its path.

        Similar to guess_type(), but takes file path istead of URL.
        """
        ...

inited: bool
knownfiles: list[StrPath]
suffix_map: dict[str, str]
encodings_map: dict[str, str]
types_map: dict[str, str]
common_types: dict[str, str]

class MimeTypes:
    """
    MIME-types datastore.

    This datastore can handle information from mime.types-style files
    and supports basic determination of MIME type from a filename or
    URL, and can guess a reasonable extension given a MIME type.
    """
    suffix_map: dict[str, str]
    encodings_map: dict[str, str]
    types_map: tuple[dict[str, str], dict[str, str]]
    types_map_inv: tuple[dict[str, str], dict[str, str]]
    def __init__(self, filenames: Iterable[StrPath] = (), strict: bool = True) -> None: ...
    def add_type(self, type: str, ext: str, strict: bool = True) -> None: ...
    def guess_extension(self, type: str, strict: bool = True) -> str | None: ...
    def guess_type(self, url: StrPath, strict: bool = True) -> tuple[str | None, str | None]: ...
    def guess_all_extensions(self, type: str, strict: bool = True) -> list[str]: ...
    def read(self, filename: StrPath, strict: bool = True) -> None: ...
    def readfp(self, fp: IO[str], strict: bool = True) -> None: ...
    def read_windows_registry(self, strict: bool = True) -> None: ...
    if sys.version_info >= (3, 13):
        def guess_file_type(self, path: StrPath, *, strict: bool = True) -> tuple[str | None, str | None]:
            """
            Guess the type of a file based on its path.

            Similar to guess_type(), but takes file path istead of URL.
            """
            ...
