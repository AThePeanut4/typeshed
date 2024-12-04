import contextlib
import types
from _typeshed import StrOrBytesPath, StrPath
from collections.abc import Generator
from typing import Generic, TypeVar
from typing_extensions import TypeAlias

from _cffi_backend import _CDataBase

def maybe_string(ptr: _CDataBase) -> str | None: ...
def to_bytes(s: _CDataBase | StrOrBytesPath | None, encoding: str = "utf-8", errors: str = "strict") -> _CDataBase | bytes: ...
def to_str(s: StrOrBytesPath) -> str: ...
def ptr_to_bytes(ptr_cdata: _CDataBase) -> bytes:
    """
    Convert a pointer coming from C code (<cdata 'some_type *'>)
    to a byte buffer containing the address that the pointer refers to.
    """
    ...
@contextlib.contextmanager
def new_git_strarray() -> Generator[_GitStrArray]: ...
def strarray_to_strings(arr: _GitStrArray) -> list[str]:
    """
    Return a list of strings from a git_strarray pointer.

    Free the strings contained in the git_strarry, this means it won't be usable after
    calling this function.
    """
    ...

# Actual type: _cffi_backend.__CDataOwn <cdata 'struct git_strarray *'>
# This is not a real subclassing. Just ensuring type-checkers sees this type as compatible with _CDataBase
# pyright has no error code for subclassing final
class _GitStrArray(_CDataBase):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    count: int
    strings: _CDataBase  # <cdata 'char * *'>

_IntoStrArray: TypeAlias = list[StrPath] | tuple[StrPath] | None

class StrArray:
    """
    A git_strarray wrapper

    Use this in order to get a git_strarray* to pass to libgit2 out of a
    list of strings. This has a context manager, which you should use, e.g.

        with StrArray(list_of_strings) as arr:
            C.git_function_that_takes_strarray(arr.ptr)

    To make a pre-existing git_strarray point to the provided list of strings,
    use the context manager's assign_to() method:

        struct = ffi.new('git_strarray *', [ffi.NULL, 0])
        with StrArray(list_of_strings) as arr:
            arr.assign_to(struct)

    The above construct is still subject to FFI scoping rules, i.e. the
    contents of 'struct' only remain valid within the StrArray context.
    """
    def __init__(self, l: _IntoStrArray) -> None: ...
    def __enter__(self) -> _CDataBase: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...
    @property
    def ptr(self) -> _CDataBase | _GitStrArray: ...
    def assign_to(self, git_strarray: _GitStrArray) -> None: ...

_T = TypeVar("_T")

class _GenericContainer(Generic[_T]):
    def __len__(self) -> int: ...
    def __getitem__(self, idx: int) -> _T: ...

class GenericIterator(Generic[_T]):
    """
    Helper to easily implement an iterator.

    The constructor gets a container which must implement __len__ and
    __getitem__
    """
    container: _GenericContainer[_T]
    length: int
    idx: int
    def __init__(self, container: _GenericContainer[_T]) -> None: ...
    def next(self) -> _T: ...
    def __next__(self) -> _T: ...
