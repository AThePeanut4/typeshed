from typing import Any

import click

class FieldId:
    """
    Extract/serialize information from the encoded form input field name
    the parts:
        [command_index].[opt_or_arg_index].[click_type].[html_input_type].[opt_or_arg_name]
    e.g.
        "0.0.option.text.text.--an-option"
        "0.1.argument.file[rb].text.an-argument"
    """
    SEPARATOR: str

    def __init__(
        self,
        command_index: int,
        param_index: int,
        param_type: str,
        click_type: str,
        nargs: int,
        form_type: str,
        name: str,
        key: str | None = None,
    ):
        """the int index of the command it belongs to"""
        ...
    @classmethod
    def from_string(cls, field_info_as_string: str) -> FieldId: ...

class NotSupported(ValueError): ...

class BaseInput:
    param_type_cls: type | None
    def __init__(self, ctx: click.Context, param: click.Parameter, command_index: int, param_index: int) -> None: ...
    def is_supported(self) -> bool: ...
    @property
    def fields(self) -> dict[str, Any]: ...
    @property
    def type_attrs(self) -> dict[str, Any]:
        """Return the input type and type specific information as dict"""
        ...
    def _to_cmd_line_name(self, name: str) -> str: ...
    def _build_name(self, name: str):
        """
        Construct a name to use for field in form that have information about
        what sub-command it belongs to, order index (for later sorting) and type of parameter.
        """
        ...

class ChoiceInput(BaseInput): ...
class FlagInput(BaseInput): ...
class IntInput(BaseInput): ...
class FloatInput(BaseInput): ...
class FolderInput(BaseInput): ...
class FileInput(BaseInput): ...
class EmailInput(BaseInput): ...
class PasswordInput(BaseInput): ...
class TextAreaInput(BaseInput): ...
class DefaultInput(BaseInput): ...

INPUT_TYPES: list[type]
_DEFAULT_INPUT: list[type]

def get_input_field(ctx: click.Context, param: click.Parameter, command_index, param_index) -> dict[str, Any]:
    """Convert a click.Parameter into a dict structure describing a html form option"""
    ...
