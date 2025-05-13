"""
Policy framework for the email package.

Allows fine grained feature control of how the package parses and emits data.
"""

from abc import ABCMeta, abstractmethod
from email.errors import MessageDefect
from email.header import Header
from email.message import Message
from typing import Any, Generic, Protocol, TypeVar, type_check_only
from typing_extensions import Self

__all__ = ["Policy", "Compat32", "compat32"]

_MessageT = TypeVar("_MessageT", bound=Message[Any, Any], default=Message[str, str])
_MessageT_co = TypeVar("_MessageT_co", covariant=True, bound=Message[Any, Any], default=Message[str, str])

@type_check_only
class _MessageFactory(Protocol[_MessageT]):
    def __call__(self, policy: Policy[_MessageT]) -> _MessageT: ...

# Policy below is the only known direct subclass of _PolicyBase. We therefore
# assume that the __init__ arguments and attributes of _PolicyBase are
# the same as those of Policy.
class _PolicyBase(Generic[_MessageT_co]):
    max_line_length: int | None
    linesep: str
    cte_type: str
    raise_on_defect: bool
    mangle_from_: bool
    message_factory: _MessageFactory[_MessageT_co] | None
    # Added in Python 3.9.20, 3.10.15, 3.11.10, 3.12.5
    verify_generated_headers: bool

    def __init__(
        self,
        *,
        max_line_length: int | None = 78,
        linesep: str = "\n",
        cte_type: str = "8bit",
        raise_on_defect: bool = False,
        mangle_from_: bool = ...,  # default depends on sub-class
        message_factory: _MessageFactory[_MessageT_co] | None = None,
        # Added in Python 3.9.20, 3.10.15, 3.11.10, 3.12.5
        verify_generated_headers: bool = True,
    ) -> None:
        """
        Create new Policy, possibly overriding some defaults.

        See class docstring for a list of overridable attributes.
        """
        ...
    def clone(
        self,
        *,
        max_line_length: int | None = ...,
        linesep: str = ...,
        cte_type: str = ...,
        raise_on_defect: bool = ...,
        mangle_from_: bool = ...,
        message_factory: _MessageFactory[_MessageT_co] | None = ...,
        # Added in Python 3.9.20, 3.10.15, 3.11.10, 3.12.5
        verify_generated_headers: bool = ...,
    ) -> Self:
        """
        Return a new instance with specified attributes changed.

        The new instance has the same attribute values as the current object,
        except for the changes passed in as keyword arguments.
        """
        ...
    def __add__(self, other: Policy) -> Self:
        """
        Non-default values from right operand override those from left.

        The object returned is a new instance of the subclass.
        """
        ...

class Policy(_PolicyBase[_MessageT_co], metaclass=ABCMeta):
    # Every Message object has a `defects` attribute, so the following
    # methods will work for any Message object.
    def handle_defect(self, obj: Message[Any, Any], defect: MessageDefect) -> None: ...
    def register_defect(self, obj: Message[Any, Any], defect: MessageDefect) -> None: ...
    def header_max_count(self, name: str) -> int | None: ...
    @abstractmethod
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]:
        """
        Given a list of linesep terminated strings constituting the lines of
        a single header, return the (name, value) tuple that should be stored
        in the model.  The input lines should retain their terminating linesep
        characters.  The lines passed in by the email package may contain
        surrogateescaped binary data.
        """
        ...
    @abstractmethod
    def header_store_parse(self, name: str, value: str) -> tuple[str, str]:
        """
        Given the header name and the value provided by the application
        program, return the (name, value) that should be stored in the model.
        """
        ...
    @abstractmethod
    def header_fetch_parse(self, name: str, value: str) -> str:
        """
        Given the header name and the value from the model, return the value
        to be returned to the application program that is requesting that
        header.  The value passed in by the email package may contain
        surrogateescaped binary data if the lines were parsed by a BytesParser.
        The returned value should not contain any surrogateescaped data.
        """
        ...
    @abstractmethod
    def fold(self, name: str, value: str) -> str:
        """
        Given the header name and the value from the model, return a string
        containing linesep characters that implement the folding of the header
        according to the policy controls.  The value passed in by the email
        package may contain surrogateescaped binary data if the lines were
        parsed by a BytesParser.  The returned value should not contain any
        surrogateescaped data.
        """
        ...
    @abstractmethod
    def fold_binary(self, name: str, value: str) -> bytes:
        """
        Given the header name and the value from the model, return binary
        data containing linesep characters that implement the folding of the
        header according to the policy controls.  The value passed in by the
        email package may contain surrogateescaped binary data.
        """
        ...

class Compat32(Policy[_MessageT_co]):
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    def header_store_parse(self, name: str, value: str) -> tuple[str, str]: ...
    def header_fetch_parse(self, name: str, value: str) -> str | Header: ...  # type: ignore[override]
    def fold(self, name: str, value: str) -> str: ...
    def fold_binary(self, name: str, value: str) -> bytes: ...

compat32: Compat32[Message[str, str]]
