from _typeshed import Incomplete
from typing import Any

class Node:
    """A node within the graph."""
    id: Any
    alias: Any
    label: Any
    labels: Any
    properties: Any
    def __init__(
        self,
        node_id: Incomplete | None = None,
        alias: Incomplete | None = None,
        label: str | list[str] | None = None,
        properties: Incomplete | None = None,
    ) -> None:
        """Create a new node."""
        ...
    def to_string(self): ...
    def __eq__(self, rhs): ...
