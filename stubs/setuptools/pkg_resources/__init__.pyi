# `pkg_resources` package of `types-setuptools` is now obsolete.
# Changes here should be mirrored to https://github.com/pypa/setuptools/tree/main/pkg_resources


"""
Package resource API
--------------------

A resource is a logical file contained within a package, or a logical
subdirectory thereof.  The package resource API expects resource names
to have their path parts separated with ``/``, *not* whatever the local
path separator is.  Do not use os.path operations to manipulate resource
names being passed into the API.

The package resource API is designed to work with normal filesystem packages,
.egg files, and unpacked .egg files.  It can also work in a limited way with
.zip files and with custom PEP 302 loaders that support the ``get_data()``
method.

This module is deprecated. Users are directed to :mod:`importlib.resources`,
:mod:`importlib.metadata` and :pypi:`packaging` instead.
"""

import types
import zipimport
from _typeshed import BytesPath, Incomplete, StrOrBytesPath, StrPath, Unused
from _typeshed.importlib import LoaderProtocol
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from io import BytesIO
from itertools import chain
from pkgutil import get_importer as get_importer
from re import Pattern
from typing import IO, Any, ClassVar, Final, Literal, NamedTuple, NoReturn, Protocol, TypeVar, overload
from typing_extensions import Self, TypeAlias
from zipfile import ZipInfo

from ._vendored_packaging import requirements as _packaging_requirements, version as _packaging_version

# defined in setuptools
_T = TypeVar("_T")
_DistributionT = TypeVar("_DistributionT", bound=Distribution)
_NestedStr: TypeAlias = str | Iterable[_NestedStr]
_StrictInstallerType: TypeAlias = Callable[[Requirement], _DistributionT]
_InstallerType: TypeAlias = Callable[[Requirement], Distribution | None]
_PkgReqType: TypeAlias = str | Requirement
_EPDistType: TypeAlias = Distribution | _PkgReqType
_MetadataType: TypeAlias = IResourceProvider | None
_ResolvedEntryPoint: TypeAlias = Any  # Can be any attribute in the module
_ResourceStream: TypeAlias = Incomplete  # A readable file-like object
_ModuleLike: TypeAlias = object | types.ModuleType  # Any object that optionally has __loader__ or __file__, usually a module
# Any: Should be _ModuleLike but we end up with issues where _ModuleLike doesn't have _ZipLoaderModule's __loader__
_ProviderFactoryType: TypeAlias = Callable[[Any], IResourceProvider]
_DistFinderType: TypeAlias = Callable[[_T, str, bool], Iterable[Distribution]]
_NSHandlerType: TypeAlias = Callable[[_T, str, str, types.ModuleType], str | None]

__all__ = [
    "require",
    "run_script",
    "get_provider",
    "get_distribution",
    "load_entry_point",
    "get_entry_map",
    "get_entry_info",
    "iter_entry_points",
    "resource_string",
    "resource_stream",
    "resource_filename",
    "resource_listdir",
    "resource_exists",
    "resource_isdir",
    "declare_namespace",
    "working_set",
    "add_activation_listener",
    "find_distributions",
    "set_extraction_path",
    "cleanup_resources",
    "get_default_cache",
    "Environment",
    "WorkingSet",
    "ResourceManager",
    "Distribution",
    "Requirement",
    "EntryPoint",
    "ResolutionError",
    "VersionConflict",
    "DistributionNotFound",
    "UnknownExtra",
    "ExtractionError",
    "PEP440Warning",
    "parse_requirements",
    "parse_version",
    "safe_name",
    "safe_version",
    "get_platform",
    "compatible_platforms",
    "yield_lines",
    "split_sections",
    "safe_extra",
    "to_filename",
    "invalid_marker",
    "evaluate_marker",
    "ensure_directory",
    "normalize_path",
    "EGG_DIST",
    "BINARY_DIST",
    "SOURCE_DIST",
    "CHECKOUT_DIST",
    "DEVELOP_DIST",
    "IMetadataProvider",
    "IResourceProvider",
    "FileMetadata",
    "PathMetadata",
    "EggMetadata",
    "EmptyProvider",
    "empty_provider",
    "NullProvider",
    "EggProvider",
    "DefaultProvider",
    "ZipProvider",
    "register_finder",
    "register_namespace_handler",
    "register_loader_type",
    "fixup_namespace_packages",
    "get_importer",
    "PkgResourcesDeprecationWarning",
    "run_main",
    "AvailableDistributions",
]

class _ZipLoaderModule(Protocol):
    __loader__: zipimport.zipimporter

def declare_namespace(packageName: str) -> None:
    """Declare that package 'packageName' is a namespace package"""
    ...
def fixup_namespace_packages(path_item: str, parent: str | None = None) -> None:
    """Ensure that previously-declared namespace packages include path_item"""
    ...

class WorkingSet:
    """A collection of active distributions on sys.path (or a similar list)"""
    entries: list[str]
    entry_keys: dict[str | None, list[str]]
    by_key: dict[str, Distribution]
    normalized_to_canonical_keys: dict[str, str]
    callbacks: list[Callable[[Distribution], object]]
    def __init__(self, entries: Iterable[str] | None = None) -> None:
        """Create working set from list of path entries (default=sys.path)"""
        ...
    def add_entry(self, entry: str) -> None:
        """
        Add a path item to ``.entries``, finding any distributions on it

        ``find_distributions(entry, True)`` is used to find distributions
        corresponding to the path entry, and they are added.  `entry` is
        always appended to ``.entries``, even if it is already present.
        (This is because ``sys.path`` can contain the same value more than
        once, and the ``.entries`` of the ``sys.path`` WorkingSet should always
        equal ``sys.path``.)
        """
        ...
    def __contains__(self, dist: Distribution) -> bool:
        """True if `dist` is the active distribution for its project"""
        ...
    def find(self, req: Requirement) -> Distribution | None:
        """
        Find a distribution matching requirement `req`

        If there is an active distribution for the requested project, this
        returns it as long as it meets the version requirement specified by
        `req`.  But, if there is an active distribution for the project and it
        does *not* meet the `req` requirement, ``VersionConflict`` is raised.
        If there is no active distribution for the requested project, ``None``
        is returned.
        """
        ...
    def iter_entry_points(self, group: str, name: str | None = None) -> Generator[EntryPoint, None, None]:
        """
        Yield entry point objects from `group` matching `name`

        If `name` is None, yields all entry points in `group` from all
        distributions in the working set, otherwise only ones matching
        both `group` and `name` are yielded (in distribution order).
        """
        ...
    def run_script(self, requires: str, script_name: str) -> None:
        """Locate distribution for `requires` and run `script_name` script"""
        ...
    def __iter__(self) -> Iterator[Distribution]:
        """
        Yield distributions for non-duplicate projects in the working set

        The yield order is the order in which the items' path entries were
        added to the working set.
        """
        ...
    def add(self, dist: Distribution, entry: str | None = None, insert: bool = True, replace: bool = False) -> None:
        """
        Add `dist` to working set, associated with `entry`

        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        On exit from this routine, `entry` is added to the end of the working
        set's ``.entries`` (if it wasn't already present).

        `dist` is only added to the working set if it's for a project that
        doesn't already have a distribution in the set, unless `replace=True`.
        If it's added, any callbacks registered with the ``subscribe()`` method
        will be called.
        """
        ...
    @overload
    def resolve(
        self,
        requirements: Iterable[Requirement],
        env: Environment | None,
        installer: _StrictInstallerType[_DistributionT],
        replace_conflicting: bool = False,
        extras: tuple[str, ...] | None = None,
    ) -> list[_DistributionT]:
        """
        List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception
        if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.

        `extras` is a list of the extras to be used with these requirements.
        This is important because extra requirements may look like `my_req;
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        optional requirement.  Instead, we want to be able to assert that these
        requirements are truly required.
        """
        ...
    @overload
    def resolve(
        self,
        requirements: Iterable[Requirement],
        env: Environment | None = None,
        *,
        installer: _StrictInstallerType[_DistributionT],
        replace_conflicting: bool = False,
        extras: tuple[str, ...] | None = None,
    ) -> list[_DistributionT]:
        """
        List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception
        if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.

        `extras` is a list of the extras to be used with these requirements.
        This is important because extra requirements may look like `my_req;
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        optional requirement.  Instead, we want to be able to assert that these
        requirements are truly required.
        """
        ...
    @overload
    def resolve(
        self,
        requirements: Iterable[Requirement],
        env: Environment | None = None,
        installer: _InstallerType | None = None,
        replace_conflicting: bool = False,
        extras: tuple[str, ...] | None = None,
    ) -> list[Distribution]:
        """
        List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception
        if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.

        `extras` is a list of the extras to be used with these requirements.
        This is important because extra requirements may look like `my_req;
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        optional requirement.  Instead, we want to be able to assert that these
        requirements are truly required.
        """
        ...
    @overload
    def find_plugins(
        self,
        plugin_env: Environment,
        full_env: Environment | None,
        installer: _StrictInstallerType[_DistributionT],
        fallback: bool = True,
    ) -> tuple[list[_DistributionT], dict[Distribution, Exception]]:
        """
        Find all activatable distributions in `plugin_env`

        Example usage::

            distributions, errors = working_set.find_plugins(
                Environment(plugin_dirlist)
            )
            # add plugins+libs to sys.path
            map(working_set.add, distributions)
            # display errors
            print('Could not load', errors)

        The `plugin_env` should be an ``Environment`` instance that contains
        only distributions that are in the project's "plugin directory" or
        directories. The `full_env`, if supplied, should be an ``Environment``
        contains all currently-available distributions.  If `full_env` is not
        supplied, one is created automatically from the ``WorkingSet`` this
        method is called on, which will typically mean that every directory on
        ``sys.path`` will be scanned for distributions.

        `installer` is a standard installer callback as used by the
        ``resolve()`` method. The `fallback` flag indicates whether we should
        attempt to resolve older versions of a plugin if the newest version
        cannot be resolved.

        This method returns a 2-tuple: (`distributions`, `error_info`), where
        `distributions` is a list of the distributions found in `plugin_env`
        that were loadable, along with any other distributions that are needed
        to resolve their dependencies.  `error_info` is a dictionary mapping
        unloadable plugin distributions to an exception instance describing the
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        ``VersionConflict`` instance.
        """
        ...
    @overload
    def find_plugins(
        self,
        plugin_env: Environment,
        full_env: Environment | None = None,
        *,
        installer: _StrictInstallerType[_DistributionT],
        fallback: bool = True,
    ) -> tuple[list[_DistributionT], dict[Distribution, Exception]]:
        """
        Find all activatable distributions in `plugin_env`

        Example usage::

            distributions, errors = working_set.find_plugins(
                Environment(plugin_dirlist)
            )
            # add plugins+libs to sys.path
            map(working_set.add, distributions)
            # display errors
            print('Could not load', errors)

        The `plugin_env` should be an ``Environment`` instance that contains
        only distributions that are in the project's "plugin directory" or
        directories. The `full_env`, if supplied, should be an ``Environment``
        contains all currently-available distributions.  If `full_env` is not
        supplied, one is created automatically from the ``WorkingSet`` this
        method is called on, which will typically mean that every directory on
        ``sys.path`` will be scanned for distributions.

        `installer` is a standard installer callback as used by the
        ``resolve()`` method. The `fallback` flag indicates whether we should
        attempt to resolve older versions of a plugin if the newest version
        cannot be resolved.

        This method returns a 2-tuple: (`distributions`, `error_info`), where
        `distributions` is a list of the distributions found in `plugin_env`
        that were loadable, along with any other distributions that are needed
        to resolve their dependencies.  `error_info` is a dictionary mapping
        unloadable plugin distributions to an exception instance describing the
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        ``VersionConflict`` instance.
        """
        ...
    @overload
    def find_plugins(
        self,
        plugin_env: Environment,
        full_env: Environment | None = None,
        installer: _InstallerType | None = None,
        fallback: bool = True,
    ) -> tuple[list[Distribution], dict[Distribution, Exception]]:
        """
        Find all activatable distributions in `plugin_env`

        Example usage::

            distributions, errors = working_set.find_plugins(
                Environment(plugin_dirlist)
            )
            # add plugins+libs to sys.path
            map(working_set.add, distributions)
            # display errors
            print('Could not load', errors)

        The `plugin_env` should be an ``Environment`` instance that contains
        only distributions that are in the project's "plugin directory" or
        directories. The `full_env`, if supplied, should be an ``Environment``
        contains all currently-available distributions.  If `full_env` is not
        supplied, one is created automatically from the ``WorkingSet`` this
        method is called on, which will typically mean that every directory on
        ``sys.path`` will be scanned for distributions.

        `installer` is a standard installer callback as used by the
        ``resolve()`` method. The `fallback` flag indicates whether we should
        attempt to resolve older versions of a plugin if the newest version
        cannot be resolved.

        This method returns a 2-tuple: (`distributions`, `error_info`), where
        `distributions` is a list of the distributions found in `plugin_env`
        that were loadable, along with any other distributions that are needed
        to resolve their dependencies.  `error_info` is a dictionary mapping
        unloadable plugin distributions to an exception instance describing the
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        ``VersionConflict`` instance.
        """
        ...
    def require(self, *requirements: _NestedStr) -> Sequence[Distribution]:
        """
        Ensure that distributions matching `requirements` are activated

        `requirements` must be a string or a (possibly-nested) sequence
        thereof, specifying the distributions and versions required.  The
        return value is a sequence of the distributions that needed to be
        activated to fulfill the requirements; all relevant distributions are
        included, even if they were already activated in this working set.
        """
        ...
    def subscribe(self, callback: Callable[[Distribution], Unused], existing: bool = True) -> None:
        """
        Invoke `callback` for all distributions

        If `existing=True` (default),
        call on all existing ones, as well.
        """
        ...

class Environment:
    """Searchable snapshot of distributions on a search path"""
    def __init__(
        self, search_path: Iterable[str] | None = None, platform: str | None = ..., python: str | None = ...
    ) -> None:
        """
        Snapshot distributions available on a search path

        Any distributions found on `search_path` are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.

        `platform` is an optional string specifying the name of the platform
        that platform-specific distributions must be compatible with.  If
        unspecified, it defaults to the current platform.  `python` is an
        optional string naming the desired version of Python (e.g. ``'3.6'``);
        it defaults to the current version.

        You may explicitly set `platform` (and/or `python`) to ``None`` if you
        wish to map *all* distributions, not just those compatible with the
        running platform or Python version.
        """
        ...
    def can_add(self, dist: Distribution) -> bool:
        """
        Is distribution `dist` acceptable for this environment?

        The distribution must match the platform and python version
        requirements specified when this environment was created, or False
        is returned.
        """
        ...
    def remove(self, dist: Distribution) -> None:
        """Remove `dist` from the environment"""
        ...
    def scan(self, search_path: Iterable[str] | None = None) -> None:
        """
        Scan `search_path` for distributions usable in this environment

        Any distributions found are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.  Only distributions conforming to
        the platform/python version defined at initialization are added.
        """
        ...
    def __getitem__(self, project_name: str) -> list[Distribution]:
        """
        Return a newest-to-oldest list of distributions for `project_name`

        Uses case-insensitive `project_name` comparison, assuming all the
        project's distributions use their project's name converted to all
        lowercase as their key.
        """
        ...
    def add(self, dist: Distribution) -> None:
        """Add `dist` if we ``can_add()`` it and it has not already been added"""
        ...
    @overload
    def best_match(
        self,
        req: Requirement,
        working_set: WorkingSet,
        installer: _StrictInstallerType[_DistributionT],
        replace_conflicting: bool = False,
    ) -> _DistributionT:
        """
        Find distribution best matching `req` and usable on `working_set`

        This calls the ``find(req)`` method of the `working_set` to see if a
        suitable distribution is already active.  (This may raise
        ``VersionConflict`` if an unsuitable version of the project is already
        active in the specified `working_set`.)  If a suitable distribution
        isn't active, this method returns the newest distribution in the
        environment that meets the ``Requirement`` in `req`.  If no suitable
        distribution is found, and `installer` is supplied, then the result of
        calling the environment's ``obtain(req, installer)`` method will be
        returned.
        """
        ...
    @overload
    def best_match(
        self,
        req: Requirement,
        working_set: WorkingSet,
        installer: _InstallerType | None = None,
        replace_conflicting: bool = False,
    ) -> Distribution | None:
        """
        Find distribution best matching `req` and usable on `working_set`

        This calls the ``find(req)`` method of the `working_set` to see if a
        suitable distribution is already active.  (This may raise
        ``VersionConflict`` if an unsuitable version of the project is already
        active in the specified `working_set`.)  If a suitable distribution
        isn't active, this method returns the newest distribution in the
        environment that meets the ``Requirement`` in `req`.  If no suitable
        distribution is found, and `installer` is supplied, then the result of
        calling the environment's ``obtain(req, installer)`` method will be
        returned.
        """
        ...
    @overload
    def obtain(self, requirement: Requirement, installer: _StrictInstallerType[_DistributionT]) -> _DistributionT:
        """
        Obtain a distribution matching `requirement` (e.g. via download)

        Obtain a distro that matches requirement (e.g. via download).  In the
        base ``Environment`` class, this routine just returns
        ``installer(requirement)``, unless `installer` is None, in which case
        None is returned instead.  This method is a hook that allows subclasses
        to attempt other ways of obtaining a distribution before falling back
        to the `installer` argument.
        """
        ...
    @overload
    def obtain(self, requirement: Requirement, installer: Callable[[Requirement], None] | None = None) -> None:
        """
        Obtain a distribution matching `requirement` (e.g. via download)

        Obtain a distro that matches requirement (e.g. via download).  In the
        base ``Environment`` class, this routine just returns
        ``installer(requirement)``, unless `installer` is None, in which case
        None is returned instead.  This method is a hook that allows subclasses
        to attempt other ways of obtaining a distribution before falling back
        to the `installer` argument.
        """
        ...
    @overload
    def obtain(self, requirement: Requirement, installer: _InstallerType | None = None) -> Distribution | None:
        """
        Obtain a distribution matching `requirement` (e.g. via download)

        Obtain a distro that matches requirement (e.g. via download).  In the
        base ``Environment`` class, this routine just returns
        ``installer(requirement)``, unless `installer` is None, in which case
        None is returned instead.  This method is a hook that allows subclasses
        to attempt other ways of obtaining a distribution before falling back
        to the `installer` argument.
        """
        ...
    def __iter__(self) -> Iterator[str]:
        """Yield the unique project names of the available distributions"""
        ...
    def __iadd__(self, other: Distribution | Environment) -> Self:
        """In-place addition of a distribution or environment"""
        ...
    def __add__(self, other: Distribution | Environment) -> Self:
        """Add an environment or distribution to an environment"""
        ...

AvailableDistributions = Environment

def parse_requirements(strs: _NestedStr) -> Iterator[Requirement]:
    """
    Yield ``Requirement`` objects for each specification in `strs`.

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    """
    ...

class RequirementParseError(_packaging_requirements.InvalidRequirement):
    """Compatibility wrapper for InvalidRequirement"""
    ...

class Requirement(_packaging_requirements.Requirement):
    unsafe_name: str
    project_name: str
    key: str
    # packaging.requirements.Requirement uses a set for its extras. setuptools/pkg_resources uses a variable-length tuple
    extras: tuple[str, ...]  # type: ignore[assignment]
    specs: list[tuple[str, str]]
    def __init__(self, requirement_string: str) -> None:
        """DO NOT CALL THIS UNDOCUMENTED METHOD; use Requirement.parse()!"""
        ...
    def __eq__(self, other: object) -> bool: ...
    def __contains__(self, item: Distribution | str | tuple[str, ...]) -> bool: ...
    @staticmethod
    def parse(s: str | Iterable[str]) -> Requirement: ...

def load_entry_point(dist: _EPDistType, group: str, name: str) -> _ResolvedEntryPoint:
    """Return `name` entry point of `group` for `dist` or raise ImportError"""
    ...
@overload
def get_entry_map(dist: _EPDistType, group: None = None) -> dict[str, dict[str, EntryPoint]]:
    """Return the entry point map for `group`, or the full entry map"""
    ...
@overload
def get_entry_map(dist: _EPDistType, group: str) -> dict[str, EntryPoint]:
    """Return the entry point map for `group`, or the full entry map"""
    ...
def get_entry_info(dist: _EPDistType, group: str, name: str) -> EntryPoint | None:
    """Return the EntryPoint object for `group`+`name`, or ``None``"""
    ...

class EntryPoint:
    """Object representing an advertised importable object"""
    name: str
    module_name: str
    attrs: tuple[str, ...]
    extras: tuple[str, ...]
    dist: Distribution | None
    def __init__(
        self, name: str, module_name: str, attrs: Iterable[str] = (), extras: Iterable[str] = (), dist: Distribution | None = None
    ) -> None: ...
    @overload
    def load(
        self, require: Literal[True] = True, env: Environment | None = None, installer: _InstallerType | None = None
    ) -> _ResolvedEntryPoint:
        """Require packages for this EntryPoint, then resolve it."""
        ...
    @overload
    def load(
        self, require: Literal[False], *args: Environment | _InstallerType | None, **kwargs: Environment | _InstallerType | None
    ) -> _ResolvedEntryPoint:
        """Require packages for this EntryPoint, then resolve it."""
        ...
    def resolve(self) -> _ResolvedEntryPoint:
        """Resolve the entry point from its module and attrs."""
        ...
    def require(self, env: Environment | None = None, installer: _InstallerType | None = None) -> None: ...
    pattern: ClassVar[Pattern[str]]
    @classmethod
    def parse(cls, src: str, dist: Distribution | None = None) -> Self:
        """
        Parse a single entry point from string `src`

        Entry point syntax follows the form::

            name = some.module:some.attr [extra1, extra2]

        The entry name and module name are required, but the ``:attrs`` and
        ``[extras]`` parts are optional
        """
        ...
    @classmethod
    def parse_group(cls, group: str, lines: _NestedStr, dist: Distribution | None = None) -> dict[str, Self]:
        """Parse an entry point group"""
        ...
    @classmethod
    def parse_map(
        cls, data: str | Iterable[str] | dict[str, str | Iterable[str]], dist: Distribution | None = None
    ) -> dict[str, dict[str, Self]]:
        """Parse a map of entry point groups"""
        ...

def find_distributions(path_item: str, only: bool = False) -> Generator[Distribution, None, None]:
    """Yield distributions accessible via `path_item`"""
    ...
def find_eggs_in_zip(importer: zipimport.zipimporter, path_item: str, only: bool = False) -> Iterator[Distribution]:
    """Find eggs in zip files; possibly multiple nested eggs."""
    ...
def find_nothing(importer: object | None, path_item: str | None, only: bool | None = False) -> tuple[Distribution, ...]: ...
def find_on_path(importer: object | None, path_item: str, only: bool = False) -> Generator[Distribution, None, None]:
    """Yield distributions accessible on a sys.path directory"""
    ...
def dist_factory(path_item: StrPath, entry: str, only: bool) -> Callable[[str], Iterable[Distribution]]:
    """Return a dist_factory for the given entry."""
    ...

class NoDists:
    """
    >>> bool(NoDists())
    False

    >>> list(NoDists()('anything'))
    []
    """
    def __bool__(self) -> Literal[False]: ...
    def __call__(self, fullpath: Unused) -> Iterator[Distribution]: ...

@overload
def get_distribution(dist: _DistributionT) -> _DistributionT:
    """Return a current distribution object for a Requirement or string"""
    ...
@overload
def get_distribution(dist: _PkgReqType) -> Distribution:
    """Return a current distribution object for a Requirement or string"""
    ...

PY_MAJOR: Final[str]
EGG_DIST: Final = 3
BINARY_DIST: Final = 2
SOURCE_DIST: Final = 1
CHECKOUT_DIST: Final = 0
DEVELOP_DIST: Final = -1

class ResourceManager:
    """Manage resource extraction and packages"""
    extraction_path: str | None
    cached_files: Incomplete
    def resource_exists(self, package_or_requirement: _PkgReqType, resource_name: str) -> bool:
        """Does the named resource exist?"""
        ...
    def resource_isdir(self, package_or_requirement: _PkgReqType, resource_name: str) -> bool:
        """Is the named resource an existing directory?"""
        ...
    def resource_filename(self, package_or_requirement: _PkgReqType, resource_name: str) -> str:
        """Return a true filesystem path for specified resource"""
        ...
    def resource_stream(self, package_or_requirement: _PkgReqType, resource_name: str) -> IO[bytes]:
        """Return a readable file-like object for specified resource"""
        ...
    def resource_string(self, package_or_requirement: _PkgReqType, resource_name: str) -> bytes:
        """Return specified resource as :obj:`bytes`"""
        ...
    def resource_listdir(self, package_or_requirement: _PkgReqType, resource_name: str) -> list[str]:
        """List the contents of the named resource directory"""
        ...
    def extraction_error(self) -> NoReturn:
        """Give an error message for problems extracting file(s)"""
        ...
    def get_cache_path(self, archive_name: str, names: Iterable[StrPath] = ()) -> str:
        """
        Return absolute location in cache for `archive_name` and `names`

        The parent directory of the resulting path will be created if it does
        not already exist.  `archive_name` should be the base filename of the
        enclosing egg (which may not be the name of the enclosing zipfile!),
        including its ".egg" extension.  `names`, if provided, should be a
        sequence of path name parts "under" the egg's extraction location.

        This method should only be called by resource providers that need to
        obtain an extraction location, and only for names they intend to
        extract, as it tracks the generated names for possible cleanup later.
        """
        ...
    def postprocess(self, tempname: StrOrBytesPath, filename: StrOrBytesPath) -> None:
        """
        Perform any platform-specific postprocessing of `tempname`

        This is where Mac header rewrites should be done; other platforms don't
        have anything special they should do.

        Resource providers should call this method ONLY after successfully
        extracting a compressed resource.  They must NOT call it on resources
        that are already in the filesystem.

        `tempname` is the current (temporary) name of the file, and `filename`
        is the name it will be renamed to by the caller after this routine
        returns.
        """
        ...
    def set_extraction_path(self, path: str) -> None:
        """
        Set the base path where resources will be extracted to, if needed.

        If you do not call this routine before any extractions take place, the
        path defaults to the return value of ``get_default_cache()``.  (Which
        is based on the ``PYTHON_EGG_CACHE`` environment variable, with various
        platform-specific fallbacks.  See that routine's documentation for more
        details.)

        Resources are extracted to subdirectories of this path based upon
        information given by the ``IResourceProvider``.  You may set this to a
        temporary directory, but then you must call ``cleanup_resources()`` to
        delete the extracted files when done.  There is no guarantee that
        ``cleanup_resources()`` will be able to remove all extracted files.

        (Note: you may not change the extraction path for a given resource
        manager once resources have been extracted, unless you first call
        ``cleanup_resources()``.)
        """
        ...
    def cleanup_resources(self, force: bool = False) -> list[str]:
        """
        Delete all extracted resource files and directories, returning a list
        of the file and directory names that could not be successfully removed.
        This function does not have any concurrency protection, so it should
        generally only be called when the extraction path is a temporary
        directory exclusive to a single process.  This method is not
        automatically called; you must call it explicitly or register it as an
        ``atexit`` function if you wish to ensure cleanup of a temporary
        directory used for extractions.
        """
        ...

@overload
def get_provider(moduleOrReq: str) -> IResourceProvider:
    """Return an IResourceProvider for the named module or requirement"""
    ...
@overload
def get_provider(moduleOrReq: Requirement) -> Distribution:
    """Return an IResourceProvider for the named module or requirement"""
    ...

class IMetadataProvider(Protocol):
    def has_metadata(self, name: str) -> bool:
        """Does the package's distribution contain the named metadata?"""
        ...
    def get_metadata(self, name: str) -> str:
        """The named metadata resource as a string"""
        ...
    def get_metadata_lines(self, name: str) -> Iterator[str]:
        """
        Yield named metadata resource as list of non-blank non-comment lines

        Leading and trailing whitespace is stripped from each line, and lines
        with ``#`` as the first non-blank character are omitted.
        """
        ...
    def metadata_isdir(self, name: str) -> bool:
        """Is the named metadata a directory?  (like ``os.path.isdir()``)"""
        ...
    def metadata_listdir(self, name: str) -> list[str]:
        """List of metadata names in the directory (like ``os.listdir()``)"""
        ...
    def run_script(self, script_name: str, namespace: dict[str, Any]) -> None:
        """Execute the named script in the supplied namespace dictionary"""
        ...

class ResolutionError(Exception):
    """Abstract base for dependency resolution errors"""
    ...

class VersionConflict(ResolutionError):
    """
    An already-installed version conflicts with the requested version.

    Should be initialized with the installed Distribution and the requested
    Requirement.
    """
    def __init__(self, dist: Distribution, req: Requirement, /, *args: object) -> None: ...
    @property
    def dist(self) -> Distribution: ...
    @property
    def req(self) -> Requirement: ...
    def report(self) -> str: ...
    def with_context(self, required_by: set[str]) -> Self | ContextualVersionConflict:
        """
        If required_by is non-empty, return a version of self that is a
        ContextualVersionConflict.
        """
        ...

class ContextualVersionConflict(VersionConflict):
    """
    A VersionConflict that accepts a third parameter, the set of the
    requirements that required the installed Distribution.
    """
    def __init__(self, dist: Distribution, req: Requirement, required_by: set[str], /, *args: object) -> None: ...
    @property
    def required_by(self) -> set[str]: ...

class DistributionNotFound(ResolutionError):
    """A requested distribution was not found"""
    def __init__(self, req: Requirement, requirers: set[str] | None, /, *args: object) -> None: ...
    @property
    def req(self) -> Requirement: ...
    @property
    def requirers(self) -> set[str] | None: ...
    @property
    def requirers_str(self) -> str: ...
    def report(self) -> str: ...

class UnknownExtra(ResolutionError):
    """Distribution doesn't have an "extra feature" of the given name"""
    ...

class ExtractionError(Exception):
    """
    An error occurred extracting a resource

    The following attributes are available from instances of this exception:

    manager
        The resource manager that raised this exception

    cache_path
        The base directory for resource extraction

    original_error
        The exception instance that caused extraction to fail
    """
    manager: ResourceManager
    cache_path: str
    original_error: BaseException | None

def register_finder(importer_type: type[_T], distribution_finder: _DistFinderType[_T]) -> None:
    """
    Register `distribution_finder` to find distributions in sys.path items

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `distribution_finder` is a callable that, passed a path
    item and the importer instance, yields ``Distribution`` instances found on
    that path item.  See ``pkg_resources.find_on_path`` for an example.
    """
    ...
def register_loader_type(loader_type: type[_ModuleLike], provider_factory: _ProviderFactoryType) -> None:
    """
    Register `provider_factory` to make providers for `loader_type`

    `loader_type` is the type or class of a PEP 302 ``module.__loader__``,
    and `provider_factory` is a function that, passed a *module* object,
    returns an ``IResourceProvider`` for that module.
    """
    ...
def resolve_egg_link(path: str) -> Iterable[Distribution]:
    """
    Given a path to an .egg-link, resolve distributions
    present in the referenced path.
    """
    ...
def register_namespace_handler(importer_type: type[_T], namespace_handler: _NSHandlerType[_T]) -> None:
    """
    Register `namespace_handler` to declare namespace packages

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `namespace_handler` is a callable like this::

        def namespace_handler(importer, path_entry, moduleName, module):
            # return a path_entry to use for child packages

    Namespace handlers are only called if the importer object has already
    agreed that it can handle the relevant path item, and they should only
    return a subpath if the module __path__ does not already contain an
    equivalent subpath.  For an example namespace handler, see
    ``pkg_resources.file_ns_handler``.
    """
    ...

class IResourceProvider(IMetadataProvider, Protocol):
    """An object that provides access to package resources"""
    def get_resource_filename(self, manager: ResourceManager, resource_name: str) -> StrPath:
        """
        Return a true filesystem path for `resource_name`

        `manager` must be a ``ResourceManager``
        """
        ...
    def get_resource_stream(self, manager: ResourceManager, resource_name: str) -> _ResourceStream:
        """
        Return a readable file-like object for `resource_name`

        `manager` must be a ``ResourceManager``
        """
        ...
    def get_resource_string(self, manager: ResourceManager, resource_name: str) -> bytes:
        """
        Return the contents of `resource_name` as :obj:`bytes`

        `manager` must be a ``ResourceManager``
        """
        ...
    def has_resource(self, resource_name: str) -> bool:
        """Does the package contain the named resource?"""
        ...
    def resource_isdir(self, resource_name: str) -> bool:
        """Is the named resource a directory?  (like ``os.path.isdir()``)"""
        ...
    def resource_listdir(self, resource_name: str) -> list[str]:
        """List of resource names in the directory (like ``os.listdir()``)"""
        ...

def invalid_marker(text: str) -> SyntaxError | Literal[False]:
    """
    Validate text as a PEP 508 environment marker; return an exception
    if invalid or False otherwise.
    """
    ...
def evaluate_marker(text: str, extra: Incomplete | None = None) -> bool:
    """
    Evaluate a PEP 508 environment marker.
    Return a boolean indicating the marker result in this environment.
    Raise SyntaxError if marker is invalid.

    This implementation uses the 'pyparsing' module.
    """
    ...

class NullProvider:
    """Try to implement resources and metadata for arbitrary PEP 302 loaders"""
    egg_name: str | None
    egg_info: str | None
    loader: LoaderProtocol | None
    module_path: str

    def __init__(self, module: _ModuleLike) -> None: ...
    def get_resource_filename(self, manager: ResourceManager, resource_name: str) -> str: ...
    def get_resource_stream(self, manager: ResourceManager, resource_name: str) -> BytesIO: ...
    def get_resource_string(self, manager: ResourceManager, resource_name: str) -> bytes: ...
    def has_resource(self, resource_name: str) -> bool: ...
    def has_metadata(self, name: str) -> bool: ...
    def get_metadata(self, name: str) -> str: ...
    def get_metadata_lines(self, name: str) -> chain[str]: ...
    def resource_isdir(self, resource_name: str) -> bool: ...
    def metadata_isdir(self, name: str) -> bool: ...
    def resource_listdir(self, resource_name: str) -> list[str]: ...
    def metadata_listdir(self, name: str) -> list[str]: ...
    def run_script(self, script_name: str, namespace: dict[str, Any]) -> None: ...

# Doesn't actually extend NullProvider, solves a typing issue in pytype_test.py
class Distribution(NullProvider):
    """Wrap an actual or potential sys.path entry w/metadata"""
    PKG_INFO: ClassVar[str]
    project_name: str
    py_version: str | None
    platform: str | None
    location: str | None
    precedence: int
    def __init__(
        self,
        location: str | None = None,
        metadata: _MetadataType = None,
        project_name: str | None = None,
        version: str | None = None,
        py_version: str | None = ...,
        platform: str | None = None,
        precedence: int = 3,
    ) -> None: ...
    @classmethod
    def from_location(
        cls, location: str, basename: StrPath, metadata: _MetadataType = None, *, precedence: int = 3
    ) -> Distribution: ...
    @property
    def hashcmp(self) -> tuple[parse_version, int, str, str | None, str, str]: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: Distribution) -> bool: ...
    def __le__(self, other: Distribution) -> bool: ...
    def __gt__(self, other: Distribution) -> bool: ...
    def __ge__(self, other: Distribution) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def key(self) -> str: ...
    @property
    def parsed_version(self) -> _packaging_version.Version: ...
    @property
    def version(self) -> str: ...
    def requires(self, extras: Iterable[str] = ()) -> list[Requirement]:
        """List of Requirements needed for this distro if `extras` are used"""
        ...
    def activate(self, path: list[str] | None = None, replace: bool = False) -> None:
        """Ensure distribution is importable on `path` (default=sys.path)"""
        ...
    def egg_name(self) -> str:
        """Return what this distribution's standard .egg filename should be"""
        ...
    def __getattr__(self, attr: str) -> Any:
        """Delegate all unrecognized public attributes to .metadata provider"""
        ...
    @classmethod
    def from_filename(cls, filename: StrPath, metadata: _MetadataType = None, *, precedence: int = 3) -> Distribution: ...
    def as_requirement(self) -> Requirement:
        """Return a ``Requirement`` that matches this distribution exactly"""
        ...
    def load_entry_point(self, group: str, name: str) -> _ResolvedEntryPoint:
        """Return the `name` entry point of `group` or raise ImportError"""
        ...
    @overload
    def get_entry_map(self, group: None = None) -> dict[str, dict[str, EntryPoint]]:
        """Return the entry point map for `group`, or the full entry map"""
        ...
    @overload
    def get_entry_map(self, group: str) -> dict[str, EntryPoint]:
        """Return the entry point map for `group`, or the full entry map"""
        ...
    def get_entry_info(self, group: str, name: str) -> EntryPoint | None:
        """Return the EntryPoint object for `group`+`name`, or ``None``"""
        ...
    def insert_on(self, path: list[str], loc: Incomplete | None = None, replace: bool = False) -> None:
        """
        Ensure self.location is on path

        If replace=False (default):
            - If location is already in path anywhere, do nothing.
            - Else:
              - If it's an egg and its parent directory is on path,
                insert just ahead of the parent.
              - Else: add to the end of path.
        If replace=True:
            - If location is already on path anywhere (not eggs)
              or higher priority than its parent (eggs)
              do nothing.
            - Else:
              - If it's an egg and its parent directory is on path,
                insert just ahead of the parent,
                removing any lower-priority entries.
              - Else: add it to the front of path.
        """
        ...
    def check_version_conflict(self) -> None: ...
    def has_version(self) -> bool: ...
    def clone(self, **kw: str | int | IResourceProvider | None) -> Requirement:
        """Copy this distribution, substituting in any changed keyword args"""
        ...
    @property
    def extras(self) -> list[str]: ...

class DistInfoDistribution(Distribution):
    """
    Wrap an actual or potential sys.path entry
    w/metadata, .dist-info style.
    """
    PKG_INFO: ClassVar[Literal["METADATA"]]
    EQEQ: ClassVar[Pattern[str]]

class EggProvider(NullProvider):
    """Provider based on a virtual filesystem"""
    egg_root: str

class DefaultProvider(EggProvider):
    """Provides access to package resources in the filesystem"""
    ...

class PathMetadata(DefaultProvider):
    """
    Metadata provider for egg directories

    Usage::

        # Development eggs:

        egg_info = "/path/to/PackageName.egg-info"
        base_dir = os.path.dirname(egg_info)
        metadata = PathMetadata(base_dir, egg_info)
        dist_name = os.path.splitext(os.path.basename(egg_info))[0]
        dist = Distribution(basedir, project_name=dist_name, metadata=metadata)

        # Unpacked egg directories:

        egg_path = "/path/to/PackageName-ver-pyver-etc.egg"
        metadata = PathMetadata(egg_path, os.path.join(egg_path,'EGG-INFO'))
        dist = Distribution.from_filename(egg_path, metadata=metadata)
    """
    egg_info: str
    module_path: str
    def __init__(self, path: str, egg_info: str) -> None: ...

class ZipProvider(EggProvider):
    """Resource support for zips and eggs"""
    eagers: list[str] | None
    zip_pre: str
    # ZipProvider's loader should always be a zipimporter
    loader: zipimport.zipimporter
    def __init__(self, module: _ZipLoaderModule) -> None: ...
    @property
    def zipinfo(self) -> dict[str, ZipInfo]: ...

class EggMetadata(ZipProvider):
    """Metadata provider for .egg files"""
    loader: zipimport.zipimporter
    module_path: str
    def __init__(self, importer: zipimport.zipimporter) -> None:
        """Create a metadata provider from a zipimporter"""
        ...

class EmptyProvider(NullProvider):
    """Provider that returns nothing for all requests"""
    # A special case, we don't want all Providers inheriting from NullProvider to have a potentially None module_path
    module_path: str | None  # type:ignore[assignment]
    def __init__(self) -> None: ...

empty_provider: EmptyProvider

class ZipManifests(dict[str, MemoizedZipManifests.manifest_mod]):
    """zip manifest builder"""
    @classmethod
    def build(cls, path: str) -> dict[str, ZipInfo]:
        """
        Build a dictionary similar to the zipimport directory
        caches, except instead of tuples, store ZipInfo objects.

        Use a platform-specific path separator (os.sep) for the path keys
        for compatibility with pypy on Windows.
        """
        ...
    load = build

class MemoizedZipManifests(ZipManifests):
    """Memoized zipfile manifests."""
    class manifest_mod(NamedTuple):
        """manifest_mod(manifest, mtime)"""
        manifest: dict[str, ZipInfo]
        mtime: float

    def load(self, path: str) -> dict[str, ZipInfo]:
        """Load a manifest at path or return a suitable manifest already loaded."""
        ...

class FileMetadata(EmptyProvider):
    """
    Metadata handler for standalone PKG-INFO files

    Usage::

        metadata = FileMetadata("/path/to/PKG-INFO")

    This provider rejects all data and metadata requests except for PKG-INFO,
    which is treated as existing, and will be the contents of the file at
    the provided location.
    """
    path: StrPath
    def __init__(self, path: StrPath) -> None: ...

class PEP440Warning(RuntimeWarning):
    """
    Used when there is an issue with a version or specifier not complying with
    PEP 440.
    """
    ...

parse_version = _packaging_version.Version

def yield_lines(iterable: _NestedStr) -> chain[str]:
    r"""
    Yield valid lines of a string or iterable.

    >>> list(yield_lines(''))
    []
    >>> list(yield_lines(['foo', 'bar']))
    ['foo', 'bar']
    >>> list(yield_lines('foo\nbar'))
    ['foo', 'bar']
    >>> list(yield_lines('\nfoo\n#bar\nbaz #comment'))
    ['foo', 'baz #comment']
    >>> list(yield_lines(['foo\nbar', 'baz', 'bing\n\n\n']))
    ['foo', 'bar', 'baz', 'bing']
    """
    ...
def split_sections(s: _NestedStr) -> Generator[tuple[str | None, list[str]], None, None]:
    """
    Split a string or iterable thereof into (section, content) pairs

    Each ``section`` is a stripped version of the section header ("[section]")
    and each ``content`` is a list of stripped lines excluding blank lines and
    comment-only lines.  If there are any such lines before the first section
    header, they're returned in a first ``section`` of ``None``.
    """
    ...
def safe_name(name: str) -> str:
    """
    Convert an arbitrary string to a standard distribution name

    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
    ...
def safe_version(version: str) -> str:
    """Convert an arbitrary string to a standard version string"""
    ...
def safe_extra(extra: str) -> str:
    """
    Convert an arbitrary string to a standard 'extra' name

    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.
    """
    ...
def to_filename(name: str) -> str:
    """
    Convert a project or version name to its filename-escaped form

    Any '-' characters are currently replaced with '_'.
    """
    ...
def get_build_platform() -> str:
    """
    Return this platform's string for platform-specific distributions

    XXX Currently this is the same as ``distutils.util.get_platform()``, but it
    needs some hacks for Linux and macOS.
    """
    ...

get_platform = get_build_platform

def get_supported_platform() -> str:
    """
    Return this platform's maximum compatible version.

    distutils.util.get_platform() normally reports the minimum version
    of macOS that would be required to *use* extensions produced by
    distutils.  But what we want when checking compatibility is to know the
    version of macOS that we are *running*.  To allow usage of packages that
    explicitly require a newer version of macOS, we must also know the
    current version of the OS.

    If this condition occurs for any other platform with a version in its
    platform strings, this function should be extended accordingly.
    """
    ...
def compatible_platforms(provided: str | None, required: str | None) -> bool:
    """
    Can code for the `provided` platform run on the `required` platform?

    Returns true if either platform is ``None``, or the platforms are equal.

    XXX Needs compatibility checks for Linux and other unixy OSes.
    """
    ...
def get_default_cache() -> str:
    """
    Return the ``PYTHON_EGG_CACHE`` environment variable
    or a platform-relevant user cache dir for an app
    named "Python-Eggs".
    """
    ...
def ensure_directory(path: StrOrBytesPath) -> None:
    """Ensure that the parent directory of `path` exists"""
    ...
@overload
def normalize_path(filename: StrPath) -> str:
    """Normalize a file/dir name for comparison purposes"""
    ...
@overload
def normalize_path(filename: BytesPath) -> bytes:
    """Normalize a file/dir name for comparison purposes"""
    ...

class PkgResourcesDeprecationWarning(Warning):
    """
    Base class for warning about deprecations in ``pkg_resources``

    This class is not derived from ``DeprecationWarning``, and as such is
    visible by default.
    """
    ...

__resource_manager: ResourceManager  # Doesn't exist at runtime
resource_exists = __resource_manager.resource_exists
resource_isdir = __resource_manager.resource_isdir
resource_filename = __resource_manager.resource_filename
resource_stream = __resource_manager.resource_stream
resource_string = __resource_manager.resource_string
resource_listdir = __resource_manager.resource_listdir
set_extraction_path = __resource_manager.set_extraction_path
cleanup_resources = __resource_manager.cleanup_resources

working_set: WorkingSet
require = working_set.require
iter_entry_points = working_set.iter_entry_points
add_activation_listener = working_set.subscribe
run_script = working_set.run_script
run_main = run_script
