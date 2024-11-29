from _typeshed import Incomplete
from typing import NoReturn

from .core import ACLCommands, DataAccessCommands, ManagementCommands, PubSubCommands, _StrType

class ClusterMultiKeyCommands:
    """A class containing commands that handle more than one key"""
    def mget_nonatomic(self, keys, *args):
        """
        Splits the keys into different slots and then calls MGET
        for the keys of every slot. This operation will not be atomic
        if keys belong to more than one slot.

        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/mget
        """
        ...
    def mset_nonatomic(self, mapping):
        """
        Sets key/values based on a mapping. Mapping is a dictionary of
        key/value pairs. Both keys and values should be strings or types that
        can be cast to a string via str().

        Splits the keys into different slots and then calls MSET
        for the keys of every slot. This operation will not be atomic
        if keys belong to more than one slot.

        For more information see https://redis.io/commands/mset
        """
        ...
    def exists(self, *keys):
        """
        Returns the number of ``names`` that exist in the
        whole cluster. The keys are first split up into slots
        and then an EXISTS command is sent for every slot

        For more information see https://redis.io/commands/exists
        """
        ...
    def delete(self, *keys):
        """
        Deletes the given keys in the cluster.
        The keys are first split up into slots
        and then an DEL command is sent for every slot

        Non-existant keys are ignored.
        Returns the number of keys that were deleted.

        For more information see https://redis.io/commands/del
        """
        ...
    def touch(self, *keys):
        """
        Updates the last access time of given keys across the
        cluster.

        The keys are first split up into slots
        and then an TOUCH command is sent for every slot

        Non-existant keys are ignored.
        Returns the number of keys that were touched.

        For more information see https://redis.io/commands/touch
        """
        ...
    def unlink(self, *keys):
        """
        Remove the specified keys in a different thread.

        The keys are first split up into slots
        and then an TOUCH command is sent for every slot

        Non-existant keys are ignored.
        Returns the number of keys that were unlinked.

        For more information see https://redis.io/commands/unlink
        """
        ...

class ClusterManagementCommands(ManagementCommands):
    """
    A class for Redis Cluster management commands

    The class inherits from Redis's core ManagementCommands class and do the
    required adjustments to work with cluster mode
    """
    def slaveof(self, *args, **kwargs) -> None:
        """
        Make the server a replica of another instance, or promote it as master.

        For more information see https://redis.io/commands/slaveof
        """
        ...
    def replicaof(self, *args, **kwargs) -> None:
        """
        Make the server a replica of another instance, or promote it as master.

        For more information see https://redis.io/commands/replicaof
        """
        ...
    def swapdb(self, *args, **kwargs) -> None:
        """
        Swaps two Redis databases.

        For more information see https://redis.io/commands/swapdb
        """
        ...

class ClusterDataAccessCommands(DataAccessCommands[_StrType]):
    """
    A class for Redis Cluster Data Access Commands

    The class inherits from Redis's core DataAccessCommand class and do the
    required adjustments to work with cluster mode
    """
    def stralgo(
        self,
        algo,
        value1,
        value2,
        specific_argument: str = "strings",
        len: bool = False,
        idx: bool = False,
        minmatchlen: Incomplete | None = None,
        withmatchlen: bool = False,
        **kwargs,
    ):
        """
        Implements complex algorithms that operate on strings.
        Right now the only algorithm implemented is the LCS algorithm
        (longest common substring). However new algorithms could be
        implemented in the future.

        ``algo`` Right now must be LCS
        ``value1`` and ``value2`` Can be two strings or two keys
        ``specific_argument`` Specifying if the arguments to the algorithm
        will be keys or strings. strings is the default.
        ``len`` Returns just the len of the match.
        ``idx`` Returns the match positions in each string.
        ``minmatchlen`` Restrict the list of matches to the ones of a given
        minimal length. Can be provided only when ``idx`` set to True.
        ``withmatchlen`` Returns the matches with the len of the match.
        Can be provided only when ``idx`` set to True.

        For more information see https://redis.io/commands/stralgo
        """
        ...

class RedisClusterCommands(
    ClusterMultiKeyCommands, ClusterManagementCommands, ACLCommands[_StrType], PubSubCommands, ClusterDataAccessCommands[_StrType]
):
    """
    A class for all Redis Cluster commands

    For key-based commands, the target node(s) will be internally determined
    by the keys' hash slot.
    Non-key-based commands can be executed with the 'target_nodes' argument to
    target specific nodes. By default, if target_nodes is not specified, the
    command will be executed on the default cluster node.

    :param :target_nodes: type can be one of the followings:
        - nodes flag: ALL_NODES, PRIMARIES, REPLICAS, RANDOM
        - 'ClusterNode'
        - 'list(ClusterNodes)'
        - 'dict(any:clusterNodes)'

    for example:
        r.cluster_info(target_nodes=RedisCluster.ALL_NODES)
    """
    def cluster_addslots(self, target_node, *slots):
        """
        Assign new hash slots to receiving node. Sends to specified node.

        :target_node: 'ClusterNode'
            The node to execute the command on

        For more information see https://redis.io/commands/cluster-addslots
        """
        ...
    def cluster_countkeysinslot(self, slot_id):
        """
        Return the number of local keys in the specified hash slot
        Send to node based on specified slot_id

        For more information see https://redis.io/commands/cluster-countkeysinslot
        """
        ...
    def cluster_count_failure_report(self, node_id):
        """
        Return the number of failure reports active for a given node
        Sends to a random node

        For more information see https://redis.io/commands/cluster-count-failure-reports
        """
        ...
    def cluster_delslots(self, *slots):
        """
        Set hash slots as unbound in the cluster.
        It determines by it self what node the slot is in and sends it there

        Returns a list of the results for each processed slot.

        For more information see https://redis.io/commands/cluster-delslots
        """
        ...
    def cluster_failover(self, target_node, option: Incomplete | None = None):
        """
        Forces a slave to perform a manual failover of its master
        Sends to specified node

        :target_node: 'ClusterNode'
            The node to execute the command on

        For more information see https://redis.io/commands/cluster-failover
        """
        ...
    def cluster_info(self, target_nodes: Incomplete | None = None):
        """
        Provides info about Redis Cluster node state.
        The command will be sent to a random node in the cluster if no target
        node is specified.

        For more information see https://redis.io/commands/cluster-info
        """
        ...
    def cluster_keyslot(self, key):
        """
        Returns the hash slot of the specified key
        Sends to random node in the cluster

        For more information see https://redis.io/commands/cluster-keyslot
        """
        ...
    def cluster_meet(self, host, port, target_nodes: Incomplete | None = None):
        """
        Force a node cluster to handshake with another node.
        Sends to specified node.

        For more information see https://redis.io/commands/cluster-meet
        """
        ...
    def cluster_nodes(self):
        """
        Get Cluster config for the node.
        Sends to random node in the cluster

        For more information see https://redis.io/commands/cluster-nodes
        """
        ...
    def cluster_replicate(self, target_nodes, node_id):
        """
        Reconfigure a node as a slave of the specified master node

        For more information see https://redis.io/commands/cluster-replicate
        """
        ...
    def cluster_reset(self, soft: bool = True, target_nodes: Incomplete | None = None):
        """
        Reset a Redis Cluster node

        If 'soft' is True then it will send 'SOFT' argument
        If 'soft' is False then it will send 'HARD' argument

        For more information see https://redis.io/commands/cluster-reset
        """
        ...
    def cluster_save_config(self, target_nodes: Incomplete | None = None):
        """
        Forces the node to save cluster state on disk

        For more information see https://redis.io/commands/cluster-saveconfig
        """
        ...
    def cluster_get_keys_in_slot(self, slot, num_keys):
        """
        Returns the number of keys in the specified cluster slot

        For more information see https://redis.io/commands/cluster-getkeysinslot
        """
        ...
    def cluster_set_config_epoch(self, epoch, target_nodes: Incomplete | None = None):
        """
        Set the configuration epoch in a new node

        For more information see https://redis.io/commands/cluster-set-config-epoch
        """
        ...
    def cluster_setslot(self, target_node, node_id, slot_id, state):
        """
        Bind an hash slot to a specific node

        :target_node: 'ClusterNode'
            The node to execute the command on

        For more information see https://redis.io/commands/cluster-setslot
        """
        ...
    def cluster_setslot_stable(self, slot_id):
        """
        Clears migrating / importing state from the slot.
        It determines by it self what node the slot is in and sends it there.

        For more information see https://redis.io/commands/cluster-setslot
        """
        ...
    def cluster_replicas(self, node_id, target_nodes: Incomplete | None = None):
        """
        Provides a list of replica nodes replicating from the specified primary
        target node.

        For more information see https://redis.io/commands/cluster-replicas
        """
        ...
    def cluster_slots(self, target_nodes: Incomplete | None = None):
        """
        Get array of Cluster slot to node mappings

        For more information see https://redis.io/commands/cluster-slots
        """
        ...
    def cluster_myshardid(self, target_nodes: Incomplete | None = None):
        """
        Returns the shard ID of the node.

        For more information see https://redis.io/commands/cluster-myshardid/
        """
        ...
    def cluster_links(self, target_node):
        """
        Each node in a Redis Cluster maintains a pair of long-lived TCP link with each
        peer in the cluster: One for sending outbound messages towards the peer and one
        for receiving inbound messages from the peer.

        This command outputs information of all such peer links as an array.

        For more information see https://redis.io/commands/cluster-links
        """
        ...
    def cluster_flushslots(self, target_nodes: Incomplete | None = None) -> NoReturn: ...
    def cluster_bumpepoch(self, target_nodes: Incomplete | None = None) -> NoReturn: ...
    read_from_replicas: bool
    def readonly(self, target_nodes: Incomplete | None = None):
        """
        Enables read queries.
        The command will be sent to the default cluster node if target_nodes is
        not specified.

        For more information see https://redis.io/commands/readonly
        """
        ...
    def readwrite(self, target_nodes: Incomplete | None = None):
        """
        Disables read queries.
        The command will be sent to the default cluster node if target_nodes is
        not specified.

        For more information see https://redis.io/commands/readwrite
        """
        ...
