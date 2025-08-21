"""
click_shell.decorators

Decorators to make using click_shell simpler and more similar to click.
"""

from collections.abc import Callable
from typing import Any

from click.decorators import _AnyCallable

from .core import Shell

def shell(name: str | None = None, **attrs: Any) -> Callable[[_AnyCallable], Shell]:
    """
    Creates a new :class:`Shell` with a function as callback.  This
    works otherwise the same as :func:`command` just that the `cls`
    parameter is set to :class:`Shell`.
    """
    ...
