"""
authlib.oauth2.rfc6750.validator.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate Bearer Token for in request, scope and token.
"""

from authlib.oauth2.rfc6749 import TokenValidator

class BearerTokenValidator(TokenValidator):
    TOKEN_TYPE: str
    def authenticate_token(self, token_string): ...
    def validate_token(self, token, scopes, request) -> None: ...
