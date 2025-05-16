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
    ) -> str: ...
    @overload
    def serialize(self, buf: _W, lineLength: int = 75, validate: bool = True, behavior=None, *args: Any, **kwargs: Any) -> _W: ...

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
    """
    Holds one content line for formats like vCard and vCalendar.

    For example::
      <SUMMARY{u'param1' : [u'val1'], u'param2' : [u'val2']}Bastille Day Party>

    @ivar name:
        The uppercased name of the contentline.
    @ivar params:
        A dictionary of parameters and associated lists of values (the list may
        be empty for empty parameters).
    @ivar value:
        The value of the contentline.
    @ivar singletonparams:
        A list of parameters for which it's unclear if the string represents the
        parameter name or the parameter value. In vCard 2.1, "The value string
        can be specified alone in those cases where the value is unambiguous".
        This is crazy, but we have to deal with it.
    @ivar encoded:
        A boolean describing whether the data in the content line is encoded.
        Generally, text read from a serialized vCard or vCalendar should be
        considered encoded.  Data added programmatically should not be encoded.
    @ivar lineNumber:
        An optional line number associated with the contentline.
    """
    name: Incomplete
    encoded: Incomplete
    params: Incomplete
    singletonparams: Incomplete
    isNative: Incomplete
    lineNumber: Incomplete
    value: Incomplete
    def __init__(
        self, name, params, value, group=None, encoded: bool = False, isNative: bool = False, lineNumber=None, *args, **kwds
    ) -> None: ...
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
    def __init__(self, name=None, *args, **kwds) -> None: ...
    @classmethod
    def duplicate(cls, copyit): ...
    def copy(self, copyit) -> None: ...
    def setProfile(self, name) -> None:
        """
        Assign a PROFILE to this unnamed component.

        Used by vCard, not by vCalendar.
        """
        ...
    def __getattr__(self, name: str):
        """
        For convenience, make self.contents directly accessible.

        Underscores, legal in python variable names, are converted to dashes,
        which are legal in IANA tokens.
        """
        ...
    normal_attributes: Incomplete
    def __setattr__(self, name: str, value) -> None:
        """
        For convenience, make self.contents directly accessible.

        Underscores, legal in python variable names, are converted to dashes,
        which are legal in IANA tokens.
        """
        ...
    def __delattr__(self, name: str) -> None: ...
    def getChildValue(self, childName, default=None, childNumber: int = 0): ...
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
    def add(self, objOrName: str, group: str | None = None) -> Any:
        """
        Add objOrName to contents, set behavior if it can be inferred.

        If objOrName is a string, create an empty component or line based on
        behavior. If no behavior is found for the object, add a ContentLine.

        group is an optional prefix to the name of the object (see RFC 2425).
        """
        ...
    def remove(self, obj) -> None:
        """Remove obj from contents."""
        ...
    def getChildren(self) -> list[Incomplete]:
        """Return an iterable of all children."""
        ...
    def components(self) -> Iterable[Component]:
        """Return an iterable of all Component children."""
        ...
    def lines(self):
        """Return an iterable of all ContentLine children."""
        ...
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
    def __init__(self, msg, lineNumber=None) -> None: ...

class ParseError(VObjectError): ...
class ValidateError(VObjectError): ...
class NativeError(VObjectError): ...

patterns: Incomplete
param_values_re: Incomplete
params_re: Incomplete
line_re: Incomplete
begin_re: Incomplete

def parseParams(string): ...
def parseLine(line, lineNumber=None): ...

wrap_re: Incomplete
logical_lines_re: Incomplete
testLines: str

def getLogicalLines(fp, allowQP: bool = True) -> None: ...
def textLineToContentLine(text, n=None): ...
def dquoteEscape(param): ...
def foldOneLine(outbuf, input, lineLength: int = 75) -> None: ...
def defaultSerialize(obj, buf, lineLength): ...

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
) -> Iterator[Component]: ...
def readOne(stream, validate: bool = False, transform: bool = True, ignoreUnreadable: bool = False, allowQP: bool = False): ...
def registerBehavior(behavior, name=None, default: bool = False, id=None) -> None: ...
def getBehavior(name, id=None): ...
def newFromBehavior(name, id=None): ...
def backslashEscape(s): ...
