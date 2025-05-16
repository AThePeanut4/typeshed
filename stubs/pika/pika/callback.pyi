"""
Callback management class, common area for keeping track of all callbacks in
the Pika stack.
"""

from _typeshed import Incomplete
from collections.abc import Callable
from logging import Logger
from typing import Literal

from pika import amqp_object, frame

LOGGER: Logger

def name_or_value(value: amqp_object.AMQPObject | frame.Frame | int | str) -> str:
    """
    Will take Frame objects, classes, etc and attempt to return a valid
    string identifier for them.

    :param pika.amqp_object.AMQPObject|pika.frame.Frame|int|str value: The
        value to sanitize
    :rtype: str
    """
    ...
def sanitize_prefix(function):
    """Automatically call name_or_value on the prefix passed in."""
    ...
def check_for_prefix_and_key(function):
    """
    Automatically return false if the key or prefix is not in the callbacks
    for the instance.
    """
    ...

class CallbackManager:
    """
    CallbackManager is a global callback system designed to be a single place
    where Pika can manage callbacks and process them. It should be referenced
    by the CallbackManager.instance() method instead of constructing new
    instances of it.
    """
    CALLS: str
    ARGUMENTS: str
    DUPLICATE_WARNING: str
    CALLBACK: str
    ONE_SHOT: str
    ONLY_CALLER: str
    def __init__(self) -> None:
        """Create an instance of the CallbackManager"""
        ...
    def add(
        self,
        prefix: str | int,
        key: str | object,
        callback: Callable[[Incomplete], Incomplete],
        one_shot: bool = True,
        only_caller: object | None = None,
        arguments=None,
    ) -> tuple[str | int, str | object]: ...
    def clear(self) -> None: ...
    def cleanup(self, prefix: str | int) -> bool: ...
    def pending(self, prefix: str | int, key: str | object) -> int | None: ...
    def process(self, prefix: str | int, key: str | object, caller, *args, **keywords) -> bool: ...
    def remove(
        self,
        prefix: str | int,
        key: str | object,
        callback_value: Callable[[Incomplete], Incomplete] | None = None,
        arguments=None,
    ) -> Literal[True]: ...
    def remove_all(self, prefix: str | int, key: str | object) -> None: ...
