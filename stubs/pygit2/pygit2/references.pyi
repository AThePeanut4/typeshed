from collections.abc import Iterator

from ._pygit2 import Oid, Reference
from .enums import ReferenceFilter
from .repository import BaseRepository

class References:
    def __init__(self, repository: BaseRepository) -> None: ...
    def __getitem__(self, name: str) -> Reference: ...
    def get(self, key: str) -> Reference | None: ...
    def __iter__(self) -> Iterator[Reference]: ...
    def iterator(self, references_return_type: ReferenceFilter = ...) -> Iterator[Reference]:
        """
        Creates a new iterator and fetches references for a given repository.

        Can also filter and pass all refs or only branches or only tags.

        Parameters:

        references_return_type: ReferenceFilter
            Optional specifier to filter references. By default, all references are
            returned.

            The following values are accepted:
            - ReferenceFilter.ALL, fetches all refs, this is the default
            - ReferenceFilter.BRANCHES, fetches only branches
            - ReferenceFilter.TAGS, fetches only tags

        TODO: Add support for filtering by reference types notes and remotes.
        """
        ...
    def create(self, name: str, target: Oid | str, force: bool = False) -> Reference: ...
    def delete(self, name: str) -> None: ...
    def __contains__(self, name: str) -> bool: ...
    @property
    def objects(self) -> list[Reference]: ...
    def compress(self) -> None: ...
