"""Implementation of the command-line I{pyflakes} tool."""

__all__ = ["check", "checkPath", "checkRecursive", "iterSourceCode", "main"]
from pyflakes.api import (
    check as check,
    checkPath as checkPath,
    checkRecursive as checkRecursive,
    iterSourceCode as iterSourceCode,
    main as main,
)
