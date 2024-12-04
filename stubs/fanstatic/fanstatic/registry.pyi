from abc import abstractmethod
from collections.abc import Iterable
from threading import Lock
from typing import Any, ClassVar, Literal, Protocol, TypeVar
from typing_extensions import Self

from fanstatic.compiler import Compiler, Minifier
from fanstatic.core import Library
from fanstatic.injector import InjectorPlugin
from pkg_resources import EntryPoint

class _HasName(Protocol):
    @property
    def name(self) -> str: ...

_NamedT = TypeVar("_NamedT", bound=_HasName)

prepare_lock: Lock

class Registry(dict[str, _NamedT]):
    @property
    @abstractmethod
    def ENTRY_POINT(self) -> str: ...
    def __init__(self, items: Iterable[_NamedT] = ()) -> None: ...
    def add(self, item: _NamedT) -> None: ...
    def load_items_from_entry_points(self) -> None: ...
    def make_item_from_entry_point(self, entry_point: EntryPoint) -> Any: ...
    @classmethod
    def instance(cls) -> Self: ...

class LibraryRegistry(Registry[Library]):
    """
    A dictionary-like registry of libraries.

    This is a dictionary that maintains libraries. A value is a
    :py:class:`Library` instance, and a key is its library ``name``.

    Normally there is only a single global LibraryRegistry,
    obtained by calling ``get_library_registry()``.

    :param libraries: a sequence of libraries
    """
    ENTRY_POINT: ClassVar[Literal["fanstatic.libraries"]]
    prepared: bool
    def prepare(self) -> None: ...

get_library_registry = LibraryRegistry.instance

class CompilerRegistry(Registry[Compiler]):
    ENTRY_POINT: ClassVar[Literal["fanstatic.compilers"]]

class MinifierRegistry(Registry[Minifier]):
    ENTRY_POINT: ClassVar[Literal["fanstatic.minifiers"]]

class InjectorRegistry(Registry[InjectorPlugin]):
    ENTRY_POINT: ClassVar[Literal["fanstatic.injectors"]]
