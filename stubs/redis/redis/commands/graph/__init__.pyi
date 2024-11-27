from typing import Any

from .commands import GraphCommands as GraphCommands
from .edge import Edge as Edge
from .node import Node as Node
from .path import Path as Path

class Graph(GraphCommands):
    """Graph, collection of nodes and edges."""
    NAME: Any
    client: Any
    execute_command: Any
    nodes: Any
    edges: Any
    version: int
    def __init__(self, client, name=...) -> None:
        """Create a new graph."""
        ...
    @property
    def name(self): ...
    def get_label(self, idx):
        """
        Returns a label by it's index

        Args:

        idx:
            The index of the label
        """
        ...
    def get_relation(self, idx):
        """
        Returns a relationship type by it's index

        Args:

        idx:
            The index of the relation
        """
        ...
    def get_property(self, idx):
        """
        Returns a property by it's index

        Args:

        idx:
            The index of the property
        """
        ...
    def add_node(self, node) -> None:
        """Adds a node to the graph."""
        ...
    def add_edge(self, edge) -> None:
        """Adds an edge to the graph."""
        ...
    def call_procedure(self, procedure, *args, read_only: bool = False, **kwagrs): ...
    def labels(self): ...
    def relationship_types(self): ...
    def property_keys(self): ...
