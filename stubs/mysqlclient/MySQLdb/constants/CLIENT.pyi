"""
MySQL CLIENT constants

These constants are used when creating the connection. Use bitwise-OR
(|) to combine options together, and pass them as the client_flags
parameter to MySQLdb.Connection. For more information on these flags,
see the MySQL C API documentation for mysql_real_connect().
"""

LONG_PASSWORD: int
FOUND_ROWS: int
LONG_FLAG: int
CONNECT_WITH_DB: int
NO_SCHEMA: int
COMPRESS: int
ODBC: int
LOCAL_FILES: int
IGNORE_SPACE: int
CHANGE_USER: int
INTERACTIVE: int
SSL: int
IGNORE_SIGPIPE: int
TRANSACTIONS: int
RESERVED: int
SECURE_CONNECTION: int
MULTI_STATEMENTS: int
MULTI_RESULTS: int
