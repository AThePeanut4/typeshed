from redis.typing import EncodedT

REDIS_CLUSTER_HASH_SLOTS: int

def key_slot(key: EncodedT, bucket: int = 16384) -> int:
    """
    Calculate key slot for a given key.
    See Keys distribution model in https://redis.io/topics/cluster-spec
    :param key - bytes
    :param bucket - int
    """
    ...
