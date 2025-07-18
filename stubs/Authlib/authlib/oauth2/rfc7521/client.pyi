from _typeshed import Incomplete

from authlib.oauth2 import OAuth2Error

class AssertionClient:
    """
    Constructs a new Assertion Framework for OAuth 2.0 Authorization Grants
    per RFC7521_.

    .. _RFC7521: https://tools.ietf.org/html/rfc7521
    """
    DEFAULT_GRANT_TYPE: Incomplete
    ASSERTION_METHODS: Incomplete
    token_auth_class: Incomplete
    oauth_error_class = OAuth2Error
    session: Incomplete
    token_endpoint: Incomplete
    grant_type: Incomplete
    issuer: Incomplete
    subject: Incomplete
    audience: Incomplete
    claims: Incomplete
    scope: Incomplete
    token_auth: Incomplete
    leeway: Incomplete
    def __init__(
        self,
        session,
        token_endpoint,
        issuer,
        subject,
        audience=None,
        grant_type=None,
        claims=None,
        token_placement: str = "header",
        scope=None,
        leeway: int = 60,
        **kwargs,
    ) -> None: ...
    @property
    def token(self): ...
    @token.setter
    def token(self, token) -> None: ...
    def refresh_token(self):
        """
        Using Assertions as Authorization Grants to refresh token as
        described in `Section 4.1`_.

        .. _`Section 4.1`: https://tools.ietf.org/html/rfc7521#section-4.1
        """
        ...
    def parse_response_token(self, resp): ...
    def __del__(self) -> None: ...
