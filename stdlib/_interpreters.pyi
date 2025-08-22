"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""

import types
from collections.abc import Callable
from typing import Any, Final, Literal, SupportsIndex, TypeVar, overload
from typing_extensions import TypeAlias

_R = TypeVar("_R")

_Configs: TypeAlias = Literal["default", "isolated", "legacy", "empty", ""]
_SharedDict: TypeAlias = dict[str, Any]  # many objects can be shared

class InterpreterError(Exception):
    """A cross-interpreter operation failed"""
    ...
class InterpreterNotFoundError(InterpreterError):
    """An interpreter was not found"""
    ...
class NotShareableError(ValueError): ...

class CrossInterpreterBufferView:
    def __buffer__(self, flags: int, /) -> memoryview:
        """Return a buffer object that exposes the underlying memory of the object."""
        ...

def new_config(name: _Configs = "isolated", /, **overides: object) -> types.SimpleNamespace: ...
def create(config: types.SimpleNamespace | _Configs | None = "isolated", *, reqrefs: bool = False) -> int: ...
def destroy(id: SupportsIndex, *, restrict: bool = False) -> None: ...
def list_all(*, require_ready: bool = False) -> list[tuple[int, _Whence]]: ...
def get_current() -> tuple[int, _Whence]: ...
def get_main() -> tuple[int, _Whence]: ...
def is_running(id: SupportsIndex, *, restrict: bool = False) -> bool: ...
def get_config(id: SupportsIndex, *, restrict: bool = False) -> types.SimpleNamespace: ...
def whence(id: SupportsIndex) -> _Whence: ...
def exec(
    id: SupportsIndex, code: str | types.CodeType | Callable[[], object], shared: _SharedDict = {}, *, restrict: bool = False
) -> None | types.SimpleNamespace: ...
def call(
    id: SupportsIndex,
    callable: Callable[..., _R],
    args: tuple[Any, ...] = (),
    kwargs: dict[str, Any] = {},
    *,
    preserve_exc: bool = False,
    restrict: bool = False,
) -> tuple[_R, types.SimpleNamespace]:
    """
    call(id, callable, args=None, kwargs=None, *, restrict=False)

    Call the provided object in the identified interpreter.
    Pass the given args and kwargs, if possible.

    "callable" may be a plain function with no free vars that takes
    no arguments.

    The function's code object is used and all its state
    is ignored, including its __globals__ dict.
    """
    ...
def run_string(
    id: SupportsIndex, script: str | types.CodeType | Callable[[], object], shared: _SharedDict = {}, *, restrict: bool = False
) -> None: ...
def run_func(
    id: SupportsIndex, func: types.CodeType | Callable[[], object], shared: _SharedDict = {}, *, restrict: bool = False
) -> None: ...
def set___main___attrs(id: SupportsIndex, updates: _SharedDict, *, restrict: bool = False) -> None: ...
def incref(id: SupportsIndex, *, implieslink: bool = False, restrict: bool = False) -> None: ...
def decref(id: SupportsIndex, *, restrict: bool = False) -> None: ...
def is_shareable(obj: object) -> bool: ...
@overload
def capture_exception(exc: BaseException) -> types.SimpleNamespace: ...
@overload
def capture_exception(exc: None = None) -> types.SimpleNamespace | None: ...

_Whence: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
WHENCE_UNKNOWN: Final = 0
WHENCE_RUNTIME: Final = 1
WHENCE_LEGACY_CAPI: Final = 2
WHENCE_CAPI: Final = 3
WHENCE_XI: Final = 4
WHENCE_STDLIB: Final = 5
