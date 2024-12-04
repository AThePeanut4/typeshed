""""""

from _typeshed import Incomplete
from typing import Any

class ADPersistentSearch:
    connection: Any
    message_id: Any
    base: Any
    scope: Any
    attributes: Any
    controls: Any
    filter: str
    def __init__(self, connection, search_base, search_scope, attributes, streaming, callback) -> None: ...
    def start(self) -> None: ...
    def stop(self, unbind: bool = True) -> None: ...
    def next(self, block: bool = False, timeout: Incomplete | None = None): ...
    def funnel(self, block: bool = False, timeout: Incomplete | None = None) -> None: ...
