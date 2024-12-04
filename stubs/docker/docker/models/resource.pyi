from typing import Any, Generic, NoReturn, TypeVar
from typing_extensions import Self

from docker import APIClient

_T = TypeVar("_T", bound=Model)

class Model:
    """A base class for representing a single object on the server."""
    id_attribute: str
    client: APIClient | None
    collection: Collection[Self] | None
    attrs: dict[str, Any]
    def __init__(
        self, attrs: dict[str, Any] | None = None, client: APIClient | None = None, collection: Collection[Self] | None = None
    ) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def id(self) -> str | None:
        """The ID of the object."""
        ...
    @property
    def short_id(self) -> str:
        """The ID of the object, truncated to 12 characters."""
        ...
    def reload(self) -> None:
        """
        Load this object from the server again and update ``attrs`` with the
        new data.
        """
        ...

class Collection(Generic[_T]):
    """
    A base class for representing all objects of a particular type on the
    server.
    """
    model: type[_T]
    client: APIClient
    def __init__(self, client: APIClient | None = None) -> None: ...
    def __call__(self, *args, **kwargs) -> NoReturn: ...
    def list(self) -> list[_T]: ...
    def get(self, key: str) -> _T: ...
    def create(self, attrs: Any | None = None) -> _T: ...
    def prepare_model(self, attrs: Model | dict[str, Any]) -> _T:
        """Create a model from a set of attributes."""
        ...
