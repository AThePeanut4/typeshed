from authlib.oauth2.rfc6749 import AuthorizationCodeMixin as _AuthorizationCodeMixin

class AuthorizationCodeMixin(_AuthorizationCodeMixin):
    def get_nonce(self) -> str | None:
        """Get "nonce" value of the authorization code object."""
        ...
    def get_auth_time(self) -> int | None:
        """Get "auth_time" value of the authorization code object."""
        ...
