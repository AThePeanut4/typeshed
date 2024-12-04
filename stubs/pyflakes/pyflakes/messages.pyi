"""Provide the class Message and its subclasses."""

import ast
from typing import Any, ClassVar

class Message:
    message: ClassVar[str]
    message_args: tuple[Any, ...]
    filename: Any
    lineno: int
    col: int
    def __init__(self, filename, loc: ast.AST) -> None: ...

class UnusedImport(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, name) -> None: ...

class RedefinedWhileUnused(Message):
    message_args: tuple[Any, int]
    def __init__(self, filename, loc: ast.AST, name, orig_loc: ast.AST) -> None: ...

class ImportShadowedByLoopVar(Message):
    message_args: tuple[Any, int]
    def __init__(self, filename, loc: ast.AST, name, orig_loc: ast.AST) -> None: ...

class ImportStarNotPermitted(Message):
    message_args: Any
    def __init__(self, filename, loc, modname) -> None: ...

class ImportStarUsed(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, modname) -> None: ...

class ImportStarUsage(Message):
    message_args: tuple[Any, Any]
    def __init__(self, filename, loc: ast.AST, name, from_list) -> None: ...

class UndefinedName(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, name) -> None: ...

class DoctestSyntaxError(Message):
    message_args: tuple[()]
    def __init__(self, filename, loc: ast.AST, position: tuple[int, int] | None = None) -> None: ...

class UndefinedExport(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, name) -> None: ...

class UndefinedLocal(Message):
    default: ClassVar[str]
    builtin: ClassVar[str]
    message_args: tuple[Any, int]
    def __init__(self, filename, loc: ast.AST, name, orig_loc: ast.AST) -> None: ...

class DuplicateArgument(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, name) -> None: ...

class MultiValueRepeatedKeyLiteral(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, key) -> None: ...

class MultiValueRepeatedKeyVariable(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, key) -> None: ...

class LateFutureImport(Message):
    message_args: tuple[()]
    def __init__(self, filename, loc: ast.AST) -> None: ...

class FutureFeatureNotDefined(Message):
    """An undefined __future__ feature name was imported."""
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, name) -> None: ...

class UnusedVariable(Message):
    """
    Indicates that a variable has been explicitly assigned to but not actually
    used.
    """
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, names) -> None: ...

class UnusedAnnotation(Message):
    """
    Indicates that a variable has been explicitly annotated to but not actually
    used.
    """
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, names) -> None: ...

class ReturnOutsideFunction(Message):
    """Indicates a return statement outside of a function/method."""
    ...
class YieldOutsideFunction(Message):
    """Indicates a yield or yield from statement outside of a function/method."""
    ...
class ContinueOutsideLoop(Message):
    """Indicates a continue statement outside of a while or for loop."""
    ...
class BreakOutsideLoop(Message):
    """Indicates a break statement outside of a while or for loop."""
    ...
class DefaultExceptNotLast(Message):
    """Indicates an except: block as not the last exception handler."""
    ...
class TwoStarredExpressions(Message):
    """Two or more starred expressions in an assignment (a, *b, *c = d)."""
    ...
class TooManyExpressionsInStarredAssignment(Message):
    """Too many expressions in an assignment with star-unpacking"""
    ...
class IfTuple(Message):
    """Conditional test is a non-empty tuple literal, which are always True."""
    ...
class AssertTuple(Message):
    """Assertion test is a non-empty tuple literal, which are always True."""
    ...

class ForwardAnnotationSyntaxError(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, annotation) -> None: ...

class RaiseNotImplemented(Message): ...
class InvalidPrintSyntax(Message): ...
class IsLiteral(Message): ...
class FStringMissingPlaceholders(Message): ...

class StringDotFormatExtraPositionalArguments(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, extra_positions) -> None: ...

class StringDotFormatExtraNamedArguments(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, extra_keywords) -> None: ...

class StringDotFormatMissingArgument(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, missing_arguments) -> None: ...

class StringDotFormatMixingAutomatic(Message): ...

class StringDotFormatInvalidFormat(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, error) -> None: ...

class PercentFormatInvalidFormat(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, error) -> None: ...

class PercentFormatMixedPositionalAndNamed(Message): ...

class PercentFormatUnsupportedFormatCharacter(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, c) -> None: ...

class PercentFormatPositionalCountMismatch(Message):
    message_args: tuple[int, int]
    def __init__(self, filename, loc: ast.AST, n_placeholders: int, n_substitutions: int) -> None: ...

class PercentFormatExtraNamedArguments(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, extra_keywords) -> None: ...

class PercentFormatMissingArgument(Message):
    message_args: tuple[Any]
    def __init__(self, filename, loc: ast.AST, missing_arguments) -> None: ...

class PercentFormatExpectedMapping(Message): ...
class PercentFormatExpectedSequence(Message): ...
class PercentFormatStarRequiresSequence(Message): ...
