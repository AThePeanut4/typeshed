from .json import JSON
from .search import Search
from .timeseries import TimeSeries

class RedisModuleCommands:
    """
    This class contains the wrapper functions to bring supported redis
    modules into the command namespace.
    """
    def json(self, encoder=..., decoder=...) -> JSON:
        """Access the json namespace, providing support for redis json."""
        ...
    def ft(self, index_name: str = "idx") -> Search:
        """Access the search namespace, providing support for redis search."""
        ...
    def ts(self) -> TimeSeries:
        """
        Access the timeseries namespace, providing support for
        redis timeseries data.
        """
        ...
    def bf(self):
        """Access the bloom namespace."""
        ...
    def cf(self):
        """Access the bloom namespace."""
        ...
    def cms(self):
        """Access the bloom namespace."""
        ...
    def topk(self):
        """Access the bloom namespace."""
        ...
    def tdigest(self):
        """Access the bloom namespace."""
        ...
    def graph(self, index_name: str = "idx"):
        """
        Access the graph namespace, providing support for
        redis graph data.
        """
        ...
