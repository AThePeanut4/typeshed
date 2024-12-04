from _typeshed import Incomplete
from collections.abc import Mapping, Sequence

import requests
from docker.tls import TLSConfig
from requests.adapters import BaseAdapter

from .build import BuildApiMixin
from .config import ConfigApiMixin
from .container import ContainerApiMixin
from .daemon import DaemonApiMixin
from .exec_api import ExecApiMixin
from .image import ImageApiMixin
from .network import NetworkApiMixin
from .plugin import PluginApiMixin
from .secret import SecretApiMixin
from .service import ServiceApiMixin
from .swarm import SwarmApiMixin
from .volume import VolumeApiMixin

class APIClient(
    requests.Session,
    BuildApiMixin,
    ConfigApiMixin,
    ContainerApiMixin,
    DaemonApiMixin,
    ExecApiMixin,
    ImageApiMixin,
    NetworkApiMixin,
    PluginApiMixin,
    SecretApiMixin,
    ServiceApiMixin,
    SwarmApiMixin,
    VolumeApiMixin,
):
    """
    A low-level client for the Docker Engine API.

    Example:

        >>> import docker
        >>> client = docker.APIClient(base_url='unix://var/run/docker.sock')
        >>> client.version()
        {u'ApiVersion': u'1.33',
         u'Arch': u'amd64',
         u'BuildTime': u'2017-11-19T18:46:37.000000000+00:00',
         u'GitCommit': u'f4ffd2511c',
         u'GoVersion': u'go1.9.2',
         u'KernelVersion': u'4.14.3-1-ARCH',
         u'MinAPIVersion': u'1.12',
         u'Os': u'linux',
         u'Version': u'17.10.0-ce'}

    Args:
        base_url (str): URL to the Docker server. For example,
            ``unix:///var/run/docker.sock`` or ``tcp://127.0.0.1:1234``.
        version (str): The version of the API to use. Set to ``auto`` to
            automatically detect the server's version. Default: ``1.35``
        timeout (int): Default timeout for API calls, in seconds.
        tls (bool or :py:class:`~docker.tls.TLSConfig`): Enable TLS. Pass
            ``True`` to enable it with default options, or pass a
            :py:class:`~docker.tls.TLSConfig` object to use custom
            configuration.
        user_agent (str): Set a custom user agent for requests to the server.
        credstore_env (dict): Override environment variables when calling the
            credential store process.
        use_ssh_client (bool): If set to `True`, an ssh connection is made
            via shelling out to the ssh client. Ensure the ssh client is
            installed and configured on the host.
        max_pool_size (int): The maximum number of connections
            to save in the pool.
    """
    __attrs__: Sequence[str]
    base_url: str
    timeout: int
    credstore_env: Mapping[Incomplete, Incomplete] | None
    def __init__(
        self,
        base_url: str | None = None,
        version: str | None = None,
        timeout: int = 60,
        tls: bool | TLSConfig = False,
        user_agent: str = ...,
        num_pools: int | None = None,
        credstore_env: Mapping[Incomplete, Incomplete] | None = None,
        use_ssh_client: bool = False,
        max_pool_size: int = 10,
    ) -> None: ...
    def get_adapter(self, url: str) -> BaseAdapter: ...
    @property
    def api_version(self) -> str: ...
    def reload_config(self, dockercfg_path: str | None = None) -> None:
        """
        Force a reload of the auth configuration

        Args:
            dockercfg_path (str): Use a custom path for the Docker config file
                (default ``$HOME/.docker/config.json`` if present,
                otherwise ``$HOME/.dockercfg``)

        Returns:
            None
        """
        ...
