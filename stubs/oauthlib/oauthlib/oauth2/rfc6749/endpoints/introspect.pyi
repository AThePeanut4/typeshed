"""
oauthlib.oauth2.rfc6749.endpoint.introspect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An implementation of the OAuth 2.0 `Token Introspection`.

.. _`Token Introspection`: https://tools.ietf.org/html/rfc7662
"""

from _typeshed import Incomplete
from logging import Logger
from typing import Any

from oauthlib.common import Request, _HTTPMethod

from .base import BaseEndpoint

log: Logger

class IntrospectEndpoint(BaseEndpoint):
    """
    Introspect token endpoint.

    This endpoint defines a method to query an OAuth 2.0 authorization
    server to determine the active state of an OAuth 2.0 token and to
    determine meta-information about this token. OAuth 2.0 deployments
    can use this method to convey information about the authorization
    context of the token from the authorization server to the protected
    resource.

    To prevent the values of access tokens from leaking into
    server-side logs via query parameters, an authorization server
    offering token introspection MAY disallow the use of HTTP GET on
    the introspection endpoint and instead require the HTTP POST method
    to be used at the introspection endpoint.
    """
    valid_token_types: Any
    valid_request_methods: Any
    request_validator: Any
    supported_token_types: Any
    def __init__(self, request_validator, supported_token_types: Incomplete | None = None) -> None: ...
    def create_introspect_response(
        self, uri: str, http_method: _HTTPMethod = "POST", body: str | None = None, headers: dict[str, str] | None = None
    ): ...
    def validate_introspect_request(self, request: Request) -> None: ...
