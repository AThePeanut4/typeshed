"""
click_shell._compat

Compatibility things for python 2.6
"""

import types
from collections.abc import Callable
from typing import Any, Final

import click

PY2: Final = False

def get_method_type(func: Callable[..., Any], obj: object) -> types.MethodType: ...
def get_choices(cli: click.Command, prog_name: str, args: list[str], incomplete: str) -> list[str]:
    """This is identical to click._bashcomplete:get_choices in click 6.4+"""
    ...
