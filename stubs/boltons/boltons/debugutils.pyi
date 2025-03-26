"""
A small set of utilities useful for debugging misbehaving
applications. Currently this focuses on ways to use :mod:`pdb`, the
built-in Python debugger.
"""

from collections.abc import Callable
from typing import Any

def pdb_on_signal(signalnum: int | None = None) -> None:
    """
    Installs a signal handler for *signalnum*, which defaults to
    ``SIGINT``, or keyboard interrupt/ctrl-c. This signal handler
    launches a :mod:`pdb` breakpoint. Results vary in concurrent
    systems, but this technique can be useful for debugging infinite
    loops, or easily getting into deep call stacks.

    Args:
        signalnum (int): The signal number of the signal to handle
            with pdb. Defaults to :mod:`signal.SIGINT`, see
            :mod:`signal` for more information.
    """
    ...
def pdb_on_exception(limit: int = 100) -> None:
    """
    Installs a handler which, instead of exiting, attaches a
    post-mortem pdb console whenever an unhandled exception is
    encountered.

    Args:
        limit (int): the max number of stack frames to display when
            printing the traceback

    A similar effect can be achieved from the command-line using the
    following command::

      python -m pdb your_code.py

    But ``pdb_on_exception`` allows you to do this conditionally and within
    your application. To restore default behavior, just do::

      sys.excepthook = sys.__excepthook__
    """
    ...
def wrap_trace(
    obj, hook: Callable[..., Any] = ..., which: str | None = None, events: str | None = None, label: str | None = None
): ...

__all__ = ["pdb_on_signal", "pdb_on_exception", "wrap_trace"]
