"""
:mod:`sassutils.builder` --- Build the whole directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from collections.abc import Mapping
from re import Pattern
from typing import Any

from sass import _OutputStyle

SUFFIXES: frozenset[str]
SUFFIX_PATTERN: Pattern[str]

def build_directory(
    sass_path: str,
    css_path: str,
    output_style: _OutputStyle = "nested",
    _root_sass: None = None,  # internal arguments for recursion
    _root_css: None = None,  # internal arguments for recursion
    strip_extension: bool = False,
) -> dict[str, str]:
    """
    Compiles all Sass/SCSS files in ``path`` to CSS.

    :param sass_path: the path of the directory which contains source files
                      to compile
    :type sass_path: :class:`str`, :class:`basestring`
    :param css_path: the path of the directory compiled CSS files will go
    :type css_path: :class:`str`, :class:`basestring`
    :param output_style: an optional coding style of the compiled result.
                         choose one of: ``'nested'`` (default), ``'expanded'``,
                         ``'compact'``, ``'compressed'``
    :type output_style: :class:`str`
    :returns: a dictionary of source filenames to compiled CSS filenames
    :rtype: :class:`collections.abc.Mapping`

    .. versionadded:: 0.6.0
       The ``output_style`` parameter.
    """
    ...

class Manifest:
    """
    Building manifest of Sass/SCSS.

    :param sass_path: the path of the directory that contains Sass/SCSS
                      source files
    :type sass_path: :class:`str`, :class:`basestring`
    :param css_path: the path of the directory to store compiled CSS
                     files
    :type css_path: :class:`str`, :class:`basestring`
    :param strip_extension: whether to remove the original file extension
    :type strip_extension: :class:`bool`
    """
    @classmethod
    def normalize_manifests(
        cls, manifests: Mapping[str, Manifest | tuple[Any, ...] | Mapping[str, Any] | str] | None
    ) -> dict[str, Manifest]: ...
    sass_path: str
    css_path: str
    wsgi_path: str
    strip_extension: bool
    def __init__(
        self, sass_path: str, css_path: str | None = None, wsgi_path: str | None = None, strip_extension: bool | None = None
    ) -> None: ...
    def resolve_filename(self, package_dir: str, filename: str) -> tuple[str, str]: ...
    def unresolve_filename(self, package_dir: str, filename: str) -> str: ...
    def build(self, package_dir: str, output_style: _OutputStyle = "nested") -> frozenset[str]: ...
    def build_one(self, package_dir: str, filename: str, source_map: bool = False) -> str: ...

__all__ = ("SUFFIXES", "SUFFIX_PATTERN", "Manifest", "build_directory")
