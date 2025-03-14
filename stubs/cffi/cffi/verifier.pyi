import io
from _typeshed import Incomplete
from typing_extensions import TypeAlias

NativeIO: TypeAlias = io.StringIO

class Verifier:
    ffi: Incomplete
    preamble: Incomplete
    flags: Incomplete
    kwds: Incomplete
    tmpdir: Incomplete
    sourcefilename: Incomplete
    modulefilename: Incomplete
    ext_package: Incomplete
    def __init__(
        self,
        ffi,
        preamble,
        tmpdir: Incomplete | None = None,
        modulename: Incomplete | None = None,
        ext_package: Incomplete | None = None,
        tag: str = "",
        force_generic_engine: bool = False,
        source_extension: str = ".c",
        flags: Incomplete | None = None,
        relative_to: Incomplete | None = None,
        **kwds,
    ) -> None: ...
    def write_source(self, file: Incomplete | None = None) -> None:
        """
        Write the C source code.  It is produced in 'self.sourcefilename',
        which can be tweaked beforehand.
        """
        ...
    def compile_module(self) -> None:
        """
        Write the C source code (if not done already) and compile it.
        This produces a dynamic link library in 'self.modulefilename'.
        """
        ...
    def load_library(self):
        """
        Get a C module from this Verifier instance.
        Returns an instance of a FFILibrary class that behaves like the
        objects returned by ffi.dlopen(), but that delegates all
        operations to the C module.  If necessary, the C code is written
        and compiled first.
        """
        ...
    def get_module_name(self): ...
    def get_extension(self): ...
    def generates_python_module(self): ...
    def make_relative_to(self, kwds, relative_to): ...

def set_tmpdir(dirname) -> None:
    """Set the temporary directory to use instead of __pycache__."""
    ...
def cleanup_tmpdir(tmpdir: Incomplete | None = None, keep_so: bool = False) -> None:
    """
    Clean up the temporary directory by removing all files in it
    called `_cffi_*.{c,so}` as well as the `build` subdirectory.
    """
    ...
