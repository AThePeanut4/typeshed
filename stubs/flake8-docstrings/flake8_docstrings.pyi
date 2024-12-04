"""
Implementation of pydocstyle integration with Flake8.

pydocstyle docstrings convention needs error code and class parser for be
included as module into flake8
"""

import argparse
import ast
from _typeshed import Incomplete
from collections.abc import Generator, Iterable
from typing import Any, ClassVar

class pep257Checker:
    """Flake8 needs a class to check python file."""
    name: ClassVar[str]
    version: ClassVar[str]
    tree: ast.AST
    filename: str
    checker: Any
    source: str
    def __init__(self, tree: ast.AST, filename: str, lines: Iterable[str]) -> None:
        """Initialize the checker."""
        ...
    @classmethod
    def add_options(cls, parser: Any) -> None:
        """Add plugin configuration option to flake8."""
        ...
    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None:
        """Parse the configuration options given to flake8."""
        ...
    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        """Use directly check() api from pydocstyle."""
        ...

def __getattr__(name: str) -> Incomplete: ...
