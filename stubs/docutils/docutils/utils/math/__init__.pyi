from typing import Final, Literal

from docutils.nodes import Node

__docformat__: Final = "reStructuredText"

class MathError(ValueError):
    """
    Exception for math syntax and math conversion errors.

    The additional attribute `details` may hold a list of Docutils
    nodes suitable as children for a ``<system_message>``.
    """
    details: list[Node]
    def __init__(self, msg: object, details: list[Node] = []) -> None: ...

def toplevel_code(code: str) -> str:
    """Return string (LaTeX math) `code` with environments stripped out."""
    ...
def pick_math_environment(code: str, numbered: bool = False) -> Literal["align*", "equation*", "align", "equation"]:
    r"""
    Return the right math environment to display `code`.

    The test simply looks for line-breaks (``\``) outside environments.
    Multi-line formulae are set with ``align``, one-liners with
    ``equation``.

    If `numbered` evaluates to ``False``, the "starred" versions are used
    to suppress numbering.
    """
    ...
def wrap_math_code(code: str, as_block: bool | None) -> str: ...
