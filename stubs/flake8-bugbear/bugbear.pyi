import argparse
import ast
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any

class BugBearChecker:
    name: str
    version: str
    tree: ast.AST | None
    filename: str
    lines: Sequence[str] | None
    max_line_length: int
    visitor: ast.NodeVisitor
    options: argparse.Namespace | None
    def run(self) -> None: ...
    @staticmethod
    def add_options(optmanager: Any) -> None:
        """Informs flake8 to ignore B9xx by default."""
        ...
    def __init__(
        self,
        tree: ast.AST | None = ...,
        filename: str = ...,
        lines: Sequence[str] | None = ...,
        max_line_length: int = ...,
        options: argparse.Namespace | None = ...,
    ) -> None:
        """Method generated by attrs for class BugBearChecker."""
        ...
    def __getattr__(self, name: str) -> Incomplete: ...  # incomplete (other attributes are normally not accessed)

def __getattr__(name: str) -> Incomplete: ...
