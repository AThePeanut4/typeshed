"""Checker of PEP-8 Naming Conventions."""

import argparse
import ast
import optparse
from collections import deque
from collections.abc import Callable, Generator, Iterable, Sequence
from typing import Final, Literal
from typing_extensions import Self

__version__: Final[str]

CLASS_METHODS: Final[frozenset[Literal["__new__", "__init_subclass__", "__class_getitem__"]]]
METACLASS_BASES: Final[frozenset[Literal["type", "ABCMeta"]]]
METHOD_CONTAINER_NODES: Final[set[ast.AST]]
FUNC_NODES: Final[tuple[type[ast.FunctionDef], type[ast.AsyncFunctionDef]]]

class _ASTCheckMeta(type):
    codes: tuple[str, ...]
    all: list[BaseASTCheck]
    def __init__(cls, class_name: str, bases: tuple[object, ...], namespace: Iterable[str]) -> None: ...

class BaseASTCheck(metaclass=_ASTCheckMeta):
    """Base for AST Checks."""
    codes: tuple[str, ...]
    all: list[BaseASTCheck]
    def err(self, node: ast.AST, code: str, **kwargs: str) -> tuple[int, int, str, Self]: ...

class NamingChecker:
    """Checker of PEP-8 Naming Conventions."""
    name: str
    version: str
    visitors: Sequence[BaseASTCheck]
    decorator_to_type: dict[str, Literal["classmethod", "staticmethod"]]
    ignore_names: frozenset[str]
    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: optparse.OptionParser) -> None: ...
    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, Self]] | tuple[()]: ...
    def visit_tree(self, node: ast.AST, parents: deque[ast.AST]) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_node(self, node: ast.AST, parents: Sequence[ast.AST]) -> Generator[tuple[int, int, str, Self]]: ...
    def tag_class_functions(self, cls_node: ast.ClassDef) -> None:
        """Tag functions if they are methods, classmethods, staticmethods"""
        ...
    def set_function_nodes_types(self, nodes: Iterable[ast.AST], ismetaclass: bool, late_decoration: dict[str, str]) -> None: ...
    @classmethod
    def find_decorator_name(cls, d: ast.Expr) -> str: ...
    @staticmethod
    def find_global_defs(func_def_node: ast.AST) -> None: ...

class ClassNameCheck(BaseASTCheck):
    """
    Almost without exception, class names use the CapWords convention.

    Classes for internal use have a leading underscore in addition.
    """
    codes: tuple[Literal["N801"], Literal["N818"]]
    N801: str
    N818: str
    @classmethod
    def get_classdef(cls, name: str, parents: Sequence[ast.AST]) -> ast.ClassDef | None: ...
    @classmethod
    def superclass_names(cls, name: str, parents: Sequence[ast.AST], _names: set[str] | None = None) -> set[str]: ...
    def visit_classdef(
        self, node: ast.ClassDef, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...

class FunctionNameCheck(BaseASTCheck):
    """
    Function names should be lowercase, with words separated by underscores
    as necessary to improve readability.

    Functions *not* being methods '__' in front and back are not allowed.

    mixedCase is allowed only in contexts where that's already the
    prevailing style (e.g. threading.py), to retain backwards compatibility.
    """
    codes: tuple[Literal["N802"], Literal["N807"]]
    N802: str
    N807: str
    @staticmethod
    def has_override_decorator(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool: ...
    def visit_functiondef(
        self, node: ast.FunctionDef, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_asyncfunctiondef(
        self, node: ast.AsyncFunctionDef, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...

class FunctionArgNamesCheck(BaseASTCheck):
    """
    The argument names of a function should be lowercase, with words separated
    by underscores.

    A classmethod should have 'cls' as first argument.
    A method should have 'self' as first argument.
    """
    codes: tuple[Literal["N803"], Literal["N804"], Literal["N805"]]
    N803: str
    N804: str
    N805: str
    def visit_functiondef(
        self, node: ast.FunctionDef, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_asyncfunctiondef(
        self, node: ast.AsyncFunctionDef, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...

class ImportAsCheck(BaseASTCheck):
    """Don't change the naming convention via an import"""
    codes: tuple[Literal["N811"], Literal["N812"], Literal["N813"], Literal["N814"], Literal["N817"]]
    N811: str
    N812: str
    N813: str
    N814: str
    N817: str
    def visit_importfrom(
        self, node: ast.ImportFrom, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_import(
        self, node: ast.Import, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...

class VariablesCheck(BaseASTCheck):
    """Class attributes and local variables in functions should be lowercase"""
    codes: tuple[Literal["N806"], Literal["N815"], Literal["N816"]]
    N806: str
    N815: str
    N816: str
    @staticmethod
    def is_namedtupe(node_value: ast.AST) -> bool: ...
    def visit_assign(
        self, node: ast.Assign, parents: Sequence[ast.AST], ignore: Iterable[str] | None = None
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_namedexpr(
        self, node: ast.NamedExpr, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_annassign(
        self, node: ast.AnnAssign, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_with(
        self, node: ast.With, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_asyncwith(
        self, node: ast.AsyncWith, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_for(
        self, node: ast.For, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_asyncfor(
        self, node: ast.AsyncFor, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_excepthandler(
        self, node: ast.ExceptHandler, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_generatorexp(
        self, node: ast.GeneratorExp, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_listcomp(
        self, node: ast.ListComp, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_dictcomp(
        self, node: ast.DictComp, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    def visit_setcomp(
        self, node: ast.SetComp, parents: Sequence[ast.AST], ignore: Iterable[str]
    ) -> Generator[tuple[int, int, str, Self]]: ...
    @staticmethod
    def global_variable_check(name: str) -> Literal["N816"] | None: ...
    @staticmethod
    def class_variable_check(name: str) -> Literal["N815"] | None: ...
    @staticmethod
    def function_variable_check(func: Callable[..., object], var_name: str) -> Literal["N806"] | None: ...

def is_mixed_case(name: str) -> bool: ...
