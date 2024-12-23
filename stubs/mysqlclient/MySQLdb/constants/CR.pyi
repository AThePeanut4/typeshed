"""
MySQL Connection Errors

Nearly all of these raise OperationalError. COMMANDS_OUT_OF_SYNC
raises ProgrammingError.
"""

ERROR_FIRST: int
MIN_ERROR: int
UNKNOWN_ERROR: int
SOCKET_CREATE_ERROR: int
CONNECTION_ERROR: int
CONN_HOST_ERROR: int
IPSOCK_ERROR: int
UNKNOWN_HOST: int
SERVER_GONE_ERROR: int
VERSION_ERROR: int
OUT_OF_MEMORY: int
WRONG_HOST_INFO: int
LOCALHOST_CONNECTION: int
TCP_CONNECTION: int
SERVER_HANDSHAKE_ERR: int
SERVER_LOST: int
COMMANDS_OUT_OF_SYNC: int
NAMEDPIPE_CONNECTION: int
NAMEDPIPEWAIT_ERROR: int
NAMEDPIPEOPEN_ERROR: int
NAMEDPIPESETSTATE_ERROR: int
CANT_READ_CHARSET: int
NET_PACKET_TOO_LARGE: int
EMBEDDED_CONNECTION: int
PROBE_SLAVE_STATUS: int
PROBE_SLAVE_HOSTS: int
PROBE_SLAVE_CONNECT: int
PROBE_MASTER_CONNECT: int
SSL_CONNECTION_ERROR: int
MALFORMED_PACKET: int
WRONG_LICENSE: int
NULL_POINTER: int
NO_PREPARE_STMT: int
PARAMS_NOT_BOUND: int
DATA_TRUNCATED: int
NO_PARAMETERS_EXISTS: int
INVALID_PARAMETER_NO: int
INVALID_BUFFER_USE: int
UNSUPPORTED_PARAM_TYPE: int
SHARED_MEMORY_CONNECTION: int
SHARED_MEMORY_CONNECT_REQUEST_ERROR: int
SHARED_MEMORY_CONNECT_ANSWER_ERROR: int
SHARED_MEMORY_CONNECT_FILE_MAP_ERROR: int
SHARED_MEMORY_CONNECT_MAP_ERROR: int
SHARED_MEMORY_FILE_MAP_ERROR: int
SHARED_MEMORY_MAP_ERROR: int
SHARED_MEMORY_EVENT_ERROR: int
SHARED_MEMORY_CONNECT_ABANDONED_ERROR: int
SHARED_MEMORY_CONNECT_SET_ERROR: int
CONN_UNKNOW_PROTOCOL: int
INVALID_CONN_HANDLE: int
UNUSED_1: int
FETCH_CANCELED: int
NO_DATA: int
NO_STMT_METADATA: int
NO_RESULT_SET: int
NOT_IMPLEMENTED: int
SERVER_LOST_EXTENDED: int
STMT_CLOSED: int
NEW_STMT_METADATA: int
ALREADY_CONNECTED: int
AUTH_PLUGIN_CANNOT_LOAD: int
DUPLICATE_CONNECTION_ATTR: int
AUTH_PLUGIN_ERR: int
INSECURE_API_ERR: int
FILE_NAME_TOO_LONG: int
SSL_FIPS_MODE_ERR: int
MAX_ERROR: int
ERROR_LAST: int
