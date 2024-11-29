from _typeshed import StrOrBytesPath, StrPath
from collections.abc import Iterator
from typing_extensions import Self, deprecated

from _cffi_backend import _CDataBase

from ._pygit2 import Diff, Oid, Tree
from .enums import DiffOption, FileMode
from .repository import BaseRepository
from .utils import _IntoStrArray

class Index:
    def __init__(self, path: StrOrBytesPath | None = None) -> None:
        """
        Create a new Index

        If path is supplied, the read and write methods will use that path
        to read from and write to.
        """
        ...
    @classmethod
    def from_c(cls, repo: _CDataBase, ptr: _CDataBase) -> Index: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, path: StrOrBytesPath | None) -> bool: ...
    def __getitem__(self, key: StrPath | int) -> IndexEntry: ...
    def __iter__(self) -> Iterator[IndexEntry]: ...
    def read(self, force: bool = True) -> None:
        """
        Update the contents of the Index by reading from a file.

        Parameters:

        force
            If True (the default) always reload. If False, only if the file
            has changed.
        """
        ...
    def write(self) -> None:
        """Write the contents of the Index to disk."""
        ...
    def clear(self) -> None: ...
    def read_tree(self, tree: str | Oid | Tree) -> None:
        """
        Replace the contents of the Index with those of the given tree,
        expressed either as a <Tree> object or as an oid (string or <Oid>).

        The tree will be read recursively and all its children will also be
        inserted into the Index.
        """
        ...
    def write_tree(self, repo: BaseRepository | None = None) -> Oid:
        """
        Create a tree out of the Index. Return the <Oid> object of the
        written tree.

        The contents of the index will be written out to the object
        database. If there is no associated repository, 'repo' must be
        passed. If there is an associated repository and 'repo' is
        passed, then that repository will be used instead.

        It returns the id of the resulting tree.
        """
        ...
    def remove(self, path: StrOrBytesPath, level: int = 0) -> None:
        """Remove an entry from the Index."""
        ...
    def remove_all(self, pathspecs: _IntoStrArray) -> None:
        """Remove all index entries matching pathspecs."""
        ...
    def add_all(self, pathspecs: _IntoStrArray = None) -> None:
        """
        Add or update index entries matching files in the working directory.

        If pathspecs are specified, only files matching those pathspecs will
        be added.
        """
        ...
    def add(self, path_or_entry: IndexEntry | StrPath) -> None:
        """
        Add or update an entry in the Index.

        If a path is given, that file will be added. The path must be relative
        to the root of the worktree and the Index must be associated with a
        repository.

        If an IndexEntry is given, that entry will be added or update in the
        Index without checking for the existence of the path or id.
        """
        ...
    def diff_to_workdir(self, flags: DiffOption = ..., context_lines: int = 3, interhunk_lines: int = 0) -> Diff:
        """
        Diff the index against the working directory. Return a <Diff> object
        with the differences between the index and the working copy.

        Parameters:

        flags
            A combination of enums.DiffOption constants.

        context_lines
            The number of unchanged lines that define the boundary of a hunk
            (and to display before and after).

        interhunk_lines
            The maximum number of unchanged lines between hunk boundaries
            before the hunks will be merged into a one.
        """
        ...
    def diff_to_tree(self, tree: Tree, flags: DiffOption = ..., context_lines: int = 3, interhunk_lines: int = 0) -> Diff:
        """
        Diff the index against a tree.  Return a <Diff> object with the
        differences between the index and the given tree.

        Parameters:

        tree
            The tree to diff.

        flags
            A combination of enums.DiffOption constants.

        context_lines
            The number of unchanged lines that define the boundary of a hunk
            (and to display before and after).

        interhunk_lines
            The maximum number of unchanged lines between hunk boundaries
            before the hunks will be merged into a one.
        """
        ...
    @property
    def conflicts(self) -> ConflictCollection | None:
        """
        A collection of conflict information

        If there are no conflicts None is returned. Otherwise return an object
        that represents the conflicts in the index.

        This object presents a mapping interface with the paths as keys. You
        can use the ``del`` operator to remove a conflict from the Index.

        Each conflict is made up of three elements. Access or iteration
        of the conflicts returns a three-tuple of
        :py:class:`~pygit2.IndexEntry`. The first is the common
        ancestor, the second is the "ours" side of the conflict, and the
        third is the "theirs" side.

        These elements may be None depending on which sides exist for
        the particular conflict.
        """
        ...

class IndexEntry:
    path: str
    id: Oid
    mode: FileMode
    def __init__(self, path: str, object_id: Oid, mode: FileMode) -> None: ...
    @property
    def oid(self) -> Oid: ...
    @property
    @deprecated("Use str(entry.id)")
    def hex(self) -> str:
        """The id of the referenced object as a hex string"""
        ...
    def __eq__(self, other: object) -> bool: ...

class ConflictCollection:
    def __init__(self, index: Index) -> None: ...
    def __getitem__(self, path: StrOrBytesPath) -> tuple[IndexEntry, IndexEntry, IndexEntry]: ...
    def __delitem__(self, path: StrOrBytesPath) -> None: ...
    def __iter__(self) -> ConflictIterator: ...
    def __contains__(self, path: StrOrBytesPath) -> bool: ...

class ConflictIterator:
    def __init__(self, index: Index) -> None: ...
    def __del__(self) -> None: ...
    def next(self) -> tuple[IndexEntry, IndexEntry, IndexEntry]: ...
    def __next__(self) -> tuple[IndexEntry, IndexEntry, IndexEntry]: ...
    def __iter__(self) -> Self: ...
