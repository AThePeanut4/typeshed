from _typeshed import Incomplete

from auth0.exceptions import RateLimitError as RateLimitError
from auth0.types import RequestData as RequestData

from .rest import (
    EmptyResponse as EmptyResponse,
    JsonResponse as JsonResponse,
    PlainResponse as PlainResponse,
    Response as Response,
    RestClient as RestClient,
)

class AsyncRestClient(RestClient):
    """
    Provides simple methods for handling all RESTful api endpoints.

    Args:
        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
        options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries. Overrides matching
            options passed to the constructor.
            (defaults to 3)
    """
    timeout: Incomplete
    def set_session(self, session) -> None: ...
    async def get(self, url: str, params: dict[str, Incomplete] | None = None, headers: dict[str, str] | None = None): ...
    async def post(self, url: str, data: RequestData | None = None, headers: dict[str, str] | None = None): ...
    async def file_post(self, *args, **kwargs): ...
    async def patch(self, url: str, data: RequestData | None = None): ...
    async def put(self, url: str, data: RequestData | None = None): ...
    async def delete(self, url: str, params: dict[str, Incomplete] | None = None, data: RequestData | None = None): ...

class RequestsResponse:
    status_code: int
    headers: Incomplete
    text: str
    def __init__(self, response, text: str) -> None: ...
