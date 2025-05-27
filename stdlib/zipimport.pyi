"""
zipimport provides support for importing Python modules from Zip archives.

This module exports two objects:
- zipimporter: a class; its constructor takes a path to a Zip archive.
- ZipImportError: exception raised by zipimporter objects. It's a
  subclass of ImportError, so it can be caught as ImportError, too.

It is usually not needed to use the zipimport module explicitly; it is
used by the builtin import mechanism for sys.path items that are paths
to Zip archives.
"""

import sys
from _typeshed import StrOrBytesPath
from importlib.machinery import ModuleSpec
from types import CodeType, ModuleType
from typing_extensions import deprecated

if sys.version_info >= (3, 10):
    from importlib.readers import ZipReader
else:
    from importlib.abc import ResourceReader

if sys.version_info >= (3, 10):
    from _frozen_importlib_external import _LoaderBasics
else:
    _LoaderBasics = object

__all__ = ["ZipImportError", "zipimporter"]

class ZipImportError(ImportError): ...

class zipimporter(_LoaderBasics):
    """
    zipimporter(archivepath) -> zipimporter object

    Create a new zipimporter instance. 'archivepath' must be a path to
    a zipfile, or to a specific path inside a zipfile. For example, it can be
    '/tmp/myimport.zip', or '/tmp/myimport.zip/mydirectory', if mydirectory is a
    valid directory inside the archive.

    'ZipImportError is raised if 'archivepath' doesn't point to a valid Zip
    archive.

    The 'archive' attribute of zipimporter objects contains the name of the
    zipfile targeted.
    """
    archive: str
    prefix: str
    if sys.version_info >= (3, 11):
        def __init__(self, path: str) -> None: ...
    else:
        def __init__(self, path: StrOrBytesPath) -> None: ...

    if sys.version_info < (3, 12):
        def find_loader(self, fullname: str, path: str | None = None) -> tuple[zipimporter | None, list[str]]:
            """
            find_loader(fullname, path=None) -> self, str or None.

    def get_code(self, fullname: str) -> CodeType: ...
    def get_data(self, pathname: str) -> bytes: ...
    def get_filename(self, fullname: str) -> str: ...
    if sys.version_info >= (3, 14):
        def get_resource_reader(self, fullname: str) -> ZipReader: ...  # undocumented
    elif sys.version_info >= (3, 10):
        def get_resource_reader(self, fullname: str) -> ZipReader | None: ...  # undocumented
    else:
        def get_resource_reader(self, fullname: str) -> ResourceReader | None: ...  # undocumented

    def get_source(self, fullname: str) -> str | None: ...
    def is_package(self, fullname: str) -> bool: ...
    @deprecated("Deprecated since 3.10; use exec_module() instead")
    def load_module(self, fullname: str) -> ModuleType:
        """
        load_module(fullname) -> module.

        Load the module specified by 'fullname'. 'fullname' must be the
        fully qualified (dotted) module name. It returns the imported
        module, or raises ZipImportError if it could not be imported.

        Deprecated since Python 3.10. Use exec_module() instead.
        """
        ...
    if sys.version_info >= (3, 10):
        def exec_module(self, module: ModuleType) -> None:
            """Execute the module."""
            ...
        def create_module(self, spec: ModuleSpec) -> None:
            """Use default semantics for module creation."""
            ...
        def find_spec(self, fullname: str, target: ModuleType | None = None) -> ModuleSpec | None:
            """
            Create a ModuleSpec for the specified module.

            Returns None if the module cannot be found.
            """
            ...
        def invalidate_caches(self) -> None:
            """Invalidates the cache of file data of the archive path."""
            ...
