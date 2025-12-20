"""
authlib.oauth2.rfc6749.resource_protector.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Accessing Protected Resources per `Section 7`_.

.. _`Section 7`: https://tools.ietf.org/html/rfc6749#section-7
"""

from _typeshed import Incomplete

class TokenValidator:
    """
    Base token validator class. Subclass this validator to register
    into ResourceProtector instance.
    """
    TOKEN_TYPE: str
    realm: Incomplete
    extra_attributes: Incomplete
    def __init__(self, realm=None, **extra_attributes) -> None: ...
    @staticmethod
    def scope_insufficient(token_scopes, required_scopes): ...
    def authenticate_token(self, token_string): ...
    def validate_request(self, request) -> None: ...
    def validate_token(self, token, scopes, request) -> None: ...

class ResourceProtector:
    def __init__(self) -> None: ...
    def register_token_validator(self, validator: TokenValidator):
        """
        Register a token validator for a given Authorization type.
        Authlib has a built-in BearerTokenValidator per rfc6750.
        """
        ...
    def get_token_validator(self, token_type):
        """Get token validator from registry for the given token type."""
        ...
    def parse_request_authorization(self, request):
        """
        Parse the token and token validator from request Authorization header.
        Here is an example of Authorization header::

            Authorization: Bearer a-token-string

        This method will parse this header, if it can find the validator for
        ``Bearer``, it will return the validator and ``a-token-string``.

        :return: validator, token_string
        :raise: MissingAuthorizationError
        :raise: UnsupportedTokenTypeError
        """
        ...
    def validate_request(self, scopes, request, **kwargs):
        """Validate the request and return a token."""
        ...
