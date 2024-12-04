"""
MySQLdb type conversion module

This module handles all the type conversions for MySQL. If the default
type conversions aren't what you need, you can make your own. The
dictionary conversions maps some kind of type to a conversion function
which returns the corresponding value:

Key: FIELD_TYPE.* (from MySQLdb.constants)

Conversion function:

    Arguments: string

    Returns: Python object

Key: Python type object (from types) or class

Conversion function:

    Arguments: Python object of indicated type or class AND
               conversion dictionary

    Returns: SQL literal value

    Notes: Most conversion functions can ignore the dictionary, but
           it is a required parameter. It is necessary for converting
           things like sequences and instances.

Don't modify conversions if you can avoid it. Instead, make copies
(with the copy() method), modify the copies, and then pass them to
MySQL.connect().
"""

import array
from _typeshed import Incomplete

from MySQLdb._exceptions import ProgrammingError as ProgrammingError
from MySQLdb._mysql import string_literal as string_literal
from MySQLdb.constants import FIELD_TYPE as FIELD_TYPE, FLAG as FLAG
from MySQLdb.times import (
    Date as Date,
    Date_or_None as Date_or_None,
    DateTime2literal as DateTime2literal,
    DateTime_or_None as DateTime_or_None,
    DateTimeDelta2literal as DateTimeDelta2literal,
    DateTimeDeltaType as DateTimeDeltaType,
    DateTimeType as DateTimeType,
    TimeDelta_or_None as TimeDelta_or_None,
)

NoneType: Incomplete
ArrayType = array.array

def Bool2Str(s, d): ...
def Set2Str(s, d): ...
def Thing2Str(s, d):
    """Convert something into a string via str()."""
    ...
def Float2Str(o, d): ...
def None2NULL(o, d):
    """Convert None to NULL."""
    ...
def Thing2Literal(o, d):
    """
    Convert something into a SQL string literal.  If using
    MySQL-3.23 or newer, string_literal() is a method of the
    _mysql.MYSQL object, and this function will be overridden with
    that method when the connection is created.
    """
    ...
def Decimal2Literal(o, d): ...
def array2Str(o, d): ...

conversions: Incomplete
