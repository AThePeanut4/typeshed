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
) -> None:
    """
    patch_thread(threading=True, _threading_local=True, Event=True, logging=True, existing_locks=True) -> None

    Replace the standard :mod:`thread` module to make it greenlet-based.

    :keyword bool threading: When True (the default),
        also patch :mod:`threading`.
    :keyword bool _threading_local: When True (the default),
        also patch :class:`_threading_local.local`.
    :keyword bool logging: When True (the default), also patch locks
        taken if the logging module has been configured.

    :keyword bool existing_locks: When True (the default), and the
        process is still single threaded, make sure that any
        :class:`threading.RLock` (and, under Python 3, :class:`importlib._bootstrap._ModuleLock`)
        instances that are currently locked can be properly unlocked. **Important**: This is a
        best-effort attempt and, on certain implementations, may not detect all
        locks. It is important to monkey-patch extremely early in the startup process.
        Setting this to False is not recommended, especially on Python 2.

    .. caution::
        Monkey-patching :mod:`thread` and using
        :class:`multiprocessing.Queue` or
        :class:`concurrent.futures.ProcessPoolExecutor` (which uses a
        ``Queue``) will hang the process.

        Monkey-patching with this function and using
        sub-interpreters (and advanced C-level API) and threads may be
        unstable on certain platforms.

    .. versionchanged:: 1.1b1
        Add *logging* and *existing_locks* params.
    .. versionchanged:: 1.3a2
        ``Event`` defaults to True.
    """
    ...
def patch_socket(dns: bool = True, aggressive: bool = True) -> None:
    """
    Replace the standard socket object with gevent's cooperative
    sockets.

    :keyword bool dns: When true (the default), also patch address
        resolution functions in :mod:`socket`. See :doc:`/dns` for details.
    """
    ...
def patch_dns() -> None:
    """
    Replace :doc:`DNS functions </dns>` in :mod:`socket` with
    cooperative versions.

    This is only useful if :func:`patch_socket` has been called and is
    done automatically by that method if requested.
    """
    ...
def patch_ssl() -> None:
    """
    patch_ssl() -> None

    Replace :class:`ssl.SSLSocket` object and socket wrapping functions in
    :mod:`ssl` with cooperative versions.

    This is only useful if :func:`patch_socket` has been called.
    """
    ...
def patch_select(aggressive: bool = True) -> None:
    """
    Replace :func:`select.select` with :func:`gevent.select.select`
    and :func:`select.poll` with :class:`gevent.select.poll` (where available).

    If ``aggressive`` is true (the default), also remove other
    blocking functions from :mod:`select` .

    - :func:`select.epoll`
    - :func:`select.kqueue`
    - :func:`select.kevent`
    - :func:`select.devpoll` (Python 3.5+)
    """
    ...
def patch_selectors(aggressive: bool = True) -> None:
    """
    Replace :class:`selectors.DefaultSelector` with
    :class:`gevent.selectors.GeventSelector`.

    If ``aggressive`` is true (the default), also remove other
    blocking classes :mod:`selectors`:

    - :class:`selectors.EpollSelector`
    - :class:`selectors.KqueueSelector`
    - :class:`selectors.DevpollSelector` (Python 3.5+)

    On Python 2, the :mod:`selectors2` module is used instead
    of :mod:`selectors` if it is available. If this module cannot
    be imported, no patching is done and :mod:`gevent.selectors` is
    not available.

    In :func:`patch_all`, the *select* argument controls both this function
    and :func:`patch_select`.

    .. versionadded:: 20.6.0
    """
    ...
def patch_subprocess() -> None:
    """
    Replace :func:`subprocess.call`, :func:`subprocess.check_call`,
    :func:`subprocess.check_output` and :class:`subprocess.Popen` with
    :mod:`cooperative versions <gevent.subprocess>`.

    .. note::
       On Windows under Python 3, the API support may not completely match
       the standard library.
    """
    ...
def patch_signal() -> None:
    """
    Make the :func:`signal.signal` function work with a :func:`monkey-patched os <patch_os>`.

    .. caution:: This method must be used with :func:`patch_os` to have proper ``SIGCHLD``
         handling. :func:`patch_all` calls both by default.

    .. caution:: For proper ``SIGCHLD`` handling, you must yield to the event loop.
         Using :func:`patch_all` is the easiest way to ensure this.

    .. seealso:: :mod:`gevent.signal`
    """
    ...
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
) -> bool | None:
    """
    Do all of the default monkey patching (calls every other applicable
    function in this module).

    :return: A true value if patching all modules wasn't cancelled, a false
      value if it was.

    .. versionchanged:: 1.1
       Issue a :mod:`warning <warnings>` if this function is called multiple times
       with different arguments. The second and subsequent calls will only add more
       patches, they can never remove existing patches by setting an argument to ``False``.
    .. versionchanged:: 1.1
       Issue a :mod:`warning <warnings>` if this function is called with ``os=False``
       and ``signal=True``. This will cause SIGCHLD handlers to not be called. This may
       be an error in the future.
    .. versionchanged:: 1.3a2
       ``Event`` defaults to True.
    .. versionchanged:: 1.3b1
       Defined the return values.
    .. versionchanged:: 1.3b1
       Add ``**kwargs`` for the benefit of event subscribers. CAUTION: gevent may add
       and interpret additional arguments in the future, so it is suggested to use prefixes
       for kwarg values to be interpreted by plugins, for example, `patch_all(mylib_futures=True)`.
    .. versionchanged:: 1.3.5
       Add *queue*, defaulting to True, for Python 3.7.
    .. versionchanged:: 1.5
       Remove the ``httplib`` argument. Previously, setting it raised a ``ValueError``.
    .. versionchanged:: 1.5a3
       Add the ``contextvars`` argument.
    .. versionchanged:: 1.5
       Better handling of patching more than once.
    """
    ...
def main() -> dict[str, Any]:
    """
    gevent.monkey - monkey patch the standard modules to use gevent.

    USAGE: ``python -m gevent.monkey [MONKEY OPTIONS] [--module] (script|module) [SCRIPT OPTIONS]``

    If no MONKEY OPTIONS are present, monkey patches all the modules as if by calling ``patch_all()``.
    You can exclude a module with --no-<module>, e.g. --no-thread. You can
    specify a module to patch with --<module>, e.g. --socket. In the latter
    case only the modules specified on the command line will be patched.

    The default behavior is to execute the script passed as argument. If you wish
    to run a module instead, pass the `--module` argument before the module name.

    .. versionchanged:: 1.3b1
        The *script* argument can now be any argument that can be passed to `runpy.run_path`,
        just like the interpreter itself does, for example a package directory containing ``__main__.py``.
        Previously it had to be the path to
        a .py source file.

    .. versionchanged:: 1.5
        The `--module` option has been added.

    MONKEY OPTIONS: ``--verbose ``
    """
    ...
