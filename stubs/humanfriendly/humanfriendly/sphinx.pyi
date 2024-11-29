"""
Customizations for and integration with the Sphinx_ documentation generator.

The :mod:`humanfriendly.sphinx` module uses the `Sphinx extension API`_ to
customize the process of generating Sphinx based Python documentation. To
explore the functionality this module offers its best to start reading
from the :func:`setup()` function.

.. _Sphinx: http://www.sphinx-doc.org/
.. _Sphinx extension API: http://sphinx-doc.org/extdev/appapi.html
"""

from typing import Any

logger: Any

def deprecation_note_callback(app, what, name, obj, options, lines) -> None:
    """
    Automatically document aliases defined using :func:`~humanfriendly.deprecation.define_aliases()`.

    Refer to :func:`enable_deprecation_notes()` to enable the use of this
    function (you probably don't want to call :func:`deprecation_note_callback()`
    directly).

    This function implements a callback for ``autodoc-process-docstring`` that
    reformats module docstrings to append an overview of aliases defined by the
    module.

    The parameters expected by this function are those defined for Sphinx event
    callback functions (i.e. I'm not going to document them here :-).
    """
    ...
def enable_deprecation_notes(app) -> None:
    """
    Enable documenting backwards compatibility aliases using the autodoc_ extension.

    :param app: The Sphinx application object.

    This function connects the :func:`deprecation_note_callback()` function to
    ``autodoc-process-docstring`` events.

    .. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
    """
    ...
def enable_man_role(app) -> None:
    """
    Enable the ``:man:`` role for linking to Debian Linux manual pages.

    :param app: The Sphinx application object.

    This function registers the :func:`man_role()` function to handle the
    ``:man:`` role.
    """
    ...
def enable_pypi_role(app) -> None:
    """
    Enable the ``:pypi:`` role for linking to the Python Package Index.

    :param app: The Sphinx application object.

    This function registers the :func:`pypi_role()` function to handle the
    ``:pypi:`` role.
    """
    ...
def enable_special_methods(app) -> None:
    """
    Enable documenting "special methods" using the autodoc_ extension.

    :param app: The Sphinx application object.

    This function connects the :func:`special_methods_callback()` function to
    ``autodoc-skip-member`` events.

    .. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
    """
    ...
def enable_usage_formatting(app) -> None:
    """
    Reformat human friendly usage messages to reStructuredText_.

    :param app: The Sphinx application object (as given to ``setup()``).

    This function connects the :func:`usage_message_callback()` function to
    ``autodoc-process-docstring`` events.

    .. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
    """
    ...
def man_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Convert a Linux manual topic to a hyperlink.

    Using the ``:man:`` role is very simple, here's an example:

    .. code-block:: rst

        See the :man:`python` documentation.

    This results in the following:

      See the :man:`python` documentation.

    As the example shows you can use the role inline, embedded in sentences of
    text. In the generated documentation the ``:man:`` text is omitted and a
    hyperlink pointing to the Debian Linux manual pages is emitted.
    """
    ...
def pypi_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Generate hyperlinks to the Python Package Index.

    Using the ``:pypi:`` role is very simple, here's an example:

    .. code-block:: rst

        See the :pypi:`humanfriendly` package.

    This results in the following:

      See the :pypi:`humanfriendly` package.

    As the example shows you can use the role inline, embedded in sentences of
    text. In the generated documentation the ``:pypi:`` text is omitted and a
    hyperlink pointing to the Python Package Index is emitted.
    """
    ...
def setup(app):
    """
    Enable all of the provided Sphinx_ customizations.

    :param app: The Sphinx application object.

    The :func:`setup()` function makes it easy to enable all of the Sphinx
    customizations provided by the :mod:`humanfriendly.sphinx` module with the
    least amount of code. All you need to do is to add the module name to the
    ``extensions`` variable in your ``conf.py`` file:

    .. code-block:: python

       # Sphinx extension module names.
       extensions = [
           'sphinx.ext.autodoc',
           'sphinx.ext.doctest',
           'sphinx.ext.intersphinx',
           'humanfriendly.sphinx',
       ]

    When Sphinx sees the :mod:`humanfriendly.sphinx` name it will import the
    module and call its :func:`setup()` function. This function will then call
    the following:

    - :func:`enable_deprecation_notes()`
    - :func:`enable_man_role()`
    - :func:`enable_pypi_role()`
    - :func:`enable_special_methods()`
    - :func:`enable_usage_formatting()`

    Of course more functionality may be added at a later stage. If you don't
    like that idea you may be better of calling the individual functions from
    your own ``setup()`` function.
    """
    ...
def special_methods_callback(app, what, name, obj, skip, options):
    """
    Enable documenting "special methods" using the autodoc_ extension.

    Refer to :func:`enable_special_methods()` to enable the use of this
    function (you probably don't want to call
    :func:`special_methods_callback()` directly).

    This function implements a callback for ``autodoc-skip-member`` events to
    include documented "special methods" (method names with two leading and two
    trailing underscores) in your documentation. The result is similar to the
    use of the ``special-members`` flag with one big difference: Special
    methods are included but other types of members are ignored. This means
    that attributes like ``__weakref__`` will always be ignored (this was my
    main annoyance with the ``special-members`` flag).

    The parameters expected by this function are those defined for Sphinx event
    callback functions (i.e. I'm not going to document them here :-).
    """
    ...
def usage_message_callback(app, what, name, obj, options, lines) -> None:
    """
    Reformat human friendly usage messages to reStructuredText_.

    Refer to :func:`enable_usage_formatting()` to enable the use of this
    function (you probably don't want to call :func:`usage_message_callback()`
    directly).

    This function implements a callback for ``autodoc-process-docstring`` that
    reformats module docstrings using :func:`.render_usage()` so that Sphinx
    doesn't mangle usage messages that were written to be human readable
    instead of machine readable. Only module docstrings whose first line starts
    with :data:`.USAGE_MARKER` are reformatted.

    The parameters expected by this function are those defined for Sphinx event
    callback functions (i.e. I'm not going to document them here :-).
    """
    ...
