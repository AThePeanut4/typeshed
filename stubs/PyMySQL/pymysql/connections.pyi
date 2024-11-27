from _typeshed import Incomplete
from collections.abc import Mapping
from socket import socket as _socket
from ssl import _PasswordType
from typing import Any, AnyStr, Generic, TypeVar, overload
from typing_extensions import Self

from .charset import charset_by_id as charset_by_id, charset_by_name as charset_by_name
from .constants import CLIENT as CLIENT, COMMAND as COMMAND, FIELD_TYPE as FIELD_TYPE, SERVER_STATUS as SERVER_STATUS
from .cursors import Cursor
from .util import byte2int as byte2int, int2byte as int2byte

SSL_ENABLED: bool
DEFAULT_USER: str | None
DEBUG: bool
DEFAULT_CHARSET: str
TEXT_TYPES: set[int]
MAX_PACKET_LEN: int

_C = TypeVar("_C", bound=Cursor)
_C2 = TypeVar("_C2", bound=Cursor)

def dump_packet(data): ...
def pack_int24(n): ...
def _lenenc_int(i: int) -> bytes: ...

class MysqlPacket:
    """
    Representation of a MySQL response packet.

    Provides an interface for reading/parsing the packet results.
    """
    connection: Any
    def __init__(self, data, encoding): ...
    def get_all_data(self): ...
    def read(self, size):
        """Read the first 'size' bytes in packet and advance cursor past them."""
        ...
    def read_all(self):
        """
        Read all remaining data in the packet.

        (Subsequent read() will return errors.)
        """
        ...
    def advance(self, length):
        """Advance the cursor in data buffer 'length' bytes."""
        ...
    def rewind(self, position: int = 0):
        """Set the position of the data buffer cursor to 'position'."""
        ...
    def get_bytes(self, position, length: int = 1):
        """
        Get 'length' bytes starting at 'position'.

        Position is start of payload (first four packet header bytes are not
        included) starting at index '0'.

        No error checking is done.  If requesting outside end of buffer
        an empty string (or string shorter than 'length') may be returned!
        """
        ...
    def read_string(self) -> bytes: ...
    def read_uint8(self) -> Any: ...
    def read_uint16(self) -> Any: ...
    def read_uint24(self) -> Any: ...
    def read_uint32(self) -> Any: ...
    def read_uint64(self) -> Any: ...
    def read_length_encoded_integer(self) -> int:
        """
        Read a 'Length Coded Binary' number from the data buffer.

        Length coded numbers can be anywhere from 1 to 9 bytes depending
        on the value of the first byte.
        """
        ...
    def read_length_coded_string(self) -> bytes:
        """
        Read a 'Length Coded String' from the data buffer.

        A 'Length Coded String' consists first of a length coded
        (unsigned, positive) integer represented in 1-9 bytes followed by
        that many bytes of binary data.  (For example "cat" would be "3cat".)
        """
        ...
    def read_struct(self, fmt: str) -> tuple[Any, ...]: ...
    def is_ok_packet(self) -> bool: ...
    def is_eof_packet(self) -> bool: ...
    def is_auth_switch_request(self) -> bool: ...
    def is_extra_auth_data(self) -> bool: ...
    def is_resultset_packet(self) -> bool: ...
    def is_load_local_packet(self) -> bool: ...
    def is_error_packet(self) -> bool: ...
    def check_error(self): ...
    def raise_for_error(self) -> None: ...
    def dump(self): ...

class FieldDescriptorPacket(MysqlPacket):
    """
    A MysqlPacket that represents a specific column's metadata in the result.

    Parsing is automatically done and the results are exported via public
    attributes on the class such as: db, table_name, name, length, type_code.
    """
    def __init__(self, data, encoding): ...
    def description(self):
        """Provides a 7-item tuple compatible with the Python PEP249 DB Spec."""
        ...
    def get_column_length(self): ...

class Connection(Generic[_C]):
    """
    Representation of a socket with a mysql server.

    The proper way to get an instance of this class is to call
    connect().

    Establish a connection to the MySQL database. Accepts several
    arguments:

    :param host: Host where the database server is located.
    :param user: Username to log in as.
    :param password: Password to use.
    :param database: Database to use, None to not use a particular one.
    :param port: MySQL port to use, default is usually OK. (default: 3306)
    :param bind_address: When the client has multiple network interfaces, specify
        the interface from which to connect to the host. Argument can be
        a hostname or an IP address.
    :param unix_socket: Use a unix socket rather than TCP/IP.
    :param read_timeout: The timeout for reading from the connection in seconds.
        (default: None - no timeout)
    :param write_timeout: The timeout for writing to the connection in seconds.
        (default: None - no timeout)
    :param str charset: Charset to use.
    :param str collation: Collation name to use.
    :param sql_mode: Default SQL_MODE to use.
    :param read_default_file:
        Specifies  my.cnf file to read these parameters from under the [client] section.
    :param conv:
        Conversion dictionary to use instead of the default one.
        This is used to provide custom marshalling and unmarshalling of types.
        See converters.
    :param use_unicode:
        Whether or not to default to unicode strings.
        This option defaults to true.
    :param client_flag: Custom flags to send to MySQL. Find potential values in constants.CLIENT.
    :param cursorclass: Custom cursor class to use.
    :param init_command: Initial SQL statement to run when connection is established.
    :param connect_timeout: The timeout for connecting to the database in seconds.
        (default: 10, min: 1, max: 31536000)
    :param ssl: A dict of arguments similar to mysql_ssl_set()'s parameters or an ssl.SSLContext.
    :param ssl_ca: Path to the file that contains a PEM-formatted CA certificate.
    :param ssl_cert: Path to the file that contains a PEM-formatted client certificate.
    :param ssl_disabled: A boolean value that disables usage of TLS.
    :param ssl_key: Path to the file that contains a PEM-formatted private key for
        the client certificate.
    :param ssl_key_password: The password for the client certificate private key.
    :param ssl_verify_cert: Set to true to check the server certificate's validity.
    :param ssl_verify_identity: Set to true to check the server's identity.
    :param read_default_group: Group to read from in the configuration file.
    :param autocommit: Autocommit mode. None means use server default. (default: False)
    :param local_infile: Boolean to enable the use of LOAD DATA LOCAL command. (default: False)
    :param max_allowed_packet: Max size of packet sent to server in bytes. (default: 16MB)
        Only used to limit size of "LOAD LOCAL INFILE" data packet smaller than default (16KB).
    :param defer_connect: Don't explicitly connect on construction - wait for connect call.
        (default: False)
    :param auth_plugin_map: A dict of plugin names to a class that processes that plugin.
        The class will take the Connection object as the argument to the constructor.
        The class needs an authenticate method taking an authentication packet as
        an argument.  For the dialog plugin, a prompt(echo, prompt) method can be used
        (if no authenticate method) for returning a string from the user. (experimental)
    :param server_public_key: SHA256 authentication plugin public key value. (default: None)
    :param binary_prefix: Add _binary prefix on bytes and bytearray. (default: False)
    :param compress: Not supported.
    :param named_pipe: Not supported.
    :param db: **DEPRECATED** Alias for database.
    :param passwd: **DEPRECATED** Alias for password.

    See `Connection <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_ in the
    specification.
    """
    ssl: Any
    host: Any
    port: Any
    user: Any
    password: Any
    db: Any
    unix_socket: Any
    charset: str
    collation: str | None
    bind_address: Any
    use_unicode: Any
    client_flag: Any
    cursorclass: Any
    connect_timeout: Any
    messages: Any
    encoders: Any
    decoders: Any
    host_info: Any
    sql_mode: Any
    init_command: Any
    max_allowed_packet: int
    server_public_key: bytes
    @overload
    def __init__(
        self: Connection[Cursor],  # different between overloads
        *,
        host: str | None = None,
        user: Incomplete | None = None,
        password: str = "",
        database: Incomplete | None = None,
        port: int = 0,
        unix_socket: Incomplete | None = None,
        charset: str = "",
        collation: str | None = None,
        sql_mode: Incomplete | None = None,
        read_default_file: Incomplete | None = None,
        conv=None,
        use_unicode: bool | None = True,
        client_flag: int = 0,
        cursorclass: None = None,  # different between overloads
        init_command: Incomplete | None = None,
        connect_timeout: int | None = 10,
        ssl: Mapping[Any, Any] | None = None,
        ssl_ca=None,
        ssl_cert=None,
        ssl_disabled=None,
        ssl_key=None,
        ssl_key_password: _PasswordType | None = None,
        ssl_verify_cert=None,
        ssl_verify_identity=None,
        read_default_group: Incomplete | None = None,
        compress: Incomplete | None = None,
        named_pipe: Incomplete | None = None,
        autocommit: bool | None = False,
        db: Incomplete | None = None,
        passwd: Incomplete | None = None,
        local_infile: Incomplete | None = False,
        max_allowed_packet: int = 16777216,
        defer_connect: bool | None = False,
        auth_plugin_map: Mapping[Any, Any] | None = None,
        read_timeout: float | None = None,
        write_timeout: float | None = None,
        bind_address: Incomplete | None = None,
        binary_prefix: bool | None = False,
        program_name: Incomplete | None = None,
        server_public_key: bytes | None = None,
    ) -> None: ...
    @overload
    def __init__(
        # different between overloads:
        self: Connection[_C],  # pyright: ignore[reportInvalidTypeVarUse]  #11780
        *,
        host: str | None = None,
        user: Incomplete | None = None,
        password: str = "",
        database: Incomplete | None = None,
        port: int = 0,
        unix_socket: Incomplete | None = None,
        charset: str = "",
        collation: str | None = None,
        sql_mode: Incomplete | None = None,
        read_default_file: Incomplete | None = None,
        conv=None,
        use_unicode: bool | None = True,
        client_flag: int = 0,
        cursorclass: type[_C] = ...,  # different between overloads
        init_command: Incomplete | None = None,
        connect_timeout: int | None = 10,
        ssl: Mapping[Any, Any] | None = None,
        ssl_ca=None,
        ssl_cert=None,
        ssl_disabled=None,
        ssl_key=None,
        ssl_verify_cert=None,
        ssl_verify_identity=None,
        read_default_group: Incomplete | None = None,
        compress: Incomplete | None = None,
        named_pipe: Incomplete | None = None,
        autocommit: bool | None = False,
        db: Incomplete | None = None,
        passwd: Incomplete | None = None,
        local_infile: Incomplete | None = False,
        max_allowed_packet: int = 16777216,
        defer_connect: bool | None = False,
        auth_plugin_map: Mapping[Any, Any] | None = None,
        read_timeout: float | None = None,
        write_timeout: float | None = None,
        bind_address: Incomplete | None = None,
        binary_prefix: bool | None = False,
        program_name: Incomplete | None = None,
        server_public_key: bytes | None = None,
    ) -> None: ...
    socket: Any
    rfile: Any
    wfile: Any
    def close(self) -> None:
        """
        Send the quit message and close the socket.

        See `Connection.close() <https://www.python.org/dev/peps/pep-0249/#Connection.close>`_
        in the specification.

        :raise Error: If the connection is already closed.
        """
        ...
    @property
    def open(self) -> bool:
        """Return True if the connection is open."""
        ...
    def autocommit(self, value) -> None: ...
    def get_autocommit(self) -> bool: ...
    def commit(self) -> None:
        """
        Commit changes to stable storage.

        See `Connection.commit() <https://www.python.org/dev/peps/pep-0249/#commit>`_
        in the specification.
        """
        ...
    def begin(self) -> None:
        """Begin transaction."""
        ...
    def rollback(self) -> None:
        """
        Roll back the current transaction.

        See `Connection.rollback() <https://www.python.org/dev/peps/pep-0249/#rollback>`_
        in the specification.
        """
        ...
    def select_db(self, db) -> None:
        """
        Set current db.

        :param db: The name of the db.
        """
        ...
    def escape(self, obj, mapping: Mapping[Any, Any] | None = None):
        """
        Escape whatever value is passed.

        Non-standard, for internal use; do not use this in your applications.
        """
        ...
    def literal(self, obj):
        """
        Alias for escape().

        Non-standard, for internal use; do not use this in your applications.
        """
        ...
    def escape_string(self, s: AnyStr) -> AnyStr: ...
    @overload
    def cursor(self, cursor: None = None) -> _C:
        """
        Create a new cursor to execute queries with.

        :param cursor: The type of cursor to create. None means use Cursor.
        :type cursor: :py:class:`Cursor`, :py:class:`SSCursor`, :py:class:`DictCursor`,
            or :py:class:`SSDictCursor`.
        """
        ...
    @overload
    def cursor(self, cursor: type[_C2]) -> _C2:
        """
        Create a new cursor to execute queries with.

        :param cursor: The type of cursor to create. None means use Cursor.
        :type cursor: :py:class:`Cursor`, :py:class:`SSCursor`, :py:class:`DictCursor`,
            or :py:class:`SSDictCursor`.
        """
        ...
    def query(self, sql, unbuffered: bool = False) -> int: ...
    def next_result(self, unbuffered: bool = False) -> int: ...
    def affected_rows(self): ...
    def kill(self, thread_id): ...
    def ping(self, reconnect: bool = True) -> None:
        """
        Check if the server is alive.

        :param reconnect: If the connection is closed, reconnect.
        :type reconnect: boolean

        :raise Error: If the connection is closed and reconnect=False.
        """
        ...
    def set_charset(self, charset) -> None:
        """Deprecated. Use set_character_set() instead."""
        ...
    def connect(self, sock: _socket | None = None) -> None: ...
    def write_packet(self, payload) -> None:
        """
        Writes an entire "mysql packet" in its entirety to the network
        adding its length and sequence number.
        """
        ...
    def _read_packet(self, packet_type=...):
        """
        Read an entire "mysql packet" in its entirety from the network
        and return a MysqlPacket type that represents the results.

        :raise OperationalError: If the connection to the MySQL server is lost.
        :raise InternalError: If the packet sequence number is wrong.
        """
        ...
    def insert_id(self): ...
    def thread_id(self): ...
    def character_set_name(self): ...
    def get_host_info(self): ...
    def get_proto_info(self): ...
    def get_server_info(self): ...
    def show_warnings(self):
        """Send the "SHOW WARNINGS" SQL command."""
        ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *exc_info: object) -> None: ...
    Warning: Any
    Error: Any
    InterfaceError: Any
    DatabaseError: Any
    DataError: Any
    OperationalError: Any
    IntegrityError: Any
    InternalError: Any
    ProgrammingError: Any
    NotSupportedError: Any

class MySQLResult:
    connection: Any
    affected_rows: Any
    insert_id: Any
    server_status: Any
    warning_count: Any
    message: Any
    field_count: Any
    description: Any
    rows: Any
    has_next: Any
    def __init__(self, connection: Connection[Any]) -> None:
        """:type connection: Connection"""
        ...
    first_packet: Any
    def read(self) -> None: ...
    def init_unbuffered_query(self) -> None:
        """
        :raise OperationalError: If the connection to the MySQL server is lost.
        :raise InternalError:
        """
        ...

class LoadLocalFile:
    filename: Any
    connection: Connection[Any]
    def __init__(self, filename: Any, connection: Connection[Any]) -> None: ...
    def send_data(self) -> None:
        """Send data packets from the local file to the server"""
        ...
