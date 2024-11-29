from _typeshed import Incomplete
from typing import Any

class GraphCommands:
    """RedisGraph Commands"""
    def commit(self):
        """Create entire graph."""
        ...
    version: Any
    def query(
        self,
        q,
        params: Incomplete | None = None,
        timeout: Incomplete | None = None,
        read_only: bool = False,
        profile: bool = False,
    ):
        """
        Executes a query against the graph.
        For more information see `GRAPH.QUERY <https://redis.io/commands/graph.query>`_. # noqa

        Args:

        q : str
            The query.
        params : dict
            Query parameters.
        timeout : int
            Maximum runtime for read queries in milliseconds.
        read_only : bool
            Executes a readonly query if set to True.
        profile : bool
            Return details on results produced by and time
            spent in each operation.
        """
        ...
    def merge(self, pattern):
        """Merge pattern."""
        ...
    def delete(self):
        """
        Deletes graph.
        For more information see `DELETE <https://redis.io/commands/graph.delete>`_. # noqa
        """
        ...
    nodes: Any
    edges: Any
    def flush(self) -> None:
        """Commit the graph and reset the edges and the nodes to zero length."""
        ...
    def explain(self, query, params: Incomplete | None = None):
        """
        Get the execution plan for given query,
        GRAPH.EXPLAIN returns ExecutionPlan object.
        For more information see `GRAPH.EXPLAIN <https://redis.io/commands/graph.explain>`_. # noqa

        Args:
            query: the query that will be executed
            params: query parameters
        """
        ...
    def bulk(self, **kwargs) -> None:
        """Internal only. Not supported."""
        ...
    def profile(self, query):
        """
        Execute a query and produce an execution plan augmented with metrics
        for each operation's execution. Return a string representation of a
        query execution plan, with details on results produced by and time
        spent in each operation.
        For more information see `GRAPH.PROFILE <https://redis.io/commands/graph.profile>`_. # noqa
        """
        ...
    def slowlog(self):
        """
        Get a list containing up to 10 of the slowest queries issued
        against the given graph ID.
        For more information see `GRAPH.SLOWLOG <https://redis.io/commands/graph.slowlog>`_. # noqa

        Each item in the list has the following structure:
        1. A unix timestamp at which the log entry was processed.
        2. The issued command.
        3. The issued query.
        4. The amount of time needed for its execution, in milliseconds.
        """
        ...
    def config(self, name, value: Incomplete | None = None, set: bool = False):
        """
        Retrieve or update a RedisGraph configuration.
        For more information see `https://redis.io/commands/graph.config-get/>`_. # noqa

        Args:

        name : str
            The name of the configuration
        value :
            The value we want to set (can be used only when `set` is on)
        set : bool
            Turn on to set a configuration. Default behavior is get.
        """
        ...
    def list_keys(self):
        """
        Lists all graph keys in the keyspace.
        For more information see `GRAPH.LIST <https://redis.io/commands/graph.list>`_. # noqa
        """
        ...
