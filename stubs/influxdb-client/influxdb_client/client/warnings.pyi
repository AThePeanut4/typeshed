"""The warnings message definition."""

class MissingPivotFunction(UserWarning):
    """User warning about missing pivot() function."""
    @staticmethod
    def print_warning(query: str):
        """Print warning about missing pivot() function and how to deal with that."""
        ...

class CloudOnlyWarning(UserWarning):
    """User warning about availability only on the InfluxDB Cloud."""
    @staticmethod
    def print_warning(api_name: str, doc_url: str):
        """Print warning about availability only on the InfluxDB Cloud."""
        ...
