"""InfluxDBClientAsync is client for API defined in https://github.com/influxdata/openapi/blob/master/contracts/oss.yml."""

from _typeshed import Incomplete
from types import TracebackType
from typing_extensions import Self

from influxdb_client.client._base import _BaseClient
from influxdb_client.client.delete_api_async import DeleteApiAsync
from influxdb_client.client.query_api import QueryOptions
from influxdb_client.client.query_api_async import QueryApiAsync
from influxdb_client.client.write_api import PointSettings
from influxdb_client.client.write_api_async import WriteApiAsync

logger: Incomplete

class InfluxDBClientAsync(_BaseClient):
    """InfluxDBClientAsync is client for InfluxDB v2."""
    api_client: Incomplete
    def __init__(
        self,
        url: str,
        token: str | None = None,
        org: str | None = None,
        debug: bool | None = None,
        timeout: int = 10000,
        enable_gzip: bool = False,
        *,
        verify_ssl: bool = ...,
        ssl_ca_cert: Incomplete | None = ...,
        cert_file: Incomplete | None = ...,
        cert_key_file: Incomplete | None = ...,
        cert_key_password: Incomplete | None = ...,
        ssl_context: Incomplete | None = ...,
        proxy: Incomplete | None = ...,
        proxy_headers: Incomplete | None = ...,
        connection_pool_maxsize: int = ...,
        username: Incomplete | None = ...,
        password: Incomplete | None = ...,
        auth_basic: bool = ...,
        retries: bool | Incomplete = ...,
        profilers: Incomplete | None = ...,
    ) -> None:
        """
        Initialize defaults.

        :param url: InfluxDB server API url (ex. http://localhost:8086).
        :param token: ``token`` to authenticate to the InfluxDB 2.x
        :param org: organization name (used as a default in Query, Write and Delete API)
        :param debug: enable verbose logging of http requests
        :param timeout: The maximal number of milliseconds for the whole HTTP request including
                        connection establishment, request sending and response reading.
                        It can also be a :class:`~aiohttp.ClientTimeout` which is directly pass to ``aiohttp``.
        :param enable_gzip: Enable Gzip compression for http requests. Currently, only the "Write" and "Query" endpoints
                            supports the Gzip compression.
        :key bool verify_ssl: Set this to false to skip verifying SSL certificate when calling API from https server.
        :key str ssl_ca_cert: Set this to customize the certificate file to verify the peer.
        :key str cert_file: Path to the certificate that will be used for mTLS authentication.
        :key str cert_key_file: Path to the file contains private key for mTLS certificate.
        :key str cert_key_password: String or function which returns password for decrypting the mTLS private key.
        :key ssl.SSLContext ssl_context: Specify a custom Python SSL Context for the TLS/ mTLS handshake.
                                         Be aware that only delivered certificate/ key files or an SSL Context are
                                         possible.
        :key str proxy: Set this to configure the http proxy to be used (ex. http://localhost:3128)
        :key str proxy_headers: A dictionary containing headers that will be sent to the proxy. Could be used for proxy
                                authentication.
        :key int connection_pool_maxsize: The total number of simultaneous connections.
                                          Defaults to "multiprocessing.cpu_count() * 5".
        :key bool auth_basic: Set this to true to enable basic authentication when talking to a InfluxDB 1.8.x that
                              does not use auth-enabled but is protected by a reverse proxy with basic authentication.
                              (defaults to false, don't set to true when talking to InfluxDB 2)
        :key str username: ``username`` to authenticate via username and password credentials to the InfluxDB 2.x
        :key str password: ``password`` to authenticate via username and password credentials to the InfluxDB 2.x
        :key bool allow_redirects: If set to ``False``, do not follow HTTP redirects. ``True`` by default.
        :key int max_redirects: Maximum number of HTTP redirects to follow. ``10`` by default.
        :key dict client_session_kwargs: Additional configuration arguments for :class:`~aiohttp.ClientSession`
        :key type client_session_type: Type of aiohttp client to use. Useful for third party wrappers like
                                       ``aiohttp-retry``. :class:`~aiohttp.ClientSession` by default.
        :key list[str] profilers: list of enabled Flux profilers
        """
        ...
    async def __aenter__(self) -> Self:
        """
        Enter the runtime context related to this object.

        return: self instance
        """
        ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        """Shutdown the client."""
        ...
    async def close(self) -> None:
        """Shutdown the client."""
        ...
    @classmethod
    def from_config_file(
        cls, config_file: str = "config.ini", debug: Incomplete | None = None, enable_gzip: bool = False, **kwargs
    ):
        """
        Configure client via configuration file. The configuration has to be under 'influx' section.

        :param config_file: Path to configuration file
        :param debug: Enable verbose logging of http requests
        :param enable_gzip: Enable Gzip compression for http requests. Currently, only the "Write" and "Query" endpoints
                            supports the Gzip compression.
        :key config_name: Name of the configuration section of the configuration file
        :key str proxy_headers: A dictionary containing headers that will be sent to the proxy. Could be used for proxy
                                authentication.
        :key urllib3.util.retry.Retry retries: Set the default retry strategy that is used for all HTTP requests
                                               except batching writes. As a default there is no one retry strategy.
        :key ssl.SSLContext ssl_context: Specify a custom Python SSL Context for the TLS/ mTLS handshake.
                                         Be aware that only delivered certificate/ key files or an SSL Context are
                                         possible.

        The supported formats:
            - https://docs.python.org/3/library/configparser.html
            - https://toml.io/en/
            - https://www.json.org/json-en.html

        Configuration options:
            - url
            - org
            - token
            - timeout,
            - verify_ssl
            - ssl_ca_cert
            - cert_file
            - cert_key_file
            - cert_key_password
            - connection_pool_maxsize
            - auth_basic
            - profilers
            - proxy


        config.ini example::

            [influx2]
            url=http://localhost:8086
            org=my-org
            token=my-token
            timeout=6000
            connection_pool_maxsize=25
            auth_basic=false
            profilers=query,operator
            proxy=http:proxy.domain.org:8080

            [tags]
            id = 132-987-655
            customer = California Miner
            data_center = ${env.data_center}

        config.toml example::

            [influx2]
                url = "http://localhost:8086"
                token = "my-token"
                org = "my-org"
                timeout = 6000
                connection_pool_maxsize = 25
                auth_basic = false
                profilers="query, operator"
                proxy = "http://proxy.domain.org:8080"

            [tags]
                id = "132-987-655"
                customer = "California Miner"
                data_center = "${env.data_center}"

        config.json example::

            {
                "url": "http://localhost:8086",
                "token": "my-token",
                "org": "my-org",
                "active": true,
                "timeout": 6000,
                "connection_pool_maxsize": 55,
                "auth_basic": false,
                "profilers": "query, operator",
                "tags": {
                    "id": "132-987-655",
                    "customer": "California Miner",
                    "data_center": "${env.data_center}"
                }
            }
        """
        ...
    @classmethod
    def from_env_properties(cls, debug: Incomplete | None = None, enable_gzip: bool = False, **kwargs):
        """
        Configure client via environment properties.

        :param debug: Enable verbose logging of http requests
        :param enable_gzip: Enable Gzip compression for http requests. Currently, only the "Write" and "Query" endpoints
                            supports the Gzip compression.
        :key str proxy: Set this to configure the http proxy to be used (ex. http://localhost:3128)
        :key str proxy_headers: A dictionary containing headers that will be sent to the proxy. Could be used for proxy
                                authentication.
        :key urllib3.util.retry.Retry retries: Set the default retry strategy that is used for all HTTP requests
                                               except batching writes. As a default there is no one retry strategy.
        :key ssl.SSLContext ssl_context: Specify a custom Python SSL Context for the TLS/ mTLS handshake.
                                         Be aware that only delivered certificate/ key files or an SSL Context are
                                         possible.


        Supported environment properties:
            - INFLUXDB_V2_URL
            - INFLUXDB_V2_ORG
            - INFLUXDB_V2_TOKEN
            - INFLUXDB_V2_TIMEOUT
            - INFLUXDB_V2_VERIFY_SSL
            - INFLUXDB_V2_SSL_CA_CERT
            - INFLUXDB_V2_CERT_FILE
            - INFLUXDB_V2_CERT_KEY_FILE
            - INFLUXDB_V2_CERT_KEY_PASSWORD
            - INFLUXDB_V2_CONNECTION_POOL_MAXSIZE
            - INFLUXDB_V2_AUTH_BASIC
            - INFLUXDB_V2_PROFILERS
            - INFLUXDB_V2_TAG
        """
        ...
    async def ping(self) -> bool:
        """
        Return the status of InfluxDB instance.

        :return: The status of InfluxDB.
        """
        ...
    async def version(self) -> str:
        """
        Return the version of the connected InfluxDB Server.

        :return: The version of InfluxDB.
        """
        ...
    async def build(self) -> str:
        """
        Return the build type of the connected InfluxDB Server.

        :return: The type of InfluxDB build.
        """
        ...
    def query_api(self, query_options: QueryOptions = ...) -> QueryApiAsync:
        """
        Create an asynchronous Query API instance.

        :param query_options: optional query api configuration
        :return: Query api instance
        """
        ...
    def write_api(self, point_settings: PointSettings = ...) -> WriteApiAsync:
        """
        Create an asynchronous Write API instance.

        Example:
            .. code-block:: python

                from influxdb_client_async import InfluxDBClientAsync


                # Initialize async/await instance of Write API
                async with InfluxDBClientAsync(url="http://localhost:8086", token="my-token", org="my-org") as client:
                    write_api = client.write_api()

        :param point_settings: settings to store default tags
        :return: write api instance
        """
        ...
    def delete_api(self) -> DeleteApiAsync:
        """
        Get the asynchronous delete metrics API instance.

        :return: delete api
        """
        ...
