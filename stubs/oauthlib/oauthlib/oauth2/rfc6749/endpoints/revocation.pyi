"""
oauthlib.oauth2.rfc6749.endpoint.revocation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An implementation of the OAuth 2 `Token Revocation`_ spec (draft 11).

.. _`Token Revocation`: https://tools.ietf.org/html/draft-ietf-oauth-revocation-11
"""

from _typeshed import Incomplete
from logging import Logger
from typing import Any

from oauthlib.common import Request, _HTTPMethod

from .base import BaseEndpoint

log: Logger

class RevocationEndpoint(BaseEndpoint):
    """
    Token revocation endpoint.

    Endpoint used by authenticated clients to revoke access and refresh tokens.
    Commonly this will be part of the Authorization Endpoint.
    """
    valid_token_types: Any
    valid_request_methods: Any
    request_validator: Any
    supported_token_types: Any
    enable_jsonp: Any
    def __init__(
        self, request_validator, supported_token_types: Incomplete | None = None, enable_jsonp: bool = False
    ) -> None: ...
    def create_revocation_response(
        self, uri: str, http_method: _HTTPMethod = "POST", body: str | None = None, headers: dict[str, str] | None = None
    ): ...
    def validate_revocation_request(self, request: Request) -> None: ...
