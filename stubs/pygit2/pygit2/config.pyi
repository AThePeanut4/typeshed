from _typeshed import StrOrBytesPath
from typing_extensions import Self

from _cffi_backend import _CDataBase

def str_to_bytes(value: str, name: object) -> bytes: ...

class ConfigIterator:
    def __init__(self, config: _CDataBase, ptr: _CDataBase) -> None: ...
    def __del__(self) -> None: ...
    def __iter__(self) -> Self: ...
    def next(self) -> ConfigEntry: ...
    def __next__(self) -> ConfigEntry: ...

class ConfigMultivarIterator(ConfigIterator):
    def __next__(self) -> str: ...  # type: ignore[override]

class Config:
    """Git configuration management."""
    def __init__(self, path: str | None = None) -> None: ...
    @classmethod
    def from_c(cls, repo: _CDataBase, ptr: _CDataBase) -> Config: ...
    def __del__(self) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str:
        """
        When using the mapping interface, the value is returned as a string. In
        order to apply the git-config parsing rules, you can use
        :meth:`Config.get_bool` or :meth:`Config.get_int`.
        """
        ...
    def __setitem__(self, key: str, value: bool | int | _CDataBase | StrOrBytesPath | None) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> ConfigIterator:
        """
        Iterate over configuration entries, returning a ``ConfigEntry``
        objects. These contain the name, level, and value of each configuration
        variable. Be aware that this may return multiple versions of each entry
        if they are set multiple times in the configuration files.
        """
        ...
    def get_multivar(self, name: str, regex: str | None = None) -> ConfigMultivarIterator:
        """
        Get each value of a multivar ''name'' as a list of strings.

        The optional ''regex'' parameter is expected to be a regular expression
        to filter the variables we're interested in.
        """
        ...
    def set_multivar(self, name: str, regex: str, value: str) -> None:
        """
        Set a multivar ''name'' to ''value''. ''regexp'' is a regular
        expression to indicate which values to replace.
        """
        ...
    def delete_multivar(self, name: str, regex: str) -> None:
        """
        Delete a multivar ''name''. ''regexp'' is a regular expression to
        indicate which values to delete.
        """
        ...
    def get_bool(self, key: str) -> bool:
        """
        Look up *key* and parse its value as a boolean as per the git-config
        rules. Return a boolean value (True or False).

        Truthy values are: 'true', 1, 'on' or 'yes'. Falsy values are: 'false',
        0, 'off' and 'no'
        """
        ...
    def get_int(self, key: str) -> int:
        """
        Look up *key* and parse its value as an integer as per the git-config
        rules. Return an integer.

        A value can have a suffix 'k', 'm' or 'g' which stand for 'kilo',
        'mega' and 'giga' respectively.
        """
        ...
    def add_file(self, path: StrOrBytesPath, level: int = 0, force: int = 0) -> None:
        """Add a config file instance to an existing config."""
        ...
    def snapshot(self) -> Config:
        """
        Create a snapshot from this Config object.

        This means that looking up multiple values will use the same version
        of the configuration files.
        """
        ...
    @staticmethod
    def parse_bool(text: _CDataBase | bytes | str | None) -> bool: ...
    @staticmethod
    def parse_int(text: _CDataBase | bytes | str | None) -> int: ...
    @staticmethod
    def get_system_config() -> Config:
        """Return a <Config> object representing the system configuration file."""
        ...
    @staticmethod
    def get_global_config() -> Config:
        """Return a <Config> object representing the global configuration file."""
        ...
    @staticmethod
    def get_xdg_config() -> Config:
        """Return a <Config> object representing the global configuration file."""
        ...

class ConfigEntry:
    """An entry in a configuation object."""
    def __del__(self) -> None: ...
    @property
    def c_value(self) -> _CDataBase:
        """The raw ``cData`` entry value."""
        ...
    @property
    def raw_name(self) -> bytes: ...
    @property
    def raw_value(self) -> bytes: ...
    @property
    def level(self) -> int:
        """The entry's ``git_config_level_t`` value."""
        ...
    @property
    def name(self) -> str:
        """The entry's name."""
        ...
    @property
    def value(self) -> str:
        """The entry's value as a string."""
        ...
