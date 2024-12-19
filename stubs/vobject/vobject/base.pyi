"""vobject module for reading vCard and vCalendar files."""

import logging
from _typeshed import Incomplete, SupportsWrite
from collections.abc import Iterable, Iterator
from typing import Any, Final, Literal, TypeVar, overload

_V = TypeVar("_V", bound=VBase)
_W = TypeVar("_W", bound=SupportsWrite[bytes])

logger: logging.Logger
DEBUG: bool
CR: str
LF: str
CRLF: str
SPACE: str
TAB: str
SPACEORTAB: str

VERSION: Final[str]

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
    def __init__(self, group: Incomplete | None = None) -> None: ...
    def copy(self, copyit: VBase) -> None: ...
    def validate(self, *args, **kwds) -> bool: ...
    def getChildren(self) -> list[Incomplete]: ...
    def clearBehavior(self, cascade: bool = True) -> None: ...
    def autoBehavior(self, cascade: bool = False) -> None: ...
    def setBehavior(self, behavior, cascade: bool = True) -> None: ...
    def transformToNative(self): ...
    def transformFromNative(self): ...
    def transformChildrenToNative(self) -> None: ...
    def transformChildrenFromNative(self, clearBehavior: bool = True) -> None: ...
    # Use Any because args and kwargs are passed to the behavior object
    @overload
    def serialize(
        self,
        buf: None = None,
        lineLength: int = 75,
        validate: bool = True,
        behavior: Incomplete | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        """
        Serialize to buf if it exists, otherwise return a string.

        Use self.behavior.serialize if behavior exists.
        """
        ...
    @overload
    def serialize(
        self, buf: _W, lineLength: int = 75, validate: bool = True, behavior: Incomplete | None = None, *args: Any, **kwargs: Any
    ) -> _W:
        """
        Serialize to buf if it exists, otherwise return a string.

        Use self.behavior.serialize if behavior exists.
        """
        ...

def toVName(name, stripNum: int = 0, upper: bool = False):
    """
    Turn a Python name into an iCalendar style name,
    optionally uppercase and with characters stripped off.
    """
    ...

class ContentLine(VBase):
    name: Incomplete
    encoded: Incomplete
    params: Incomplete
    singletonparams: Incomplete
    isNative: Incomplete
    lineNumber: Incomplete
    value: Incomplete
    def __init__(
        self,
        name,
        params,
        value,
        group: Incomplete | None = None,
        encoded: bool = False,
        isNative: bool = False,
        lineNumber: Incomplete | None = None,
        *args,
        **kwds,
    ) -> None:
        """
        Take output from parseLine, convert params list to dictionary.

        Group is used as a positional argument to match parseLine's return
        """
        ...
    @classmethod
    def duplicate(cls, copyit): ...
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
    def valueRepr(self):
        """
        Transform the representation of the value
        according to the behavior, if any.
        """
        ...
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
    name: Incomplete
    useBegin: bool
    def __init__(self, name: Incomplete | None = None, *args, **kwds) -> None: ...
    @classmethod
    def duplicate(cls, copyit): ...
    def copy(self, copyit) -> None: ...
    def setProfile(self, name) -> None: ...
    def __getattr__(self, name: str): ...
    normal_attributes: Incomplete
    def __setattr__(self, name: str, value) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def getChildValue(self, childName, default: Incomplete | None = None, childNumber: int = 0):
        """Return a child's value (the first, by default), or None."""
        ...
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
    def components(self) -> Iterable[Component]: ...
    def lines(self): ...
    def sortChildKeys(self): ...
    def getSortedChildren(self): ...
    def setBehaviorFromVersionLine(self, versionLine) -> None:
        """Set behavior if one matches name, versionLine.value."""
        ...
    def transformChildrenToNative(self) -> None:
        """
        Recursively replace children with their native representation.

        Sort to get dependency order right, like vtimezone before vevent.
        """
        ...
    def transformChildrenFromNative(self, clearBehavior: bool = True) -> None:
        """Recursively transform native children to vanilla representations."""
        ...
    def prettyPrint(self, level: int = 0, tabwidth: int = 3) -> None: ...

class VObjectError(Exception):
    msg: Incomplete
    lineNumber: Incomplete
    def __init__(self, msg, lineNumber: Incomplete | None = None) -> None: ...

class ParseError(VObjectError): ...
class ValidateError(VObjectError): ...
class NativeError(VObjectError): ...

patterns: Incomplete
param_values_re: Incomplete
params_re: Incomplete
line_re: Incomplete
begin_re: Incomplete

def parseParams(string):
    """Parse parameters"""
    ...
def parseLine(line, lineNumber: Incomplete | None = None):
    """Parse line"""
    ...

wrap_re: Incomplete
logical_lines_re: Incomplete
testLines: str

def getLogicalLines(fp, allowQP: bool = True) -> None:
    """
    Iterate through a stream, yielding one logical line at a time.

    Because many applications still use vCard 2.1, we have to deal with the
    quoted-printable encoding for long lines, as well as the vCard 3.0 and
    vCalendar line folding technique, a whitespace character at the start
    of the line.

    Quoted-printable data will be decoded in the Behavior decoding phase.

    # We're leaving this test in for awhile, because the unittest was ugly and dumb.
    >>> from six import StringIO
    >>> f=StringIO(testLines)
    >>> for n, l in enumerate(getLogicalLines(f)):
    ...     print("Line %s: %s" % (n, l[0]))
    ...
    Line 0: Line 0 text, Line 0 continued.
    Line 1: Line 1;encoding=quoted-printable:this is an evil=
     evil=
     format.
    Line 2: Line 2 is a new line, it does not start with whitespace.
    """
    ...
def textLineToContentLine(text, n: Incomplete | None = None): ...
def dquoteEscape(param):
    """Return param, or "param" if ',' or ';' or ':' is in param."""
    ...
def foldOneLine(outbuf, input, lineLength: int = 75) -> None:
    """
    Folding line procedure that ensures multi-byte utf-8 sequences are not
    broken across lines

    TO-DO: This all seems odd. Is it still needed, especially in python3?
    """
    ...
def defaultSerialize(obj, buf, lineLength):
    """Encode and fold obj and its children, write to buf or return a string."""
    ...

class Stack:
    stack: Incomplete
    def __len__(self) -> int: ...
    def top(self): ...
    def topName(self): ...
    def modifyTop(self, item) -> None: ...
    def push(self, obj) -> None: ...
    def pop(self): ...

def readComponents(
    streamOrString, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False
) -> Iterator[Component]:
    """Generate one Component at a time from a stream."""
    ...
def readOne(stream, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False):
    """Return the first component from stream."""
    ...
def registerBehavior(behavior, name: Incomplete | None = None, default: bool = False, id: Incomplete | None = None) -> None:
    """
    Register the given behavior.

    If default is True (or if this is the first version registered with this
    name), the version will be the default if no id is given.
    """
    ...
def getBehavior(name, id: Incomplete | None = None):
    """
    Return a matching behavior if it exists, or None.

    If id is None, return the default for name.
    """
    ...
def newFromBehavior(name, id: Incomplete | None = None):
    """Given a name, return a behaviored ContentLine or Component."""
    ...
def backslashEscape(s): ...
