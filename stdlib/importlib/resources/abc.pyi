import sys
from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from io import BufferedReader
from typing import IO, Any, Literal, Protocol, overload, runtime_checkable

if sys.version_info >= (3, 11):
    class ResourceReader(metaclass=ABCMeta):
        """Abstract base class for loaders to provide resource reading support."""
        @abstractmethod
        def open_resource(self, resource: str) -> IO[bytes]:
            """
            Return an opened, file-like object for binary reading.

            The 'resource' argument is expected to represent only a file name.
            If the resource cannot be found, FileNotFoundError is raised.
            """
            ...
        @abstractmethod
        def resource_path(self, resource: str) -> str: ...
        @abstractmethod
        def is_resource(self, path: str) -> bool: ...
        @abstractmethod
        def contents(self) -> Iterator[str]:
            """Return an iterable of entries in `package`."""
            ...

    @runtime_checkable
    class Traversable(Protocol):
        """
        An object with a subset of pathlib.Path methods suitable for
        traversing directories and opening files.

        Any exceptions that occur when accessing the backing resource
        may propagate unaltered.
        """
        @abstractmethod
        def is_dir(self) -> bool:
            """Return True if self is a directory"""
            ...
        @abstractmethod
        def is_file(self) -> bool:
            """Return True if self is a file"""
            ...
        @abstractmethod
        def iterdir(self) -> Iterator[Traversable]: ...
        @abstractmethod
        def joinpath(self, *descendants: str) -> Traversable: ...

        # The documentation and runtime protocol allows *args, **kwargs arguments,
        # but this would mean that all implementers would have to support them,
        # which is not the case.
        @overload
        @abstractmethod
        def open(self, mode: Literal["r"] = "r", *, encoding: str | None = None, errors: str | None = None) -> IO[str]:
            """
            mode may be 'r' or 'rb' to open as text or binary. Return a handle
            suitable for reading (same as pathlib.Path.open).

            When opening as text, accepts encoding parameters such as those
            accepted by io.TextIOWrapper.
            """
            ...
        @overload
        @abstractmethod
        def open(self, mode: Literal["rb"]) -> IO[bytes]:
            """
            mode may be 'r' or 'rb' to open as text or binary. Return a handle
            suitable for reading (same as pathlib.Path.open).

            When opening as text, accepts encoding parameters such as those
            accepted by io.TextIOWrapper.
            """
            ...
        @property
        @abstractmethod
        def name(self) -> str: ...
        def __truediv__(self, child: str, /) -> Traversable: ...
        @abstractmethod
        def read_bytes(self) -> bytes:
            """Read contents of self as bytes"""
            ...
        @abstractmethod
        def read_text(self, encoding: str | None = None) -> str:
            """Read contents of self as text"""
            ...

    class TraversableResources(ResourceReader):
        """
        The required interface for providing traversable
        resources.
        """
        @abstractmethod
        def files(self) -> Traversable:
            """Return a Traversable object for the loaded package."""
            ...
        def open_resource(self, resource: str) -> BufferedReader: ...
        def resource_path(self, resource: Any) -> str: ...
        def is_resource(self, path: str) -> bool: ...
        def contents(self) -> Iterator[str]: ...

    __all__ = ["ResourceReader", "Traversable", "TraversableResources"]
