"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""

import types
from collections.abc import Callable, Mapping
from typing import Final, Literal, SupportsIndex
from typing_extensions import TypeAlias

_Configs: TypeAlias = Literal["default", "isolated", "legacy", "empty", ""]

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
def list_all(*, require_ready: bool) -> list[tuple[int, int]]: ...
def get_current() -> tuple[int, int]: ...
def get_main() -> tuple[int, int]: ...
def is_running(id: SupportsIndex, *, restrict: bool = False) -> bool: ...
def get_config(id: SupportsIndex, *, restrict: bool = False) -> types.SimpleNamespace: ...
def whence(id: SupportsIndex) -> int: ...
def exec(
    id: SupportsIndex, code: str | types.CodeType | Callable[[], object], shared: bool | None = None, *, restrict: bool = False
) -> None | types.SimpleNamespace: ...
def call(
    id: SupportsIndex,
    callable: Callable[..., object],
    args: tuple[object, ...] | None = None,
    kwargs: dict[str, object] | None = None,
    *,
    restrict: bool = False,
) -> object:
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
    id: SupportsIndex, script: str | types.CodeType | Callable[[], object], shared: bool | None = None, *, restrict: bool = False
) -> None:
    """
    run_string(id, script, shared=None, *, restrict=False)

    Execute the provided string in the identified interpreter.

    (See _interpreters.exec().
    """
    ...
def run_func(
    id: SupportsIndex, func: types.CodeType | Callable[[], object], shared: bool | None = None, *, restrict: bool = False
) -> None:
    """
    run_func(id, func, shared=None, *, restrict=False)

    Execute the body of the provided function in the identified interpreter.
    Code objects are also supported.  In both cases, closures and args
    are not supported.  Methods and other callables are not supported either.

    (See _interpreters.exec().
    """
    ...
def set___main___attrs(id: SupportsIndex, updates: Mapping[str, object], *, restrict: bool = False) -> None:
    """
    set___main___attrs(id, ns, *, restrict=False)

    Bind the given attributes in the interpreter's __main__ module.
    """
    ...
def incref(id: SupportsIndex, *, implieslink: bool = False, restrict: bool = False) -> None: ...
def decref(id: SupportsIndex, *, restrict: bool = False) -> None: ...
def is_shareable(obj: object) -> bool:
    """
    is_shareable(obj) -> bool

    Return True if the object's data may be shared between interpreters and
    False otherwise.
    """
    ...
def capture_exception(exc: BaseException | None = None) -> types.SimpleNamespace:
    """
    capture_exception(exc=None) -> types.SimpleNamespace

    Return a snapshot of an exception.  If "exc" is None
    then the current exception, if any, is used (but not cleared).

    The returned snapshot is the same as what _interpreters.exec() returns.
    """
    ...

WHENCE_UNKNOWN: Final = 0
WHENCE_RUNTIME: Final = 1
WHENCE_LEGACY_CAPI: Final = 2
WHENCE_CAPI: Final = 3
WHENCE_XI: Final = 4
WHENCE_STDLIB: Final = 5
