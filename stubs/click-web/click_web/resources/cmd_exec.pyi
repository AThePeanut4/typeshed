import logging
from collections.abc import Generator
from typing import ClassVar, Final

from flask import Response

from .input_fields import FieldId

logger: logging.Logger | None

HTML_HEAD: Final[str]
HTML_TAIL: Final[str]

class Executor:
    RAW_CMD_PATH: ClassVar[str]
    returncode: int | None

    def __init__(self) -> None: ...
    def exec(self, command_path: str) -> Response: ...
    def _exec_raw(self, command: list[str]) -> Response: ...  # undocumented
    def _exec_html(self, command_path: str) -> Response: ...  # undocumented
    def _run_script_and_generate_stream(self) -> Generator[str]: ...  # undocumented
    def _create_cmd_header(self, commands: list[CmdPart]) -> str: ...  # undocumented
    def _create_result_footer(self) -> Generator[str]: ...  # undocumented

        :param command: the command line after the root command.
                        For example:
                         print-lines 5 --delay 1 --message Red
        """
        ...
    def _exec_html(self, command_path: str) -> Response:
        """
        Execute the command and stream the output from it as response
        :param command_path:
        """
        ...
    def _run_script_and_generate_stream(self) -> None:
        """Execute the command the via Popen and yield output"""
        ...
    def _create_cmd_header(self, commands: list[CmdPart]) -> str:
        """
        Generate a command header.
        Note:
            here we always allow to generate HTML as long as we have it between CLICK-WEB comments.
            This way the JS frontend can insert it in the correct place in the DOM.
        """
        ...
    def _create_result_footer(self) -> str:
        """
        Generate a footer.
        Note:
            here we always allow to generate HTML as long as we have it between CLICK-WEB comments.
            This way the JS frontend can insert it in the correct place in the DOM.
        """
        ...

def _get_download_link(field_info: FieldFileInfo) -> str:
    """Hack as url_for need request context"""
    ...

class CommandLineRaw:
    def __init__(self, script_file_path: str, command: str) -> None: ...
    def append(self, part: str, secret: bool = False) -> None: ...
    def get_commandline(self, obfuscate: bool = False) -> list[str]:
        """
        Return command line as a list of strings.
        obfuscate - not supported for this implementation
        """
        ...
    def get_download_field_infos(self) -> list[FieldInfo]: ...
    def after_script_executed(self) -> None: ...

class CommandLineForm:
    command_line_bulder: FormToCommandLineBuilder
    def __init__(self, script_file_path: str, commands: list[str]) -> None: ...
    def append(self, part: str, secret: bool = False) -> None: ...
    def get_commandline(self, obfuscate: bool = False) -> list[str]:
        """
        Return command line as a list of strings.
        obfuscate - if True secret parts like passwords are replaced with *****. Use for logging etc.
        """
        ...
    def get_download_field_infos(self) -> list[FieldInfo]: ...
    def after_script_executed(self) -> None:
        """Call this after the command has executed"""
        ...

def _get_python_interpreter() -> str: ...

class CmdPart:
    def __init__(self, part: str, secret: bool = False) -> None: ...

class FormToCommandLineBuilder:
    def __init__(self, command_line: CommandLineForm) -> None: ...
    def add_command_args(self, command_index: int) -> None:
        """
        Convert the post request into a list of command line arguments

        :param command_index: (int) the index for the command to get arguments for.
        """
        ...
    @staticmethod
    def _is_option(cmd_option: str) -> bool: ...
    def _process_option(self, field_info: FieldInfo) -> None: ...

class FieldInfo:
    param: FieldId
    key: str
    is_file: bool
    cmd_opt: str
    generate_download_link: bool
    @staticmethod
    def factory(key: str) -> FieldInfo: ...
    def __init__(self, param: FieldId) -> None: ...
    def before_script_execute(self) -> None: ...
    def after_script_executed(self) -> None: ...
    def __lt__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class FieldFileInfo(FieldInfo):
    mode: str
    generate_download_link: bool
    link_name: str
    file_path: str
    def __init__(self, fimeta: FieldId) -> None: ...
    def before_script_execute(self) -> None: ...
    @classmethod
    def temp_dir(cls) -> str: ...
    def save(self) -> None: ...

class FieldOutFileInfo(FieldFileInfo):
    file_suffix: str
    def __init__(self, fimeta: FieldId) -> None: ...
    def save(self) -> None: ...

class FieldPathInfo(FieldFileInfo):
    """
    Use for processing input fields of path type.
    Extracts the posted data to a temp folder.
    When script finished zip that folder and provide download link to zip file.
    """
    def save(self) -> None: ...
    def after_script_executed(self) -> None: ...

class FieldPathOutInfo(FieldOutFileInfo):
    """
    Use for processing output fields of path type.
    Create a folder and use as path to script.
    When script finished zip that folder and provide download link to zip file.
    """
    def save(self) -> None: ...
    def after_script_executed(self) -> None: ...

def zip_folder(folder_path: str, out_folder: str, out_prefix: str) -> str: ...
