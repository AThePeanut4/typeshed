"""Small, fast HTTP client library for Python."""

import http.client
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, ClassVar
from typing_extensions import Self

from .error import *

__author__: str
__copyright__: str
__contributors__: list[str]
__license__: str
__version__: str

debuglevel: int
RETRIES: int

class Authentication:
    path: Any
    host: Any
    credentials: Any
    http: Any
    def __init__(self, credentials, host, request_uri, headers, response, content, http) -> None: ...
    def depth(self, request_uri): ...
    def inscope(self, host, request_uri): ...
    def request(self, method, request_uri, headers, content) -> None:
        """
        Modify the request headers to add the appropriate
        Authorization header. Over-rise this in sub-classes.
        """
        ...
    def response(self, response, content):
        """
        Gives us a chance to update with new nonces
        or such returned from the last authorized response.
        Over-rise this in sub-classes if necessary.

        Return TRUE is the request is to be retried, for
        example Digest may return stale=true.
        """
        ...
    def __eq__(self, auth): ...
    def __ne__(self, auth): ...
    def __lt__(self, auth): ...
    def __gt__(self, auth): ...
    def __le__(self, auth): ...
    def __ge__(self, auth): ...
    def __bool__(self) -> bool: ...

class BasicAuthentication(Authentication):
    def __init__(self, credentials, host, request_uri, headers, response, content, http) -> None: ...
    def request(self, method, request_uri, headers, content) -> None:
        """
        Modify the request headers to add the appropriate
        Authorization header.
        """
        ...

class DigestAuthentication(Authentication):
    """
    Only do qop='auth' and MD5, since that
    is all Apache currently implements
    """
    challenge: Any
    A1: Any
    def __init__(self, credentials, host, request_uri, headers, response, content, http) -> None: ...
    def request(self, method, request_uri, headers, content, cnonce: Incomplete | None = None):
        """Modify the request headers"""
        ...
    def response(self, response, content): ...

class HmacDigestAuthentication(Authentication):
    """Adapted from Robert Sayre's code and DigestAuthentication above."""
    challenge: Any
    hashmod: Any
    pwhashmod: Any
    key: Any
    __author__: ClassVar[str]
    def __init__(self, credentials, host, request_uri, headers, response, content, http) -> None: ...
    def request(self, method, request_uri, headers, content) -> None:
        """Modify the request headers"""
        ...
    def response(self, response, content): ...

class WsseAuthentication(Authentication):
    """
    This is thinly tested and should not be relied upon.
    At this time there isn't any third party server to test against.
    Blogger and TypePad implemented this algorithm at one point
    but Blogger has since switched to Basic over HTTPS and
    TypePad has implemented it wrong, by never issuing a 401
    challenge but instead requiring your client to telepathically know that
    their endpoint is expecting WSSE profile="UsernameToken".
    """
    def __init__(self, credentials, host, request_uri, headers, response, content, http) -> None: ...
    def request(self, method, request_uri, headers, content) -> None:
        """
        Modify the request headers to add the appropriate
        Authorization header.
        """
        ...

class GoogleLoginAuthentication(Authentication):
    Auth: str
    def __init__(self, credentials, host, request_uri, headers, response, content, http) -> None: ...
    def request(self, method, request_uri, headers, content) -> None:
        """
        Modify the request headers to add the appropriate
        Authorization header.
        """
        ...

class FileCache:
    """
    Uses a local directory as a store for cached files.
    Not really safe to use if multiple threads or processes are going to
    be running on the same cache.
    """
    cache: Any
    safe: Any
    def __init__(self, cache, safe=...) -> None: ...
    def get(self, key): ...
    def set(self, key, value) -> None: ...
    def delete(self, key) -> None: ...

class Credentials:
    credentials: Any
    def __init__(self) -> None: ...
    def add(self, name, password, domain: str = "") -> None: ...
    def clear(self) -> None: ...
    def iter(self, domain) -> Generator[tuple[str, str], None, None]: ...

class KeyCerts(Credentials):
    """
    Identical to Credentials except that
    name/password are mapped to key/cert.
    """
    def add(self, key, cert, domain, password) -> None: ...  # type: ignore[override]
    def iter(self, domain) -> Generator[tuple[str, str, str], None, None]: ...  # type: ignore[override]

class AllHosts: ...

class ProxyInfo:
    """Collect information required to use a proxy."""
    bypass_hosts: Any
    def __init__(
        self,
        proxy_type,
        proxy_host,
        proxy_port,
        proxy_rdns: bool = True,
        proxy_user: Incomplete | None = None,
        proxy_pass: Incomplete | None = None,
        proxy_headers: Incomplete | None = None,
    ) -> None:
        """
        Args:

        proxy_type: The type of proxy server.  This must be set to one of
        socks.PROXY_TYPE_XXX constants.  For example:  p =
        ProxyInfo(proxy_type=socks.PROXY_TYPE_HTTP, proxy_host='localhost',
        proxy_port=8000)
        proxy_host: The hostname or IP address of the proxy server.
        proxy_port: The port that the proxy server is running on.
        proxy_rdns: If True (default), DNS queries will not be performed
        locally, and instead, handed to the proxy to resolve.  This is useful
        if the network does not allow resolution of non-local names. In
        httplib2 0.9 and earlier, this defaulted to False.
        proxy_user: The username used to authenticate with the proxy server.
        proxy_pass: The password used to authenticate with the proxy server.
        proxy_headers: Additional or modified headers for the proxy connect
        request.
        """
        ...
    def astuple(self): ...
    def isgood(self): ...
    def applies_to(self, hostname): ...
    def bypass_host(self, hostname):
        """Has this host been excluded from the proxy config"""
        ...

class HTTPConnectionWithTimeout(http.client.HTTPConnection):
    """
    HTTPConnection subclass that supports timeouts

    HTTPConnection subclass that supports timeouts

    All timeouts are in seconds. If None is passed for timeout then
    Python's default timeout for sockets will be used. See for example
    the docs of socket.setdefaulttimeout():
    http://docs.python.org/library/socket.html#socket.setdefaulttimeout
    """
    proxy_info: Any
    def __init__(
        self, host, port: Incomplete | None = None, timeout: Incomplete | None = None, proxy_info: Incomplete | None = None
    ) -> None: ...
    sock: Any
    def connect(self) -> None:
        """Connect to the host and port specified in __init__."""
        ...

class HTTPSConnectionWithTimeout(http.client.HTTPSConnection):
    """
    This class allows communication via SSL.

    All timeouts are in seconds. If None is passed for timeout then
    Python's default timeout for sockets will be used. See for example
    the docs of socket.setdefaulttimeout():
    http://docs.python.org/library/socket.html#socket.setdefaulttimeout
    """
    disable_ssl_certificate_validation: Any
    ca_certs: Any
    proxy_info: Any
    key_file: Any
    cert_file: Any
    key_password: Any
    def __init__(
        self,
        host,
        port: Incomplete | None = None,
        key_file: Incomplete | None = None,
        cert_file: Incomplete | None = None,
        timeout: Incomplete | None = None,
        proxy_info: Incomplete | None = None,
        ca_certs: Incomplete | None = None,
        disable_ssl_certificate_validation: bool = False,
        tls_maximum_version: Incomplete | None = None,
        tls_minimum_version: Incomplete | None = None,
        key_password: Incomplete | None = None,
    ) -> None: ...
    sock: Any
    def connect(self) -> None:
        """Connect to a host on a given (SSL) port."""
        ...

class Http:
    """
    An HTTP client that handles:

    - all methods
    - caching
    - ETags
    - compression,
    - HTTPS
    - Basic
    - Digest
    - WSSE

    and more.
    """
    proxy_info: Any
    ca_certs: Any
    disable_ssl_certificate_validation: Any
    tls_maximum_version: Any
    tls_minimum_version: Any
    connections: Any
    cache: Any
    credentials: Any
    certificates: Any
    authorizations: Any
    follow_redirects: bool
    redirect_codes: Any
    optimistic_concurrency_methods: Any
    safe_methods: Any
    follow_all_redirects: bool
    ignore_etag: bool
    force_exception_to_status_code: bool
    timeout: Any
    forward_authorization_headers: bool
    def __init__(
        self,
        cache: Incomplete | None = None,
        timeout: Incomplete | None = None,
        proxy_info=...,
        ca_certs: Incomplete | None = None,
        disable_ssl_certificate_validation: bool = False,
        tls_maximum_version: Incomplete | None = None,
        tls_minimum_version: Incomplete | None = None,
    ) -> None:
        """
        If 'cache' is a string then it is used as a directory name for
        a disk cache. Otherwise it must be an object that supports the
        same interface as FileCache.

        All timeouts are in seconds. If None is passed for timeout
        then Python's default timeout for sockets will be used. See
        for example the docs of socket.setdefaulttimeout():
        http://docs.python.org/library/socket.html#socket.setdefaulttimeout

        `proxy_info` may be:
          - a callable that takes the http scheme ('http' or 'https') and
            returns a ProxyInfo instance per request. By default, uses
            proxy_info_from_environment.
          - a ProxyInfo instance (static proxy config).
          - None (proxy disabled).

        ca_certs is the path of a file containing root CA certificates for SSL
        server certificate validation.  By default, a CA cert file bundled with
        httplib2 is used.

        If disable_ssl_certificate_validation is true, SSL cert validation will
        not be performed.

        tls_maximum_version / tls_minimum_version require Python 3.7+ /
        OpenSSL 1.1.0g+. A value of "TLSv1_3" requires OpenSSL 1.1.1+.
        """
        ...
    def close(self) -> None:
        """
        Close persistent connections, clear sensitive data.
        Not thread-safe, requires external synchronization against concurrent requests.
        """
        ...
    def add_credentials(self, name, password, domain: str = "") -> None:
        """
        Add a name and password that will be used
        any time a request requires authentication.
        """
        ...
    def add_certificate(self, key, cert, domain, password: Incomplete | None = None) -> None:
        """
        Add a key and cert that will be used
        any time a request requires authentication.
        """
        ...
    def clear_credentials(self) -> None:
        """
        Remove all the names and passwords
        that are used for authentication
        """
        ...
    def request(
        self,
        uri,
        method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        redirections=5,
        connection_type: Incomplete | None = None,
    ):
        """
        Performs a single HTTP request.
        The 'uri' is the URI of the HTTP resource and can begin
        with either 'http' or 'https'. The value of 'uri' must be an absolute URI.

        The 'method' is the HTTP method to perform, such as GET, POST, DELETE, etc.
        There is no restriction on the methods allowed.

        The 'body' is the entity body to be sent with the request. It is a string
        object.

        Any extra headers that are to be sent with the request should be provided in the
        'headers' dictionary.

        The maximum number of redirect to follow before raising an
        exception is 'redirections. The default is 5.

        The return value is a tuple of (response, content), the first
        being and instance of the 'Response' class, the second being
        a string that contains the response entity body.
        
        """
        ...

class Response(dict[str, Any]):
    """An object more like email.message than httplib.HTTPResponse."""
    fromcache: bool
    version: int
    status: int
    reason: str
    previous: Any
    def __init__(self, info) -> None: ...
    @property
    def dict(self) -> Self: ...
