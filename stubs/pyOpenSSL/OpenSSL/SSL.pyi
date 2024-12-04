import socket
from _socket import _Address, _RetAddress
from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Callable, MutableSequence, Sequence
from typing import Any, TypeVar

import _cffi_backend as cffi
from OpenSSL.crypto import X509, PKey, X509Name

OPENSSL_VERSION_NUMBER: int
SSLEAY_VERSION: int
SSLEAY_CFLAGS: int
SSLEAY_PLATFORM: int
SSLEAY_DIR: int
SSLEAY_BUILT_ON: int

SENT_SHUTDOWN: int
RECEIVED_SHUTDOWN: int

SSLv23_METHOD: int
TLSv1_METHOD: int
TLSv1_1_METHOD: int
TLSv1_2_METHOD: int

TLS_METHOD: int
TLS_SERVER_METHOD: int
TLS_CLIENT_METHOD: int
DTLS_METHOD: int
DTLS_SERVER_METHOD: int
DTLS_CLIENT_METHOD: int

SSL3_VERSION: int
TLS1_VERSION: int
TLS1_1_VERSION: int
TLS1_2_VERSION: int
TLS1_3_VERSION: int

OP_NO_SSLv2: int
OP_NO_SSLv3: int
OP_NO_TLSv1: int
OP_NO_TLSv1_1: int
OP_NO_TLSv1_2: int
OP_NO_TLSv1_3: int

MODE_RELEASE_BUFFERS: int

OP_SINGLE_DH_USE: int
OP_SINGLE_ECDH_USE: int
OP_EPHEMERAL_RSA: int
OP_MICROSOFT_SESS_ID_BUG: int
OP_NETSCAPE_CHALLENGE_BUG: int
OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG: int

OP_SSLREF2_REUSE_CERT_TYPE_BUG: int
OP_MICROSOFT_BIG_SSLV3_BUFFER: int
OP_MSIE_SSLV2_RSA_PADDING: int
OP_SSLEAY_080_CLIENT_DH_BUG: int
OP_TLS_D5_BUG: int
OP_TLS_BLOCK_PADDING_BUG: int
OP_DONT_INSERT_EMPTY_FRAGMENTS: int
OP_CIPHER_SERVER_PREFERENCE: int
OP_TLS_ROLLBACK_BUG: int
OP_PKCS1_CHECK_1: int
OP_PKCS1_CHECK_2: int
OP_NETSCAPE_CA_DN_BUG: int
OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG: int

OP_NO_COMPRESSION: int

OP_NO_QUERY_MTU: int
OP_COOKIE_EXCHANGE: int
OP_NO_TICKET: int

OP_ALL: int

VERIFY_PEER: int
VERIFY_FAIL_IF_NO_PEER_CERT: int
VERIFY_CLIENT_ONCE: int
VERIFY_NONE: int

SESS_CACHE_OFF: int
SESS_CACHE_CLIENT: int
SESS_CACHE_SERVER: int
SESS_CACHE_BOTH: int
SESS_CACHE_NO_AUTO_CLEAR: int
SESS_CACHE_NO_INTERNAL_LOOKUP: int
SESS_CACHE_NO_INTERNAL_STORE: int
SESS_CACHE_NO_INTERNAL: int

SSL_ST_CONNECT: int
SSL_ST_ACCEPT: int
SSL_ST_MASK: int

SSL_CB_LOOP: int
SSL_CB_EXIT: int
SSL_CB_READ: int
SSL_CB_WRITE: int
SSL_CB_ALERT: int
SSL_CB_READ_ALERT: int
SSL_CB_WRITE_ALERT: int
SSL_CB_ACCEPT_LOOP: int
SSL_CB_ACCEPT_EXIT: int
SSL_CB_CONNECT_LOOP: int
SSL_CB_CONNECT_EXIT: int
SSL_CB_HANDSHAKE_START: int
SSL_CB_HANDSHAKE_DONE: int

NO_OVERLAPPING_PROTOCOLS: object

class Error(Exception):
    """An error occurred in an `OpenSSL.SSL` API."""
    ...
class WantReadError(Error): ...
class WantWriteError(Error): ...
class WantX509LookupError(Error): ...
class ZeroReturnError(Error): ...
class SysCallError(Error): ...

def SSLeay_version(type: int) -> bytes:
    """
    Return a string describing the version of OpenSSL in use.

    :param type: One of the :const:`OPENSSL_` constants defined in this module.
    """
    ...

class Session:
    """
    A class representing an SSL session.  A session defines certain connection
    parameters which may be re-used to speed up the setup of subsequent
    connections.

    .. versionadded:: 0.14
    """
    ...

class Connection:
    def __getattr__(self, name: str) -> Any:
        """
        Look up attributes on the wrapped socket object if they are not found
        on the Connection object.
        """
        ...
    def __init__(self, context: Context, socket: socket.socket | None = None) -> None:
        """
        Create a new Connection object, using the given OpenSSL.SSL.Context
        instance and socket.

        :param context: An SSL Context to use for this connection
        :param socket: The socket to use for transport layer
        """
        ...
    def get_context(self) -> Context:
        """
        Retrieve the :class:`Context` object associated with this
        :class:`Connection`.
        """
        ...
    def set_context(self, context: Context) -> None:
        """
        Switch this connection to a new session context.

        :param context: A :class:`Context` instance giving the new session
            context to use.
        """
        ...
    def get_servername(self) -> bytes | None:
        """
        Retrieve the servername extension value if provided in the client hello
        message, or None if there wasn't one.

        :return: A byte string giving the server name or :data:`None`.

        .. versionadded:: 0.13
        """
        ...
    def set_tlsext_host_name(self, name: bytes) -> None:
        """
        Set the value of the servername extension to send in the client hello.

        :param name: A byte string giving the name.

        .. versionadded:: 0.13
        """
        ...
    def pending(self) -> int:
        """
        Get the number of bytes that can be safely read from the SSL buffer
        (**not** the underlying transport buffer).

        :return: The number of bytes available in the receive buffer.
        """
        ...
    def send(self, buf: ReadableBuffer | str, flags: int = 0) -> int:
        """
        Send data on the connection. NOTE: If you get one of the WantRead,
        WantWrite or WantX509Lookup exceptions on this, you have to call the
        method again with the SAME buffer.

        :param buf: The string, buffer or memoryview to send
        :param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        :return: The number of bytes written
        """
        ...
    write = send
    def sendall(self, buf: ReadableBuffer | str, flags: int = 0) -> int:
        """
        Send "all" data on the connection. This calls send() repeatedly until
        all data is sent. If an error occurs, it's impossible to tell how much
        data has been sent.

        :param buf: The string, buffer or memoryview to send
        :param flags: (optional) Included for compatibility with the socket
                      API, the value is ignored
        :return: The number of bytes written
        """
        ...
    def recv(self, bufsiz: int, flags: int | None = None) -> bytes:
        """
        Receive data on the connection.

        :param bufsiz: The maximum number of bytes to read
        :param flags: (optional) The only supported flag is ``MSG_PEEK``,
            all other flags are ignored.
        :return: The string read from the Connection
        """
        ...
    read = recv
    def recv_into(self, buffer: MutableSequence[int], nbytes: int | None = None, flags: int | None = None) -> int:
        """
        Receive data on the connection and copy it directly into the provided
        buffer, rather than creating a new string.

        :param buffer: The buffer to copy into.
        :param nbytes: (optional) The maximum number of bytes to read into the
            buffer. If not present, defaults to the size of the buffer. If
            larger than the size of the buffer, is reduced to the size of the
            buffer.
        :param flags: (optional) The only supported flag is ``MSG_PEEK``,
            all other flags are ignored.
        :return: The number of bytes read into the buffer.
        """
        ...
    def connect(self, addr: str | bytes | Sequence[str | int]) -> None:
        """
        Call the :meth:`connect` method of the underlying socket and set up SSL
        on the socket, using the :class:`Context` object supplied to this
        :class:`Connection` object at creation.

        :param addr: A remote address
        :return: What the socket's connect method returns
        """
        ...
    def connect_ex(self, addr: _Address | bytes) -> int:
        """
        Call the :meth:`connect_ex` method of the underlying socket and set up
        SSL on the socket, using the Context object supplied to this Connection
        object at creation. Note that if the :meth:`connect_ex` method of the
        socket doesn't return 0, SSL won't be initialized.

        :param addr: A remove address
        :return: What the socket's connect_ex method returns
        """
        ...
    def accept(self) -> tuple[Connection, _RetAddress]:
        """
        Call the :meth:`accept` method of the underlying socket and set up SSL
        on the returned socket, using the Context object supplied to this
        :class:`Connection` object at creation.

        :return: A *(conn, addr)* pair where *conn* is the new
            :class:`Connection` object created, and *address* is as returned by
            the socket's :meth:`accept`.
        """
        ...
    def DTLSv1_listen(self) -> None:
        """
        Call the OpenSSL function DTLSv1_listen on this connection. See the
        OpenSSL manual for more details.

        :return: None
        """
        ...
    def DTLSv1_get_timeout(self) -> float | None:
        """
        Determine when the DTLS SSL object next needs to perform internal
        processing due to the passage of time.

        When the returned number of seconds have passed, the
        :meth:`DTLSv1_handle_timeout` method needs to be called.

        :return: The time left in seconds before the next timeout or `None`
            if no timeout is currently active.
        """
        ...
    def DTLSv1_handle_timeout(self) -> bool:
        """
        Handles any timeout events which have become pending on a DTLS SSL
        object.

        :return: `True` if there was a pending timeout, `False` otherwise.
        """
        ...
    def shutdown(self) -> bool:
        """
        Send the shutdown message to the Connection.

        :return: True if the shutdown completed successfully (i.e. both sides
                 have sent closure alerts), False otherwise (in which case you
                 call :meth:`recv` or :meth:`send` when the connection becomes
                 readable/writeable).
        """
        ...
    def do_handshake(self) -> None:
        """
        Perform an SSL handshake (usually called after :meth:`renegotiate` or
        one of :meth:`set_accept_state` or :meth:`set_connect_state`). This can
        raise the same exceptions as :meth:`send` and :meth:`recv`.

        :return: None.
        """
        ...
    def get_certificate(self) -> X509 | None:
        """
        Retrieve the local certificate (if any)

        :return: The local certificate
        """
        ...
    def get_peer_certificate(self) -> X509 | None:
        """
        Retrieve the other side's certificate (if any)

        :return: The peer's certificate
        """
        ...
    def get_peer_cert_chain(self) -> list[X509] | None:
        """
        Retrieve the other side's certificate (if any)

        :return: A list of X509 instances giving the peer's certificate chain,
                 or None if it does not have one.
        """
        ...
    def get_verified_chain(self) -> list[X509] | None:
        """
        Retrieve the verified certificate chain of the peer including the
        peer's end entity certificate. It must be called after a session has
        been successfully established. If peer verification was not successful
        the chain may be incomplete, invalid, or None.

        :return: A list of X509 instances giving the peer's verified
                 certificate chain, or None if it does not have one.

        .. versionadded:: 20.0
        """
        ...
    def bio_read(self, bufsiz: int) -> bytes:
        """
        If the Connection was created with a memory BIO, this method can be
        used to read bytes from the write end of that memory BIO.  Many
        Connection methods will add bytes which must be read in this manner or
        the buffer will eventually fill up and the Connection will be able to
        take no further actions.

        :param bufsiz: The maximum number of bytes to read
        :return: The string read.
        """
        ...
    def bio_write(self, buf: bytes) -> int:
        """
        If the Connection was created with a memory BIO, this method can be
        used to add bytes to the read end of that memory BIO.  The Connection
        can then read the bytes (for example, in response to a call to
        :meth:`recv`).

        :param buf: The string to put into the memory BIO.
        :return: The number of bytes written
        """
        ...
    def bio_shutdown(self) -> None:
        """
        If the Connection was created with a memory BIO, this method can be
        used to indicate that *end of file* has been reached on the read end of
        that memory BIO.

        :return: None
        """
        ...
    def renegotiate(self) -> bool:
        """
        Renegotiate the session.

        :return: True if the renegotiation can be started, False otherwise
        :rtype: bool
        """
        ...
    def renegotiate_pending(self) -> bool:
        """
        Check if there's a renegotiation in progress, it will return False once
        a renegotiation is finished.

        :return: Whether there's a renegotiation in progress
        :rtype: bool
        """
        ...
    def total_renegotiations(self) -> int:
        """
        Find out the total number of renegotiations.

        :return: The number of renegotiations.
        :rtype: int
        """
        ...
    def set_accept_state(self) -> None:
        """
        Set the connection to work in server mode. The handshake will be
        handled automatically by read/write.

        :return: None
        """
        ...
    def set_connect_state(self) -> None:
        """
        Set the connection to work in client mode. The handshake will be
        handled automatically by read/write.

        :return: None
        """
        ...
    def get_client_ca_list(self) -> list[X509Name]:
        """
        Get CAs whose certificates are suggested for client authentication.

        :return: If this is a server connection, the list of certificate
            authorities that will be sent or has been sent to the client, as
            controlled by this :class:`Connection`'s :class:`Context`.

            If this is a client connection, the list will be empty until the
            connection with the server is established.

        .. versionadded:: 0.10
        """
        ...
    def get_cipher_list(self) -> list[str]:
        """
        Retrieve the list of ciphers used by the Connection object.

        :return: A list of native cipher strings.
        """
        ...
    def get_cipher_name(self) -> str | None:
        """
        Obtain the name of the currently used cipher.

        :returns: The name of the currently used cipher or :obj:`None`
            if no connection has been established.
        :rtype: :class:`unicode` or :class:`NoneType`

        .. versionadded:: 0.15
        """
        ...
    def get_cipher_bits(self) -> int | None:
        """
        Obtain the number of secret bits of the currently used cipher.

        :returns: The number of secret bits of the currently used cipher
            or :obj:`None` if no connection has been established.
        :rtype: :class:`int` or :class:`NoneType`

        .. versionadded:: 0.15
        """
        ...
    def get_cipher_version(self) -> str | None:
        """
        Obtain the protocol version of the currently used cipher.

        :returns: The protocol name of the currently used cipher
            or :obj:`None` if no connection has been established.
        :rtype: :class:`unicode` or :class:`NoneType`

        .. versionadded:: 0.15
        """
        ...
    def get_protocol_version_name(self) -> str:
        """
        Retrieve the protocol version of the current connection.

        :returns: The TLS version of the current connection, for example
            the value for TLS 1.2 would be ``TLSv1.2``or ``Unknown``
            for connections that were not successfully established.
        :rtype: :class:`unicode`
        """
        ...
    def get_protocol_version(self) -> int:
        """
        Retrieve the SSL or TLS protocol version of the current connection.

        :returns: The TLS version of the current connection.  For example,
            it will return ``0x769`` for connections made over TLS version 1.
        :rtype: :class:`int`
        """
        ...
    def get_shutdown(self) -> int:
        """
        Get the shutdown state of the Connection.

        :return: The shutdown state, a bitvector of SENT_SHUTDOWN,
            RECEIVED_SHUTDOWN.
        """
        ...
    def set_shutdown(self, state: int) -> None:
        """
        Set the shutdown state of the Connection.

        :param state: bitvector of SENT_SHUTDOWN, RECEIVED_SHUTDOWN.
        :return: None
        """
        ...
    def get_state_string(self) -> bytes:
        """
        Retrieve a verbose string detailing the state of the Connection.

        :return: A string representing the state
        :rtype: bytes
        """
        ...
    def server_random(self) -> bytes | None:
        """
        Retrieve the random value used with the server hello message.

        :return: A string representing the state
        """
        ...
    def client_random(self) -> bytes | None:
        """
        Retrieve the random value used with the client hello message.

        :return: A string representing the state
        """
        ...
    def master_key(self) -> bytes | None:
        """
        Retrieve the value of the master key for this session.

        :return: A string representing the state
        """
        ...
    def export_keying_material(self, label: bytes, olen: int, context: bytes | None = None) -> cffi.buffer:
        """
        Obtain keying material for application use.

        :param: label - a disambiguating label string as described in RFC 5705
        :param: olen - the length of the exported key material in bytes
        :param: context - a per-association context value
        :return: the exported key material bytes or None
        """
        ...
    def get_app_data(self) -> Any:
        """
        Retrieve application data as set by :meth:`set_app_data`.

        :return: The application data
        """
        ...
    def set_app_data(self, data: Any) -> None:
        """
        Set application data

        :param data: The application data
        :return: None
        """
        ...
    def sock_shutdown(self, how: int, /) -> None:
        """
        Call the :meth:`shutdown` method of the underlying socket.
        See :manpage:`shutdown(2)`.

        :return: What the socket's shutdown() method returns
        """
        ...
    def want_read(self) -> bool:
        """
        Checks if more data has to be read from the transport layer to complete
        an operation.

        :return: True iff more data has to be read
        """
        ...
    def want_write(self) -> bool:
        """
        Checks if there is data to write to the transport layer to complete an
        operation.

        :return: True iff there is data to write
        """
        ...
    def get_session(self) -> Session | None:
        """
        Returns the Session currently used.

        :return: An instance of :class:`OpenSSL.SSL.Session` or
            :obj:`None` if no session exists.

        .. versionadded:: 0.14
        """
        ...
    def set_session(self, session: Session) -> None:
        """
        Set the session to be used when the TLS/SSL connection is established.

        :param session: A Session instance representing the session to use.
        :returns: None

        .. versionadded:: 0.14
        """
        ...
    def get_finished(self) -> bytes | None:
        """
        Obtain the latest TLS Finished message that we sent.

        :return: The contents of the message or :obj:`None` if the TLS
            handshake has not yet completed.
        :rtype: :class:`bytes` or :class:`NoneType`

        .. versionadded:: 0.15
        """
        ...
    def get_peer_finished(self) -> bytes | None:
        """
        Obtain the latest TLS Finished message that we received from the peer.

        :return: The contents of the message or :obj:`None` if the TLS
            handshake has not yet completed.
        :rtype: :class:`bytes` or :class:`NoneType`

        .. versionadded:: 0.15
        """
        ...
    def set_alpn_protos(self, protos: Sequence[bytes]) -> None:
        """
        Specify the client's ALPN protocol list.

        These protocols are offered to the server during protocol negotiation.

        :param protos: A list of the protocols to be offered to the server.
            This list should be a Python list of bytestrings representing the
            protocols to offer, e.g. ``[b'http/1.1', b'spdy/2']``.
        """
        ...
    def get_alpn_proto_negotiated(self) -> bytes:
        """
        Get the protocol that was negotiated by ALPN.

        :returns: A bytestring of the protocol name.  If no protocol has been
            negotiated yet, returns an empty bytestring.
        """
        ...
    def get_selected_srtp_profile(self) -> bytes:
        """
        Get the SRTP protocol which was negotiated.

        :returns: A bytestring of the SRTP profile name. If no profile has been
            negotiated yet, returns an empty bytestring.
        """
        ...
    def request_ocsp(self) -> None:
        """
        Called to request that the server sends stapled OCSP data, if
        available. If this is not called on the client side then the server
        will not send OCSP data. Should be used in conjunction with
        :meth:`Context.set_ocsp_client_callback`.
        """
        ...

_T = TypeVar("_T")

class Context:
    """
    :class:`OpenSSL.SSL.Context` instances define the parameters for setting
    up new SSL connections.

    :param method: One of TLS_METHOD, TLS_CLIENT_METHOD, TLS_SERVER_METHOD,
                   DTLS_METHOD, DTLS_CLIENT_METHOD, or DTLS_SERVER_METHOD.
                   SSLv23_METHOD, TLSv1_METHOD, etc. are deprecated and should
                   not be used.
    """
    def __getattr__(self, name: str) -> Incomplete: ...
    def __init__(self, method: int) -> None: ...
    def load_verify_locations(self, cafile: str | None, capath: str | None = None) -> None:
        """
        Let SSL know where we can find trusted certificates for the certificate
        chain.  Note that the certificates have to be in PEM format.

        If capath is passed, it must be a directory prepared using the
        ``c_rehash`` tool included with OpenSSL.  Either, but not both, of
        *pemfile* or *capath* may be :data:`None`.

        :param cafile: In which file we can find the certificates (``bytes`` or
            ``unicode``).
        :param capath: In which directory we can find the certificates
            (``bytes`` or ``unicode``).

        :return: None
        """
        ...
    def set_options(self, options: int) -> None:
        """
        Add options. Options set before are not cleared!
        This method should be used with the :const:`OP_*` constants.

        :param options: The options to add.
        :return: The new option bitmask.
        """
        ...
    def set_verify(self, mode: int, callback: Callable[[Connection, X509, int, int, int], bool] | None = None) -> None:
        """
        Set the verification flags for this Context object to *mode* and
        specify that *callback* should be used for verification callbacks.

        :param mode: The verify mode, this should be one of
            :const:`VERIFY_NONE` and :const:`VERIFY_PEER`. If
            :const:`VERIFY_PEER` is used, *mode* can be OR:ed with
            :const:`VERIFY_FAIL_IF_NO_PEER_CERT` and
            :const:`VERIFY_CLIENT_ONCE` to further control the behaviour.
        :param callback: The optional Python verification callback to use.
            This should take five arguments: A Connection object, an X509
            object, and three integer variables, which are in turn potential
            error number, error depth and return code. *callback* should
            return True if verification passes and False otherwise.
            If omitted, OpenSSL's default verification is used.
        :return: None

        See SSL_CTX_set_verify(3SSL) for further details.
        """
        ...
    def set_min_proto_version(self, version: int) -> None:
        """
        Set the minimum supported protocol version. Setting the minimum
        version to 0 will enable protocol versions down to the lowest version
        supported by the library.

        If the underlying OpenSSL build is missing support for the selected
        version, this method will raise an exception.
        """
        ...
    def set_max_proto_version(self, version: int) -> None:
        """
        Set the maximum supported protocol version. Setting the maximum
        version to 0 will enable protocol versions up to the highest version
        supported by the library.

        If the underlying OpenSSL build is missing support for the selected
        version, this method will raise an exception.
        """
        ...
    def use_certificate_chain_file(self, certfile: str | bytes) -> None:
        """
        Load a certificate chain from a file.

        :param certfile: The name of the certificate chain file (``bytes`` or
            ``unicode``).  Must be PEM encoded.

        :return: None
        """
        ...
    def use_certificate_file(self, certfile: str | bytes, filetype: int = 1) -> None:
        """
        Load a certificate from a file

        :param certfile: The name of the certificate file (``bytes`` or
            ``unicode``).
        :param filetype: (optional) The encoding of the file, which is either
            :const:`FILETYPE_PEM` or :const:`FILETYPE_ASN1`.  The default is
            :const:`FILETYPE_PEM`.

        :return: None
        """
        ...
    def use_certificate(self, cert: X509) -> None:
        """
        Load a certificate from a X509 object

        :param cert: The X509 object
        :return: None
        """
        ...
    def use_privatekey_file(self, keyfile: str | bytes, filetype: int | None = ...) -> None:
        """
        Load a private key from a file

        :param keyfile: The name of the key file (``bytes`` or ``unicode``)
        :param filetype: (optional) The encoding of the file, which is either
            :const:`FILETYPE_PEM` or :const:`FILETYPE_ASN1`.  The default is
            :const:`FILETYPE_PEM`.

        :return: None
        """
        ...
    def use_privatekey(self, pkey: PKey) -> None:
        """
        Load a private key from a PKey object

        :param pkey: The PKey object
        :return: None
        """
        ...
    def add_extra_chain_cert(self, certobj: X509) -> None:
        """
        Add certificate to chain

        :param certobj: The X509 certificate object to add to the chain
        :return: None
        """
        ...
    def set_cipher_list(self, cipher_list: bytes) -> None:
        """
        Set the list of ciphers to be used in this context.

        See the OpenSSL manual for more information (e.g.
        :manpage:`ciphers(1)`).

        :param bytes cipher_list: An OpenSSL cipher string.
        :return: None
        """
        ...
    def set_keylog_callback(self, callback: Callable[[Connection, bytes], object]) -> None:
        """
        Set the TLS key logging callback to *callback*. This function will be
        called whenever TLS key material is generated or received, in order
        to allow applications to store this keying material for debugging
        purposes.

        :param callback: The Python callback to use.  This should take two
            arguments: a Connection object and a bytestring that contains
            the key material in the format used by NSS for its SSLKEYLOGFILE
            debugging output.
        :return: None
        """
        ...
    def set_alpn_protos(self, protos: Sequence[bytes]) -> None:
        """
        Specify the protocols that the client is prepared to speak after the
        TLS connection has been negotiated using Application Layer Protocol
        Negotiation.

        :param protos: A list of the protocols to be offered to the server.
            This list should be a Python list of bytestrings representing the
            protocols to offer, e.g. ``[b'http/1.1', b'spdy/2']``.
        """
        ...
    def set_alpn_select_callback(self, callback: Callable[[Connection, list[bytes]], bytes]) -> None:
        """
        Specify a callback function that will be called on the server when a
        client offers protocols using ALPN.

        :param callback: The callback function.  It will be invoked with two
            arguments: the Connection, and a list of offered protocols as
            bytestrings, e.g ``[b'http/1.1', b'spdy/2']``.  It can return
            one of those bytestrings to indicate the chosen protocol, the
            empty bytestring to terminate the TLS connection, or the
            :py:obj:`NO_OVERLAPPING_PROTOCOLS` to indicate that no offered
            protocol was selected, but that the connection should not be
            aborted.
        """
        ...
    def set_ocsp_server_callback(self, callback: Callable[[Connection, _T | None], bytes], data: _T | None = None) -> None:
        """
        Set a callback to provide OCSP data to be stapled to the TLS handshake
        on the server side.

        :param callback: The callback function. It will be invoked with two
            arguments: the Connection, and the optional arbitrary data you have
            provided. The callback must return a bytestring that contains the
            OCSP data to staple to the handshake. If no OCSP data is available
            for this connection, return the empty bytestring.
        :param data: Some opaque data that will be passed into the callback
            function when called. This can be used to avoid needing to do
            complex data lookups or to keep track of what context is being
            used. This parameter is optional.
        """
        ...
    def set_ocsp_client_callback(
        self, callback: Callable[[Connection, bytes, _T | None], bool], data: _T | None = None
    ) -> None:
        """
        Set a callback to validate OCSP data stapled to the TLS handshake on
        the client side.

        :param callback: The callback function. It will be invoked with three
            arguments: the Connection, a bytestring containing the stapled OCSP
            assertion, and the optional arbitrary data you have provided. The
            callback must return a boolean that indicates the result of
            validating the OCSP data: ``True`` if the OCSP data is valid and
            the certificate can be trusted, or ``False`` if either the OCSP
            data is invalid or the certificate has been revoked.
        :param data: Some opaque data that will be passed into the callback
            function when called. This can be used to avoid needing to do
            complex data lookups or to keep track of what context is being
            used. This parameter is optional.
        """
        ...
