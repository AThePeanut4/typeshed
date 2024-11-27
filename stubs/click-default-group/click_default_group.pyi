"""
click_default_group
~~~~~~~~~~~~~~~~~~~

Define a default subcommand by `default=True`:

.. sourcecode:: python

   import click
   from click_default_group import DefaultGroup

   @click.group(cls=DefaultGroup, default_if_no_args=True)
   def cli():
       pass

   @cli.command(default=True)
   def foo():
       click.echo('foo')

   @cli.command()
   def bar():
       click.echo('bar')

Then you can invoke that without explicit subcommand name:

.. sourcecode:: console

   $ cli.py --help
   Usage: cli.py [OPTIONS] COMMAND [ARGS]...

   Options:
     --help    Show this message and exit.

   Command:
     foo*
     bar

   $ cli.py
   foo
   $ cli.py foo
   foo
   $ cli.py bar
   bar
"""

import typing as t
from _typeshed import Incomplete

import click

__version__: str

class DefaultGroup(click.Group):
    """
    Invokes a subcommand marked with `default=True` if any subcommand not
    chosen.

    :param default_if_no_args: resolves to the default command if no arguments
                               passed.
    """
    ignore_unknown_options: bool
    default_cmd_name: str | None
    default_if_no_args: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def set_default_command(self, command: click.Command) -> None:
        """Sets a command function as the default command."""
        ...
    def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]: ...
    def get_command(self, ctx: click.Context, cmd_name: str) -> click.Command | None: ...
    def resolve_command(self, ctx: click.Context, args: list[str]) -> tuple[str | None, click.Command | None, list[str]]: ...
    def format_commands(self, ctx: click.Context, formatter: click.HelpFormatter) -> None: ...
    def command(self, *args, **kwargs) -> click.Command: ...  # incomplete

class DefaultCommandFormatter:
    """Wraps a formatter to mark a default command."""
    group: click.Group
    formatter: click.HelpFormatter
    mark: str
    def __init__(self, group: click.Group, formatter: click.HelpFormatter, mark: str = ...) -> None: ...
    def write_dl(self, rows: t.Sequence[tuple[str, str]], col_max: int = 30, col_spacing: int = -2) -> None: ...
    def __getattr__(self, attr: str) -> Incomplete: ...
    # __getattr__ used to ala-derive from click.HelpFormatter:
    # indent_increment: int
    # width: int | None
    # current_indent: int
    # buffer: t.List[str]
    # def write(self, string: str) -> None: ...
    # def indent(self) -> None: ...
    # def dedent(self) -> None: ...
    # def write_usage(self, prog: str, args: str = ..., prefix: str | None = ...) -> None: ...
    # def write_heading(self, heading: str) -> None: ...
    # def write_paragraph(self) -> None: ...
    # def write_text(self, text: str) -> None: ...
    # def section(self, name: str) -> t.Iterator[None]: ...
    # def indentation(self) -> t.Iterator[None]: ...
    # def getvalue(self) -> str: ...
