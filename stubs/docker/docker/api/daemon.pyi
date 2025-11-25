from datetime import datetime
from typing import Any, Literal, overload

from docker.types.daemon import CancellableStream

class DaemonApiMixin:
    def df(self) -> dict[str, Any]: ...
    @overload
    def events(
        self,
        since: datetime | int | None = None,
        until: datetime | int | None = None,
        filters: dict[str, Any] | None = None,
        decode: Literal[False] | None = None,
    ) -> CancellableStream[str]: ...
    @overload
    def events(
        self,
        since: datetime | int | None = None,
        until: datetime | int | None = None,
        filters: dict[str, Any] | None = None,
        decode: Literal[True] = ...,
    ) -> CancellableStream[dict[str, Any]]: ...
    def info(self) -> dict[str, Any]: ...
    def login(
        self,
        username: str,
        password: str | None = None,
        email: str | None = None,
        registry: str | None = None,
        reauth: bool = False,
        dockercfg_path: str | None = None,
    ) -> dict[str, Any]:
        """
        Authenticate with a registry. Similar to the ``docker login`` command.

        Args:
            username (str): The registry username
            password (str): The plaintext password
            email (str): The email for the registry account
            registry (str): URL to the registry.  E.g.
                ``https://index.docker.io/v1/``
            reauth (bool): Whether or not to refresh existing authentication on
                the Docker server.
            dockercfg_path (str): Use a custom path for the Docker config file
                (default ``$HOME/.docker/config.json`` if present,
                otherwise ``$HOME/.dockercfg``)

        Returns:
            (dict): The response from the login request

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def ping(self) -> bool:
        """
        Checks the server is responsive. An exception will be raised if it
        isn't responding.

        Returns:
            (bool) The response from the server.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def version(self, api_version: bool = True) -> dict[str, Any]:
        """
        Returns version information from the server. Similar to the ``docker
        version`` command.

        Returns:
            (dict): The server version information

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
