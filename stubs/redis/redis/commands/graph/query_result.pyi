from typing import Any, ClassVar, Literal

LABELS_ADDED: str
NODES_CREATED: str
NODES_DELETED: str
RELATIONSHIPS_DELETED: str
PROPERTIES_SET: str
RELATIONSHIPS_CREATED: str
INDICES_CREATED: str
INDICES_DELETED: str
CACHED_EXECUTION: str
INTERNAL_EXECUTION_TIME: str
STATS: Any

class ResultSetColumnTypes:
    COLUMN_UNKNOWN: ClassVar[Literal[0]]
    COLUMN_SCALAR: ClassVar[Literal[1]]
    COLUMN_NODE: ClassVar[Literal[2]]
    COLUMN_RELATION: ClassVar[Literal[3]]

class ResultSetScalarTypes:
    VALUE_UNKNOWN: ClassVar[Literal[0]]
    VALUE_NULL: ClassVar[Literal[1]]
    VALUE_STRING: ClassVar[Literal[2]]
    VALUE_INTEGER: ClassVar[Literal[3]]
    VALUE_BOOLEAN: ClassVar[Literal[4]]
    VALUE_DOUBLE: ClassVar[Literal[5]]
    VALUE_ARRAY: ClassVar[Literal[6]]
    VALUE_EDGE: ClassVar[Literal[7]]
    VALUE_NODE: ClassVar[Literal[8]]
    VALUE_PATH: ClassVar[Literal[9]]
    VALUE_MAP: ClassVar[Literal[10]]
    VALUE_POINT: ClassVar[Literal[11]]

class QueryResult:
    graph: Any
    header: Any
    result_set: Any
    def __init__(self, graph, response, profile: bool = False) -> None:
        """
        A class that represents a result of the query operation.

        Args:

        graph:
            The graph on which the query was executed.
        response:
            The response from the server.
        profile:
            A boolean indicating if the query command was "GRAPH.PROFILE"
        """
        ...
    def parse_results(self, raw_result_set) -> None:
        """Parse the query execution result returned from the server."""
        ...
    statistics: Any
    def parse_statistics(self, raw_statistics) -> None:
        """Parse the statistics returned in the response."""
        ...
    def parse_header(self, raw_result_set):
        """Parse the header of the result."""
        ...
    def parse_records(self, raw_result_set):
        """Parses the result set and returns a list of records."""
        ...
    def parse_entity_properties(self, props):
        """Parse node / edge properties."""
        ...
    def parse_string(self, cell):
        """Parse the cell as a string."""
        ...
    def parse_node(self, cell):
        """Parse the cell to a node."""
        ...
    def parse_edge(self, cell):
        """Parse the cell to an edge."""
        ...
    def parse_path(self, cell):
        """Parse the cell to a path."""
        ...
    def parse_map(self, cell):
        """Parse the cell as a map."""
        ...
    def parse_point(self, cell):
        """Parse the cell to point."""
        ...
    def parse_scalar(self, cell):
        """Parse a scalar value from a cell in the result set."""
        ...
    def parse_profile(self, response) -> None: ...
    def is_empty(self): ...
    @property
    def labels_added(self):
        """Returns the number of labels added in the query"""
        ...
    @property
    def nodes_created(self):
        """Returns the number of nodes created in the query"""
        ...
    @property
    def nodes_deleted(self):
        """Returns the number of nodes deleted in the query"""
        ...
    @property
    def properties_set(self):
        """Returns the number of properties set in the query"""
        ...
    @property
    def relationships_created(self):
        """Returns the number of relationships created in the query"""
        ...
    @property
    def relationships_deleted(self):
        """Returns the number of relationships deleted in the query"""
        ...
    @property
    def indices_created(self):
        """Returns the number of indices created in the query"""
        ...
    @property
    def indices_deleted(self):
        """Returns the number of indices deleted in the query"""
        ...
    @property
    def cached_execution(self):
        """Returns whether or not the query execution plan was cached"""
        ...
    @property
    def run_time_ms(self):
        """Returns the server execution time of the query"""
        ...
