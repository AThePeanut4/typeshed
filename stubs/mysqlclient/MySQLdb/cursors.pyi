"""
MySQLdb Cursors

This module implements Cursors of various types for MySQLdb. By
default, MySQLdb uses the Cursor class.
"""

from _typeshed import Incomplete
from collections.abc import Iterable
from re import Pattern
from typing_extensions import LiteralString, TypeAlias

from .connections import _Literal

_Arguments: TypeAlias = dict[str, _Literal] | dict[bytes, _Literal] | Iterable[_Literal]

RE_INSERT_VALUES: Pattern[str]

class BaseCursor:
    """
    A base for Cursor classes. Useful attributes:

    description
        A tuple of DB API 7-tuples describing the columns in
        the last executed query; see PEP-249 for details.

    description_flags
        Tuple of column flags for last query, one entry per column
        in the result set. Values correspond to those in
        MySQLdb.constants.FLAG. See MySQL documentation (C API)
        for more information. Non-standard extension.

    arraysize
        default number of rows fetchmany() will fetch
    """
    from ._exceptions import (
        DatabaseError as DatabaseError,
        DataError as DataError,
        Error as Error,
        IntegrityError as IntegrityError,
        InterfaceError as InterfaceError,
        InternalError as InternalError,
        MySQLError as MySQLError,
        NotSupportedError as NotSupportedError,
        OperationalError as OperationalError,
        ProgrammingError as ProgrammingError,
        Warning as Warning,
    )

    max_stmt_length: Incomplete
    connection: Incomplete
    description: Incomplete
    description_flags: Incomplete
    rowcount: int
    arraysize: int
    lastrowid: Incomplete
    rownumber: Incomplete
    def __init__(self, connection) -> None: ...
    def close(self) -> None:
        """Close the cursor. No further queries will be possible."""
        ...
    def __enter__(self): ...
    def __exit__(self, *exc_info: object) -> None: ...
    def nextset(self): ...
    def setinputsizes(self, *args) -> None: ...
    def setoutputsizes(self, *args) -> None: ...
    def execute(self, query, args=None): ...
    def mogrify(self, query: str | bytes, args: _Arguments | None = None) -> str: ...
    def executemany(self, query: LiteralString, args: Iterable[_Arguments]) -> int | None: ...
    def callproc(self, procname, args=()): ...
    def __iter__(self): ...

class CursorStoreResultMixIn:
    """
    This is a MixIn class which causes the entire result set to be
    stored on the client side, i.e. it uses mysql_store_result(). If the
    result set can be very large, consider adding a LIMIT clause to your
    query, or using CursorUseResultMixIn instead.
    """
    rownumber: Incomplete
    def fetchone(self): ...
    def fetchmany(self, size=None): ...
    def fetchall(self): ...
    def scroll(self, value, mode: str = "relative") -> None: ...
    def __iter__(self): ...

class CursorUseResultMixIn:
    """
    This is a MixIn class which causes the result set to be stored
    in the server and sent row-by-row to client side, i.e. it uses
    mysql_use_result(). You MUST retrieve the entire result set and
    close() the cursor before additional queries can be performed on
    the connection.
    """
    rownumber: Incomplete
    def fetchone(self): ...
    def fetchmany(self, size=None): ...
    def fetchall(self): ...
    def __iter__(self): ...
    def next(self): ...
    __next__ = next

class CursorTupleRowsMixIn:
    """
    This is a MixIn class that causes all rows to be returned as tuples,
    which is the standard form required by DB API.
    """
    ...
class CursorDictRowsMixIn:
    """
    This is a MixIn class that causes all rows to be returned as
    dictionaries. This is a non-standard feature.
    """
    ...
class Cursor(CursorStoreResultMixIn, CursorTupleRowsMixIn, BaseCursor):
    """
    This is the standard Cursor class that returns rows as tuples
    and stores the result set in the client.
    """
    ...
class DictCursor(CursorStoreResultMixIn, CursorDictRowsMixIn, BaseCursor):
    """
    This is a Cursor class that returns rows as dictionaries and
    stores the result set in the client.
    """
    ...
class SSCursor(CursorUseResultMixIn, CursorTupleRowsMixIn, BaseCursor):
    """
    This is a Cursor class that returns rows as tuples and stores
    the result set in the server.
    """
    ...
class SSDictCursor(CursorUseResultMixIn, CursorDictRowsMixIn, BaseCursor):
    """
    This is a Cursor class that returns rows as dictionaries and
    stores the result set in the server.
    """
    ...
