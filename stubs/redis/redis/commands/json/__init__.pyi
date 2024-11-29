from _typeshed import Incomplete
from typing import Any

from ...client import Pipeline as ClientPipeline
from .commands import JSONCommands

class JSON(JSONCommands):
    """
    Create a client for talking to json.

    :param decoder:
    :type json.JSONDecoder: An instance of json.JSONDecoder

    :param encoder:
    :type json.JSONEncoder: An instance of json.JSONEncoder
    """
    MODULE_CALLBACKS: dict[str, Any]
    client: Any
    execute_command: Any
    MODULE_VERSION: Incomplete | None
    def __init__(self, client, version: Incomplete | None = None, decoder=..., encoder=...) -> None:
        """
        Create a client for talking to json.

        :param decoder:
        :type json.JSONDecoder: An instance of json.JSONDecoder

        :param encoder:
        :type json.JSONEncoder: An instance of json.JSONEncoder
        """
        ...
    def pipeline(self, transaction: bool = True, shard_hint: Incomplete | None = None) -> Pipeline:
        """
        Creates a pipeline for the JSON module, that can be used for executing
        JSON commands, as well as classic core commands.

        Usage example:

        r = redis.Redis()
        pipe = r.json().pipeline()
        pipe.jsonset('foo', '.', {'hello!': 'world'})
        pipe.jsonget('foo')
        pipe.jsonget('notakey')
        """
        ...

class Pipeline(JSONCommands, ClientPipeline[Incomplete]):
    """Pipeline for the module."""
    ...
