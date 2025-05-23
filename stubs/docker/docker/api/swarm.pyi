from _typeshed import Incomplete

log: Incomplete

class SwarmApiMixin:
    def create_swarm_spec(self, *args, **kwargs):
        """
        Create a :py:class:`docker.types.SwarmSpec` instance that can be used
        as the ``swarm_spec`` argument in
        :py:meth:`~docker.api.swarm.SwarmApiMixin.init_swarm`.

        Args:
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
            external_cas (:py:class:`list`): Configuration for forwarding
                signing requests to an external certificate authority. Use
                a list of :py:class:`docker.types.SwarmExternalCA`.
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
            :py:class:`docker.types.SwarmSpec`

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> spec = client.api.create_swarm_spec(
              snapshot_interval=5000, log_entries_for_slow_followers=1200
            )
            >>> client.api.init_swarm(
              advertise_addr='eth0', listen_addr='0.0.0.0:5000',
              force_new_cluster=False, swarm_spec=spec
            )
        """
        ...
    def get_unlock_key(self):
        """
        Get the unlock key for this Swarm manager.

        Returns:
            A ``dict`` containing an ``UnlockKey`` member
        """
        ...
    def init_swarm(
        self,
        advertise_addr=None,
        listen_addr: str = "0.0.0.0:2377",
        force_new_cluster: bool = False,
        swarm_spec=None,
        default_addr_pool=None,
        subnet_size=None,
        data_path_addr=None,
        data_path_port=None,
    ):
        """
        Initialize a new Swarm using the current connected engine as the first
        node.

        Args:
            advertise_addr (string): Externally reachable address advertised
                to other nodes. This can either be an address/port combination
                in the form ``192.168.1.1:4567``, or an interface followed by a
                port number, like ``eth0:4567``. If the port number is omitted,
                the port number from the listen address is used. If
                ``advertise_addr`` is not specified, it will be automatically
                detected when possible. Default: None
            listen_addr (string): Listen address used for inter-manager
                communication, as well as determining the networking interface
                used for the VXLAN Tunnel Endpoint (VTEP). This can either be
                an address/port combination in the form ``192.168.1.1:4567``,
                or an interface followed by a port number, like ``eth0:4567``.
                If the port number is omitted, the default swarm listening port
                is used. Default: '0.0.0.0:2377'
            force_new_cluster (bool): Force creating a new Swarm, even if
                already part of one. Default: False
            swarm_spec (dict): Configuration settings of the new Swarm. Use
                ``APIClient.create_swarm_spec`` to generate a valid
                configuration. Default: None
            default_addr_pool (list of strings): Default Address Pool specifies
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

        Returns:
            (str): The ID of the created node.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def inspect_swarm(self):
        """
        Retrieve low-level information about the current swarm.

        Returns:
            A dictionary containing data about the swarm.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def inspect_node(self, node_id):
        """
        Retrieve low-level information about a swarm node

        Args:
            node_id (string): ID of the node to be inspected.

        Returns:
            A dictionary containing data about this node.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def join_swarm(
        self, remote_addrs, join_token, listen_addr: str = "0.0.0.0:2377", advertise_addr=None, data_path_addr=None
    ):
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
    def leave_swarm(self, force: bool = False):
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
    def nodes(self, filters=None):
        """
        List swarm nodes.

        Args:
            filters (dict): Filters to process on the nodes list. Valid
                filters: ``id``, ``name``, ``membership`` and ``role``.
                Default: ``None``

        Returns:
            A list of dictionaries containing data about each swarm node.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def remove_node(self, node_id, force: bool = False):
        """
        Remove a node from the swarm.

        Args:
            node_id (string): ID of the node to be removed.
            force (bool): Force remove an active node. Default: `False`

        Raises:
            :py:class:`docker.errors.NotFound`
                If the node referenced doesn't exist in the swarm.

            :py:class:`docker.errors.APIError`
                If the server returns an error.
        Returns:
            `True` if the request was successful.
        """
        ...
    def unlock_swarm(self, key):
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
    def update_node(self, node_id, version, node_spec=None):
        """
        Update the node's configuration

        Args:

            node_id (string): ID of the node to be updated.
            version (int): The version number of the node object being
                updated. This is required to avoid conflicting writes.
            node_spec (dict): Configuration settings to update. Any values
                not provided will be removed. Default: ``None``

        Returns:
            `True` if the request went through.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> node_spec = {'Availability': 'active',
                         'Name': 'node-name',
                         'Role': 'manager',
                         'Labels': {'foo': 'bar'}
                        }
            >>> client.api.update_node(node_id='24ifsmvkjbyhk', version=8,
                node_spec=node_spec)
        """
        ...
    def update_swarm(
        self,
        version,
        swarm_spec=None,
        rotate_worker_token: bool = False,
        rotate_manager_token: bool = False,
        rotate_manager_unlock_key: bool = False,
    ):
        """
        Update the Swarm's configuration

        Args:
            version (int): The version number of the swarm object being
                updated. This is required to avoid conflicting writes.
            swarm_spec (dict): Configuration settings to update. Use
                :py:meth:`~docker.api.swarm.SwarmApiMixin.create_swarm_spec` to
                generate a valid configuration. Default: ``None``.
            rotate_worker_token (bool): Rotate the worker join token. Default:
                ``False``.
            rotate_manager_token (bool): Rotate the manager join token.
                Default: ``False``.
            rotate_manager_unlock_key (bool): Rotate the manager unlock key.
                Default: ``False``.

        Returns:
            ``True`` if the request went through.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
