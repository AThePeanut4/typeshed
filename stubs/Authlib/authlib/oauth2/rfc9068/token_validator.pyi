"""
authlib.oauth2.rfc9068.token_validator.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of Validating JWT Access Tokens per `Section 4`_.

.. _`Section 7`: https://www.rfc-editor.org/rfc/rfc9068.html#name-validating-jwt-access-token
"""

from _typeshed import Incomplete

from authlib.oauth2.rfc6750 import BearerTokenValidator

class JWTBearerTokenValidator(BearerTokenValidator):
    """
    JWTBearerTokenValidator can protect your resource server endpoints.

    :param issuer: The issuer from which tokens will be accepted.
    :param resource_server: An identifier for the current resource server,
        which must appear in the JWT ``aud`` claim.

    Developers needs to implement the missing methods::

        class MyJWTBearerTokenValidator(JWTBearerTokenValidator):
            def get_jwks(self): ...


        require_oauth = ResourceProtector()
        require_oauth.register_token_validator(
            MyJWTBearerTokenValidator(
                issuer="https://authorization-server.example.org",
                resource_server="https://resource-server.example.org",
            )
        )

    You can then protect resources depending on the JWT `scope`, `groups`,
    `roles` or `entitlements` claims::

        @require_oauth(
            scope="profile",
            groups="admins",
            roles="student",
            entitlements="captain",
        )
        def resource_endpoint(): ...
    """
    issuer: Incomplete
    resource_server: Incomplete
    def __init__(self, issuer, resource_server, *args, **kwargs) -> None: ...
    def get_jwks(self): ...
    def validate_iss(self, claims, iss: str) -> bool: ...
    def authenticate_token(self, token_string): ...
    def validate_token(self, token, scopes, request, groups=None, roles=None, entitlements=None) -> None: ...
