"""Definitions and behavior for vCard 3.0"""

from _typeshed import Incomplete

from .behavior import Behavior

class Name:
    family: Incomplete
    given: Incomplete
    additional: Incomplete
    prefix: Incomplete
    suffix: Incomplete
    def __init__(
        self,
        family: str | list[str] = "",
        given: str | list[str] = "",
        additional: str | list[str] = "",
        prefix: str | list[str] = "",
        suffix: str | list[str] = "",
    ) -> None:
        """Each name attribute can be a string or a list of strings."""
        ...
    @staticmethod
    def toString(val):
        """Turn a string or array value into a string."""
        ...
    def __eq__(self, other): ...

class Address:
    box: Incomplete
    extended: Incomplete
    street: Incomplete
    city: Incomplete
    region: Incomplete
    code: Incomplete
    country: Incomplete
    def __init__(
        self,
        street: str | list[str] = "",
        city: str | list[str] = "",
        region: str | list[str] = "",
        code: str | list[str] = "",
        country: str | list[str] = "",
        box: str | list[str] = "",
        extended: str | list[str] = "",
    ) -> None:
        """Each name attribute can be a string or a list of strings."""
        ...
    @staticmethod
    def toString(val, join_char: str = "\n"):
        """Turn a string or array value into a string."""
        ...
    lines: Incomplete
    one_line: Incomplete
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
    defaultBehavior: Incomplete

class VCard3_0(VCardBehavior):
    """vCard 3.0 behavior."""
    name: str
    description: str
    versionString: str
    isComponent: bool
    sortFirst: Incomplete
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

class GEO(VCardBehavior): ...

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
def serializeFields(obj, order=None):
    """
    Turn an object's fields into a ';' and ',' seperated string.

    If order is None, obj should be a list, backslash escape each field and
    return a ';' separated string.
    """
    ...

NAME_ORDER: Incomplete
ADDRESS_ORDER: Incomplete

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
