"""Simplified function-based API for importlib.resources"""

import sys

# Even though this file is 3.13+ only, Pyright will complain in stubtest for older versions.
if sys.version_info >= (3, 13):
    from _typeshed import StrPath
    from collections.abc import Iterator
    from contextlib import AbstractContextManager
    from importlib.resources._common import Anchor
    from io import TextIOWrapper
    from pathlib import Path
    from typing import BinaryIO, Literal, overload
    from typing_extensions import Unpack, deprecated

    def open_binary(anchor: Anchor, *path_names: StrPath) -> BinaryIO:
        """Open for binary reading the *resource* within *package*."""
        ...
    @overload
    def open_text(
        anchor: Anchor, *path_names: Unpack[tuple[StrPath]], encoding: str | None = "utf-8", errors: str | None = "strict"
    ) -> TextIOWrapper:
        """Open for text reading the *resource* within *package*."""
        ...
    @overload
    def open_text(anchor: Anchor, *path_names: StrPath, encoding: str | None, errors: str | None = "strict") -> TextIOWrapper:
        """Open for text reading the *resource* within *package*."""
        ...
    def read_binary(anchor: Anchor, *path_names: StrPath) -> bytes:
        """Read and return contents of *resource* within *package* as bytes."""
        ...
    @overload
    def read_text(
        anchor: Anchor, *path_names: Unpack[tuple[StrPath]], encoding: str | None = "utf-8", errors: str | None = "strict"
    ) -> str:
        """Read and return contents of *resource* within *package* as str."""
        ...
    @overload
    def read_text(anchor: Anchor, *path_names: StrPath, encoding: str | None, errors: str | None = "strict") -> str: ...
    def path(anchor: Anchor, *path_names: StrPath) -> AbstractContextManager[Path, Literal[False]]: ...
    def is_resource(anchor: Anchor, *path_names: StrPath) -> bool: ...
    @deprecated("Deprecated since Python 3.11. Use `files(anchor).iterdir()`.")
    def contents(anchor: Anchor, *path_names: StrPath) -> Iterator[str]: ...
