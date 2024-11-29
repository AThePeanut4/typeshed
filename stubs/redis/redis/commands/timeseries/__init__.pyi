from _typeshed import Incomplete
from typing import Any

from ...client import Pipeline as ClientPipeline
from .commands import TimeSeriesCommands

class TimeSeries(TimeSeriesCommands):
    """
    This class subclasses redis-py's `Redis` and implements RedisTimeSeries's
    commands (prefixed with "ts").
    The client allows to interact with RedisTimeSeries and use all of it's
    functionality.
    """
    MODULE_CALLBACKS: dict[str, Any]
    client: Any
    execute_command: Any
    def __init__(self, client: Incomplete | None = None, **kwargs) -> None:
        """Create a new RedisTimeSeries client."""
        ...
    def pipeline(self, transaction: bool = True, shard_hint: Incomplete | None = None) -> Pipeline:
        """
        Creates a pipeline for the TimeSeries module, that can be used
        for executing only TimeSeries commands and core commands.

        Usage example:

        r = redis.Redis()
        pipe = r.ts().pipeline()
        for i in range(100):
            pipeline.add("with_pipeline", i, 1.1 * i)
        pipeline.execute()
        """
        ...

class Pipeline(TimeSeriesCommands, ClientPipeline[Incomplete]):
    """Pipeline for the module."""
    ...
