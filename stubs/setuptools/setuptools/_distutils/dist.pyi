"""
distutils.dist

Provides the Distribution class, which represents the module distribution
being built/installed/distributed.
"""

from _typeshed import Incomplete, StrOrBytesPath, StrPath, SupportsWrite
from collections.abc import Iterable, MutableMapping
from re import Pattern
from typing import IO, ClassVar, Literal, TypeVar, overload
from typing_extensions import TypeAlias

from .cmd import Command

command_re: Pattern[str]

_OptionsList: TypeAlias = list[tuple[str, str | None, str, int] | tuple[str, str | None, str]]
_CommandT = TypeVar("_CommandT", bound=Command)

class DistributionMetadata:
    """
    Dummy class to hold the distribution meta-data: name, version,
    author, and so forth.
    """
    def __init__(self, path: StrOrBytesPath | None = None) -> None: ...
    name: str | None
    version: str | None
    author: str | None
    author_email: str | None
    maintainer: str | None
    maintainer_email: str | None
    url: str | None
    license: str | None
    description: str | None
    long_description: str | None
    keywords: str | list[str] | None
    platforms: str | list[str] | None
    classifiers: str | list[str] | None
    download_url: str | None
    provides: list[str] | None
    requires: list[str] | None
    obsoletes: list[str] | None
    def read_pkg_file(self, file: IO[str]) -> None:
        """Reads the metadata values from a file object."""
        ...
    def write_pkg_info(self, base_dir: StrPath) -> None:
        """Write the PKG-INFO file into the release tree."""
        ...
    def write_pkg_file(self, file: SupportsWrite[str]) -> None:
        """Write the PKG-INFO format data to a file object."""
        ...
    def get_name(self) -> str: ...
    def get_version(self) -> str: ...
    def get_fullname(self) -> str: ...
    def get_author(self) -> str | None: ...
    def get_author_email(self) -> str | None: ...
    def get_maintainer(self) -> str | None: ...
    def get_maintainer_email(self) -> str | None: ...
    def get_contact(self) -> str | None: ...
    def get_contact_email(self) -> str | None: ...
    def get_url(self) -> str | None: ...
    def get_license(self) -> str | None: ...
    get_licence = get_license
    def get_description(self) -> str | None: ...
    def get_long_description(self) -> str | None: ...
    def get_keywords(self) -> str | list[str]: ...
    def set_keywords(self, value: str | Iterable[str]) -> None: ...
    def get_platforms(self) -> str | list[str] | None: ...
    def set_platforms(self, value: str | Iterable[str]) -> None: ...
    def get_classifiers(self) -> str | list[str]: ...
    def set_classifiers(self, value): ...
    def get_download_url(self) -> str | None: ...
    def get_requires(self) -> str | list[str]: ...
    def set_requires(self, value: Iterable[str]) -> None: ...
    def get_provides(self) -> str | list[str]: ...
    def set_provides(self, value: Iterable[str]) -> None: ...
    def get_obsoletes(self) -> str | list[str]: ...
    def set_obsoletes(self, value: Iterable[str]) -> None: ...

class Distribution:
    """
    The core of the Distutils.  Most of the work hiding behind 'setup'
    is really done within a Distribution instance, which farms the work out
    to the Distutils commands specified on the command line.

    Setup scripts will almost never instantiate Distribution directly,
    unless the 'setup()' function is totally inadequate to their needs.
    However, it is conceivable that a setup script might wish to subclass
    Distribution for some specialized purpose, and then pass the subclass
    to 'setup()' as the 'distclass' keyword argument.  If so, it is
    necessary to respect the expectations that 'setup' has of Distribution.
    See the code for 'setup()', in core.py, for details.
    """
    cmdclass: dict[str, type[Command]]
    metadata: DistributionMetadata
    def __init__(self, attrs: MutableMapping[str, Incomplete] | None = None) -> None:
        """
        Construct a new Distribution instance: initialize all the
        attributes of a Distribution, and then use 'attrs' (a dictionary
        mapping attribute names to values) to assign some of those
        attributes their "real" values.  (Any attributes not mentioned in
        'attrs' will be assigned to some null value: 0, None, an empty list
        or dictionary, etc.)  Most importantly, initialize the
        'command_obj' attribute to the empty dictionary; this will be
        filled in with real command objects by 'parse_command_line()'.
        """
        ...
    def get_option_dict(self, command: str) -> dict[str, tuple[str, str]]:
        """
        Get the option dictionary for a given command.  If that
        command's option dictionary hasn't been created yet, then create it
        and return the new dictionary; otherwise, return the existing
        option dictionary.
        """
        ...
    def parse_config_files(self, filenames: Iterable[str] | None = None) -> None: ...
    global_options: ClassVar[_OptionsList]
    common_usage: ClassVar[str]
    display_options: ClassVar[_OptionsList]
    display_option_names: ClassVar[list[str]]
    negative_opt: ClassVar[dict[str, str]]
    verbose: bool
    dry_run: bool
    help: bool
    command_packages: str | list[str] | None
    script_name: StrPath | None
    script_args: list[str] | None
    command_options: dict[str, dict[str, tuple[str, str]]]
    dist_files: list[tuple[str, str, str]]
    packages: Incomplete
    package_data: dict[str, list[str]]
    package_dir: Incomplete
    py_modules: Incomplete
    libraries: Incomplete
    headers: Incomplete
    ext_modules: Incomplete
    ext_package: Incomplete
    include_dirs: Incomplete
    extra_path: Incomplete
    scripts: Incomplete
    data_files: Incomplete
    password: str
    command_obj: dict[str, Command]
    have_run: dict[str, bool]
    want_user_cfg: bool
    def dump_option_dicts(self, header=None, commands=None, indent: str = "") -> None: ...
    def find_config_files(self):
        """
        Find as many configuration files as should be processed for this
        platform, and return a list of filenames in the order in which they
        should be parsed.  The filenames returned are guaranteed to exist
        (modulo nasty race conditions).

        There are multiple possible config files:
        - distutils.cfg in the Distutils installation directory (i.e.
          where the top-level Distutils __inst__.py file lives)
        - a file in the user's home directory named .pydistutils.cfg
          on Unix and pydistutils.cfg on Windows/Mac; may be disabled
          with the ``--no-user-cfg`` option
        - setup.cfg in the current directory
        - a file named by an environment variable
        """
        ...
    commands: Incomplete
    def parse_command_line(self):
        """
        Parse the setup script's command line, taken from the
        'script_args' instance attribute (which defaults to 'sys.argv[1:]'
        -- see 'setup()' in core.py).  This list is first processed for
        "global options" -- options that set attributes of the Distribution
        instance.  Then, it is alternately scanned for Distutils commands
        and options for that command.  Each new command terminates the
        options for the previous command.  The allowed options for a
        command are determined by the 'user_options' attribute of the
        command class -- thus, we have to be able to load command classes
        in order to parse the command line.  Any error in that 'options'
        attribute raises DistutilsGetoptError; any error on the
        command-line raises DistutilsArgError.  If no Distutils commands
        were found on the command line, raises DistutilsArgError.  Return
        true if command-line was successfully parsed and we should carry
        on with executing commands; false if no errors but we shouldn't
        execute commands (currently, this only happens if user asks for
        help).
        """
        ...
    def finalize_options(self) -> None:
        """
        Set final values for all the options on the Distribution
        instance, analogous to the .finalize_options() method of Command
        objects.
        """
        ...
    def handle_display_options(self, option_order):
        """
        If there were any non-global "display-only" options
        (--help-commands or the metadata display options) on the command
        line, display the requested info and return true; else return
        false.
        """
        ...
    def print_command_list(self, commands, header, max_length) -> None:
        """
        Print a subset of the list of all commands -- used by
        'print_commands()'.
        """
        ...
    def print_commands(self) -> None:
        """
        Print out a help message listing all available commands with a
        description of each.  The list is divided into "standard commands"
        (listed in distutils.command.__all__) and "extra commands"
        (mentioned in self.cmdclass, but not a standard command).  The
        descriptions come from the command class attribute
        'description'.
        """
        ...
    def get_command_list(self):
        """
        Get a list of (command, description) tuples.
        The list is divided into "standard commands" (listed in
        distutils.command.__all__) and "extra commands" (mentioned in
        self.cmdclass, but not a standard command).  The descriptions come
        from the command class attribute 'description'.
        """
        ...
    def get_command_packages(self):
        """Return a list of packages from which commands are loaded."""
        ...
    # NOTE: Because this is private setuptools implementation and we don't re-expose all commands here,
    # we're not overloading each and every command possibility.
    @overload
    def get_command_obj(self, command: str, create: Literal[True] = True) -> Command:
        """
        Return the command object for 'command'.  Normally this object
        is cached on a previous call to 'get_command_obj()'; if no command
        object for 'command' is in the cache, then we either create and
        return it (if 'create' is true) or return None.
        """
        ...
    @overload
    def get_command_obj(self, command: str, create: Literal[False]) -> Command | None:
        """
        Return the command object for 'command'.  Normally this object
        is cached on a previous call to 'get_command_obj()'; if no command
        object for 'command' is in the cache, then we either create and
        return it (if 'create' is true) or return None.
        """
        ...
    def get_command_class(self, command: str) -> type[Command]:
        """
        Return the class that implements the Distutils command named by
        'command'.  First we check the 'cmdclass' dictionary; if the
        command is mentioned there, we fetch the class object from the
        dictionary and return it.  Otherwise we load the command module
        ("distutils.command." + command) and fetch the command class from
        the module.  The loaded class is also stored in 'cmdclass'
        to speed future calls to 'get_command_class()'.

        Raises DistutilsModuleError if the expected module could not be
        found, or if that module does not define the expected class.
        """
        ...
    @overload
    def reinitialize_command(self, command: str, reinit_subcommands: bool = False) -> Command:
        """
        Reinitializes a command to the state it was in when first
        returned by 'get_command_obj()': ie., initialized but not yet
        finalized.  This provides the opportunity to sneak option
        values in programmatically, overriding or supplementing
        user-supplied values from the config files and command line.
        You'll have to re-finalize the command object (by calling
        'finalize_options()' or 'ensure_finalized()') before using it for
        real.

        'command' should be a command name (string) or command object.  If
        'reinit_subcommands' is true, also reinitializes the command's
        sub-commands, as declared by the 'sub_commands' class attribute (if
        it has one).  See the "install" command for an example.  Only
        reinitializes the sub-commands that actually matter, ie. those
        whose test predicates return true.

        Returns the reinitialized command object.
        """
        ...
    @overload
    def reinitialize_command(self, command: _CommandT, reinit_subcommands: bool = False) -> _CommandT:
        """
        Reinitializes a command to the state it was in when first
        returned by 'get_command_obj()': ie., initialized but not yet
        finalized.  This provides the opportunity to sneak option
        values in programmatically, overriding or supplementing
        user-supplied values from the config files and command line.
        You'll have to re-finalize the command object (by calling
        'finalize_options()' or 'ensure_finalized()') before using it for
        real.

        'command' should be a command name (string) or command object.  If
        'reinit_subcommands' is true, also reinitializes the command's
        sub-commands, as declared by the 'sub_commands' class attribute (if
        it has one).  See the "install" command for an example.  Only
        reinitializes the sub-commands that actually matter, ie. those
        whose test predicates return true.

        Returns the reinitialized command object.
        """
        ...
    def announce(self, msg, level: int = 20) -> None: ...
    def run_commands(self) -> None:
        """
        Run each command that was seen on the setup script command line.
        Uses the list of commands found and cache of command objects
        created by 'get_command_obj()'.
        """
        ...
    def run_command(self, command: str) -> None:
        """
        Do whatever it takes to run a command (including nothing at all,
        if the command has already been run).  Specifically: if we have
        already created and run the command named by 'command', return
        silently without doing anything.  If the command named by 'command'
        doesn't even have a command object yet, create one.  Then invoke
        'run()' on that command object (or an existing one).
        """
        ...
    def has_pure_modules(self) -> bool: ...
    def has_ext_modules(self) -> bool: ...
    def has_c_libraries(self) -> bool: ...
    def has_modules(self) -> bool: ...
    def has_headers(self) -> bool: ...
    def has_scripts(self) -> bool: ...
    def has_data_files(self) -> bool: ...
    def is_pure(self) -> bool: ...

    # Default getter methods generated in __init__ from self.metadata._METHOD_BASENAMES
    def get_name(self) -> str: ...
    def get_version(self) -> str: ...
    def get_fullname(self) -> str: ...
    def get_author(self) -> str: ...
    def get_author_email(self) -> str: ...
    def get_maintainer(self) -> str: ...
    def get_maintainer_email(self) -> str: ...
    def get_contact(self) -> str: ...
    def get_contact_email(self) -> str: ...
    def get_url(self) -> str: ...
    def get_license(self) -> str: ...
    def get_licence(self) -> str: ...
    def get_description(self) -> str: ...
    def get_long_description(self) -> str: ...
    def get_keywords(self) -> str | list[str]: ...
    def get_platforms(self) -> str | list[str]: ...
    def get_classifiers(self) -> str | list[str]: ...
    def get_download_url(self) -> str: ...
    def get_requires(self) -> list[str]: ...
    def get_provides(self) -> list[str]: ...
    def get_obsoletes(self) -> list[str]: ...

    # Default attributes generated in __init__ from self.display_option_names
    help_commands: bool
    name: str | Literal[False]
    version: str | Literal[False]
    fullname: str | Literal[False]
    author: str | Literal[False]
    author_email: str | Literal[False]
    maintainer: str | Literal[False]
    maintainer_email: str | Literal[False]
    contact: str | Literal[False]
    contact_email: str | Literal[False]
    url: str | Literal[False]
    license: str | Literal[False]
    licence: str | Literal[False]
    description: str | Literal[False]
    long_description: str | Literal[False]
    platforms: str | list[str] | Literal[False]
    classifiers: str | list[str] | Literal[False]
    keywords: str | list[str] | Literal[False]
    provides: list[str] | Literal[False]
    requires: list[str] | Literal[False]
    obsoletes: list[str] | Literal[False]
