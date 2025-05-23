"""Utilities for extracting common archive formats"""

from _typeshed import Incomplete
from collections.abc import Callable

from ._distutils.errors import DistutilsError

__all__ = [
    "unpack_archive",
    "unpack_zipfile",
    "unpack_tarfile",
    "default_filter",
    "UnrecognizedFormat",
    "extraction_drivers",
    "unpack_directory",
]

class UnrecognizedFormat(DistutilsError):
    """Couldn't recognize the archive type"""
    ...

def default_filter(src, dst):
    """The default progress/filter callback; returns True for all files"""
    ...
def unpack_archive(filename, extract_dir, progress_filter=..., drivers=None) -> None:
    """
    Unpack `filename` to `extract_dir`, or raise ``UnrecognizedFormat``

    `progress_filter` is a function taking two arguments: a source path
    internal to the archive ('/'-separated), and a filesystem path where it
    will be extracted.  The callback must return the desired extract path
    (which may be the same as the one passed in), or else ``None`` to skip
    that file or directory.  The callback can thus be used to report on the
    progress of the extraction, as well as to filter the items extracted or
    alter their extraction paths.

    `drivers`, if supplied, must be a non-empty sequence of functions with the
    same signature as this function (minus the `drivers` argument), that raise
    ``UnrecognizedFormat`` if they do not support extracting the designated
    archive type.  The `drivers` are tried in sequence until one is found that
    does not raise an error, or until all are exhausted (in which case
    ``UnrecognizedFormat`` is raised).  If you do not supply a sequence of
    drivers, the module's ``extraction_drivers`` constant will be used, which
    means that ``unpack_zipfile`` and ``unpack_tarfile`` will be tried, in that
    order.
    """
    ...
def unpack_directory(filename, extract_dir, progress_filter=...) -> None:
    """
    "Unpack" a directory, using the same interface as for archives

    Raises ``UnrecognizedFormat`` if `filename` is not a directory
    """
    ...
def unpack_zipfile(filename, extract_dir, progress_filter=...) -> None:
    """
    Unpack zip `filename` to `extract_dir`

    Raises ``UnrecognizedFormat`` if `filename` is not a zipfile (as determined
    by ``zipfile.is_zipfile()``).  See ``unpack_archive()`` for an explanation
    of the `progress_filter` argument.
    """
    ...
def unpack_tarfile(filename, extract_dir, progress_filter=...):
    """
    Unpack tar/tar.gz/tar.bz2 `filename` to `extract_dir`

    Raises ``UnrecognizedFormat`` if `filename` is not a tarfile (as determined
    by ``tarfile.open()``).  See ``unpack_archive()`` for an explanation
    of the `progress_filter` argument.
    """
    ...

extraction_drivers: tuple[Callable[..., Incomplete], ...]
