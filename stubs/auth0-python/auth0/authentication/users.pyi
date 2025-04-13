from _typeshed import Incomplete

from auth0.rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from auth0.types import TimeoutType as TimeoutType

class Users:
    domain: str
    protocol: str
    client: RestClient
    def __init__(self, domain: str, telemetry: bool = True, timeout: TimeoutType = 5.0, protocol: str = "https") -> None: ...
    def userinfo(self, access_token: str) -> dict[str, Incomplete]:
        """
        Returns the user information based on the Auth0 access token.
        This endpoint will work only if openid was granted as a scope for the access_token.

        Args:
            access_token (str): Auth0 access token (obtained during login).

        Returns:
            The user profile.
        """
        ...
