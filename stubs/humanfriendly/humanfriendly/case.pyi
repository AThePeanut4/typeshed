"""
Simple case insensitive dictionaries.

The :class:`CaseInsensitiveDict` class is a dictionary whose string keys
are case insensitive. It works by automatically coercing string keys to
:class:`CaseInsensitiveKey` objects. Keys that are not strings are
supported as well, just without case insensitivity.

At its core this module works by normalizing strings to lowercase before
comparing or hashing them. It doesn't support proper case folding nor
does it support Unicode normalization, hence the word "simple".
"""

from _typeshed import Incomplete
from collections import OrderedDict
from typing import TypeVar

from humanfriendly.compat import unicode

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class CaseInsensitiveDict(OrderedDict[_KT, _VT]):
    """
    Simple case insensitive dictionary implementation (that remembers insertion order).

    This class works by overriding methods that deal with dictionary keys to
    coerce string keys to :class:`CaseInsensitiveKey` objects before calling
    down to the regular dictionary handling methods. While intended to be
    complete this class has not been extensively tested yet.
    """
    def __init__(self, other: Incomplete | None = None, **kw) -> None:
        """Initialize a :class:`CaseInsensitiveDict` object."""
        ...
    def coerce_key(self, key):
        """
        Coerce string keys to :class:`CaseInsensitiveKey` objects.

        :param key: The value to coerce (any type).
        :returns: If `key` is a string then a :class:`CaseInsensitiveKey`
                  object is returned, otherwise the value of `key` is
                  returned unmodified.
        """
        ...
    @classmethod
    def fromkeys(cls, iterable, value: Incomplete | None = None):
        """Create a case insensitive dictionary with keys from `iterable` and values set to `value`."""
        ...
    def get(self, key, default: Incomplete | None = None):
        """Get the value of an existing item."""
        ...
    def pop(self, key, default: Incomplete | None = None):
        """Remove an item from a case insensitive dictionary."""
        ...
    def setdefault(self, key, default: Incomplete | None = None):
        """Get the value of an existing item or add a new item."""
        ...
    def update(self, other: Incomplete | None = None, **kw) -> None:
        """Update a case insensitive dictionary with new items."""
        ...
    def __contains__(self, key):
        """Check if a case insensitive dictionary contains the given key."""
        ...
    def __delitem__(self, key) -> None:
        """Delete an item in a case insensitive dictionary."""
        ...
    def __getitem__(self, key):
        """Get the value of an item in a case insensitive dictionary."""
        ...
    def __setitem__(self, key, value) -> None:
        """Set the value of an item in a case insensitive dictionary."""
        ...

class CaseInsensitiveKey(unicode):
    """
    Simple case insensitive dictionary key implementation.

    The :class:`CaseInsensitiveKey` class provides an intentionally simple
    implementation of case insensitive strings to be used as dictionary keys.

    If you need features like Unicode normalization or proper case folding
    please consider using a more advanced implementation like the :pypi:`istr`
    package instead.
    """
    def __new__(cls, value):
        """Create a :class:`CaseInsensitiveKey` object."""
        ...
    def __hash__(self) -> int:
        """Get the hash value of the lowercased string."""
        ...
    def __eq__(self, other):
        """Compare two strings as lowercase."""
        ...
