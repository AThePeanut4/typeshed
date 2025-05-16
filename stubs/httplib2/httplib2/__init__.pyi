"""Small, fast HTTP client library for Python."""

import http.client
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
    def request(self, method, request_uri, headers, content, cnonce=None): ...
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
        self, proxy_type, proxy_host, proxy_port, proxy_rdns: bool = True, proxy_user=None, proxy_pass=None, proxy_headers=None
    ) -> None: ...
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
    def __init__(self, host, port=None, timeout=None, proxy_info=None) -> None: ...
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
        port=None,
        key_file=None,
        cert_file=None,
        timeout=None,
        proxy_info=None,
        ca_certs=None,
        disable_ssl_certificate_validation: bool = False,
        tls_maximum_version=None,
        tls_minimum_version=None,
        key_password=None,
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
        cache=None,
        timeout=None,
        proxy_info=...,
        ca_certs=None,
        disable_ssl_certificate_validation: bool = False,
        tls_maximum_version=None,
        tls_minimum_version=None,
    ) -> None: ...
    def close(self) -> None: ...
    def add_credentials(self, name, password, domain: str = "") -> None: ...
    def add_certificate(self, key, cert, domain, password=None) -> None: ...
    def clear_credentials(self) -> None: ...
    def request(self, uri, method: str = "GET", body=None, headers=None, redirections=5, connection_type=None): ...

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

__all__ = [
    "debuglevel",
    "FailedToDecompressContent",
    "Http",
    "HttpLib2Error",
    "ProxyInfo",
    "RedirectLimit",
    "RedirectMissingLocation",
    "Response",
    "RETRIES",
    "UnimplementedDigestAuthOptionError",
    "UnimplementedHmacDigestAuthOptionError",
]
