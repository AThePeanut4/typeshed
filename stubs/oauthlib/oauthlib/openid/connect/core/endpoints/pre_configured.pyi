"""
oauthlib.openid.connect.core.endpoints.pre_configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various endpoints needed
for providing OpenID Connect servers.
"""

from _typeshed import Incomplete
from typing import Any

from oauthlib.oauth2.rfc6749.endpoints import (
    AuthorizationEndpoint as AuthorizationEndpoint,
    IntrospectEndpoint as IntrospectEndpoint,
    ResourceEndpoint as ResourceEndpoint,
    RevocationEndpoint as RevocationEndpoint,
    TokenEndpoint as TokenEndpoint,
)

from .userinfo import UserInfoEndpoint as UserInfoEndpoint

class Server(AuthorizationEndpoint, IntrospectEndpoint, TokenEndpoint, ResourceEndpoint, RevocationEndpoint, UserInfoEndpoint):
    """An all-in-one endpoint featuring all four major grant types."""
    auth_grant: Any
    implicit_grant: Any
    password_grant: Any
    credentials_grant: Any
    refresh_grant: Any
    openid_connect_auth: Any
    openid_connect_implicit: Any
    openid_connect_hybrid: Any
    bearer: Any
    jwt: Any
    auth_grant_choice: Any
    implicit_grant_choice: Any
    token_grant_choice: Any
    def __init__(
        self,
        request_validator,
        token_expires_in: Incomplete | None = None,
        token_generator: Incomplete | None = None,
        refresh_token_generator: Incomplete | None = None,
        *args,
        **kwargs,
    ) -> None:
        """
        Construct a new all-grants-in-one server.

        :param request_validator: An implementation of
                                  oauthlib.oauth2.RequestValidator.
        :param token_expires_in: An int or a function to generate a token
                                 expiration offset (in seconds) given a
                                 oauthlib.common.Request object.
        :param token_generator: A function to generate a token from a request.
        :param refresh_token_generator: A function to generate a token from a
                                        request for the refresh token.
        :param kwargs: Extra parameters to pass to authorization-,
                       token-, resource-, and revocation-endpoint constructors.
        """
        ...
