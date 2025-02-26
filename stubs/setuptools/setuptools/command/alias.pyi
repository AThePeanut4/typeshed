from _typeshed import Incomplete
from typing import ClassVar

from .setopt import option_base

def shquote(arg):
    """Quote an argument for later parsing by shlex.split()"""
    ...

class alias(option_base):
    """Define a shortcut that invokes one or more commands"""
    description: str
    command_consumes_arguments: bool
    user_options: ClassVar[list[tuple[str, str, str]]]
    boolean_options: ClassVar[list[str]]
    args: Incomplete
    remove: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

def format_alias(name, aliases): ...
