from types import TracebackType
from typing_extensions import Self

from auth0.rest import RestClientOptions as RestClientOptions

from ..asyncify import asyncify as asyncify
from .auth0 import Auth0 as Auth0

class AsyncAuth0:
    """
    Provides easy access to all endpoint classes

    Args:
        domain (str): Your Auth0 domain, for example 'username.auth0.com'

        token (str): Management API v2 Token

        rest_options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries.
            (defaults to None)
    """
    def __init__(self, domain: str, token: str, rest_options: RestClientOptions | None = None) -> None: ...
    def set_session(self, session) -> None:
        """
        Set Client Session to improve performance by reusing session.

        Args:
            session (aiohttp.ClientSession): The client session which should be closed
                manually or within context manager.
        """
        ...
    async def __aenter__(self) -> Self:
        """Automatically create and set session within context manager."""
        ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        """Automatically close session within context manager."""
        ...
