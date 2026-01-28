"""Assertion library for python unit testing with a fluent API"""

import logging
from collections.abc import Callable, Generator
from typing import Any, TypeVar
from typing_extensions import Self

from .base import BaseMixin
from .collection import CollectionMixin
from .contains import ContainsMixin
from .date import DateMixin
from .dict import DictMixin
from .dynamic import DynamicMixin
from .exception import ExceptionMixin
from .extracting import ExtractingMixin
from .file import FileMixin
from .helpers import HelpersMixin
from .numeric import NumericMixin
from .snapshot import SnapshotMixin
from .string import StringMixin

_T = TypeVar("_T")
_V = TypeVar("_V", default=Any)

__version__: str
__tracebackhide__: bool

class WarningLoggingAdapter(logging.LoggerAdapter[logging.Logger]):
    """Logging adapter to unwind the stack to get the correct callee filename and line number."""
    def process(self, msg: str, kwargs: _T) -> tuple[str, _T]: ...

class AssertionBuilder(
    StringMixin,
    SnapshotMixin,
    NumericMixin,
    HelpersMixin,
    FileMixin,
    ExtractingMixin,
    ExceptionMixin,
    DynamicMixin,
    DictMixin,
    DateMixin,
    ContainsMixin[_V],
    CollectionMixin[_V],
    BaseMixin,
):
    """
    The main assertion class.  Never call the constructor directly, always use the
    :meth:`assert_that` helper instead.  Or if you just want warning messages, use the
    :meth:`assert_warn` helper.

    Args:
        val: the value to be tested (aka the actual value)
        description (str, optional): the extra error message description.  Defaults to ``''``
            (aka empty string)
        kind (str, optional): the kind of assertions, one of ``None``, ``soft``, or ``warn``.
            Defaults to ``None``
        expected (Error, optional): the expected exception.  Defaults to ``None``
        logger (Logger, optional): the logger for warning messages.  Defaults to ``None``
    """
    val: _V
    description: str
    kind: str | None
    expected: BaseException | None
    logger: logging.Logger
    def __init__(
        self,
        val: _V,
        description: str = "",
        kind: str | None = None,
        expected: BaseException | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        """Never call this constructor directly."""
        ...
    def builder(
        self,
        val: _V,
        description: str = "",
        kind: str | None = None,
        expected: BaseException | None = None,
        logger: logging.Logger | None = None,
    ) -> Self:
        """
        Helper to build a new :class:`AssertionBuilder` instance. Use this only if not chaining to ``self``.

def soft_assertions() -> Generator[None]: ...
def assert_that(val: _V, description: str = "") -> AssertionBuilder[_V]: ...
def assert_warn(val: _V, description: str = "", logger: logging.Logger | None = None) -> AssertionBuilder: ...
def fail(msg: str = "") -> None: ...
def soft_fail(msg: str = "") -> None: ...
def add_extension(func: Callable[..., AssertionBuilder[Any]]) -> None: ...
def remove_extension(func: Callable[..., AssertionBuilder[Any]]) -> None: ...
