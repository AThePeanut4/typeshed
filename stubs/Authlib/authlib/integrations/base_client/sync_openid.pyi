from _typeshed import Incomplete

class OpenIDMixin:
    def fetch_jwk_set(self, force: bool = False): ...
    def userinfo(self, **kwargs):
        """Fetch user info from ``userinfo_endpoint``."""
        ...
    def parse_id_token(self, token, nonce, claims_options: Incomplete | None = None, leeway: int = 120):
        """Return an instance of UserInfo from token's ``id_token``."""
        ...
    def create_load_key(self): ...
