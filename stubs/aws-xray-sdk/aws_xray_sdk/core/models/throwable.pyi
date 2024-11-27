from typing import Any

log: Any

class Throwable:
    """
    An object recording exception infomation under trace entity
    `cause` section. The information includes the stack trace,
    working directory and message from the original exception.
    """
    id: Any
    message: Any
    type: Any
    remote: Any
    stack: Any
    def __init__(self, exception, stack, remote: bool = False) -> None:
        """
        :param Exception exception: the catched exception.
        :param list stack: the formatted stack trace gathered
            through `traceback` module.
        :param bool remote: If False it means it's a client error
            instead of a downstream service.
        """
        ...
    def to_dict(self):
        """
        Convert Throwable object to dict with required properties that
        have non-empty values. 
        """
        ...
