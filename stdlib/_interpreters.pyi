"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""

import types
from collections.abc import Callable
from typing import Any, Final, Literal, SupportsIndex
from typing_extensions import TypeAlias

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

def new_config(name: _Configs = "isolated", /, **overides: object) -> types.SimpleNamespace:
    """
    new_config(name='isolated', /, **overrides) -> type.SimpleNamespace

    Return a representation of a new PyInterpreterConfig.

    The name determines the initial values of the config.  Supported named
    configs are: default, isolated, legacy, and empty.

    Any keyword arguments are set on the corresponding config fields,
    overriding the initial values.
    """
    ...
def create(config: types.SimpleNamespace | _Configs | None = "isolated", *, reqrefs: bool = False) -> int:
    """
    create([config], *, reqrefs=False) -> ID

    Create a new interpreter and return a unique generated ID.

    The caller is responsible for destroying the interpreter before exiting,
    typically by using _interpreters.destroy().  This can be managed 
    automatically by passing "reqrefs=True" and then using _incref() and
    _decref()` appropriately.

    "config" must be a valid interpreter config or the name of a
    predefined config ("isolated" or "legacy").  The default
    is "isolated".
    """
    ...
def destroy(id: SupportsIndex, *, restrict: bool = False) -> None:
    """
    destroy(id, *, restrict=False)

    Destroy the identified interpreter.

    Attempting to destroy the current interpreter raises InterpreterError.
    So does an unrecognized ID.
    """
    ...
def list_all(*, require_ready: bool) -> list[tuple[int, int]]:
    """
    list_all() -> [(ID, whence)]

    Return a list containing the ID of every existing interpreter.
    """
    ...
def get_current() -> tuple[int, int]:
    """
    get_current() -> (ID, whence)

    Return the ID of current interpreter.
    """
    ...
def get_main() -> tuple[int, int]:
    """
    get_main() -> (ID, whence)

    Return the ID of main interpreter.
    """
    ...
def is_running(id: SupportsIndex, *, restrict: bool = False) -> bool:
    """
    is_running(id, *, restrict=False) -> bool

    Return whether or not the identified interpreter is running.
    """
    ...
def get_config(id: SupportsIndex, *, restrict: bool = False) -> types.SimpleNamespace:
    """
    get_config(id, *, restrict=False) -> types.SimpleNamespace

    Return a representation of the config used to initialize the interpreter.
    """
    ...
def whence(id: SupportsIndex) -> int:
    """
    whence(id) -> int

    Return an identifier for where the interpreter was created.
    """
    ...
def exec(
    id: SupportsIndex,
    code: str | types.CodeType | Callable[[], object],
    shared: _SharedDict | None = None,
    *,
    restrict: bool = False,
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
    id: SupportsIndex,
    script: str | types.CodeType | Callable[[], object],
    shared: _SharedDict | None = None,
    *,
    restrict: bool = False,
) -> None: ...
def run_func(
    id: SupportsIndex, func: types.CodeType | Callable[[], object], shared: _SharedDict | None = None, *, restrict: bool = False
) -> None: ...
def set___main___attrs(id: SupportsIndex, updates: _SharedDict, *, restrict: bool = False) -> None: ...
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
