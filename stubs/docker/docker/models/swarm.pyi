from collections.abc import Iterable
from typing import Any

from .resource import Model

class Swarm(Model):
    """
    The server's Swarm state. This a singleton that must be reloaded to get
    the current state of the Swarm.
    """
    id_attribute: str
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def version(self) -> str | None:
        """
        The version number of the swarm. If this is not the same as the
        server, the :py:meth:`update` function will not work and you will
        need to call :py:meth:`reload` before calling it again.
        """
        ...
    def get_unlock_key(self) -> dict[str, Any]:
        """
        Get the unlock key for this Swarm manager.

        Returns:
            A ``dict`` containing an ``UnlockKey`` member
        """
        ...
    def init(
        self,
        advertise_addr: str | None = None,
        listen_addr: str = "0.0.0.0:2377",
        force_new_cluster: bool = False,
        default_addr_pool: Iterable[str] | None = None,
        subnet_size: int | None = None,
        data_path_addr: str | None = None,
        data_path_port: int | None = None,
        **kwargs,
    ) -> str:
        """
        Initialize a new swarm on this Engine.

        Args:
            advertise_addr (str): Externally reachable address advertised to
                other nodes. This can either be an address/port combination in
                the form ``192.168.1.1:4567``, or an interface followed by a
                port number, like ``eth0:4567``. If the port number is omitted,
                the port number from the listen address is used.

                If not specified, it will be automatically detected when
                possible.
            listen_addr (str): Listen address used for inter-manager
                communication, as well as determining the networking interface
                used for the VXLAN Tunnel Endpoint (VTEP). This can either be
                an address/port combination in the form ``192.168.1.1:4567``,
                or an interface followed by a port number, like ``eth0:4567``.
                If the port number is omitted, the default swarm listening port
                is used. Default: ``0.0.0.0:2377``
            force_new_cluster (bool): Force creating a new Swarm, even if
                already part of one. Default: False
            default_addr_pool (list of str): Default Address Pool specifies
                default subnet pools for global scope networks. Each pool
                should be specified as a CIDR block, like '10.0.0.0/8'.
                Default: None
            subnet_size (int): SubnetSize specifies the subnet size of the
                networks created from the default subnet pool. Default: None
            data_path_addr (string): Address or interface to use for data path
                traffic. For example, 192.168.1.1, or an interface, like eth0.
            data_path_port (int): Port number to use for data path traffic.
                Acceptable port range is 1024 to 49151. If set to ``None`` or
                0, the default port 4789 will be used. Default: None
            task_history_retention_limit (int): Maximum number of tasks
                history stored.
            snapshot_interval (int): Number of logs entries between snapshot.
            keep_old_snapshots (int): Number of snapshots to keep beyond the
                current snapshot.
            log_entries_for_slow_followers (int): Number of log entries to
                keep around to sync up slow followers after a snapshot is
                created.
            heartbeat_tick (int): Amount of ticks (in seconds) between each
                heartbeat.
            election_tick (int): Amount of ticks (in seconds) needed without a
                leader to trigger a new election.
            dispatcher_heartbeat_period (int):  The delay for an agent to send
                a heartbeat to the dispatcher.
            node_cert_expiry (int): Automatic expiry for nodes certificates.
            external_ca (dict): Configuration for forwarding signing requests
                to an external certificate authority. Use
                ``docker.types.SwarmExternalCA``.
            name (string): Swarm's name
            labels (dict): User-defined key/value metadata.
            signing_ca_cert (str): The desired signing CA certificate for all
                swarm node TLS leaf certificates, in PEM format.
            signing_ca_key (str): The desired signing CA key for all swarm
                node TLS leaf certificates, in PEM format.
            ca_force_rotate (int): An integer whose purpose is to force swarm
                to generate a new signing CA certificate and key, if none have
                been specified.
            autolock_managers (boolean): If set, generate a key and use it to
                lock data stored on the managers.
            log_driver (DriverConfig): The default log driver to use for tasks
                created in the orchestrator.

        Returns:
            (str): The ID of the created node.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> client.swarm.init(
                advertise_addr='eth0', listen_addr='0.0.0.0:5000',
                force_new_cluster=False, default_addr_pool=['10.20.0.0/16],
                subnet_size=24, snapshot_interval=5000,
                log_entries_for_slow_followers=1200
            )
        """
        ...
    def join(self, *args, **kwargs) -> bool:
        """
        Make this Engine join a swarm that has already been created.

        Args:
            remote_addrs (:py:class:`list`): Addresses of one or more manager
                nodes already participating in the Swarm to join.
            join_token (string): Secret token for joining this Swarm.
            listen_addr (string): Listen address used for inter-manager
                communication if the node gets promoted to manager, as well as
                determining the networking interface used for the VXLAN Tunnel
                Endpoint (VTEP). Default: ``'0.0.0.0:2377``
            advertise_addr (string): Externally reachable address advertised
                to other nodes. This can either be an address/port combination
                in the form ``192.168.1.1:4567``, or an interface followed by a
                port number, like ``eth0:4567``. If the port number is omitted,
                the port number from the listen address is used. If
                AdvertiseAddr is not specified, it will be automatically
                detected when possible. Default: ``None``
            data_path_addr (string): Address or interface to use for data path
                traffic. For example, 192.168.1.1, or an interface, like eth0.

        Returns:
            ``True`` if the request went through.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def leave(self, *args, **kwargs) -> bool:
        """
        Leave a swarm.

        Args:
            force (bool): Leave the swarm even if this node is a manager.
                Default: ``False``

        Returns:
            ``True`` if the request went through.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def reload(self) -> None:
        """
        Inspect the swarm on the server and store the response in
        :py:attr:`attrs`.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def unlock(self, key: str) -> bool:
        """
        Unlock a locked swarm.

        Args:
            key (string): The unlock key as provided by
                :py:meth:`get_unlock_key`

        Raises:
            :py:class:`docker.errors.InvalidArgument`
                If the key argument is in an incompatible format

            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Returns:
            `True` if the request was successful.

        Example:

            >>> key = client.api.get_unlock_key()
            >>> client.unlock_swarm(key)
        """
        ...
    def update(
        self,
        rotate_worker_token: bool = False,
        rotate_manager_token: bool = False,
        rotate_manager_unlock_key: bool = False,
        **kwargs,
    ) -> bool:
        """
        Update the swarm's configuration.

        It takes the same arguments as :py:meth:`init`, except
        ``advertise_addr``, ``listen_addr``, and ``force_new_cluster``. In
        addition, it takes these arguments:

        Args:
            rotate_worker_token (bool): Rotate the worker join token. Default:
                ``False``.
            rotate_manager_token (bool): Rotate the manager join token.
                Default: ``False``.
            rotate_manager_unlock_key (bool): Rotate the manager unlock key.
                Default: ``False``.
        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
