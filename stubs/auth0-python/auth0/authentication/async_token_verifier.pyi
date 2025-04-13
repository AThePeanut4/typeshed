from .. import TokenValidationError as TokenValidationError
from ..rest_async import AsyncRestClient as AsyncRestClient
from .token_verifier import (
    AsymmetricSignatureVerifier as AsymmetricSignatureVerifier,
    JwksFetcher as JwksFetcher,
    TokenVerifier as TokenVerifier,
)

class AsyncAsymmetricSignatureVerifier(AsymmetricSignatureVerifier):
    """
    Async verifier for RSA signatures, which rely on public key certificates.

    Args:
        jwks_url (str): The url where the JWK set is located.
        algorithm (str, optional): The expected signing algorithm. Defaults to "RS256".
    """
    def __init__(self, jwks_url: str, algorithm: str = "RS256") -> None: ...
    def set_session(self, session) -> None:
        """
        Set Client Session to improve performance by reusing session.

        Args:
            session (aiohttp.ClientSession): The client session which should be closed
                manually or within context manager.
        """
        ...

class AsyncJwksFetcher(JwksFetcher):
    """
    Class that async fetches and holds a JSON web key set.
    This class makes use of an in-memory cache. For it to work properly, define this instance once and re-use it.

    Args:
        jwks_url (str): The url where the JWK set is located.
        cache_ttl (str, optional): The lifetime of the JWK set cache in seconds. Defaults to 600 seconds.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def set_session(self, session) -> None:
        """
        Set Client Session to improve performance by reusing session.

        Args:
            session (aiohttp.ClientSession): The client session which should be closed
                manually or within context manager.
        """
        ...
    async def get_key(self, key_id: str):
        """
        Obtains the JWK associated with the given key id.

        Args:
            key_id (str): The id of the key to fetch.

        Returns:
            the JWK associated with the given key id.

        Raises:
            TokenValidationError: when a key with that id cannot be found
        """
        ...

class AsyncTokenVerifier(TokenVerifier):
    iss: str
    aud: str
    leeway: int
    def __init__(
        self, signature_verifier: AsyncAsymmetricSignatureVerifier, issuer: str, audience: str, leeway: int = 0
    ) -> None: ...
    def set_session(self, session) -> None:
        """
        Set Client Session to improve performance by reusing session.

        Args:
            session (aiohttp.ClientSession): The client session which should be closed
                manually or within context manager.
        """
        ...
