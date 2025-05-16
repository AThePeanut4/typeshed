from collections import OrderedDict
from collections.abc import Callable
from typing import Any, NamedTuple, TypeVar, overload

from psycopg2._ipaddress import register_ipaddress as register_ipaddress
from psycopg2._json import (
    Json as Json,
    register_default_json as register_default_json,
    register_default_jsonb as register_default_jsonb,
    register_json as register_json,
)
from psycopg2._psycopg import (
    REPLICATION_LOGICAL as REPLICATION_LOGICAL,
    REPLICATION_PHYSICAL as REPLICATION_PHYSICAL,
    ReplicationConnection as _replicationConnection,
    ReplicationCursor as _replicationCursor,
    ReplicationMessage as ReplicationMessage,
    connection as _connection,
    cursor as _cursor,
    quote_ident as quote_ident,
)
from psycopg2._range import (
    DateRange as DateRange,
    DateTimeRange as DateTimeRange,
    DateTimeTZRange as DateTimeTZRange,
    NumericRange as NumericRange,
    Range as Range,
    RangeAdapter as RangeAdapter,
    RangeCaster as RangeCaster,
    register_range as register_range,
)

_T_cur = TypeVar("_T_cur", bound=_cursor)

class DictCursorBase(_cursor):
    """Base class for all dict-like cursors."""
    def __init__(self, *args, **kwargs) -> None: ...

class DictConnection(_connection):
    """A connection that uses `DictCursor` automatically."""
    @overload
    def cursor(
        self, name: str | bytes | None = None, cursor_factory: None = None, withhold: bool = False, scrollable: bool | None = None
    ) -> DictCursor: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None = None,
        *,
        cursor_factory: Callable[[_connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None,
        cursor_factory: Callable[[_connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...

class DictCursor(DictCursorBase):
    """
    A cursor that keeps a list of column name -> index mappings__.

    .. __: https://docs.python.org/glossary.html#term-mapping
    """
    def __init__(self, *args, **kwargs) -> None: ...
    index: Any
    def execute(self, query, vars=None): ...
    def callproc(self, procname, vars=None): ...
    def fetchone(self) -> DictRow | None: ...  # type: ignore[override]
    def fetchmany(self, size: int | None = None) -> list[DictRow]: ...  # type: ignore[override]
    def fetchall(self) -> list[DictRow]: ...  # type: ignore[override]
    def __next__(self) -> DictRow:
        """Implement next(self)."""
        ...

class DictRow(list[Any]):
    """A row object that allow by-column-name access to data."""
    def __init__(self, cursor) -> None: ...
    def __getitem__(self, x): ...
    def __setitem__(self, x, v) -> None: ...
    def items(self): ...
    def keys(self): ...
    def values(self): ...
    def get(self, x, default=None): ...
    def copy(self): ...
    def __contains__(self, x): ...
    def __reduce__(self): ...

class RealDictConnection(_connection):
    """A connection that uses `RealDictCursor` automatically."""
    @overload
    def cursor(
        self, name: str | bytes | None = None, cursor_factory: None = None, withhold: bool = False, scrollable: bool | None = None
    ) -> RealDictCursor: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None = None,
        *,
        cursor_factory: Callable[[_connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None,
        cursor_factory: Callable[[_connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...

class RealDictCursor(DictCursorBase):
    """
    A cursor that uses a real dict as the base type for rows.

    Note that this cursor is extremely specialized and does not allow
    the normal access (using integer indices) to fetched data. If you need
    to access database rows both as a dictionary and a list, then use
    the generic `DictCursor` instead of `!RealDictCursor`.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    column_mapping: Any
    def execute(self, query, vars=None): ...
    def callproc(self, procname, vars=None): ...
    def fetchone(self) -> RealDictRow | None: ...  # type: ignore[override]
    def fetchmany(self, size: int | None = None) -> list[RealDictRow]: ...  # type: ignore[override]
    def fetchall(self) -> list[RealDictRow]: ...  # type: ignore[override]
    def __next__(self) -> RealDictRow:
        """Implement next(self)."""
        ...

class RealDictRow(OrderedDict[Any, Any]):
    """A `!dict` subclass representing a data record."""
    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...

class NamedTupleConnection(_connection):
    """A connection that uses `NamedTupleCursor` automatically."""
    @overload
    def cursor(
        self, name: str | bytes | None = None, cursor_factory: None = None, withhold: bool = False, scrollable: bool | None = None
    ) -> NamedTupleCursor: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None = None,
        *,
        cursor_factory: Callable[[_connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...
    @overload
    def cursor(
        self,
        name: str | bytes | None,
        cursor_factory: Callable[[_connection, str | bytes | None], _T_cur],
        withhold: bool = False,
        scrollable: bool | None = None,
    ) -> _T_cur: ...

class NamedTupleCursor(_cursor):
    """
    A cursor that generates results as `~collections.namedtuple`.

    `!fetch*()` methods will return named tuples instead of regular tuples, so
    their elements can be accessed both as regular numeric items as well as
    attributes.

        >>> nt_cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        >>> rec = nt_cur.fetchone()
        >>> rec
        Record(id=1, num=100, data="abc'def")
        >>> rec[1]
        100
        >>> rec.data
        "abc'def"
    """
    Record: Any
    MAX_CACHE: int
    def execute(self, query, vars=None): ...
    def executemany(self, query, vars): ...
    def callproc(self, procname, vars=None): ...
    def fetchone(self) -> NamedTuple | None: ...
    def fetchmany(self, size: int | None = None) -> list[NamedTuple]: ...  # type: ignore[override]
    def fetchall(self) -> list[NamedTuple]: ...  # type: ignore[override]
    def __next__(self) -> NamedTuple:
        """Implement next(self)."""
        ...

class LoggingConnection(_connection):
    """
    A connection that logs all queries to a file or logger__ object.

    .. __: https://docs.python.org/library/logging.html
    """
    log: Any
    def initialize(self, logobj) -> None:
        """
        Initialize the connection to log to `!logobj`.

        The `!logobj` parameter can be an open file object or a Logger/LoggerAdapter
        instance from the standard logging module.
        """
        ...
    def filter(self, msg, curs):
        """
        Filter the query before logging it.

        This is the method to overwrite to filter unwanted queries out of the
        log or to add some extra data to the output. The default implementation
        just does nothing.
        """
        ...
    def cursor(self, *args, **kwargs): ...

class LoggingCursor(_cursor):
    def execute(self, query, vars=None): ...
    def callproc(self, procname, vars=None): ...

class MinTimeLoggingConnection(LoggingConnection):
    """
    A connection that logs queries based on execution time.

    This is just an example of how to sub-class `LoggingConnection` to
    provide some extra filtering for the logged queries. Both the
    `initialize()` and `filter()` methods are overwritten to make sure
    that only queries executing for more than ``mintime`` ms are logged.

    Note that this connection uses the specialized cursor
    `MinTimeLoggingCursor`.
    """
    def initialize(self, logobj, mintime: int = 0) -> None: ...
    def filter(self, msg, curs): ...
    def cursor(self, *args, **kwargs): ...

class MinTimeLoggingCursor(LoggingCursor):
    """The cursor sub-class companion to `MinTimeLoggingConnection`."""
    timestamp: Any
    def execute(self, query, vars=None): ...
    def callproc(self, procname, vars=None): ...

class LogicalReplicationConnection(_replicationConnection):
    def __init__(self, *args, **kwargs) -> None: ...

class PhysicalReplicationConnection(_replicationConnection):
    def __init__(self, *args, **kwargs) -> None: ...

class StopReplication(Exception):
    """
    Exception used to break out of the endless loop in
    `~ReplicationCursor.consume_stream()`.

    Subclass of `~exceptions.Exception`.  Intentionally *not* inherited from
    `~psycopg2.Error` as occurrence of this exception does not indicate an
    error.
    """
    ...

class ReplicationCursor(_replicationCursor):
    def create_replication_slot(self, slot_name, slot_type=None, output_plugin=None) -> None: ...
    def drop_replication_slot(self, slot_name) -> None: ...
    def start_replication(
        self,
        slot_name=None,
        slot_type=None,
        start_lsn: int = 0,
        timeline: int = 0,
        options=None,
        decode: bool = False,
        status_interval: int = 10,
    ) -> None:
        """Start replication stream."""
        ...
    def fileno(self): ...
    def consume_stream(
        self, consume: Callable[[ReplicationMessage], object], keepalive_interval: float | None = None
    ) -> None:
        """consume_stream(consumer, keepalive_interval=None) -- Consume replication stream."""
        ...

class UUID_adapter:
    """
    Adapt Python's uuid.UUID__ type to PostgreSQL's uuid__.

    .. __: https://docs.python.org/library/uuid.html
    .. __: https://www.postgresql.org/docs/current/static/datatype-uuid.html
    """
    def __init__(self, uuid) -> None: ...
    def __conform__(self, proto): ...
    def getquoted(self): ...

def register_uuid(oids=None, conn_or_curs=None): ...

class Inet:
    """
    Wrap a string to allow for correct SQL-quoting of inet values.

    Note that this adapter does NOT check the passed value to make
    sure it really is an inet-compatible address but DOES call adapt()
    on it to make sure it is impossible to execute an SQL-injection
    by passing an evil value to the initializer.
    """
    addr: Any
    def __init__(self, addr) -> None: ...
    def prepare(self, conn) -> None: ...
    def getquoted(self): ...
    def __conform__(self, proto): ...

def register_inet(oid=None, conn_or_curs=None): ...
def wait_select(conn) -> None: ...

class HstoreAdapter:
    """Adapt a Python dict to the hstore syntax."""
    wrapped: Any
    def __init__(self, wrapped) -> None: ...
    conn: Any
    getquoted: Any
    def prepare(self, conn) -> None: ...
    @classmethod
    def parse(cls, s, cur, _bsdec=...):
        """
        Parse an hstore representation in a Python string.

        The hstore is represented as something like::

            "a"=>"1", "b"=>"2"

        with backslash-escaped strings.
        """
        ...
    @classmethod
    def parse_unicode(cls, s, cur):
        """Parse an hstore returning unicode keys and values."""
        ...
    @classmethod
    def get_oids(cls, conn_or_curs):
        """
        Return the lists of OID of the hstore and hstore[] types.
        
        """
        ...

def register_hstore(conn_or_curs, globally: bool = False, unicode: bool = False, oid=None, array_oid=None) -> None: ...

class CompositeCaster:
    """
    Helps conversion of a PostgreSQL composite type into a Python object.

    The class is usually created by the `register_composite()` function.
    You may want to create and register manually instances of the class if
    querying the database at registration time is not desirable (such as when
    using an :ref:`asynchronous connections <async-support>`).
    """
    name: Any
    schema: Any
    oid: Any
    array_oid: Any
    attnames: Any
    atttypes: Any
    typecaster: Any
    array_typecaster: Any
    def __init__(self, name, oid, attrs, array_oid=None, schema=None) -> None: ...
    def parse(self, s, curs): ...
    def make(self, values):
        """
        Return a new Python object representing the data being casted.

        *values* is the list of attributes, already casted into their Python
        representation.

        You can subclass this method to :ref:`customize the composite cast
        <custom-composite>`.
        """
        ...
    @classmethod
    def tokenize(cls, s): ...

def register_composite(name, conn_or_curs, globally: bool = False, factory=None): ...
def execute_batch(cur, sql, argslist, page_size: int = 100) -> None: ...
def execute_values(cur, sql, argslist, template=None, page_size: int = 100, fetch: bool = False): ...
