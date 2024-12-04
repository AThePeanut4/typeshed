"""Definitions and behavior for vCard 3.0"""

from _typeshed import Incomplete
from typing import Any

from .behavior import Behavior

class Name:
    family: Any
    given: Any
    additional: Any
    prefix: Any
    suffix: Any
    def __init__(self, family: str = "", given: str = "", additional: str = "", prefix: str = "", suffix: str = "") -> None:
        """Each name attribute can be a string or a list of strings."""
        ...
    @staticmethod
    def toString(val):
        """Turn a string or array value into a string."""
        ...
    def __eq__(self, other): ...

class Address:
    box: Any
    extended: Any
    street: Any
    city: Any
    region: Any
    code: Any
    country: Any
    def __init__(
        self,
        street: str = "",
        city: str = "",
        region: str = "",
        code: str = "",
        country: str = "",
        box: str = "",
        extended: str = "",
    ) -> None:
        """Each name attribute can be a string or a list of strings."""
        ...
    @staticmethod
    def toString(val, join_char: str = "\n"):
        """Turn a string or array value into a string."""
        ...
    lines: Any
    one_line: Any
    def __eq__(self, other): ...

class VCardTextBehavior(Behavior):
    """
    Provide backslash escape encoding/decoding for single valued properties.

    TextBehavior also deals with base64 encoding if the ENCODING parameter is
    explicitly set to BASE64.
    """
    allowGroup: bool
    base64string: str
    @classmethod
    def decode(cls, line) -> None:
        """
        Remove backslash escaping from line.valueDecode line, either to remove
        backslash espacing, or to decode base64 encoding. The content line should
        contain a ENCODING=b for base64 encoding, but Apple Addressbook seems to
        export a singleton parameter of 'BASE64', which does not match the 3.0
        vCard spec. If we encouter that, then we transform the parameter to
        ENCODING=b
        """
        ...
    @classmethod
    def encode(cls, line) -> None:
        """Backslash escape line.value."""
        ...

class VCardBehavior(Behavior):
    allowGroup: bool
    defaultBehavior: Any

class VCard3_0(VCardBehavior):
    """vCard 3.0 behavior."""
    name: str
    description: str
    versionString: str
    isComponent: bool
    sortFirst: Any
    knownChildren: Any
    @classmethod
    def generateImplicitParameters(cls, obj) -> None:
        """
        Create PRODID, VERSION, and VTIMEZONEs if needed.

        VTIMEZONEs will need to exist whenever TZID parameters exist or when
        datetimes with tzinfo exist.
        """
        ...

class FN(VCardTextBehavior):
    name: str
    description: str

class Label(VCardTextBehavior):
    name: str
    description: str

wacky_apple_photo_serialize: bool
REALLY_LARGE: float

class Photo(VCardTextBehavior):
    name: str
    description: str
    @classmethod
    def valueRepr(cls, line): ...
    @classmethod
    def serialize(cls, obj, buf, lineLength, validate, *args, **kwargs) -> None:
        """
        Apple's Address Book is *really* weird with images, it expects
        base64 data to have very specific whitespace.  It seems Address Book
        can handle PHOTO if it's not wrapped, so don't wrap it.
        """
        ...

def toListOrString(string): ...
def splitFields(string):
    """Return a list of strings or lists from a Name or Address."""
    ...
def toList(stringOrList): ...
def serializeFields(obj, order: Incomplete | None = None):
    """
    Turn an object's fields into a ';' and ',' seperated string.

    If order is None, obj should be a list, backslash escape each field and
    return a ';' separated string.
    """
    ...

NAME_ORDER: Any
ADDRESS_ORDER: Any

class NameBehavior(VCardBehavior):
    """A structured name."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Turn obj.value into a Name."""
        ...
    @staticmethod
    def transformFromNative(obj):
        """Replace the Name in obj.value with a string."""
        ...

class AddressBehavior(VCardBehavior):
    """A structured address."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Turn obj.value into an Address."""
        ...
    @staticmethod
    def transformFromNative(obj):
        """Replace the Address in obj.value with a string."""
        ...

class OrgBehavior(VCardBehavior):
    """A list of organization values and sub-organization values."""
    hasNative: bool
    @staticmethod
    def transformToNative(obj):
        """Turn obj.value into a list."""
        ...
    @staticmethod
    def transformFromNative(obj):
        """Replace the list in obj.value with a string."""
        ...
