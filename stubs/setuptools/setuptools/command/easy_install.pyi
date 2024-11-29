"""
Easy Install
------------

A tool for doing automatic download/extract/build of distutils-based Python
packages.  For detailed documentation, see the accompanying EasyInstall.txt
file, or visit the `EasyInstall home page`__.

__ https://setuptools.pypa.io/en/latest/deprecated/easy_install.html
"""

from _typeshed import Incomplete
from collections.abc import Iterable, Iterator
from typing import Any, ClassVar, Literal, NoReturn, TypedDict
from typing_extensions import Self

from pkg_resources import Distribution, Environment
from setuptools.package_index import PackageIndex

from .. import Command, SetuptoolsDeprecationWarning

__all__ = ["PthDistributions", "easy_install", "extract_wininst_cfg", "get_exe_prefixes"]

class easy_install(Command):
    """Manage a download/build/install process"""
    description: str
    command_consumes_arguments: bool
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    boolean_options: ClassVar[list[str]]
    negative_opt: ClassVar[dict[str, str]]
    create_index: ClassVar[type[PackageIndex]]
    user: bool
    zip_ok: Incomplete
    install_dir: Incomplete
    index_url: Incomplete
    find_links: Incomplete
    build_directory: Incomplete
    args: Incomplete
    optimize: Incomplete
    upgrade: Incomplete
    editable: Incomplete
    root: Incomplete
    version: Incomplete
    install_purelib: Incomplete
    install_platlib: Incomplete
    install_headers: Incomplete
    install_lib: Incomplete
    install_scripts: Incomplete
    install_data: Incomplete
    install_base: Incomplete
    install_platbase: Incomplete
    install_userbase: str | None
    install_usersite: str | None
    no_find_links: Incomplete
    package_index: Incomplete
    pth_file: Incomplete
    site_dirs: Incomplete
    installed_projects: Incomplete
    verbose: bool | Literal[0, 1]
    def initialize_options(self) -> None: ...
    def delete_blockers(self, blockers) -> None: ...
    config_vars: dict[str, Any]
    script_dir: Incomplete
    all_site_dirs: list[str]
    shadow_path: list[str]
    local_index: Environment
    outputs: list[str]
    def finalize_options(self) -> None: ...
    def expand_basedirs(self) -> None:
        """
        Calls `os.path.expanduser` on install_base, install_platbase and
        root.
        """
        ...
    def expand_dirs(self) -> None:
        """Calls `os.path.expanduser` on install dirs."""
        ...
    def run(self, show_deprecation: bool = True) -> None: ...
    def pseudo_tempname(self):
        """
        Return a pseudo-tempname base in the install directory.
        This code is intentionally naive; if a malicious party can write to
        the target directory you're already in deep doodoo.
        """
        ...
    def warn_deprecated_options(self) -> None: ...
    def check_site_dir(self) -> None:
        """Verify that self.install_dir is .pth-capable dir, if needed"""
        ...
    def cant_write_to_target(self) -> NoReturn: ...
    def check_pth_processing(self):
        """Empirically verify whether .pth files are supported in inst. dir"""
        ...
    def install_egg_scripts(self, dist) -> None:
        """Write all the scripts for `dist`, unless scripts are excluded"""
        ...
    def add_output(self, path) -> None: ...
    def not_editable(self, spec) -> None: ...
    def check_editable(self, spec) -> None: ...
    def easy_install(self, spec, deps: bool = False) -> Distribution | None: ...
    def install_item(self, spec, download, tmpdir, deps, install_needed: bool = False) -> Distribution | None: ...
    def select_scheme(self, name) -> None: ...
    def process_distribution(self, requirement, dist, deps: bool = True, *info) -> None: ...
    def should_unzip(self, dist) -> bool: ...
    def maybe_move(self, spec, dist_filename, setup_base): ...
    def install_wrapper_scripts(self, dist) -> None: ...
    def install_script(self, dist, script_name, script_text, dev_path: Incomplete | None = None) -> None:
        """Generate a legacy script wrapper and install it"""
        ...
    def write_script(self, script_name, contents, mode: str = "t", blockers=()) -> None:
        """Write an executable file to the scripts directory"""
        ...
    def install_eggs(self, spec, dist_filename, tmpdir) -> list[Distribution]: ...
    def egg_distribution(self, egg_path): ...
    def install_egg(self, egg_path, tmpdir): ...
    def install_exe(self, dist_filename, tmpdir): ...
    def exe_to_egg(self, dist_filename, egg_tmp) -> None:
        """Extract a bdist_wininst to the directories an egg would use"""
        ...
    def install_wheel(self, wheel_path, tmpdir): ...
    def installation_report(self, req, dist, what: str = "Installed") -> str:
        """Helpful installation message for display to package users"""
        ...
    def report_editable(self, spec, setup_script): ...
    def run_setup(self, setup_script, setup_base, args) -> None: ...
    def build_and_install(self, setup_script, setup_base): ...
    def update_pth(self, dist) -> None: ...
    def unpack_progress(self, src, dst): ...
    def unpack_and_compile(self, egg_path, destination): ...
    def byte_compile(self, to_compile) -> None: ...
    def create_home_path(self) -> None:
        """Create directories under ~."""
        ...
    INSTALL_SCHEMES: ClassVar[dict[str, dict[str, str]]]
    DEFAULT_SCHEME: ClassVar[dict[str, str]]

def extract_wininst_cfg(dist_filename):
    """
    Extract configuration data from a bdist_wininst .exe

    Returns a configparser.RawConfigParser, or None
    """
    ...
def get_exe_prefixes(exe_filename):
    """Get exe->egg path translations for a given .exe file"""
    ...

class PthDistributions(Environment):
    """A .pth file with Distribution paths in it"""
    dirty: bool
    filename: Incomplete
    sitedirs: list[str]
    basedir: Incomplete
    paths: list[str]
    def __init__(self, filename, sitedirs=()) -> None: ...
    def save(self) -> None:
        """Write changed .pth file back to disk"""
        ...
    def add(self, dist) -> None:
        """Add `dist` to the distribution map"""
        ...
    def remove(self, dist) -> None:
        """Remove `dist` from the distribution map"""
        ...
    def make_relative(self, path): ...

class RewritePthDistributions(PthDistributions):
    prelude: str
    postlude: str

class _SplitArgs(TypedDict, total=False):
    comments: bool
    posix: bool

class CommandSpec(list[str]):
    """
    A command spec for a #! header, specified as a list of arguments akin to
    those passed to Popen.
    """
    options: list[str]
    split_args: ClassVar[_SplitArgs]
    @classmethod
    def best(cls) -> type[CommandSpec]:
        """Choose the best CommandSpec class based on environmental conditions."""
        ...
    @classmethod
    def from_param(cls, param: Self | str | Iterable[str] | None) -> Self:
        """
        Construct a CommandSpec from a parameter to build_scripts, which may
        be None.
        """
        ...
    @classmethod
    def from_environment(cls) -> CommandSpec: ...
    @classmethod
    def from_string(cls, string: str) -> CommandSpec:
        """
        Construct a command spec from a simple string representing a command
        line parseable by shlex.split.
        """
        ...
    def install_options(self, script_text: str) -> None: ...
    def as_header(self) -> str: ...

class WindowsCommandSpec(CommandSpec): ...

class ScriptWriter:
    """
    Encapsulates behavior around writing entry point scripts for console and
    gui apps.
    """
    template: ClassVar[str]
    command_spec_class: ClassVar[type[CommandSpec]]
    @classmethod
    def get_args(cls, dist, header: Incomplete | None = None) -> Iterator[tuple[str, str]]:
        """
        Yield write_script() argument tuples for a distribution's
        console_scripts and gui_scripts entry points.
        """
        ...
    @classmethod
    def best(cls) -> type[ScriptWriter]:
        """Select the best ScriptWriter for this environment."""
        ...
    @classmethod
    def get_header(cls, script_text: str = "", executable: str | CommandSpec | Iterable[str] | None = None) -> str:
        """Create a #! line, getting options (if any) from script_text"""
        ...

class WindowsScriptWriter(ScriptWriter):
    command_spec_class: ClassVar[type[WindowsCommandSpec]]
    @classmethod
    def best(cls) -> type[WindowsScriptWriter]:
        """Select the best ScriptWriter suitable for Windows"""
        ...

class WindowsExecutableLauncherWriter(WindowsScriptWriter): ...
class EasyInstallDeprecationWarning(SetuptoolsDeprecationWarning): ...
