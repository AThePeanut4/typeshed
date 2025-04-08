"""
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
"""

from _typeshed import Incomplete
from collections.abc import Callable

from .base import Client, _TokenPlacement

class ServiceApplicationClient(Client):
    """
    A public client utilizing the JWT bearer grant.

    JWT bearer tokes can be used to request an access token when a client
    wishes to utilize an existing trust relationship, expressed through the
    semantics of (and digital signature or keyed message digest calculated
    over) the JWT, without a direct user approval step at the authorization
    server.

    This grant type does not involve an authorization step. It may be
    used by both public and confidential clients.
    """
    grant_type: str
    private_key: str | None
    subject: str | None
    issuer: str | None
    audience: str | None
    def __init__(
        self,
        client_id: str,
        private_key: str | None = None,
        subject: str | None = None,
        issuer: str | None = None,
        audience: str | None = None,
        *,
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
        Initialize a JWT client with defaults for implicit use later.

        :param client_id: Client identifier given by the OAuth provider upon
                          registration.

        :param private_key: Private key used for signing and encrypting.
                            Must be given as a string.

        :param subject: The principal that is the subject of the JWT, i.e.
                        which user is the token requested on behalf of.
                        For example, ``foo@example.com.

        :param issuer: The JWT MUST contain an "iss" (issuer) claim that
                       contains a unique identifier for the entity that issued
                       the JWT. For example, ``your-client@provider.com``.

        :param audience: A value identifying the authorization server as an
                         intended audience, e.g.
                         ``https://provider.com/oauth2/token``.

        :param kwargs: Additional arguments to pass to base client, such as
                       state and token. See ``Client.__init__.__doc__`` for
                       details.
        """
        ...
    def prepare_request_body(
        self,
        private_key: str | None = None,
        subject: str | None = None,
        issuer: str | None = None,
        audience: str | None = None,
        expires_at: float | None = None,
        issued_at: float | None = None,
        extra_claims: dict[str, Incomplete] | None = None,
        body: str = "",
        scope: str | set[object] | tuple[object] | list[object] | None = None,
        include_client_id: bool = False,
        *,
        not_before: int | None = None,
        jwt_id: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        **kwargs,
    ) -> str: ...
