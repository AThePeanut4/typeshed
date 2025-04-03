from _typeshed import ConvertibleToInt, Incomplete
from collections.abc import Callable
from typing import Final, Literal
from typing_extensions import TypeAlias

from oauthlib.common import _HTTPMethod
from oauthlib.oauth2.rfc6749.tokens import OAuth2Token

_TokenPlacement: TypeAlias = Literal["auth_header", "query", "body"]

AUTH_HEADER: Final[_TokenPlacement]
URI_QUERY: Final[_TokenPlacement]
BODY: Final[_TokenPlacement]
FORM_ENC_HEADERS: Final[dict[str, str]]

class Client:
    """
    Base OAuth2 client responsible for access token management.

    This class also acts as a generic interface providing methods common to all
    client types such as ``prepare_authorization_request`` and
    ``prepare_token_revocation_request``. The ``prepare_x_request`` methods are
    the recommended way of interacting with clients (as opposed to the abstract
    prepare uri/body/etc methods). They are recommended over the older set
    because they are easier to use (more consistent) and add a few additional
    security checks, such as HTTPS and state checking.

    Some of these methods require further implementation only provided by the
    specific purpose clients such as
    :py:class:`oauthlib.oauth2.MobileApplicationClient` and thus you should always
    seek to use the client class matching the OAuth workflow you need. For
    Python, this is usually :py:class:`oauthlib.oauth2.WebApplicationClient`.
    """
    refresh_token_key: str
    client_id: str
    default_token_placement: _TokenPlacement
    token_type: str
    access_token: str | None
    refresh_token: str | None
    mac_key: str | bytes | bytearray | None
    mac_algorithm: str | None
    token: dict[str, Incomplete]
    scope: str | set[object] | tuple[object] | list[object]
    state_generator: Callable[[], str]
    state: str | None
    redirect_url: str | None
    code: Incomplete
    expires_in: ConvertibleToInt | None
    code_verifier: str | None
    code_challenge: str | None
    code_challenge_method: str | None
    def __init__(
        self,
        client_id: str,
        default_token_placement: _TokenPlacement = "auth_header",
        token_type: str = "Bearer",
        access_token: str | None = None,
        refresh_token: str | None = None,
        mac_key: str | bytes | bytearray | None = None,
        mac_algorithm: str | None = None,
        token: dict[str, Incomplete] | None = None,
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        state: str | None = None,
        redirect_url: str | None = None,
        state_generator: Callable[[], str] = ...,
        code_verifier: str | None = None,
        code_challenge: str | None = None,
        code_challenge_method: str | None = None,
        **kwargs,
    ) -> None:
        """
        Initialize a client with commonly used attributes.

        :param client_id: Client identifier given by the OAuth provider upon
        registration.

        :param default_token_placement: Tokens can be supplied in the Authorization
        header (default), the URL query component (``query``) or the request
        body (``body``).

        :param token_type: OAuth 2 token type. Defaults to Bearer. Change this
        if you specify the ``access_token`` parameter and know it is of a
        different token type, such as a MAC, JWT or SAML token. Can
        also be supplied as ``token_type`` inside the ``token`` dict parameter.

        :param access_token: An access token (string) used to authenticate
        requests to protected resources. Can also be supplied inside the
        ``token`` dict parameter.

        :param refresh_token: A refresh token (string) used to refresh expired
        tokens. Can also be supplied inside the ``token`` dict parameter.

        :param mac_key: Encryption key used with MAC tokens.

        :param mac_algorithm:  Hashing algorithm for MAC tokens.

        :param token: A dict of token attributes such as ``access_token``,
        ``token_type`` and ``expires_at``.

        :param scope: A list of default scopes to request authorization for.

        :param state: A CSRF protection string used during authorization.

        :param redirect_url: The redirection endpoint on the client side to which
        the user returns after authorization.

        :param state_generator: A no argument state generation callable. Defaults
        to :py:meth:`oauthlib.common.generate_token`.

        :param code_verifier: PKCE parameter. A cryptographically random string that is used to correlate the
        authorization request to the token request.

        :param code_challenge: PKCE parameter. A challenge derived from the code verifier that is sent in the
        authorization request, to be verified against later.

        :param code_challenge_method: PKCE parameter. A method that was used to derive code challenge.
        Defaults to "plain" if not present in the request.
        """
        ...
    @property
    def token_types(
        self,
    ) -> dict[
        Literal["Bearer", "MAC"],
        Callable[
            [str, str, str | None, dict[str, str] | None, str | None, Incomplete], tuple[str, dict[str, str] | None, str | None]
        ],
    ]: ...
    def prepare_request_uri(self, *args, **kwargs) -> str: ...
    def prepare_request_body(self, *args, **kwargs) -> str: ...
    def parse_request_uri_response(self, *args, **kwargs) -> dict[str, str]: ...
    def add_token(
        self,
        uri: str,
        http_method: _HTTPMethod = "GET",
        body: str | None = None,
        headers: dict[str, str] | None = None,
        token_placement: _TokenPlacement | None = None,
        **kwargs,
    ) -> tuple[str, dict[str, str] | None, str | None]: ...
    def prepare_authorization_request(
        self,
        authorization_url: str,
        state: str | None = None,
        redirect_url: str | None = None,
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        **kwargs,
    ) -> tuple[str, dict[str, str], str]: ...
    def prepare_token_request(
        self,
        token_url: str,
        authorization_response: str | None = None,
        redirect_url: str | None = None,
        state: str | None = None,
        body: str = "",
        **kwargs,
    ) -> tuple[str, dict[str, str], str]: ...
    def prepare_refresh_token_request(
        self,
        token_url: str,
        refresh_token: str | None = None,
        body: str = "",
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        **kwargs,
    ) -> tuple[str, dict[str, str], str]: ...
    def prepare_token_revocation_request(
        self,
        revocation_url,
        token,
        token_type_hint: Literal["access_token", "refresh_token"] | None = "access_token",
        body: str = "",
        callback: Callable[[Incomplete], Incomplete] | None = None,
        **kwargs,
    ): ...
    def parse_request_body_response(
        self, body: str, scope: str | set[object] | tuple[object] | list[object] | None = None, **kwargs
    ) -> OAuth2Token: ...
    def prepare_refresh_body(
        self,
        body: str = "",
        refresh_token: str | None = None,
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        **kwargs,
    ) -> str: ...
    def create_code_verifier(self, length: int) -> str: ...
    def create_code_challenge(self, code_verifier: str, code_challenge_method: str | None = None) -> str: ...
    def populate_code_attributes(self, response: dict[str, Incomplete]) -> None: ...
    def populate_token_attributes(self, response: dict[str, Incomplete]) -> None: ...
