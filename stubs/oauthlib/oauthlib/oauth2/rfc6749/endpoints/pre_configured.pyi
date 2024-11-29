"""
oauthlib.oauth2.rfc6749.endpoints.pre_configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various endpoints needed
for providing OAuth 2.0 RFC6749 servers.
"""

from _typeshed import Incomplete
from typing import Any

from .authorization import AuthorizationEndpoint as AuthorizationEndpoint
from .introspect import IntrospectEndpoint as IntrospectEndpoint
from .resource import ResourceEndpoint as ResourceEndpoint
from .revocation import RevocationEndpoint as RevocationEndpoint
from .token import TokenEndpoint as TokenEndpoint

class Server(AuthorizationEndpoint, IntrospectEndpoint, TokenEndpoint, ResourceEndpoint, RevocationEndpoint):
    """An all-in-one endpoint featuring all four major grant types."""
    auth_grant: Any
    implicit_grant: Any
    password_grant: Any
    credentials_grant: Any
    refresh_grant: Any
    bearer: Any
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

class WebApplicationServer(AuthorizationEndpoint, IntrospectEndpoint, TokenEndpoint, ResourceEndpoint, RevocationEndpoint):
    """An all-in-one endpoint featuring Authorization code grant and Bearer tokens."""
    auth_grant: Any
    refresh_grant: Any
    bearer: Any
    def __init__(
        self,
        request_validator,
        token_generator: Incomplete | None = None,
        token_expires_in: Incomplete | None = None,
        refresh_token_generator: Incomplete | None = None,
        **kwargs,
    ) -> None:
        """
        Construct a new web application server.

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

class MobileApplicationServer(AuthorizationEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint):
    """An all-in-one endpoint featuring Implicit code grant and Bearer tokens."""
    implicit_grant: Any
    bearer: Any
    def __init__(
        self,
        request_validator,
        token_generator: Incomplete | None = None,
        token_expires_in: Incomplete | None = None,
        refresh_token_generator: Incomplete | None = None,
        **kwargs,
    ) -> None:
        """
        Construct a new implicit grant server.

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

class LegacyApplicationServer(TokenEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint):
    """An all-in-one endpoint featuring Resource Owner Password Credentials grant and Bearer tokens."""
    password_grant: Any
    refresh_grant: Any
    bearer: Any
    def __init__(
        self,
        request_validator,
        token_generator: Incomplete | None = None,
        token_expires_in: Incomplete | None = None,
        refresh_token_generator: Incomplete | None = None,
        **kwargs,
    ) -> None:
        """
        Construct a resource owner password credentials grant server.

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

class BackendApplicationServer(TokenEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint):
    """An all-in-one endpoint featuring Client Credentials grant and Bearer tokens."""
    credentials_grant: Any
    bearer: Any
    def __init__(
        self,
        request_validator,
        token_generator: Incomplete | None = None,
        token_expires_in: Incomplete | None = None,
        refresh_token_generator: Incomplete | None = None,
        **kwargs,
    ) -> None:
        """
        Construct a client credentials grant server.

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
