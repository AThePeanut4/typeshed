"""Utilities to support packages."""

import sys
from _typeshed import StrOrBytesPath, SupportsRead
from _typeshed.importlib import LoaderProtocol, MetaPathFinderProtocol, PathEntryFinderProtocol
from collections.abc import Callable, Iterable, Iterator
from typing import IO, Any, NamedTuple, TypeVar
from typing_extensions import deprecated

__all__ = [
    "get_importer",
    "iter_importers",
    "get_loader",
    "find_loader",
    "walk_packages",
    "iter_modules",
    "get_data",
    "read_code",
    "extend_path",
    "ModuleInfo",
]
if sys.version_info < (3, 12):
    __all__ += ["ImpImporter", "ImpLoader"]

_PathT = TypeVar("_PathT", bound=Iterable[str])

class ModuleInfo(NamedTuple):
    """A namedtuple with minimal info about a module."""
    module_finder: MetaPathFinderProtocol | PathEntryFinderProtocol
    name: str
    ispkg: bool

def extend_path(path: _PathT, name: str) -> _PathT:
    """
    Extend a package's path.

    Intended use is to place the following code in a package's __init__.py:

        from pkgutil import extend_path
        __path__ = extend_path(__path__, __name__)

    For each directory on sys.path that has a subdirectory that
    matches the package name, add the subdirectory to the package's
    __path__.  This is useful if one wants to distribute different
    parts of a single logical package as multiple directories.

    It also looks for *.pkg files beginning where * matches the name
    argument.  This feature is similar to *.pth files (see site.py),
    except that it doesn't special-case lines starting with 'import'.
    A *.pkg file is trusted at face value: apart from checking for
    duplicates, all entries found in a *.pkg file are added to the
    path, regardless of whether they are exist the filesystem.  (This
    is a feature.)

    If the input path is not a list (as is the case for frozen
    packages) it is returned unchanged.  The input path is not
    modified; an extended copy is returned.  Items are only appended
    to the copy at the end.

    It is assumed that sys.path is a sequence.  Items of sys.path that
    are not (unicode or 8-bit) strings referring to existing
    directories are ignored.  Unicode items of sys.path that cause
    errors when used as filenames may cause this function to raise an
    exception (in line with os.path.isdir() behavior).
    """
    ...

if sys.version_info < (3, 12):
    class ImpImporter:
        def __init__(self, path: StrOrBytesPath | None = None) -> None: ...

    class ImpLoader:
        def __init__(self, fullname: str, file: IO[str], filename: StrOrBytesPath, etc: tuple[str, str, int]) -> None: ...

@deprecated("Use importlib.util.find_spec() instead. Will be removed in Python 3.14.")
def find_loader(fullname: str) -> LoaderProtocol | None: ...
def get_importer(path_item: StrOrBytesPath) -> PathEntryFinderProtocol | None: ...
@deprecated("Use importlib.util.find_spec() instead. Will be removed in Python 3.14.")
def get_loader(module_or_name: str) -> LoaderProtocol | None: ...
def iter_importers(fullname: str = "") -> Iterator[MetaPathFinderProtocol | PathEntryFinderProtocol]: ...
def iter_modules(path: Iterable[StrOrBytesPath] | None = None, prefix: str = "") -> Iterator[ModuleInfo]: ...
def read_code(stream: SupportsRead[bytes]) -> Any: ...  # undocumented
def walk_packages(
    path: Iterable[StrOrBytesPath] | None = None, prefix: str = "", onerror: Callable[[str], object] | None = None
) -> Iterator[ModuleInfo]: ...
def get_data(package: str, resource: str) -> bytes | None: ...

if sys.version_info >= (3, 9):
    def resolve_name(name: str) -> Any:
        """
        Resolve a name to an object.

        It is expected that `name` will be a string in one of the following
        formats, where W is shorthand for a valid Python identifier and dot stands
        for a literal period in these pseudo-regexes:

        W(.W)*
        W(.W)*:(W(.W)*)?

        The first form is intended for backward compatibility only. It assumes that
        some part of the dotted name is a package, and the rest is an object
        somewhere within that package, possibly nested inside other objects.
        Because the place where the package stops and the object hierarchy starts
        can't be inferred by inspection, repeated attempts to import must be done
        with this form.

        In the second form, the caller makes the division point clear through the
        provision of a single colon: the dotted name to the left of the colon is a
        package to be imported, and the dotted name to the right is the object
        hierarchy within that package. Only one import is needed in this form. If
        it ends with the colon, then a module object is returned.

        The function will return an object (which might be a module), or raise one
        of the following exceptions:

        ValueError - if `name` isn't in a recognised format
        ImportError - if an import failed when it shouldn't have
        AttributeError - if a failure occurred when traversing the object hierarchy
                         within the imported package to get to the desired object.
        """
        ...
