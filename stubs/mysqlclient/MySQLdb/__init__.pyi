"""
MySQLdb - A DB API v2.0 compatible interface to MySQL.

This package is a wrapper around _mysql, which mostly implements the
MySQL C API.

connect() -- connects to server

See the C API specification and the MySQL documentation for more info
on other items.

For information on how MySQLdb handles type conversion, see the
MySQLdb.converters module.
"""

from _typeshed import Incomplete

from MySQLdb import connections as connections, constants as constants, converters as converters, cursors as cursors
from MySQLdb._mysql import (
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
    debug as debug,
    get_client_info as get_client_info,
    string_literal as string_literal,
)
from MySQLdb.connections import Connection as Connection
from MySQLdb.constants import FIELD_TYPE as FIELD_TYPE
from MySQLdb.release import version_info as version_info
from MySQLdb.times import (
    Date as Date,
    DateFromTicks as DateFromTicks,
    Time as Time,
    TimeFromTicks as TimeFromTicks,
    Timestamp as Timestamp,
    TimestampFromTicks as TimestampFromTicks,
)

threadsafety: int
apilevel: str
paramstyle: str

class DBAPISet(frozenset[Incomplete]):
    """
    A special type of set for which A == x is true if A is a
    DBAPISet and x is a member of that set.
    """
    def __eq__(self, other): ...

STRING: Incomplete
BINARY: Incomplete
NUMBER: Incomplete
DATE: Incomplete
TIME: Incomplete
TIMESTAMP: Incomplete
DATETIME: Incomplete
ROWID: Incomplete

def Binary(x): ...
def Connect(*args, **kwargs) -> Connection:
    """Factory function for connections.Connection."""
    ...

connect = Connect
