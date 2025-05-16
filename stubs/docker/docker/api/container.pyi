import datetime
from _typeshed import Incomplete
from typing import Any, Literal, TypedDict, overload, type_check_only
from typing_extensions import TypeAlias

from docker._types import WaitContainerResponse
from docker.types.daemon import CancellableStream

from ..types import ContainerConfig, EndpointConfig, HostConfig, NetworkingConfig

@type_check_only
class _HasId(TypedDict):
    Id: str

@type_check_only
class _HasID(TypedDict):
    ID: str

_Container: TypeAlias = _HasId | _HasID | str

class ContainerApiMixin:
    def attach(
        self,
        container: _Container,
        stdout: bool = True,
        stderr: bool = True,
        stream: bool = False,
        logs: bool = False,
        demux: bool = False,
    ): ...
    def attach_socket(self, container: _Container, params=None, ws: bool = False): ...
    def commit(
        self,
        container: _Container,
        repository: str | None = None,
        tag: str | None = None,
        message=None,
        author=None,
        pause: bool = True,
        changes=None,
        conf=None,
    ): ...
    def containers(
        self,
        quiet: bool = False,
        all: bool = False,
        trunc: bool = False,
        latest: bool = False,
        since: str | None = None,
        before: str | None = None,
        limit: int = -1,
        size: bool = False,
        filters=None,
    ): ...
    def create_container(
        self,
        image,
        command: str | list[str] | None = None,
        hostname: str | None = None,
        user: str | int | None = None,
        detach: bool = False,
        stdin_open: bool = False,
        tty: bool = False,
        # list is invariant, enumerating all possible union combination would be too complex for:
        # list[str | int | tuple[int | str, str] | tuple[int | str, ...]]
        ports: dict[str, dict[Incomplete, Incomplete]] | list[Any] | None = None,
        environment: dict[str, str] | list[str] | None = None,
        volumes: str | list[str] | None = None,
        network_disabled: bool = False,
        name: str | None = None,
        entrypoint: str | list[str] | None = None,
        working_dir: str | None = None,
        domainname: str | None = None,
        host_config=None,
        mac_address: str | None = None,
        labels: dict[str, str] | list[str] | None = None,
        stop_signal: str | None = None,
        networking_config=None,
        healthcheck=None,
        stop_timeout: int | None = None,
        runtime: str | None = None,
        use_config_proxy: bool = True,
        platform: str | None = None,
    ):
        """
        Creates a container. Parameters are similar to those for the ``docker
        run`` command except it doesn't support the attach options (``-a``).

        The arguments that are passed directly to this function are
        host-independent configuration options. Host-specific configuration
        is passed with the `host_config` argument. You'll normally want to
        use this method in combination with the :py:meth:`create_host_config`
        method to generate ``host_config``.

        **Port bindings**

        Port binding is done in two parts: first, provide a list of ports to
        open inside the container with the ``ports`` parameter, then declare
        bindings with the ``host_config`` parameter. For example:

        .. code-block:: python

            container_id = client.api.create_container(
                'busybox', 'ls', ports=[1111, 2222],
                host_config=client.api.create_host_config(port_bindings={
                    1111: 4567,
                    2222: None
                })
            )


        You can limit the host address on which the port will be exposed like
        such:

        .. code-block:: python

            client.api.create_host_config(
                port_bindings={1111: ('127.0.0.1', 4567)}
            )

        Or without host port assignment:

        .. code-block:: python

            client.api.create_host_config(port_bindings={1111: ('127.0.0.1',)})

        If you wish to use UDP instead of TCP (default), you need to declare
        ports as such in both the config and host config:

        .. code-block:: python

            container_id = client.api.create_container(
                'busybox', 'ls', ports=[(1111, 'udp'), 2222],
                host_config=client.api.create_host_config(port_bindings={
                    '1111/udp': 4567, 2222: None
                })
            )

        To bind multiple host ports to a single container port, use the
        following syntax:

        .. code-block:: python

            client.api.create_host_config(port_bindings={
                1111: [1234, 4567]
            })

        You can also bind multiple IPs to a single container port:

        .. code-block:: python

            client.api.create_host_config(port_bindings={
                1111: [
                    ('192.168.0.100', 1234),
                    ('192.168.0.101', 1234)
                ]
            })

        **Using volumes**

        Volume declaration is done in two parts. Provide a list of
        paths to use as mountpoints inside the container with the
        ``volumes`` parameter, and declare mappings from paths on the host
        in the ``host_config`` section.

        .. code-block:: python

            container_id = client.api.create_container(
                'busybox', 'ls', volumes=['/mnt/vol1', '/mnt/vol2'],
                host_config=client.api.create_host_config(binds={
                    '/home/user1/': {
                        'bind': '/mnt/vol2',
                        'mode': 'rw',
                    },
                    '/var/www': {
                        'bind': '/mnt/vol1',
                        'mode': 'ro',
                    },
                    '/autofs/user1': {
                        'bind': '/mnt/vol3',
                        'mode': 'rw',
                        'propagation': 'shared'
                    }
                })
            )

        You can alternatively specify binds as a list. This code is equivalent
        to the example above:

        .. code-block:: python

            container_id = client.api.create_container(
                'busybox', 'ls', volumes=['/mnt/vol1', '/mnt/vol2', '/mnt/vol3'],
                host_config=client.api.create_host_config(binds=[
                    '/home/user1/:/mnt/vol2',
                    '/var/www:/mnt/vol1:ro',
                    '/autofs/user1:/mnt/vol3:rw,shared',
                ])
            )

        **Networking**

        You can specify networks to connect the container to by using the
        ``networking_config`` parameter. At the time of creation, you can
        only connect a container to a single networking, but you
        can create more connections by using
        :py:meth:`~connect_container_to_network`.

        For example:

        .. code-block:: python

            networking_config = client.api.create_networking_config({
                'network1': client.api.create_endpoint_config(
                    ipv4_address='172.28.0.124',
                    aliases=['foo', 'bar'],
                    links=['container2']
                )
            })

            ctnr = client.api.create_container(
                img, command, networking_config=networking_config
            )

        Args:
            image (str): The image to run
            command (str or list): The command to be run in the container
            hostname (str): Optional hostname for the container
            user (str or int): Username or UID
            detach (bool): Detached mode: run container in the background and
                return container ID
            stdin_open (bool): Keep STDIN open even if not attached
            tty (bool): Allocate a pseudo-TTY
            ports (list of ints): A list of port numbers
            environment (dict or list): A dictionary or a list of strings in
                the following format ``["PASSWORD=xxx"]`` or
                ``{"PASSWORD": "xxx"}``.
            volumes (str or list): List of paths inside the container to use
                as volumes.
            network_disabled (bool): Disable networking
            name (str): A name for the container
            entrypoint (str or list): An entrypoint
            working_dir (str): Path to the working directory
            domainname (str): The domain name to use for the container
            host_config (dict): A dictionary created with
                :py:meth:`create_host_config`.
            mac_address (str): The Mac Address to assign the container
            labels (dict or list): A dictionary of name-value labels (e.g.
                ``{"label1": "value1", "label2": "value2"}``) or a list of
                names of labels to set with empty values (e.g.
                ``["label1", "label2"]``)
            stop_signal (str): The stop signal to use to stop the container
                (e.g. ``SIGINT``).
            stop_timeout (int): Timeout to stop the container, in seconds.
                Default: 10
            networking_config (dict): A networking configuration generated
                by :py:meth:`create_networking_config`.
            runtime (str): Runtime to use with this container.
            healthcheck (dict): Specify a test to perform to check that the
                container is healthy.
            use_config_proxy (bool): If ``True``, and if the docker client
                configuration file (``~/.docker/config.json`` by default)
                contains a proxy configuration, the corresponding environment
                variables will be set in the container being created.
            platform (str): Platform in the format ``os[/arch[/variant]]``.

        Returns:
            A dictionary with an image 'Id' key and a 'Warnings' key.

        Raises:
            :py:class:`docker.errors.ImageNotFound`
                If the specified image does not exist.
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def create_container_config(self, *args, **kwargs) -> ContainerConfig: ...
    def create_container_from_config(self, config, name=None, platform=None): ...
    def create_host_config(self, *args, **kwargs) -> HostConfig: ...
    def create_networking_config(self, *args, **kwargs) -> NetworkingConfig: ...
    def create_endpoint_config(self, *args, **kwargs) -> EndpointConfig: ...
    def diff(self, container: _Container) -> list[dict[Incomplete, Incomplete]]: ...
    def export(self, container: _Container, chunk_size: int | None = 2097152): ...
    def get_archive(
        self, container: _Container, path, chunk_size: int | None = 2097152, encode_stream: bool = False
    ) -> tuple[Incomplete, Incomplete]:
        """
        Retrieve a file or folder from a container in the form of a tar
        archive.

        Args:
            container (str): The container where the file is located
            path (str): Path to the file or folder to retrieve
            chunk_size (int): The number of bytes returned by each iteration
                of the generator. If ``None``, data will be streamed as it is
                received. Default: 2 MB
            encode_stream (bool): Determines if data should be encoded
                (gzip-compressed) during transmission. Default: False

        Returns:
            (tuple): First element is a raw tar data stream. Second element is
            a dict containing ``stat`` information on the specified ``path``.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> c = docker.APIClient()
            >>> f = open('./sh_bin.tar', 'wb')
            >>> bits, stat = c.api.get_archive(container, '/bin/sh')
            >>> print(stat)
            {'name': 'sh', 'size': 1075464, 'mode': 493,
             'mtime': '2018-10-01T15:37:48-07:00', 'linkTarget': ''}
            >>> for chunk in bits:
            ...    f.write(chunk)
            >>> f.close()
        """
        ...
    def inspect_container(self, container: _Container):
        """
        Identical to the `docker inspect` command, but only for containers.

        Args:
            container (str): The container to inspect

        Returns:
            (dict): Similar to the output of `docker inspect`, but as a
            single dict

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def kill(self, container: _Container, signal: str | int | None = None) -> None:
        """
        Kill a container or send a signal to a container.

        Args:
            container (str): The container to kill
            signal (str or int): The signal to send. Defaults to ``SIGKILL``

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    @overload
    def logs(
        self,
        container: _Container,
        stdout: bool = True,
        stderr: bool = True,
        *,
        stream: Literal[True],
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> CancellableStream[bytes]:
        """
        Get logs from a container. Similar to the ``docker logs`` command.

        The ``stream`` parameter makes the ``logs`` function return a blocking
        generator you can iterate over to retrieve log output as it happens.

        Args:
            container (str): The container to get logs from
            stdout (bool): Get ``STDOUT``. Default ``True``
            stderr (bool): Get ``STDERR``. Default ``True``
            stream (bool): Stream the response. Default ``False``
            timestamps (bool): Show timestamps. Default ``False``
            tail (str or int): Output specified number of lines at the end of
                logs. Either an integer of number of lines or the string
                ``all``. Default ``all``
            since (datetime, int, or float): Show logs since a given datetime,
                integer epoch (in seconds) or float (in fractional seconds)
            follow (bool): Follow log output. Default ``False``
            until (datetime, int, or float): Show logs that occurred before
                the given datetime, integer epoch (in seconds), or
                float (in fractional seconds)

        Returns:
            (generator of bytes or bytes)

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    @overload
    def logs(
        self,
        container: _Container,
        stdout: bool,
        stderr: bool,
        stream: Literal[True],
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> CancellableStream[bytes]:
        """
        Get logs from a container. Similar to the ``docker logs`` command.

        The ``stream`` parameter makes the ``logs`` function return a blocking
        generator you can iterate over to retrieve log output as it happens.

        Args:
            container (str): The container to get logs from
            stdout (bool): Get ``STDOUT``. Default ``True``
            stderr (bool): Get ``STDERR``. Default ``True``
            stream (bool): Stream the response. Default ``False``
            timestamps (bool): Show timestamps. Default ``False``
            tail (str or int): Output specified number of lines at the end of
                logs. Either an integer of number of lines or the string
                ``all``. Default ``all``
            since (datetime, int, or float): Show logs since a given datetime,
                integer epoch (in seconds) or float (in fractional seconds)
            follow (bool): Follow log output. Default ``False``
            until (datetime, int, or float): Show logs that occurred before
                the given datetime, integer epoch (in seconds), or
                float (in fractional seconds)

        Returns:
            (generator of bytes or bytes)

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    @overload
    def logs(
        self,
        container: _Container,
        stdout: bool = True,
        stderr: bool = True,
        stream: Literal[False] = False,
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> bytes: ...
    def pause(self, container: _Container) -> None: ...
    def port(self, container: _Container, private_port: int): ...
    def put_archive(self, container: _Container, path: str, data) -> bool: ...
    def prune_containers(self, filters=None): ...
    def remove_container(self, container: _Container, v: bool = False, link: bool = False, force: bool = False) -> None: ...
    def rename(self, container: _Container, name: str) -> None: ...
    def resize(self, container: _Container, height: int, width: int) -> None: ...
    def restart(self, container: _Container, timeout: int = 10) -> None: ...
    def start(self, container: _Container) -> None: ...
    def stats(self, container: _Container, decode: bool | None = None, stream: bool = True, one_shot: bool | None = None): ...
    def stop(self, container: _Container, timeout: int | None = None) -> None: ...
    def top(self, container: _Container, ps_args: str | None = None) -> str: ...
    def unpause(self, container: _Container) -> None: ...
    def update_container(
        self,
        container: _Container,
        blkio_weight: int | None = None,
        cpu_period: int | None = None,
        cpu_quota: int | None = None,
        cpu_shares: int | None = None,
        cpuset_cpus: str | None = None,
        cpuset_mems: str | None = None,
        mem_limit: float | str | None = None,
        mem_reservation: float | str | None = None,
        memswap_limit: int | str | None = None,
        kernel_memory: int | str | None = None,
        restart_policy=None,
    ): ...
    def wait(
        self,
        container: _Container,
        timeout: int | None = None,
        condition: Literal["not-running", "next-exit", "removed"] | None = None,
    ) -> WaitContainerResponse:
        """
        Block until a container stops, then return its exit code. Similar to
        the ``docker wait`` command.

        Args:
            container (str or dict): The container to wait on. If a dict, the
                ``Id`` key is used.
            timeout (int): Request timeout
            condition (str): Wait until a container state reaches the given
                condition, either ``not-running`` (default), ``next-exit``,
                or ``removed``

        Returns:
            (dict): The API's response as a Python dictionary, including
                the container's exit code under the ``StatusCode`` attribute.

        Raises:
            :py:class:`requests.exceptions.ReadTimeout`
                If the timeout is exceeded.
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
