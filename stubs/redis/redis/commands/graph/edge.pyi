from _typeshed import Incomplete
from typing import Any

class Edge:
    """An edge connecting two nodes."""
    id: Any
    relation: Any
    properties: Any
    src_node: Any
    dest_node: Any
    def __init__(
        self, src_node, relation, dest_node, edge_id: Incomplete | None = None, properties: Incomplete | None = None
    ) -> None:
        """Create a new edge."""
        ...
    def to_string(self): ...
    def __eq__(self, rhs): ...
