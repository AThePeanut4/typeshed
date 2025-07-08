"""vobject module for reading vCard and vCalendar files."""

import logging
import re
from _typeshed import Incomplete, MaybeNone, SupportsWrite
from collections.abc import Generator, Iterator
from typing import Any, AnyStr, Final, Literal, TypeVar, overload
from typing_extensions import Self

_V = TypeVar("_V", bound=VBase)
_W = TypeVar("_W", bound=SupportsWrite[bytes])

VERSION: Final[str]

def to_unicode(value: str | bytes | bytearray) -> str: ...
def to_basestring(s: str | bytes) -> bytes: ...

logger: logging.Logger
DEBUG: bool
CR: str
LF: str
CRLF: str
SPACE: str
TAB: str
SPACEORTAB: str

class VBase:
    """
    Base class for ContentLine and Component.

    @ivar behavior:
        The Behavior class associated with this object, which controls
        validation, transformations, and encoding.
    @ivar parentBehavior:
        The object's parent's behavior, or None if no behaviored parent exists.
    @ivar isNative:
        Boolean describing whether this component is a Native instance.
    @ivar group:
        An optional group prefix, should be used only to indicate sort order in
        vCards, according to spec.

    Current spec: 4.0 (http://tools.ietf.org/html/rfc6350)
    """
    group: Incomplete | None
    behavior: Incomplete | None
    parentBehavior: Incomplete | None
    isNative: bool
    def __init__(self, group=None) -> None: ...
    def copy(self, copyit: VBase) -> None: ...
    def validate(self, *args, **kwds) -> bool:
        """Call the behavior's validate method, or return True."""
        ...
    def getChildren(self) -> list[Incomplete]:
        """Return an iterable containing the contents of the object."""
        ...
    def clearBehavior(self, cascade: bool = True) -> None:
        """Set behavior to None. Do for all descendants if cascading."""
        ...
    def autoBehavior(self, cascade: bool = False) -> None:
        """
        Set behavior if name is in self.parentBehavior.knownChildren.

        If cascade is True, unset behavior and parentBehavior for all
        descendants, then recalculate behavior and parentBehavior.
        """
        ...
    def setBehavior(self, behavior, cascade: bool = True) -> None:
        """Set behavior. If cascade is True, autoBehavior all descendants."""
        ...
    def transformToNative(self):
        """
        Transform this object into a custom VBase subclass.

        transformToNative should always return a representation of this object.
        It may do so by modifying self in place then returning self, or by
        creating a new object.
        """
        ...
    def transformFromNative(self):
        """
        Return self transformed into a ContentLine or Component if needed.

        May have side effects.  If it does, transformFromNative and
        transformToNative MUST have perfectly inverse side effects. Allowing
        such side effects is convenient for objects whose transformations only
        change a few attributes.

        Note that it isn't always possible for transformFromNative to be a
        perfect inverse of transformToNative, in such cases transformFromNative
        should return a new object, not self after modifications.
        """
        ...
    def transformChildrenToNative(self) -> None:
        """Recursively replace children with their native representation."""
        ...
    def transformChildrenFromNative(self, clearBehavior: bool = True) -> None:
        """Recursively transform native children to vanilla representations."""
        ...
    # Use Any because args and kwargs are passed to the behavior object
    @overload
    def serialize(
        self, buf: None = None, lineLength: int = 75, validate: bool = True, behavior=None, *args: Any, **kwargs: Any
    ) -> str:
        """
        Serialize to buf if it exists, otherwise return a string.

def toVName(name: str, stripNum: int = 0, upper: bool = False) -> str: ...

class ContentLine(VBase):
    name: str
    encoded: bool
    params: dict[Incomplete, list[Incomplete]]
    singletonparams: list[Incomplete]
    isNative: bool
    lineNumber: int | None
    value: str
    def __init__(
        self,
        name: str,
        params: dict[Incomplete, list[Incomplete]],
        value: str,
        group=None,
        encoded: bool = False,
        isNative: bool = False,
        lineNumber: int | None = None,
        *args,
        **kwds,
    ) -> None: ...
    @classmethod
    def duplicate(cls, copyit) -> Self: ...
    def copy(self, copyit) -> None: ...
    def __eq__(self, other): ...
    def __getattr__(self, name: str):
        """
        Make params accessible via self.foo_param or self.foo_paramlist.

        Underscores, legal in python variable names, are converted to dashes,
        which are legal in IANA tokens.
        """
        ...
    def __setattr__(self, name: str, value) -> None:
        """
        Make params accessible via self.foo_param or self.foo_paramlist.

        Underscores, legal in python variable names, are converted to dashes,
        which are legal in IANA tokens.
        """
        ...
    def __delattr__(self, name: str) -> None: ...
    def valueRepr(self) -> str: ...
    def __unicode__(self) -> str: ...
    def prettyPrint(self, level: int = 0, tabwidth: int = 3) -> None: ...

class Component(VBase):
    """
    A complex property that can contain multiple ContentLines.

    For our purposes, a component must start with a BEGIN:xxxx line and end with
    END:xxxx, or have a PROFILE:xxx line if a top-level component.

    @ivar contents:
        A dictionary of lists of Component or ContentLine instances. The keys
        are the lowercased names of child ContentLines or Components.
        Note that BEGIN and END ContentLines are not included in contents.
    @ivar name:
        Uppercase string used to represent this Component, i.e VCARD if the
        serialized object starts with BEGIN:VCARD.
    @ivar useBegin:
        A boolean flag determining whether BEGIN: and END: lines should
        be serialized.
    """
    contents: dict[str, list[VBase]]
    name: str
    useBegin: bool
    def __init__(self, name: str | None = None, *args, **kwds) -> None: ...
    @classmethod
    def duplicate(cls, copyit) -> Self: ...
    def copy(self, copyit) -> None: ...
    def setProfile(self, name: str) -> None: ...
    def __getattr__(self, name: str): ...
    normal_attributes: list[str]
    def __setattr__(self, name: str, value) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def getChildValue(self, childName: str, default=None, childNumber: int = 0): ...
    @overload
    def add(self, objOrName: _V, group: str | None = None) -> _V:
        """
        Add objOrName to contents, set behavior if it can be inferred.

        If objOrName is a string, create an empty component or line based on
        behavior. If no behavior is found for the object, add a ContentLine.

        group is an optional prefix to the name of the object (see RFC 2425).
        """
        ...
    @overload
    def add(self, objOrName: Literal["vevent"], group: str | None = None) -> Component:
        """
        Add objOrName to contents, set behavior if it can be inferred.

        If objOrName is a string, create an empty component or line based on
        behavior. If no behavior is found for the object, add a ContentLine.

        group is an optional prefix to the name of the object (see RFC 2425).
        """
        ...
    @overload
    def add(
        self, objOrName: Literal["uid", "summary", "description", "dtstart", "dtend"], group: str | None = None
    ) -> ContentLine:
        """
        Add objOrName to contents, set behavior if it can be inferred.

        If objOrName is a string, create an empty component or line based on
        behavior. If no behavior is found for the object, add a ContentLine.

        group is an optional prefix to the name of the object (see RFC 2425).
        """
        ...
    @overload
    def add(self, objOrName: str, group: str | None = None) -> Any: ...  # returns VBase sub-class
    def remove(self, obj) -> None: ...
    def getChildren(self) -> list[Incomplete]: ...
    def components(self) -> Generator[Component]: ...
    def lines(self) -> Generator[ContentLine]: ...
    def sortChildKeys(self) -> list[Incomplete]: ...
    def getSortedChildren(self) -> list[Incomplete]: ...
    def setBehaviorFromVersionLine(self, versionLine) -> None: ...
    def transformChildrenToNative(self) -> None: ...
    def transformChildrenFromNative(self, clearBehavior: bool = True) -> None: ...
    def prettyPrint(self, level: int = 0, tabwidth: int = 3) -> None: ...

class VObjectError(Exception):
    msg: str
    lineNumber: int
    def __init__(self, msg: str, lineNumber: int | None = None) -> None: ...

class ParseError(VObjectError): ...
class ValidateError(VObjectError): ...
class NativeError(VObjectError): ...

patterns: dict[str, str]
param_values_re: re.Pattern[str]
params_re: re.Pattern[str]
line_re: re.Pattern[str]
begin_re: re.Pattern[str]

def parseParams(string: str) -> list[list[Any]]: ...  # Any was taken from re module stubs
def parseLine(
    line: str, lineNumber: int | None = None
) -> tuple[str, list[list[Any]], str | MaybeNone, str | MaybeNone]: ...  # Any is result of parseParams()

wrap_re: re.Pattern[str]
logical_lines_re: re.Pattern[str]
testLines: str

def getLogicalLines(fp, allowQP: bool = True) -> Generator[tuple[str, int]]: ...
def textLineToContentLine(text, n: int | None = None) -> ContentLine: ...
def dquoteEscape(param: str) -> str: ...
def foldOneLine(outbuf: SupportsWrite[AnyStr], input: AnyStr, lineLength: int = 75) -> None: ...
def defaultSerialize(obj: Component | ContentLine, buf, lineLength: int): ...

class Stack:
    stack: list[Incomplete]
    def __len__(self) -> int: ...
    def top(self): ...
    def topName(self): ...
    def modifyTop(self, item) -> None: ...
    def push(self, obj) -> None: ...
    def pop(self): ...

def readComponents(
    streamOrString, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False
) -> Iterator[Component]: ...
def readOne(stream, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False): ...
def registerBehavior(behavior, name: str | None = None, default: bool = False, id=None) -> None: ...
def getBehavior(name: str, id=None): ...
def newFromBehavior(name: str, id=None) -> Component | ContentLine: ...
def backslashEscape(s: str) -> str: ...
