"""
A Path-like interface for zipfiles.

This codebase is shared between zipfile.Path in the stdlib
and zipp in PyPI. See
https://github.com/python/importlib_metadata/wiki/Development-Methodology
for more detail.
"""

import sys
from _typeshed import StrPath
from collections.abc import Iterator, Sequence
from io import TextIOWrapper
from os import PathLike
from typing import IO, Literal, TypeVar, overload
from typing_extensions import Self
from zipfile import ZipFile

_ZF = TypeVar("_ZF", bound=ZipFile)

if sys.version_info >= (3, 12):
    __all__ = ["Path"]

    class InitializedState:
        """Mix-in to save the initialization state for pickling."""
        def __init__(self, *args: object, **kwargs: object) -> None: ...
        def __getstate__(self) -> tuple[list[object], dict[object, object]]: ...
        def __setstate__(self, state: Sequence[tuple[list[object], dict[object, object]]]) -> None: ...

    class CompleteDirs(InitializedState, ZipFile):
        """
        A ZipFile subclass that ensures that implied directories
        are always included in the namelist.

        >>> list(CompleteDirs._implied_dirs(['foo/bar.txt', 'foo/bar/baz.txt']))
        ['foo/', 'foo/bar/']
        >>> list(CompleteDirs._implied_dirs(['foo/bar.txt', 'foo/bar/baz.txt', 'foo/bar/']))
        ['foo/']
        """
        def resolve_dir(self, name: str) -> str:
            """
            If the name represents a directory, return that name
            as a directory (with the trailing slash).
            """
            ...
        @overload
        @classmethod
        def make(cls, source: ZipFile) -> CompleteDirs:
            """
            Given a source (filename or zipfile), return an
            appropriate CompleteDirs subclass.
            """
            ...
        @overload
        @classmethod
        def make(cls, source: StrPath | IO[bytes]) -> Self:
            """
            Given a source (filename or zipfile), return an
            appropriate CompleteDirs subclass.
            """
            ...
        if sys.version_info >= (3, 13):
            @classmethod
            def inject(cls, zf: _ZF) -> _ZF:
                """
                Given a writable zip file zf, inject directory entries for
                any directories implied by the presence of children.
                """
                ...

    class Path:
        "A :class:`importlib.resources.abc.Traversable` interface for zip files.\n\nImplements many of the features users enjoy from\n:class:`pathlib.Path`.\n\nConsider a zip file with this structure::\n\n    .\n    ├── a.txt\n    └── b\n        ├── c.txt\n        └── d\n            └── e.txt\n\n>>> data = io.BytesIO()\n>>> zf = ZipFile(data, 'w')\n>>> zf.writestr('a.txt', 'content of a')\n>>> zf.writestr('b/c.txt', 'content of c')\n>>> zf.writestr('b/d/e.txt', 'content of e')\n>>> zf.filename = 'mem/abcde.zip'\n\nPath accepts the zipfile object itself or a filename\n\n>>> path = Path(zf)\n\nFrom there, several path operations are available.\n\nDirectory iteration (including the zip file itself):\n\n>>> a, b = path.iterdir()\n>>> a\nPath('mem/abcde.zip', 'a.txt')\n>>> b\nPath('mem/abcde.zip', 'b/')\n\nname property:\n\n>>> b.name\n'b'\n\njoin with divide operator:\n\n>>> c = b / 'c.txt'\n>>> c\nPath('mem/abcde.zip', 'b/c.txt')\n>>> c.name\n'c.txt'\n\nRead text:\n\n>>> c.read_text(encoding='utf-8')\n'content of c'\n\nexistence:\n\n>>> c.exists()\nTrue\n>>> (b / 'missing.txt').exists()\nFalse\n\nCoercion to string:\n\n>>> import os\n>>> str(c).replace(os.sep, posixpath.sep)\n'mem/abcde.zip/b/c.txt'\n\nAt the root, ``name``, ``filename``, and ``parent``\nresolve to the zipfile.\n\n>>> str(path)\n'mem/abcde.zip/'\n>>> path.name\n'abcde.zip'\n>>> path.filename == pathlib.Path('mem/abcde.zip')\nTrue\n>>> str(path.parent)\n'mem'\n\nIf the zipfile has no filename, such \ufeffattributes are not\nvalid and accessing them will raise an Exception.\n\n>>> zf.filename = None\n>>> path.name\nTraceback (most recent call last):\n...\nTypeError: ...\n\n>>> path.filename\nTraceback (most recent call last):\n...\nTypeError: ...\n\n>>> path.parent\nTraceback (most recent call last):\n...\nTypeError: ...\n\n# workaround python/cpython#106763\n>>> pass"
        root: CompleteDirs
        at: str
        def __init__(self, root: ZipFile | StrPath | IO[bytes], at: str = "") -> None:
            """
            Construct a Path from a ZipFile or filename.

            Note: When the source is an existing ZipFile object,
            its type (__class__) will be mutated to a
            specialized type. If the caller wishes to retain the
            original type, the caller should either create a
            separate ZipFile object or pass a filename.
            """
            ...
        @property
        def name(self) -> str: ...
        @property
        def parent(self) -> PathLike[str]: ...  # undocumented
        @property
        def filename(self) -> PathLike[str]: ...  # undocumented
        @property
        def suffix(self) -> str: ...
        @property
        def suffixes(self) -> list[str]: ...
        @property
        def stem(self) -> str: ...
        @overload
        def open(
            self,
            mode: Literal["r", "w"] = "r",
            encoding: str | None = None,
            errors: str | None = None,
            newline: str | None = None,
            line_buffering: bool = ...,
            write_through: bool = ...,
            *,
            pwd: bytes | None = None,
        ) -> TextIOWrapper:
            """
            Open this entry as text or binary following the semantics
            of ``pathlib.Path.open()`` by passing arguments through
            to io.TextIOWrapper().
            """
            ...
        @overload
        def open(self, mode: Literal["rb", "wb"], *, pwd: bytes | None = None) -> IO[bytes]:
            """
            Open this entry as text or binary following the semantics
            of ``pathlib.Path.open()`` by passing arguments through
            to io.TextIOWrapper().
            """
            ...
        def iterdir(self) -> Iterator[Self]: ...
        def is_dir(self) -> bool: ...
        def is_file(self) -> bool: ...
        def exists(self) -> bool: ...
        def read_text(
            self,
            encoding: str | None = ...,
            errors: str | None = ...,
            newline: str | None = ...,
            line_buffering: bool = ...,
            write_through: bool = ...,
        ) -> str: ...
        def read_bytes(self) -> bytes: ...
        def joinpath(self, *other: StrPath) -> Path: ...
        def glob(self, pattern: str) -> Iterator[Self]: ...
        def rglob(self, pattern: str) -> Iterator[Self]: ...
        def is_symlink(self) -> Literal[False]:
            """Return whether this path is a symlink."""
            ...
        def relative_to(self, other: Path, *extra: StrPath) -> str: ...
        def match(self, path_pattern: str) -> bool: ...
        def __eq__(self, other: object) -> bool:
            """
            >>> Path(zipfile.ZipFile(io.BytesIO(), 'w')) == 'foo'
            False
            """
            ...
        def __hash__(self) -> int: ...
        def __truediv__(self, add: StrPath) -> Path: ...
