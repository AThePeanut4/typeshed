"""
Make the standard library cooperative.

The primary purpose of this module is to carefully patch, in place,
portions of the standard library with gevent-friendly functions that
behave in the same way as the original (at least as closely as possible).

The primary interface to this is the :func:`patch_all` function, which
performs all the available patches. It accepts arguments to limit the
patching to certain modules, but most programs **should** use the
default values as they receive the most wide-spread testing, and some monkey
patches have dependencies on others.

Patching **should be done as early as possible** in the lifecycle of the
program. For example, the main module (the one that tests against
``__main__`` or is otherwise the first imported) should begin with
this code, ideally before any other imports::

    from gevent import monkey
    monkey.patch_all()

A corollary of the above is that patching **should be done on the main
thread** and **should be done while the program is single-threaded**.

.. tip::

    Some frameworks, such as gunicorn, handle monkey-patching for you.
    Check their documentation to be sure.

.. warning::

    Patching too late can lead to unreliable behaviour (for example, some
    modules may still use blocking sockets) or even errors.

.. tip::

    Be sure to read the documentation for each patch function to check for
    known incompatibilities.

Querying
========

Sometimes it is helpful to know if objects have been monkey-patched, and in
advanced cases even to have access to the original standard library functions. This
module provides functions for that purpose.

- :func:`is_module_patched`
- :func:`is_object_patched`
- :func:`get_original`

.. _plugins:

Plugins and Events
==================

Beginning in gevent 1.3, events are emitted during the monkey patching process.
These events are delivered first to :mod:`gevent.events` subscribers, and then
to `setuptools entry points`_.

The following events are defined. They are listed in (roughly) the order
that a call to :func:`patch_all` will emit them.

- :class:`gevent.events.GeventWillPatchAllEvent`
- :class:`gevent.events.GeventWillPatchModuleEvent`
- :class:`gevent.events.GeventDidPatchModuleEvent`
- :class:`gevent.events.GeventDidPatchBuiltinModulesEvent`
- :class:`gevent.events.GeventDidPatchAllEvent`

Each event class documents the corresponding setuptools entry point name. The
entry points will be called with a single argument, the same instance of
the class that was sent to the subscribers.

You can subscribe to the events to monitor the monkey-patching process and
to manipulate it, for example by raising :exc:`gevent.events.DoNotPatch`.

You can also subscribe to the events to provide additional patching beyond what
gevent distributes, either for additional standard library modules, or
for third-party packages. The suggested time to do this patching is in
the subscriber for :class:`gevent.events.GeventDidPatchBuiltinModulesEvent`.
For example, to automatically patch `psycopg2`_ using `psycogreen`_
when the call to :func:`patch_all` is made, you could write code like this::

    # mypackage.py
    def patch_psycopg(event):
        from psycogreen.gevent import patch_psycopg
        patch_psycopg()

In your ``setup.py`` you would register it like this::

    from setuptools import setup
    setup(
        ...
        entry_points={
            'gevent.plugins.monkey.did_patch_builtins': [
                'psycopg2 = mypackage:patch_psycopg',
            ],
        },
        ...
    )

For more complex patching, gevent provides a helper method
that you can call to replace attributes of modules with attributes of your
own modules. This function also takes care of emitting the appropriate events.

- :func:`patch_module`

.. _setuptools entry points: http://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins
.. _psycopg2: https://pypi.python.org/pypi/psycopg2
.. _psycogreen: https://pypi.python.org/pypi/psycogreen

Use as a module
===============

Sometimes it is useful to run existing python scripts or modules that
were not built to be gevent aware under gevent. To do so, this module
can be run as the main module, passing the script and its arguments.
For details, see the :func:`main` function.

.. versionchanged:: 1.3b1
   Added support for plugins and began emitting will/did patch events.
"""

from typing import Any

from gevent.monkey.api import get_original as get_original, patch_module as patch_module

class MonkeyPatchWarning(RuntimeWarning):
    """
    The type of warnings we issue.

    .. versionadded:: 1.3a2
    """
    ...

def is_module_patched(mod_name: str) -> bool:
    """
    Check if a module has been replaced with a cooperative version.

    :param str mod_name: The name of the standard library module,
        e.g., ``'socket'``.
    """
    ...
def is_object_patched(mod_name: str, item_name: str) -> bool:
    """
    Check if an object in a module has been replaced with a
    cooperative version.

    :param str mod_name: The name of the standard library module,
        e.g., ``'socket'``.
    :param str item_name: The name of the attribute in the module,
        e.g., ``'create_connection'``.
    """
    ...
def patch_os() -> None:
    """
    Replace :func:`os.fork` with :func:`gevent.fork`, and, on POSIX,
    :func:`os.waitpid` with :func:`gevent.os.waitpid` (if the
    environment variable ``GEVENT_NOWAITPID`` is not defined). Does
    nothing if fork is not available.

    .. caution:: This method must be used with :func:`patch_signal` to have proper `SIGCHLD`
         handling and thus correct results from ``waitpid``.
         :func:`patch_all` calls both by default.

    .. caution:: For `SIGCHLD` handling to work correctly, the event loop must run.
         The easiest way to help ensure this is to use :func:`patch_all`.
    """
    ...
def patch_queue() -> None:
    """
    Patch objects in :mod:`queue`.


    Currently, this just replaces :class:`queue.SimpleQueue` (implemented
    in C) with its Python counterpart, but the details may change at any time.

    .. versionadded:: 1.3.5
    """
    ...
def patch_time() -> None:
    """Replace :func:`time.sleep` with :func:`gevent.sleep`."""
    ...
def patch_thread(
    threading: bool = True, _threading_local: bool = True, Event: bool = True, logging: bool = True, existing_locks: bool = True
) -> None: ...
def patch_socket(dns: bool = True, aggressive: bool = True) -> None: ...
def patch_builtins() -> None: ...
def patch_dns() -> None: ...
def patch_ssl() -> None: ...
def patch_select(aggressive: bool = True) -> None: ...
def patch_selectors(aggressive: bool = True) -> None: ...
def patch_subprocess() -> None: ...
def patch_sys(stdin: bool = True, stdout: bool = True, stderr: bool = True) -> None: ...
def patch_signal() -> None: ...
def patch_all(
    socket: bool = True,
    dns: bool = True,
    time: bool = True,
    select: bool = True,
    thread: bool = True,
    os: bool = True,
    ssl: bool = True,
    subprocess: bool = True,
    sys: bool = False,
    aggressive: bool = True,
    Event: bool = True,
    builtins: bool = True,  # does nothing on Python 3
    signal: bool = True,
    queue: bool = True,
    contextvars: bool = True,  # does nothing on Python 3.7+
    **kwargs: object,
) -> bool | None: ...
def main() -> dict[str, Any]: ...

__all__ = [
    "patch_all",
    "patch_builtins",
    "patch_dns",
    "patch_os",
    "patch_queue",
    "patch_select",
    "patch_signal",
    "patch_socket",
    "patch_ssl",
    "patch_subprocess",
    "patch_sys",
    "patch_thread",
    "patch_time",
    # query functions
    "get_original",
    "is_module_patched",
    "is_object_patched",
    # plugin API
    "patch_module",
    # module functions
    "main",
    # Errors and warnings
    "MonkeyPatchWarning",
]
