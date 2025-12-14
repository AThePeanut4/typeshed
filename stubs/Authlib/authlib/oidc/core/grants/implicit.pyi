from _typeshed import Incomplete
from logging import Logger

from authlib.oauth2.client import OAuth2Client
from authlib.oauth2.rfc6749 import ImplicitGrant
from authlib.oidc.core import UserInfo

log: Logger

class OpenIDImplicitGrant(ImplicitGrant):
    RESPONSE_TYPES: Incomplete
    DEFAULT_RESPONSE_MODE: str
    def exists_nonce(self, nonce, request) -> bool:
        """
        Check if the given nonce is existing in your database. Developers
        should implement this method in subclass, e.g.::

            def exists_nonce(self, nonce, request):
                exists = AuthorizationCode.query.filter_by(
                    client_id=request.payload.client_id, nonce=nonce
                ).first()
                return bool(exists)

        :param nonce: A string of "nonce" parameter in request
        :param request: OAuth2Request instance
        :return: Boolean
        """
        ...
    def get_jwt_config(self, client: OAuth2Client) -> dict[str, Incomplete]:
        """
        Get the JWT configuration for OpenIDImplicitGrant. The JWT
        configuration will be used to generate ``id_token``. Developers
        MUST implement this method in subclass, e.g.::

            def get_jwt_config(self, client):
                return {
                    "key": read_private_key_file(key_path),
                    "alg": client.id_token_signed_response_alg or "RS256",
                    "iss": "issuer-identity",
                    "exp": 3600,
                }

        :param client: OAuth2 client instance
        :return: dict
        """
        ...
    def generate_user_info(self, user, scope) -> UserInfo:
        """
        Provide user information for the given scope. Developers
        MUST implement this method in subclass, e.g.::

            from authlib.oidc.core import UserInfo


            def generate_user_info(self, user, scope):
                user_info = UserInfo(sub=user.id, name=user.name)
                if "email" in scope:
                    user_info["email"] = user.email
                return user_info

        :param user: user instance
        :param scope: scope of the token
        :return: ``authlib.oidc.core.UserInfo`` instance
        """
        ...
    def get_audiences(self, request):
        """
        Parse `aud` value for id_token, default value is client id. Developers
        MAY rewrite this method to provide a customized audience value.
        """
        ...
    def validate_authorization_request(self) -> str: ...
    def validate_consent_request(self) -> str: ...
    def create_authorization_response(self, redirect_uri, grant_user): ...
    def create_granted_params(self, grant_user): ...
    def process_implicit_token(self, token, code=None): ...
