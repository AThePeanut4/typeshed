"""
oauthlib.common
~~~~~~~~~~~~~~

This module provides data structures and utilities common
to all implementations of OAuth.
"""

from _typeshed import Incomplete
from typing import Any

UNICODE_ASCII_CHARACTER_SET: str
CLIENT_ID_CHARACTER_SET: str
SANITIZE_PATTERN: Any
INVALID_HEX_PATTERN: Any
always_safe: str
log: Any

def quote(s, safe: bytes = b"/"): ...
def unquote(s): ...
def urlencode(params): ...
def encode_params_utf8(params):
    """
    Ensures that all parameters in a list of 2-element tuples are encoded to
    bytestrings using UTF-8
    """
    ...
def decode_params_utf8(params):
    """
    Ensures that all parameters in a list of 2-element tuples are decoded to
    unicode using UTF-8.
    """
    ...

urlencoded: Any

def urldecode(query):
    """
    Decode a query string in x-www-form-urlencoded format into a sequence
    of two-element tuples.

    Unlike urlparse.parse_qsl(..., strict_parsing=True) urldecode will enforce
    correct formatting of the query string by validation. If validation fails
    a ValueError will be raised. urllib.parse_qsl will only raise errors if
    any of name-value pairs omits the equals sign.
    """
    ...
def extract_params(raw):
    """
    Extract parameters and return them as a list of 2-tuples.

    Will successfully extract parameters from urlencoded query strings,
    dicts, or lists of 2-tuples. Empty strings/dicts/lists will return an
    empty list of parameters. Any other input will result in a return
    value of None.
    """
    ...
def generate_nonce():
    """
    Generate pseudorandom nonce that is unlikely to repeat.

    Per `section 3.3`_ of the OAuth 1 RFC 5849 spec.
    Per `section 3.2.1`_ of the MAC Access Authentication spec.

    A random 64-bit number is appended to the epoch timestamp for both
    randomness and to decrease the likelihood of collisions.

    .. _`section 3.2.1`: https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01#section-3.2.1
    .. _`section 3.3`: https://tools.ietf.org/html/rfc5849#section-3.3
    """
    ...
def generate_timestamp():
    """
    Get seconds since epoch (UTC).

    Per `section 3.3`_ of the OAuth 1 RFC 5849 spec.
    Per `section 3.2.1`_ of the MAC Access Authentication spec.

    .. _`section 3.2.1`: https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01#section-3.2.1
    .. _`section 3.3`: https://tools.ietf.org/html/rfc5849#section-3.3
    """
    ...
def generate_token(length: int = 30, chars=...):
    """
    Generates a non-guessable OAuth token

    OAuth (1 and 2) does not specify the format of tokens except that they
    should be strings of random characters. Tokens should not be guessable
    and entropy when generating the random characters is important. Which is
    why SystemRandom is used instead of the default random.choice method.
    """
    ...
def generate_signed_token(private_pem, request): ...
def verify_signed_token(public_pem, token): ...
def generate_client_id(length: int = 30, chars=...):
    """
    Generates an OAuth client_id

    OAuth 2 specify the format of client_id in
    https://tools.ietf.org/html/rfc6749#appendix-A.
    """
    ...
def add_params_to_qs(query, params):
    """Extend a query with a list of two-tuples."""
    ...
def add_params_to_uri(uri, params, fragment: bool = False):
    """Add a list of two-tuples to the uri query components."""
    ...
def safe_string_equals(a, b):
    """
    Near-constant time string comparison.

    Used in order to avoid timing attacks on sensitive information such
    as secret keys during request verification (`rootLabs`_).

    .. _`rootLabs`: http://rdist.root.org/2010/01/07/timing-independent-array-comparison/
    """
    ...
def to_unicode(data, encoding: str = "UTF-8"):
    """Convert a number of different types of objects to unicode."""
    ...

class CaseInsensitiveDict(dict[Any, Any]):
    """Basic case insensitive dict with strings only keys."""
    proxy: Any
    def __init__(self, data) -> None: ...
    def __contains__(self, k): ...
    def __delitem__(self, k) -> None: ...
    def __getitem__(self, k): ...
    def get(self, k, default: Incomplete | None = None): ...
    def __setitem__(self, k, v) -> None: ...
    def update(self, *args, **kwargs) -> None: ...

class Request:
    """
    A malleable representation of a signable HTTP request.

    Body argument may contain any data, but parameters will only be decoded if
    they are one of:

    * urlencoded query string
    * dict
    * list of 2-tuples

    Anything else will be treated as raw body data to be passed through
    unmolested.
    """
    uri: Any
    http_method: Any
    headers: Any
    body: Any
    decoded_body: Any
    oauth_params: Any
    validator_log: Any
    def __init__(
        self,
        uri,
        http_method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        encoding: str = "utf-8",
    ): ...
    def __getattr__(self, name: str): ...
    @property
    def uri_query(self): ...
    @property
    def uri_query_params(self): ...
    @property
    def duplicate_params(self): ...
