"""
oauthlib.oauth2.rfc6749.tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains methods for adding two types of access tokens to requests.

- Bearer https://tools.ietf.org/html/rfc6750
- MAC https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01
"""

from _typeshed import Incomplete
from typing import Any

class OAuth2Token(dict[Any, Any]):
    def __init__(self, params, old_scope: Incomplete | None = None) -> None: ...
    @property
    def scope_changed(self): ...
    @property
    def old_scope(self): ...
    @property
    def old_scopes(self): ...
    @property
    def scope(self): ...
    @property
    def scopes(self): ...
    @property
    def missing_scopes(self): ...
    @property
    def additional_scopes(self): ...

def prepare_mac_header(
    token,
    uri,
    key,
    http_method,
    nonce: Incomplete | None = None,
    headers: Incomplete | None = None,
    body: Incomplete | None = None,
    ext: str = "",
    hash_algorithm: str = "hmac-sha-1",
    issue_time: Incomplete | None = None,
    draft: int = 0,
):
    """
    Add an `MAC Access Authentication`_ signature to headers.

    Unlike OAuth 1, this HMAC signature does not require inclusion of the
    request payload/body, neither does it use a combination of client_secret
    and token_secret but rather a mac_key provided together with the access
    token.

    Currently two algorithms are supported, "hmac-sha-1" and "hmac-sha-256",
    `extension algorithms`_ are not supported.

    Example MAC Authorization header, linebreaks added for clarity

    Authorization: MAC id="h480djs93hd8",
                       nonce="1336363200:dj83hs9s",
                       mac="bhCQXTVyfj5cmA9uKkPFx1zeOXM="

    .. _`MAC Access Authentication`: https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01
    .. _`extension algorithms`: https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01#section-7.1

    :param token:
    :param uri: Request URI.
    :param key: MAC given provided by token endpoint.
    :param http_method: HTTP Request method.
    :param nonce:
    :param headers: Request headers as a dictionary.
    :param body:
    :param ext:
    :param hash_algorithm: HMAC algorithm provided by token endpoint.
    :param issue_time: Time when the MAC credentials were issued (datetime).
    :param draft: MAC authentication specification version.
    :return: headers dictionary with the authorization field added.
    """
    ...
def prepare_bearer_uri(token, uri):
    """
    Add a `Bearer Token`_ to the request URI.
    Not recommended, use only if client can't use authorization header or body.

    http://www.example.com/path?access_token=h480djs93hd8

    .. _`Bearer Token`: https://tools.ietf.org/html/rfc6750

    :param token:
    :param uri:
    """
    ...
def prepare_bearer_headers(token, headers: Incomplete | None = None):
    """
    Add a `Bearer Token`_ to the request URI.
    Recommended method of passing bearer tokens.

    Authorization: Bearer h480djs93hd8

    .. _`Bearer Token`: https://tools.ietf.org/html/rfc6750

    :param token:
    :param headers:
    """
    ...
def prepare_bearer_body(token, body: str = ""):
    """
    Add a `Bearer Token`_ to the request body.

    access_token=h480djs93hd8

    .. _`Bearer Token`: https://tools.ietf.org/html/rfc6750

    :param token:
    :param body:
    """
    ...
def random_token_generator(request, refresh_token: bool = False):
    """
    :param request: OAuthlib request.
    :type request: oauthlib.common.Request
    :param refresh_token:
    """
    ...
def signed_token_generator(private_pem, **kwargs):
    """:param private_pem:"""
    ...
def get_token_from_header(request):
    """
    Helper function to extract a token from the request header.

    :param request: OAuthlib request.
    :type request: oauthlib.common.Request
    :return: Return the token or None if the Authorization header is malformed.
    """
    ...

class TokenBase:
    def __call__(self, request, refresh_token: bool = False) -> None: ...
    def validate_request(self, request) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
        ...
    def estimate_type(self, request) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
        ...

class BearerToken(TokenBase):
    request_validator: Any
    token_generator: Any
    refresh_token_generator: Any
    expires_in: Any
    def __init__(
        self,
        request_validator: Incomplete | None = None,
        token_generator: Incomplete | None = None,
        expires_in: Incomplete | None = None,
        refresh_token_generator: Incomplete | None = None,
    ) -> None: ...
    def create_token(self, request, refresh_token: bool = False, **kwargs):
        """
        Create a BearerToken, by default without refresh token.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param refresh_token:
        """
        ...
    def validate_request(self, request):
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
        ...
    def estimate_type(self, request):
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
        ...
