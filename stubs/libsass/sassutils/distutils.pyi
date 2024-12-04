"""
:mod:`sassutils.distutils` --- :mod:`setuptools`/:mod:`distutils` integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides extensions (and some magical monkey-patches, sorry)
of the standard :mod:`distutils` and :mod:`setuptools` (now it's named
Distribute) for libsass.

To use this, add ``libsass`` into ``setup_requires`` (not ``install_requires``)
option of the :file:`setup.py` script::

    from setuptools import setup

    setup(
        # ...,
        setup_requires=['libsass >= 0.6.0']
    )

It will adds :class:`build_sass` command to the :file:`setup.py` script:

.. sourcecode:: console

   $ python setup.py build_sass

This commands builds Sass/SCSS files to compiled CSS files of the project
and makes the package archive (made by :class:`~distutils.command.sdist.sdist`,
:class:`~distutils.command.bdist.bdist`, and so on) to include these compiled
CSS files.

To set the directory of Sass/SCSS source files and the directory to
store compiled CSS files, specify ``sass_manifests`` option::

    from setuptools import find_packages, setup

    setup(
        name='YourPackage',
        packages=find_packages(),
        sass_manifests={
            'your.webapp': ('static/sass', 'static/css')
        },
        setup_requires=['libsass >= 0.6.0']
    )

The option should be a mapping of package names to pairs of paths, e.g.::

    {
        'package': ('static/sass', 'static/css'),
        'package.name': ('static/scss', 'static')
    }

The option can also be a mapping of package names to manifest dictionaries::

    {
        'package': {
            'sass_path': 'static/sass',
            'css_path': 'static/css',
            'strip_extension': True,
        },
    }

.. versionadded:: 0.15.0
    Added ``strip_extension`` so ``a.scss`` is compiled to ``a.css`` instead
    of ``a.scss.css``.  This option will default to ``True`` in the future.

.. versionadded:: 0.6.0
   Added ``--output-style``/``-s`` option to :class:`build_sass` command.
"""

from typing import ClassVar

from sassutils.builder import Manifest as Manifest
from setuptools import Command, Distribution

def validate_manifests(dist: Distribution, attr: str, value: object) -> None:
    """
    Verifies that ``value`` is an expected mapping of package to
    :class:`sassutils.builder.Manifest`.
    """
    ...

class build_sass(Command):
    """Builds Sass/SCSS files to CSS files."""
    description: str
    user_options: ClassVar[list[tuple[str, str, str]]]
    package_dir: dict[str, str] | None
    output_style: str
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_package_dir(self, package: str) -> str:
        """
        Returns the directory, relative to the top of the source
        distribution, where package ``package`` should be found
        (at least according to the :attr:`package_dir` option, if any).

        Copied from :meth:`distutils.command.build_py.get_package_dir()`
        method.
        """
        ...
