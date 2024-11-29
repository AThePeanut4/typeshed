class Path:
    """This class represents a path in a JSON value."""
    strPath: str
    @staticmethod
    def root_path() -> str:
        """Return the root path's string representation."""
        ...
    def __init__(self, path: str) -> None:
        """Make a new path based on the string representation in `path`."""
        ...
