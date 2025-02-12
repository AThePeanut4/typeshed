"""
Top-level module for Flake8.

This module

- initializes logging for the command-line tool
- tracks the version of the package
- provides a way to configure logging for the command-line tool

.. autofunction:: flake8.configure_logging
"""

from logging import Logger

LOG: Logger
__version__: str
__version_info__: tuple[int, int, int]
LOG_FORMAT: str

def configure_logging(verbosity: int, filename: str | None = None, logformat: str = ...) -> None:
    """
    Configure logging for flake8.

    :param verbosity:
        How verbose to be in logging information.
    :param filename:
        Name of the file to append log information to.
        If ``None`` this will log to ``sys.stderr``.
        If the name is "stdout" or "stderr" this will log to the appropriate
        stream.
    """
    ...
