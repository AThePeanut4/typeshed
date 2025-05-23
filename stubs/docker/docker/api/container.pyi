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
    ):
        """
        Attach to a container.

        The ``.logs()`` function is a wrapper around this method, which you can
        use instead if you want to fetch/stream container output without first
        retrieving the entire backlog.

        Args:
            container (str): The container to attach to.
            stdout (bool): Include stdout.
            stderr (bool): Include stderr.
            stream (bool): Return container output progressively as an iterator
                of strings, rather than a single string.
            logs (bool): Include the container's previous output.
            demux (bool): Keep stdout and stderr separate.

        Returns:
            By default, the container's output as a single string (two if
            ``demux=True``: one for stdout and one for stderr).

            If ``stream=True``, an iterator of output strings. If
            ``demux=True``, two iterators are returned: one for stdout and one
            for stderr.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def attach_socket(self, container: _Container, params=None, ws: bool = False):
        """
        Like ``attach``, but returns the underlying socket-like object for the
        HTTP request.

        Args:
            container (str): The container to attach to.
            params (dict): Dictionary of request parameters (e.g. ``stdout``,
                ``stderr``, ``stream``).
                For ``detachKeys``, ~/.docker/config.json is used by default.
            ws (bool): Use websockets instead of raw HTTP.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
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
    ):
        """
        Commit a container to an image. Similar to the ``docker commit``
        command.

        Args:
            container (str): The image hash of the container
            repository (str): The repository to push the image to
            tag (str): The tag to push
            message (str): A commit message
            author (str): The name of the author
            pause (bool): Whether to pause the container before committing
            changes (str): Dockerfile instructions to apply while committing
            conf (dict): The configuration for the container. See the
                `Engine API documentation
                <https://docs.docker.com/reference/api/docker_remote_api/>`_
                for full details.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
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
    ):
        """
        List containers. Similar to the ``docker ps`` command.

        Args:
            quiet (bool): Only display numeric Ids
            all (bool): Show all containers. Only running containers are shown
                by default
            trunc (bool): Truncate output
            latest (bool): Show only the latest created container, include
                non-running ones.
            since (str): Show only containers created since Id or Name, include
                non-running ones
            before (str): Show only container created before Id or Name,
                include non-running ones
            limit (int): Show `limit` last created containers, include
                non-running ones
            size (bool): Display sizes
            filters (dict): Filters to be processed on the image list.
                Available filters:

                - `exited` (int): Only containers with specified exit code
                - `status` (str): One of ``restarting``, ``running``,
                    ``paused``, ``exited``
                - `label` (str|list): format either ``"key"``, ``"key=value"``
                    or a list of such.
                - `id` (str): The id of the container.
                - `name` (str): The name of the container.
                - `ancestor` (str): Filter by container ancestor. Format of
                    ``<image-name>[:tag]``, ``<image-id>``, or
                    ``<image@digest>``.
                - `before` (str): Only containers created before a particular
                    container. Give the container name or id.
                - `since` (str): Only containers created after a particular
                    container. Give container name or id.

                A comprehensive list can be found in the documentation for
                `docker ps
                <https://docs.docker.com/engine/reference/commandline/ps>`_.

        Returns:
            A list of dicts, one per container

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
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
    def create_host_config(self, *args, **kwargs) -> HostConfig:
        """
        Create a dictionary for the ``host_config`` argument to
        :py:meth:`create_container`.

        Args:
            auto_remove (bool): enable auto-removal of the container on daemon
                side when the container's process exits.
            binds (dict): Volumes to bind. See :py:meth:`create_container`
                    for more information.
            blkio_weight_device: Block IO weight (relative device weight) in
                the form of: ``[{"Path": "device_path", "Weight": weight}]``.
            blkio_weight: Block IO weight (relative weight), accepts a weight
                value between 10 and 1000.
            cap_add (list of str): Add kernel capabilities. For example,
                ``["SYS_ADMIN", "MKNOD"]``.
            cap_drop (list of str): Drop kernel capabilities.
            cpu_period (int): The length of a CPU period in microseconds.
            cpu_quota (int): Microseconds of CPU time that the container can
                get in a CPU period.
            cpu_shares (int): CPU shares (relative weight).
            cpuset_cpus (str): CPUs in which to allow execution (``0-3``,
                ``0,1``).
            cpuset_mems (str): Memory nodes (MEMs) in which to allow execution
                (``0-3``, ``0,1``). Only effective on NUMA systems.
            device_cgroup_rules (:py:class:`list`): A list of cgroup rules to
                apply to the container.
            device_read_bps: Limit read rate (bytes per second) from a device
                in the form of: `[{"Path": "device_path", "Rate": rate}]`
            device_read_iops: Limit read rate (IO per second) from a device.
            device_write_bps: Limit write rate (bytes per second) from a
                device.
            device_write_iops: Limit write rate (IO per second) from a device.
            devices (:py:class:`list`): Expose host devices to the container,
                as a list of strings in the form
                ``<path_on_host>:<path_in_container>:<cgroup_permissions>``.

                For example, ``/dev/sda:/dev/xvda:rwm`` allows the container
                to have read-write access to the host's ``/dev/sda`` via a
                node named ``/dev/xvda`` inside the container.
            device_requests (:py:class:`list`): Expose host resources such as
                GPUs to the container, as a list of
                :py:class:`docker.types.DeviceRequest` instances.
            dns (:py:class:`list`): Set custom DNS servers.
            dns_opt (:py:class:`list`): Additional options to be added to the
                container's ``resolv.conf`` file
            dns_search (:py:class:`list`): DNS search domains.
            extra_hosts (dict): Additional hostnames to resolve inside the
                container, as a mapping of hostname to IP address.
            group_add (:py:class:`list`): List of additional group names and/or
                IDs that the container process will run as.
            init (bool): Run an init inside the container that forwards
                signals and reaps processes
            ipc_mode (str): Set the IPC mode for the container.
            isolation (str): Isolation technology to use. Default: ``None``.
            links (dict): Mapping of links using the
                ``{'container': 'alias'}`` format. The alias is optional.
                Containers declared in this dict will be linked to the new
                container using the provided alias. Default: ``None``.
            log_config (LogConfig): Logging configuration
            lxc_conf (dict): LXC config.
            mem_limit (float or str): Memory limit. Accepts float values
                (which represent the memory limit of the created container in
                bytes) or a string with a units identification char
                (``100000b``, ``1000k``, ``128m``, ``1g``). If a string is
                specified without a units character, bytes are assumed as an
            mem_reservation (float or str): Memory soft limit.
            mem_swappiness (int): Tune a container's memory swappiness
                behavior. Accepts number between 0 and 100.
            memswap_limit (str or int): Maximum amount of memory + swap a
                container is allowed to consume.
            mounts (:py:class:`list`): Specification for mounts to be added to
                the container. More powerful alternative to ``binds``. Each
                item in the list is expected to be a
                :py:class:`docker.types.Mount` object.
            network_mode (str): One of:

                - ``bridge`` Create a new network stack for the container on
                  the bridge network.
                - ``none`` No networking for this container.
                - ``container:<name|id>`` Reuse another container's network
                  stack.
                - ``host`` Use the host network stack.
                  This mode is incompatible with ``port_bindings``.

            oom_kill_disable (bool): Whether to disable OOM killer.
            oom_score_adj (int): An integer value containing the score given
                to the container in order to tune OOM killer preferences.
            pid_mode (str): If set to ``host``, use the host PID namespace
                inside the container.
            pids_limit (int): Tune a container's pids limit. Set ``-1`` for
                unlimited.
            port_bindings (dict): See :py:meth:`create_container`
                for more information.
                Imcompatible with ``host`` in ``network_mode``.
            privileged (bool): Give extended privileges to this container.
            publish_all_ports (bool): Publish all ports to the host.
            read_only (bool): Mount the container's root filesystem as read
                only.
            restart_policy (dict): Restart the container when it exits.
                Configured as a dictionary with keys:

                - ``Name`` One of ``on-failure``, or ``always``.
                - ``MaximumRetryCount`` Number of times to restart the
                  container on failure.
            security_opt (:py:class:`list`): A list of string values to
                customize labels for MLS systems, such as SELinux.
            shm_size (str or int): Size of /dev/shm (e.g. ``1G``).
            storage_opt (dict): Storage driver options per container as a
                key-value mapping.
            sysctls (dict): Kernel parameters to set in the container.
            tmpfs (dict): Temporary filesystems to mount, as a dictionary
                mapping a path inside the container to options for that path.

                For example:

                .. code-block:: python

                    {
                        '/mnt/vol2': '',
                        '/mnt/vol1': 'size=3G,uid=1000'
                    }

            ulimits (:py:class:`list`): Ulimits to set inside the container,
                as a list of :py:class:`docker.types.Ulimit` instances.
            userns_mode (str): Sets the user namespace mode for the container
                when user namespace remapping option is enabled. Supported
                values are: ``host``
            uts_mode (str): Sets the UTS namespace mode for the container.
                Supported values are: ``host``
            volumes_from (:py:class:`list`): List of container names or IDs to
                get volumes from.
            runtime (str): Runtime to use with this container.


        Returns:
            (dict) A dictionary which can be passed to the ``host_config``
            argument to :py:meth:`create_container`.

        Example:

            >>> client.api.create_host_config(
            ...     privileged=True,
            ...     cap_drop=['MKNOD'],
            ...     volumes_from=['nostalgic_newton'],
            ... )
            {'CapDrop': ['MKNOD'], 'LxcConf': None, 'Privileged': True,
            'VolumesFrom': ['nostalgic_newton'], 'PublishAllPorts': False}
        """
        ...
    def create_networking_config(self, *args, **kwargs) -> NetworkingConfig:
        """
        Create a networking config dictionary to be used as the
        ``networking_config`` parameter in :py:meth:`create_container`.

        Args:
            endpoints_config (dict): A dictionary mapping network names to
                endpoint configurations generated by
                :py:meth:`create_endpoint_config`.

        Returns:
            (dict) A networking config.

        Example:

            >>> client.api.create_network('network1')
            >>> networking_config = client.api.create_networking_config({
                'network1': client.api.create_endpoint_config()
            })
            >>> container = client.api.create_container(
                img, command, networking_config=networking_config
            )
        """
        ...
    def create_endpoint_config(self, *args, **kwargs) -> EndpointConfig:
        """
        Create an endpoint config dictionary to be used with
        :py:meth:`create_networking_config`.

        Args:
            aliases (:py:class:`list`): A list of aliases for this endpoint.
                Names in that list can be used within the network to reach the
                container. Defaults to ``None``.
            links (dict): Mapping of links for this endpoint using the
                ``{'container': 'alias'}`` format. The alias is optional.
                Containers declared in this dict will be linked to this
                container using the provided alias. Defaults to ``None``.
            ipv4_address (str): The IP address of this container on the
                network, using the IPv4 protocol. Defaults to ``None``.
            ipv6_address (str): The IP address of this container on the
                network, using the IPv6 protocol. Defaults to ``None``.
            link_local_ips (:py:class:`list`): A list of link-local (IPv4/IPv6)
                addresses.
            driver_opt (dict): A dictionary of options to provide to the
                network driver. Defaults to ``None``.

        Returns:
            (dict) An endpoint config.

        Example:

            >>> endpoint_config = client.api.create_endpoint_config(
                aliases=['web', 'app'],
                links={'app_db': 'db', 'another': None},
                ipv4_address='132.65.0.123'
            )
        """
        ...
    def diff(self, container: _Container) -> list[dict[Incomplete, Incomplete]]:
        """
        Inspect changes on a container's filesystem.

        Args:
            container (str): The container to diff

        Returns:
            (list) A list of dictionaries containing the attributes `Path`
                and `Kind`.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def export(self, container: _Container, chunk_size: int | None = 2097152):
        """
        Export the contents of a filesystem as a tar archive.

        Args:
            container (str): The container to export
            chunk_size (int): The number of bytes returned by each iteration
                of the generator. If ``None``, data will be streamed as it is
                received. Default: 2 MB

        Returns:
            (generator): The archived filesystem data stream

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
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
    ) -> bytes:
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
    def pause(self, container: _Container) -> None:
        """
        Pauses all processes within a container.

        Args:
            container (str): The container to pause

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def port(self, container: _Container, private_port: int):
        """
        Lookup the public-facing port that is NAT-ed to ``private_port``.
        Identical to the ``docker port`` command.

        Args:
            container (str): The container to look up
            private_port (int): The private port to inspect

        Returns:
            (list of dict): The mapping for the host ports

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:
            .. code-block:: bash

                $ docker run -d -p 80:80 ubuntu:14.04 /bin/sleep 30
                7174d6347063a83f412fad6124c99cffd25ffe1a0807eb4b7f9cec76ac8cb43b

            .. code-block:: python

                >>> client.api.port('7174d6347063', 80)
                [{'HostIp': '0.0.0.0', 'HostPort': '80'}]
        """
        ...
    def put_archive(self, container: _Container, path: str, data) -> bool:
        """
        Insert a file or folder in an existing container using a tar archive as
        source.

        Args:
            container (str): The container where the file(s) will be extracted
            path (str): Path inside the container where the file(s) will be
                extracted. Must exist.
            data (bytes or stream): tar data to be extracted

        Returns:
            (bool): True if the call succeeds.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def prune_containers(self, filters=None):
        """
        Delete stopped containers

        Args:
            filters (dict): Filters to process on the prune list.

        Returns:
            (dict): A dict containing a list of deleted container IDs and
                the amount of disk space reclaimed in bytes.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def remove_container(self, container: _Container, v: bool = False, link: bool = False, force: bool = False) -> None:
        """
        Remove a container. Similar to the ``docker rm`` command.

        Args:
            container (str): The container to remove
            v (bool): Remove the volumes associated with the container
            link (bool): Remove the specified link and not the underlying
                container
            force (bool): Force the removal of a running container (uses
                ``SIGKILL``)

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def rename(self, container: _Container, name: str) -> None:
        """
        Rename a container. Similar to the ``docker rename`` command.

        Args:
            container (str): ID of the container to rename
            name (str): New name for the container

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def resize(self, container: _Container, height: int, width: int) -> None:
        """
        Resize the tty session.

        Args:
            container (str or dict): The container to resize
            height (int): Height of tty session
            width (int): Width of tty session

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def restart(self, container: _Container, timeout: int = 10) -> None:
        """
        Restart a container. Similar to the ``docker restart`` command.

        Args:
            container (str or dict): The container to restart. If a dict, the
                ``Id`` key is used.
            timeout (int): Number of seconds to try to stop for before killing
                the container. Once killed it will then be restarted. Default
                is 10 seconds.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def start(self, container: _Container) -> None:
        """
        Start a container. Similar to the ``docker start`` command, but
        doesn't support attach options.

        **Deprecation warning:** Passing configuration options in ``start`` is
        no longer supported. Users are expected to provide host config options
        in the ``host_config`` parameter of
        :py:meth:`~ContainerApiMixin.create_container`.


        Args:
            container (str): The container to start

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
            :py:class:`docker.errors.DeprecatedMethod`
                If any argument besides ``container`` are provided.

        Example:

            >>> container = client.api.create_container(
            ...     image='busybox:latest',
            ...     command='/bin/sleep 30')
            >>> client.api.start(container=container.get('Id'))
        """
        ...
    def stats(self, container: _Container, decode: bool | None = None, stream: bool = True, one_shot: bool | None = None):
        """
        Stream statistics for a specific container. Similar to the
        ``docker stats`` command.

        Args:
            container (str): The container to stream statistics from
            decode (bool): If set to true, stream will be decoded into dicts
                on the fly. Only applicable if ``stream`` is True.
                False by default.
            stream (bool): If set to false, only the current stats will be
                returned instead of a stream. True by default.
            one_shot (bool): If set to true, Only get a single stat instead of
                waiting for 2 cycles. Must be used with stream=false. False by
                default.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def stop(self, container: _Container, timeout: int | None = None) -> None:
        """
        Stops a container. Similar to the ``docker stop`` command.

        Args:
            container (str): The container to stop
            timeout (int): Timeout in seconds to wait for the container to
                stop before sending a ``SIGKILL``. If None, then the
                StopTimeout value of the container will be used.
                Default: None

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def top(self, container: _Container, ps_args: str | None = None) -> str:
        """
        Display the running processes of a container.

        Args:
            container (str): The container to inspect
            ps_args (str): An optional arguments passed to ps (e.g. ``aux``)

        Returns:
            (str): The output of the top

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def unpause(self, container: _Container) -> None:
        """
        Unpause all processes within a container.

        Args:
            container (str): The container to unpause
        """
        ...
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
    ):
        """
        Update resource configs of one or more containers.

        Args:
            container (str): The container to inspect
            blkio_weight (int): Block IO (relative weight), between 10 and 1000
            cpu_period (int): Limit CPU CFS (Completely Fair Scheduler) period
            cpu_quota (int): Limit CPU CFS (Completely Fair Scheduler) quota
            cpu_shares (int): CPU shares (relative weight)
            cpuset_cpus (str): CPUs in which to allow execution
            cpuset_mems (str): MEMs in which to allow execution
            mem_limit (float or str): Memory limit
            mem_reservation (float or str): Memory soft limit
            memswap_limit (int or str): Total memory (memory + swap), -1 to
                disable swap
            kernel_memory (int or str): Kernel memory limit
            restart_policy (dict): Restart policy dictionary

        Returns:
            (dict): Dictionary containing a ``Warnings`` key.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
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
