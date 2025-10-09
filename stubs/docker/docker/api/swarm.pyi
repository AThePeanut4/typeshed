import logging
from typing import Literal

from docker.types.swarm import SwarmSpec

log: logging.Logger

class SwarmApiMixin:
    def create_swarm_spec(self, *args, **kwargs) -> SwarmSpec: ...
    def get_unlock_key(self): ...
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
    ) -> Literal[True]: ...
    def leave_swarm(self, force: bool = False) -> Literal[True]: ...
    def nodes(self, filters=None): ...
    def remove_node(self, node_id, force: bool = False) -> Literal[True]: ...
    def unlock_swarm(self, key) -> Literal[True]: ...
    def update_node(self, node_id, version, node_spec=None) -> Literal[True]: ...
    def update_swarm(
        self,
        version,
        swarm_spec=None,
        rotate_worker_token: bool = False,
        rotate_manager_token: bool = False,
        rotate_manager_unlock_key: bool = False,
    ) -> Literal[True]: ...
