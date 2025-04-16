import io
from _typeshed import Incomplete, StrOrBytesPath, StrPath
from collections.abc import Generator, Iterable, MutableSequence
from os import PathLike
from tarfile import _Fileobj
from tempfile import _TemporaryFileWrapper

def match_tag(tag: str) -> bool: ...
def tar(
    path: PathLike[str],
    exclude: list[str] | None = None,
    dockerfile: tuple[str | None, str | None] | None = None,
    fileobj: _Fileobj | None = None,
    gzip: bool = False,
) -> _TemporaryFileWrapper[bytes] | _Fileobj: ...
def exclude_paths(root: StrPath, patterns: MutableSequence[str], dockerfile: str | None = None) -> set[str]:
    """
    Given a root directory path and a list of .dockerignore patterns, return
    an iterator of all paths (both regular files and directories) in the root
    directory that do *not* match any of the patterns.

    All paths returned are relative to the root.
    """
    ...
def build_file_list(root: str) -> list[str]: ...
def create_archive(
    root: str,
    files: Iterable[str] | None = None,
    fileobj: _Fileobj | None = None,
    gzip: bool = False,
    extra_files: Incomplete | None = None,
) -> _TemporaryFileWrapper[bytes] | _Fileobj: ...
def mkbuildcontext(dockerfile: io.IOBase | StrOrBytesPath) -> _TemporaryFileWrapper[bytes]: ...
def split_path(p: str) -> list[str]: ...
def normalize_slashes(p: str) -> str: ...
def walk(root: StrPath, patterns: Iterable[str], default: bool = True) -> Generator[str]: ...

class PatternMatcher:
    patterns: list[Pattern]
    def __init__(self, patterns: Iterable[str]) -> None: ...
    def matches(self, filepath: PathLike[str]) -> bool: ...
    def walk(self, root: StrPath) -> Generator[str]: ...

class Pattern:
    exclusion: bool
    dirs: list[str]
    cleaned_pattern: str
    def __init__(self, pattern_str: str) -> None: ...
    @classmethod
    def normalize(cls, p: str) -> list[str]: ...
    def match(self, filepath: str) -> bool: ...
