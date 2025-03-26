from _typeshed import Incomplete, StrOrBytesPath
from typing import Any, Final

LIST_OF_FILE_NAMES: Final[list[str]]

def get_extension(srcfilename, modname, sources=(), **kwds): ...
def compile(tmpdir, ext, compiler_verbose: int = 0, debug: Incomplete | None = None):
    """Compile a C extension module using distutils."""
    ...
def maybe_relative_path(path: StrOrBytesPath) -> StrOrBytesPath | str: ...

int_or_long = int

def flatten(x: int | str | list[Any] | tuple[Any] | dict[Any, Any]) -> str: ...
