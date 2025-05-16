from typing import Any

from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin
from requests import Response

class Raft(SystemBackendMixin):
    """
    Raft cluster-related system backend methods.

    When using Shamir seal, as soon as the Vault server is brought up, this API should be invoked
    instead of sys/init. This API completes in 2 phases. Once this is invoked, the joining node
    will receive a challenge from the Raft's leader node. This challenge can be answered by the
    joining node only after a successful unseal. Hence, the joining node should be unsealed using
    the unseal keys of the Raft's leader node.

    Reference: https://www.vaultproject.io/api-docs/system/storage/raft
    """
    def join_raft_cluster(
        self, leader_api_addr, retry: bool = False, leader_ca_cert=None, leader_client_cert=None, leader_client_key=None
    ): ...
    def read_raft_config(self): ...
    def remove_raft_node(self, server_id): ...
    def take_raft_snapshot(self): ...
    def restore_raft_snapshot(self, snapshot): ...
    def force_restore_raft_snapshot(self, snapshot): ...
    def read_raft_auto_snapshot_status(self, name: str) -> Response: ...
    def read_raft_auto_snapshot_config(self, name: str) -> Response: ...
    def list_raft_auto_snapshot_configs(self) -> Response: ...
    def create_or_update_raft_auto_snapshot_config(
        self, name: str, interval: str, storage_type: str, retain: int = 1, **kwargs: Any
    ) -> Response:
        """
        Create or update the configuration of the raft auto snapshot.

        Supported methods:
            POST: /sys/storage/raft/snapshot-auto/config/:name. Produces: 204 application/json

        :param name: The name of the snapshot configuration.
        :type name: str
        :param interval: The interval at which snapshots should be taken.
        :type interval: str
        :param storage_type: The type of storage to use for the snapshot.
        :type storage_type: str
        :param retain: The number of snapshots to retain. Default is 1
        :type retain: int
        :param kwargs: Additional parameters to send in the request. Should be params specific to the storage type.
        :type kwargs: dict
        :return: The response of the create_or_update_raft_auto_snapshot_config request.
        :rtype: requests.Response
        """
        ...
    def delete_raft_auto_snapshot_config(self, name: str) -> Response:
        """
        Delete the configuration of the raft auto snapshot.

        Supported methods:
            DELETE: /sys/storage/raft/snapshot-auto/config/:name. Produces: 204 application/json

        :param name: The name of the snapshot configuration.
        :type name: str
        :return: The response of the delete_raft_auto_snapshot_config request.
        :rtype: requests.Response
        """
        ...
