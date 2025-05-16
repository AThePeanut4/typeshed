from _typeshed import Incomplete
from collections.abc import Mapping

from authlib.oauth2.rfc6749 import ClientMixin

class OAuth2Request:
    method: str
    uri: str
    body: Mapping[str, str] | None
    headers: Mapping[str, str] | None
    client: ClientMixin | None
    auth_method: str | None
    user: Incomplete | None
    authorization_code: Incomplete | None
    refresh_token: Incomplete | None
    credential: Incomplete | None
    def __init__(
        self, method: str, uri: str, body: Mapping[str, str] | None = None, headers: Mapping[str, str] | None = None
    ) -> None: ...
    @property
    def args(self) -> dict[str, str | None]: ...
    @property
    def form(self) -> dict[str, str]: ...
    @property
    def data(self) -> dict[str, str]: ...
    @property
    def datalist(self) -> dict[str, list[Incomplete]]:
        """
        Return all the data in query parameters and the body of the request as a dictionary
        with all the values in lists.
        """
        ...
    @property
    def client_id(self) -> str:
        """
        The authorization server issues the registered client a client
        identifier -- a unique string representing the registration
        information provided by the client. The value is extracted from
        request.

        :return: string
        """
        ...
    @property
    def response_type(self) -> str: ...
    @property
    def grant_type(self) -> str: ...
    @property
    def redirect_uri(self) -> str: ...
    @property
    def scope(self) -> str: ...
    @property
    def state(self) -> str | None: ...

class JsonRequest:
    method: Incomplete
    uri: Incomplete
    body: Incomplete
    headers: Incomplete
    def __init__(self, method, uri, body=None, headers=None) -> None: ...
    @property
    def data(self): ...
