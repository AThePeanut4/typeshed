from _typeshed import Incomplete
from typing import Any

# TODO: define and use:
# from redis.asyncio.cluster import ClusterNode

class CommandsParser:
    """
    Parses Redis commands to get command keys.

    COMMAND output is used to determine key locations.
    Commands that do not have a predefined key location are flagged with 'movablekeys',
    and these commands' keys are determined by the command 'COMMAND GETKEYS'.

    NOTE: Due to a bug in redis<7.0, this does not work properly
    for EVAL or EVALSHA when the `numkeys` arg is 0.
     - issue: https://github.com/redis/redis/issues/9493
     - fix: https://github.com/redis/redis/pull/9733

    So, don't use this with EVAL or EVALSHA.
    """
    async def initialize(self, node: Incomplete | None = None) -> None: ...  # TODO: ClusterNode
    async def get_keys(self, *args: Any) -> tuple[str, ...] | None: ...
