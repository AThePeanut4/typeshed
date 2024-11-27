from typing import Any
from typing_extensions import Self

from requests import Response, Session
from requests.sessions import _Auth, _Data, _Files

from .serialize import Serializer

__all__ = ["Resource", "API"]

class ResourceAttributesMixin:
    """
    A Mixin that allows access to an undefined attribute on a class.
    Instead of raising an attribute error, the undefined attribute will
    return a Resource Instance which can be used to make calls to the
    resource identified by the attribute.

    The type of the resource returned can be overridden by adding a
    resource_class attribute.

    It assumes that a Meta class exists at self._meta with all the required
    attributes.
    """
    # Exists at runtime:
    def __getattr__(self, item: str) -> Any: ...

class Resource(ResourceAttributesMixin):
    """
    Resource provides the main functionality behind slumber. It handles the
    attribute -> url, kwarg -> query param, and other related behind the scenes
    python to HTTP transformations. It's goal is to represent a single resource
    which may or may not have children.

    It assumes that a Meta class exists at self._meta with all the required
    attributes.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, id: str | None = None, format: str | None = None, url_override: str | None = None) -> Self:
        """
        Returns a new instance of self modified by one or more of the available
        parameters. These allows us to do things like override format for a
        specific request, and enables the api.resource(ID).get() syntax to get
        a specific resource by it's ID.
        """
        ...
    def as_raw(self) -> Self: ...
    def get(self, **kwargs: Any) -> Response: ...
    def options(self, **kwargs: Any) -> Response: ...
    def head(self, **kwargs: Any) -> Response: ...
    def post(self, data: _Data | None = None, files: _Files | None = None, **kwargs: Any) -> Response: ...
    def patch(self, data: _Data | None = None, files: _Files | None = None, **kwargs: Any) -> Response: ...
    def put(self, data: _Data | None = None, files: _Files | None = None, **kwargs: Any) -> Response: ...
    def delete(self, **kwargs: Any) -> Response: ...
    def url(self) -> str: ...

class API(ResourceAttributesMixin):
    resource_class: type[Resource]
    def __init__(
        self,
        base_url: str | None = None,
        auth: _Auth | None = None,
        format: str | None = None,
        append_slash: bool = True,
        session: Session | None = None,
        serializer: Serializer | None = None,
        raw: bool = ...,
    ) -> None: ...
