"""
click_shell.core

Core functionality for click-shell
"""

from collections.abc import Callable
from logging import Logger
from typing import Any

import click

from ._cmd import ClickCmd

logger: Logger

def get_invoke(command: click.Command) -> Callable[[ClickCmd, str], bool]:
    """
    Get the Cmd main method from the click command
    :param command: The click Command object
    :return: the do_* method for Cmd
    :rtype: function
    """
    ...
def get_help(command: click.Command) -> Callable[[ClickCmd], None]:
    """
    Get the Cmd help function from the click command
    :param command: The click Command object
    :return: the help_* method for Cmd
    :rtype: function
    """
    ...
def get_complete(command: click.Command) -> Callable[[ClickCmd, str, str, int, int], list[str]]:
    """
    Get the Cmd complete function for the click command
    :param command: The click Command object
    :return: the complete_* method for Cmd
    :rtype: function
    """
    ...

class ClickShell(ClickCmd):
    def add_command(self, cmd: click.Command, name: str) -> None: ...

def make_click_shell(
    ctx: click.Context,
    prompt: str | Callable[[], str] | Callable[[click.Context, str], str] | None = None,
    intro: str | None = None,
    hist_file: str | None = None,
) -> ClickShell: ...

class Shell(click.Group):
    def __init__(
        self,
        prompt: str | Callable[[], str] | Callable[[click.Context, str], str] | None = None,
        intro: str | None = None,
        hist_file: str | None = None,
        on_finished: Callable[[click.Context], None] | None = None,
        **attrs: Any,
    ) -> None: ...
    def add_command(self, cmd: click.Command, name: str | None = None) -> None: ...
    def invoke(self, ctx: click.Context) -> Any: ...
