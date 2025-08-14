"""
Command-line and common processing for Docutils front-end tools.

This module is provisional.
Major changes will happen with the switch from the deprecated
"optparse" module to "arparse".

Applications should use the high-level API provided by `docutils.core`.
See https://docutils.sourceforge.io/docs/api/runtime-settings.html.

Exports the following classes:

* `OptionParser`: Standard Docutils command-line processing.
  Deprecated. Will be replaced by an ArgumentParser.
* `Option`: Customized version of `optparse.Option`; validation support.
  Deprecated. Will be removed.
* `Values`: Runtime settings; objects are simple structs
  (``object.attribute``).  Supports cumulative list settings (attributes).
  Deprecated. Will be removed.
* `ConfigParser`: Standard Docutils config file processing.
  Provisional. Details will change.

Also exports the following functions:

Interface function:
  `get_default_settings()`.  New in 0.19.

Option callbacks:
  `store_multiple()`, `read_config_file()`. Deprecated.

Setting validators:
  `validate_encoding()`, `validate_encoding_error_handler()`,
  `validate_encoding_and_error_handler()`,
  `validate_boolean()`, `validate_ternary()`,
  `validate_nonnegative_int()`, `validate_threshold()`,
  `validate_colon_separated_string_list()`,
  `validate_comma_separated_list()`,
  `validate_url_trailing_slash()`,
  `validate_dependency_file()`,
  `validate_strip_class()`
  `validate_smartquotes_locales()`.

  Provisional.

Misc:
  `make_paths_absolute()`, `filter_settings_spec()`. Provisional.
"""

import optparse
from _typeshed import Incomplete, StrPath
from collections.abc import Iterable, Mapping, Sequence
from configparser import RawConfigParser
from typing import Any, ClassVar, Final, Literal, Protocol, overload, type_check_only
from typing_extensions import deprecated

from docutils import SettingsSpec
from docutils.utils import DependencyList

__docformat__: Final = "reStructuredText"

@type_check_only
class _OptionValidator(Protocol):
    def __call__(
        self,
        setting: str,
        value: str | None,
        option_parser: OptionParser,
        /,
        config_parser: ConfigParser | None = None,
        config_section: str | None = None,
    ) -> Any: ...

@deprecated("Deprecated and will be removed with the switch to from optparse to argparse.")
def store_multiple(option: optparse.Option, opt: str, value, parser: OptionParser, *args: str, **kwargs) -> None: ...
@deprecated("Deprecated and will be removed with the switch to from optparse to argparse.")
def read_config_file(option: optparse.Option, opt: str, value, parser: OptionParser) -> None: ...
def validate_encoding(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_encoding_error_handler(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_encoding_and_error_handler(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_boolean(
    setting: str | bool,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> bool: ...
def validate_ternary(
    setting: str | bool,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str | bool | None: ...
def validate_nonnegative_int(
    setting: str | int,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> int: ...
def validate_threshold(
    setting: str | int,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> int: ...
def validate_colon_separated_string_list(
    setting: str | list[str],
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[str]: ...
def validate_comma_separated_list(
    setting: str | list[str],
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[str]: ...
def validate_math_output(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> tuple[()] | tuple[str, str]: ...
def validate_url_trailing_slash(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> str: ...
def validate_dependency_file(
    setting: str | None,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> DependencyList: ...
def validate_strip_class(
    setting: str,
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[str]: ...
def validate_smartquotes_locales(
    setting: str | list[str | tuple[str, str]],
    value: str | None = None,
    option_parser: OptionParser | None = None,
    config_parser: ConfigParser | None = None,
    config_section: str | None = None,
) -> list[tuple[str, Sequence[str]]]: ...
def make_paths_absolute(
    pathdict: dict[str, list[StrPath] | StrPath], keys: tuple[str], base_path: StrPath | None = None
) -> None: ...
@deprecated("The `frontend.make_one_path_absolute` will be removed in Docutils 2.0 or later.")
def make_one_path_absolute(base_path: StrPath, path: StrPath) -> str: ...
def filter_settings_spec(settings_spec, *exclude, **replace) -> tuple[Any, ...]: ...
@deprecated("The `frontend.Values` class will be removed in Docutils 2.0 or later.")
class Values(optparse.Values):
    record_dependencies: DependencyList
    def __init__(self, defaults: dict[str, Any] | None = None) -> None: ...
    def update(self, other_dict: Values | Mapping[str, Incomplete], option_parser: OptionParser) -> None: ...
    def copy(self) -> Values: ...
    def setdefault(self, name: str, default): ...

@deprecated("The `frontend.Option` class will be removed in Docutils 2.0 or later.")
class Option(optparse.Option):
    ATTRS: list[str]
    validator: _OptionValidator
    overrides: str | None
    def __init__(self, *args: str | None, **kwargs) -> None: ...

@deprecated(
    "The `frontend.OptionParser` class will be replaced by a subclass of `argparse.ArgumentParser` in Docutils 2.0 or later."
)
class OptionParser(optparse.OptionParser, SettingsSpec):
    """
    Settings parser for command-line and library use.

    The `settings_spec` specification here and in other Docutils components
    are merged to build the set of command-line options and runtime settings
    for this process.

    Common settings (defined below) and component-specific settings must not
    conflict.  Short options are reserved for common settings, and components
    are restricted to using long options.

    Deprecated.
    Will be replaced by a subclass of `argparse.ArgumentParser`.
    """
    standard_config_files: ClassVar[list[str]]
    threshold_choices: ClassVar[tuple[str, ...]]
    thresholds: ClassVar[dict[str, int]]
    booleans: ClassVar[dict[str, bool]]
    default_error_encoding: ClassVar[str]
    default_error_encoding_error_handler: ClassVar[str]
    config_section: ClassVar[str]
    version_template: ClassVar[str]
    details: str
    lists: dict[str, Literal[True]]
    config_files: list[str]
    relative_path_settings: ClassVar[tuple[str, ...]]
    version: str
    components: tuple[SettingsSpec, ...]
    def __init__(
        self,
        components: Iterable[SettingsSpec | type[SettingsSpec]] = (),
        defaults: Mapping[str, Any] | None = None,
        read_config_files: bool | None = False,
        *args,
        **kwargs,
    ) -> None: ...
    def populate_from_components(self, components: Iterable[SettingsSpec]) -> None: ...
    @classmethod
    def get_standard_config_files(cls) -> Sequence[StrPath]: ...
    def get_standard_config_settings(self) -> Values: ...
    def get_config_file_settings(self, config_file: str) -> dict[str, Incomplete]: ...
    def check_values(self, values: Values, args: list[str]) -> Values: ...  # type: ignore[override]
    def check_args(self, args: list[str]) -> tuple[str | None, str | None]: ...
    def get_default_values(self) -> Values: ...
    def get_option_by_dest(self, dest: str) -> Option: ...

class ConfigParser(RawConfigParser):
    old_settings: ClassVar[dict[str, tuple[str, str]]]
    old_warning: ClassVar[str]
    not_utf8_error: ClassVar[str]
    @overload  # type: ignore[override]
    def read(self, filenames: str | Sequence[str], option_parser: None = None) -> list[str]: ...
    @overload
    @deprecated("The `option_parser` parameter is deprecated and will be removed in Docutils 0.24.")
    def read(self, filenames: str | Sequence[str], option_parser: OptionParser = ...) -> list[str]: ...
    def handle_old_config(self, filename: str) -> None: ...
    def validate_settings(self, filename: str, option_parser: OptionParser) -> None: ...
    def optionxform(self, optionstr: str) -> str: ...

        So the cmdline form of option names can be used in config files.
        """
        ...
    def get_section(self, section):
        """
        Return a given section as a dictionary.

def get_default_settings(*components: SettingsSpec) -> Values: ...
