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
    ): ...
    def inspect_swarm(self): ...
    def inspect_node(self, node_id): ...
    def join_swarm(
        self, remote_addrs, join_token, listen_addr: str = "0.0.0.0:2377", advertise_addr=None, data_path_addr=None
    ): ...
    def leave_swarm(self, force: bool = False): ...
    def nodes(self, filters=None): ...
    def remove_node(self, node_id, force: bool = False): ...
    def unlock_swarm(self, key): ...
    def update_node(self, node_id, version, node_spec=None): ...
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
