from redis.client import AbstractRedis
from redis.typing import EncodableT

class CommandsParser:
    """
    Parses Redis commands to get command keys.
    COMMAND output is used to determine key locations.
    Commands that do not have a predefined key location are flagged with
    'movablekeys', and these commands' keys are determined by the command
    'COMMAND GETKEYS'.
    """
    commands: dict[str, str]
    def __init__(self, redis_connection: AbstractRedis) -> None: ...
    def initialize(self, r: AbstractRedis) -> None: ...
    def get_keys(self, redis_conn: AbstractRedis, *args: EncodableT) -> list[EncodableT] | None:
        """
        Get the keys from the passed command.

        NOTE: Due to a bug in redis<7.0, this function does not work properly
        for EVAL or EVALSHA when the `numkeys` arg is 0.
         - issue: https://github.com/redis/redis/issues/9493
         - fix: https://github.com/redis/redis/pull/9733

        So, don't use this function with EVAL or EVALSHA.
        """
        ...
