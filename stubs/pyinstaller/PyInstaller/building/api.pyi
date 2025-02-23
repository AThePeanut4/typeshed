# PYZ, EXE and COLLECT referenced in https://pyinstaller.org/en/stable/spec-files.html#spec-file-operation
# MERGE is referenced in https://pyinstaller.org/en/stable/spec-files.html#example-merge-spec-file
# hide_console referenced in https://pyinstaller.org/en/stable/feature-notes.html#automatic-hiding-and-minimization-of-console-window-under-windows
# Not to be imported during runtime, but is the type reference for spec files which are executed as python code

"""
This module contains classes that are available for the .spec files.

Spec file is generated by PyInstaller. The generated code from .spec file
is a way how PyInstaller does the dependency analysis and creates executable.
"""

import sys
from _typeshed import FileDescriptorOrPath, StrOrBytesPath, StrPath, Unused
from collections.abc import Iterable, Mapping, Sequence
from types import CodeType
from typing import ClassVar, Final, Literal
from typing_extensions import TypeAlias

from PyInstaller.building import _PyiBlockCipher
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import Target, _TOCTuple
from PyInstaller.building.splash import Splash
from PyInstaller.utils.win32.versioninfo import VSVersionInfo

if sys.platform == "darwin":
    _TargetArch: TypeAlias = Literal["x86_64", "arm64", "universal2"]
    _SupportedTargetArchParam: TypeAlias = _TargetArch | None
    _CodesignIdentity: TypeAlias = str | None
    _CodesignIdentityParam: TypeAlias = str | None
else:
    _TargetArch: TypeAlias = None
    _SupportedTargetArchParam: TypeAlias = Unused
    _CodesignIdentity: TypeAlias = None
    _CodesignIdentityParam: TypeAlias = Unused

if sys.platform == "win32":
    _Icon: TypeAlias = list[StrPath] | str
    _IconParam: TypeAlias = StrPath | list[StrPath] | None
elif sys.platform == "darwin":
    _Icon: TypeAlias = list[StrPath] | None
    _IconParam: TypeAlias = StrPath | list[StrPath] | None
else:
    _Icon: TypeAlias = None
    _IconParam: TypeAlias = Unused

if sys.platform == "win32":
    _VersionSrc: TypeAlias = VSVersionInfo | None
    _VersionParam: TypeAlias = VSVersionInfo | StrOrBytesPath | None
    _Manifest: TypeAlias = bytes
    _ManifestParam: TypeAlias = str | None
else:
    _VersionSrc: TypeAlias = None
    _VersionParam: TypeAlias = Unused
    _Manifest: TypeAlias = None
    _ManifestParam: TypeAlias = Unused

_HideConsole: TypeAlias = Literal["hide-early", "minimize-early", "hide-late", "minimize-late"] | None

class PYZ(Target):
    """Creates a zlib-based PYZ archive that contains byte-compiled pure Python modules."""
    name: str
    cipher: _PyiBlockCipher
    dependencies: list[_TOCTuple]
    toc: list[_TOCTuple]
    code_dict: dict[str, CodeType]
    def __init__(self, *tocs: Iterable[_TOCTuple], name: str | None = None, cipher: _PyiBlockCipher = None) -> None:
        """
        tocs
            One or more TOC (Table of Contents) lists, usually an `Analysis.pure`.

        kwargs
            Possible keyword arguments:

            name
                A filename for the .pyz. Normally not needed, as the generated name will do fine.
        """
        ...
    def assemble(self) -> None: ...

class PKG(Target):
    """
    Creates a CArchive. CArchive is the data structure that is embedded into the executable. This data structure allows
    to include various read-only data in a single-file deployment.
    """
    xformdict: ClassVar[dict[str, str]]
    toc: list[_TOCTuple]
    cdict: Mapping[str, bool]
    python_lib_name: str
    name: str
    exclude_binaries: bool
    strip_binaries: bool
    upx_binaries: bool
    upx_exclude: Iterable[str]
    target_arch: _TargetArch | None
    codesign_identity: _CodesignIdentity
    entitlements_file: FileDescriptorOrPath | None
    def __init__(
        self,
        toc: Iterable[_TOCTuple],
        python_lib_name: str,
        name: str | None = None,
        cdict: Mapping[str, bool] | None = None,
        exclude_binaries: bool = False,
        strip_binaries: bool = False,
        upx_binaries: bool = False,
        upx_exclude: Iterable[str] | None = None,
        target_arch: _SupportedTargetArchParam = None,
        codesign_identity: _CodesignIdentityParam = None,
        entitlements_file: FileDescriptorOrPath | None = None,
    ) -> None:
        """
        toc
            A TOC (Table of Contents) list.
        python_lib_name
            Name of the python shared library to store in PKG. Required by bootloader.
        name
            An optional filename for the PKG.
        cdict
            Dictionary that specifies compression by typecode. For Example, PYZ is left uncompressed so that it
            can be accessed inside the PKG. The default uses sensible values. If zlib is not available, no
            compression is used.
        exclude_binaries
            If True, EXTENSIONs and BINARYs will be left out of the PKG, and forwarded to its container (usually
            a COLLECT).
        strip_binaries
            If True, use 'strip' command to reduce the size of binary files.
        upx_binaries
        """
        ...
    def assemble(self) -> None: ...

class EXE(Target):
    """Creates the final executable of the frozen app. This bundles all necessary files together."""
    exclude_binaries: bool
    bootloader_ignore_signals: bool
    console: bool
    hide_console: _HideConsole
    disable_windowed_traceback: bool
    debug: bool
    name: str
    icon: _Icon
    versrsrc: _VersionSrc
    manifest: _Manifest
    embed_manifest: bool
    resources: Sequence[str]
    strip: bool
    upx_exclude: Iterable[str]
    runtime_tmpdir: str | None
    contents_directory: str | None
    append_pkg: bool
    uac_admin: bool
    uac_uiaccess: bool
    argv_emulation: bool
    target_arch: _TargetArch
    codesign_identity: _CodesignIdentity
    entitlements_file: FileDescriptorOrPath | None
    upx: bool
    pkgname: str
    toc: list[_TOCTuple]
    pkg: PKG
    dependencies: list[_TOCTuple]
    exefiles: list[_TOCTuple]
    def __init__(
        self,
        *args: Iterable[_TOCTuple] | PYZ | Splash,
        exclude_binaries: bool = False,
        bootloader_ignore_signals: bool = False,
        console: bool = True,
        hide_console: _HideConsole = None,
        disable_windowed_traceback: bool = False,
        debug: bool = False,
        name: str | None = None,
        icon: _IconParam = None,
        version: _VersionParam = None,
        manifest: _ManifestParam = None,
        embed_manifest: Literal[True] = True,
        resources: Sequence[str] = ...,
        strip: bool = False,
        upx_exclude: Iterable[str] = ...,
        runtime_tmpdir: str | None = None,
        contents_directory: str = "_internal",
        append_pkg: bool = True,
        uac_admin: bool = False,
        uac_uiaccess: bool = False,
        argv_emulation: bool = False,
        target_arch: _SupportedTargetArchParam = None,
        codesign_identity: _CodesignIdentityParam = None,
        entitlements_file: FileDescriptorOrPath | None = None,
        upx: bool = False,
        cdict: Mapping[str, bool] | None = None,
    ) -> None:
        """
        args
            One or more arguments that are either an instance of `Target` or an iterable representing TOC list.
        kwargs
            Possible keyword arguments:

            bootloader_ignore_signals
                Non-Windows only. If True, the bootloader process will ignore all ignorable signals. If False (default),
                it will forward all signals to the child process. Useful in situations where for example a supervisor
                process signals both the bootloader and the child (e.g., via a process group) to avoid signalling the
                child twice.
            console
                On Windows or macOS governs whether to use the console executable or the windowed executable. Always
                True on Linux/Unix (always console executable - it does not matter there).
            hide_console
                Windows only. In console-enabled executable, hide or minimize the console window if the program owns the
                console window (i.e., was not launched from existing console window). Depending on the setting, the
                console is hidden/mininized either early in the bootloader execution ('hide-early', 'minimize-early') or
                late in the bootloader execution ('hide-late', 'minimize-late'). The early option takes place as soon as
                the PKG archive is found. In onefile builds, the late option takes place after application has unpacked
                itself and before it launches the child process. In onedir builds, the late option takes place before
                starting the embedded python interpreter.
            disable_windowed_traceback
                Disable traceback dump of unhandled exception in windowed (noconsole) mode (Windows and macOS only),
                and instead display a message that this feature is disabled.
            debug
                Setting to True gives you progress messages from the executable (for console=False there will be
                annoying MessageBoxes on Windows).
            name
                The filename for the executable. On Windows suffix '.exe' is appended.
            exclude_binaries
                Forwarded to the PKG the EXE builds.
            icon
                Windows and macOS only. icon='myicon.ico' to use an icon file or icon='notepad.exe,0' to grab an icon
                resource. Defaults to use PyInstaller's console or windowed icon. Use icon=`NONE` to not add any icon.
            version
                Windows only. version='myversion.txt'. Use grab_version.py to get a version resource from an executable
                and then edit the output to create your own. (The syntax of version resources is so arcane that I would
                not attempt to write one from scratch).
            uac_admin
                Windows only. Setting to True creates a Manifest with will request elevation upon application start.
            uac_uiaccess
                Windows only. Setting to True allows an elevated application to work with Remote Desktop.
            argv_emulation
                macOS only. Enables argv emulation in macOS .app bundles (i.e., windowed bootloader). If enabled, the
                initial open document/URL Apple Events are intercepted by bootloader and converted into sys.argv.
            target_arch
                macOS only. Used to explicitly specify the target architecture; either single-arch ('x86_64' or 'arm64')
                or 'universal2'. Used in checks that the collected binaries contain the requires arch slice(s) and/or
                to convert fat binaries into thin ones as necessary. If not specified (default), a single-arch build
                corresponding to running architecture is assumed.
            codesign_identity
                macOS only. Use the provided identity to sign collected binaries and the generated executable. If
                signing identity is not provided, ad-hoc signing is performed.
            entitlements_file
                macOS only. Optional path to entitlements file to use with code signing of collected binaries
                (--entitlements option to codesign utility).
            contents_directory
                Onedir mode only. Specifies the name of the directory where all files par the executable will be placed.
                Setting the name to '.' (or '' or None) re-enables old onedir layout without contents directory.
        """
        ...
    mtm: float
    def assemble(self) -> None: ...

class COLLECT(Target):
    """In one-dir mode creates the output folder with all necessary files."""
    strip_binaries: bool
    upx_exclude: Iterable[str]
    console: bool
    target_arch: _TargetArch | None
    codesign_identity: _CodesignIdentity
    entitlements_file: FileDescriptorOrPath | None
    upx_binaries: bool
    name: str
    toc: list[_TOCTuple]
    def __init__(
        self,
        *args: Iterable[_TOCTuple] | EXE,
        strip: bool = False,
        upx_exclude: Iterable[str] = ...,
        upx: bool = False,
        name: str,
    ) -> None:
        """
        args
            One or more arguments that are either an instance of `Target` or an iterable representing TOC list.
        kwargs
            Possible keyword arguments:

            name
                The name of the directory to be built.
        """
        ...
    def assemble(self) -> None: ...

class MERGE:
    """
    Given Analysis objects for multiple executables, replace occurrences of data and binary files with references to the
    first executable in which they occur. The actual data and binary files are then collected only once, thereby
    reducing the disk space used by multiple executables. Every executable (even onedir ones!) obtained from a
    MERGE-processed Analysis gains onefile semantics, because it needs to extract its referenced dependencies from other
    executables into temporary directory before they can run.
    """
    def __init__(self, *args: tuple[Analysis, Unused, str]) -> None:
        """
        args
            Dependencies as a list of (analysis, identifier, path_to_exe) tuples. `analysis` is an instance of
            `Analysis`, `identifier` is the basename of the entry-point script (without .py suffix), and `path_to_exe`
            is path to the corresponding executable, relative to the `dist` directory (without .exe suffix in the
            filename component). For onefile executables, `path_to_exe` is usually just executable's base name
            (e.g., `myexecutable`). For onedir executables, `path_to_exe` usually comprises both the application's
            directory name and executable name (e.g., `myapp/myexecutable`).
        """
        ...

UNCOMPRESSED: Final = False
COMPRESSED: Final = True
