"""
Functions for working with filesystem paths.

The :func:`expandpath` function expands the tilde to $HOME and environment
variables to their values.

The :func:`augpath` function creates variants of an existing path without
having to spend multiple lines of code splitting it up and stitching it back
together.

The :func:`shrinkuser` function replaces your home directory with a tilde.
"""

from _typeshed import StrPath

def augpath(
    path: StrPath,
    suffix: str = "",
    prefix: str = "",
    ext: str | None = None,
    base: str | None = None,
    dpath: str | None = None,
    multidot: bool = False,
) -> str: ...
def shrinkuser(path: StrPath, home: str = "~") -> str: ...
def expandpath(path: StrPath) -> str: ...

__all__ = ["augpath", "shrinkuser", "expandpath"]
