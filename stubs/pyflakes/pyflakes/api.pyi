"""API for the command-line I{pyflakes} tool."""

from _typeshed import Incomplete
from collections.abc import Iterable, Iterator, Sequence
from re import Pattern

from pyflakes.reporter import Reporter

__all__ = ["check", "checkPath", "checkRecursive", "iterSourceCode", "main"]

PYTHON_SHEBANG_REGEX: Pattern[bytes]

def check(codeString: str, filename: str, reporter: Reporter | None = None) -> int:
    """
    Check the Python source given by C{codeString} for flakes.

    @param codeString: The Python source to check.
    @type codeString: C{str}

    @param filename: The name of the file the source came from, used to report
        errors.
    @type filename: C{str}

    @param reporter: A L{Reporter} instance, where errors and warnings will be
        reported.

    @return: The number of warnings emitted.
    @rtype: C{int}
    """
    ...
def checkPath(filename, reporter: Reporter | None = None) -> int:
    """
    Check the given path, printing out any warnings detected.

    @param reporter: A L{Reporter} instance, where errors and warnings will be
        reported.

    @return: the number of warnings printed
    """
    ...
def isPythonFile(filename) -> bool:
    """Return True if filename points to a Python file."""
    ...
def iterSourceCode(paths: Iterable[Incomplete]) -> Iterator[Incomplete]:
    """
    Iterate over all Python source files in C{paths}.

    @param paths: A list of paths.  Directories will be recursed into and
        any .py files found will be yielded.  Any non-directories will be
        yielded as-is.
    """
    ...
def checkRecursive(paths: Iterable[Incomplete], reporter: Reporter) -> int:
    """
    Recursively check all source files in C{paths}.

    @param paths: A list of paths to Python source files and directories
        containing Python source files.
    @param reporter: A L{Reporter} where all of the warnings and errors
        will be reported to.
    @return: The number of warnings found.
    """
    ...
def main(prog: str | None = None, args: Sequence[Incomplete] | None = None) -> None:
    """Entry point for the script "pyflakes"."""
    ...
