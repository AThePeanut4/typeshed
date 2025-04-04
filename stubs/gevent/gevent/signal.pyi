"""
Cooperative implementation of special cases of :func:`signal.signal`.

This module is designed to work with libev's child watchers, as used
by default in :func:`gevent.os.fork` Note that each ``SIGCHLD``
handler will be run in a new greenlet when the signal is delivered
(just like :class:`gevent.hub.signal`)

The implementations in this module are only monkey patched if
:func:`gevent.os.waitpid` is being used (the default) and if
:const:`signal.SIGCHLD` is available; see :func:`gevent.os.fork` for
information on configuring this not to be the case for advanced uses.

.. versionadded:: 1.1b4
.. versionchanged:: 1.5a4
   Previously there was a backwards compatibility alias
   ``gevent.signal``, introduced in 1.1b4, that partly shadowed this
   module, confusing humans and static analysis tools alike. That alias
   has been removed. (See `gevent.signal_handler`.)
"""

import sys
from signal import _HANDLER, _SIGNUM

# technically the implementations will always be around, but since they always
# throw an exception on windows, due to the missing SIGCHLD, we might as well
# pretent they don't exist, but what is different, is that the parameters are
# named even pre 3.10, so we don't just import the symbol from stdlib signal
if sys.platform != "win32":
    def getsignal(signalnum: _SIGNUM) -> _HANDLER:
        """
        Exactly the same as :func:`signal.getsignal` except where
        :const:`signal.SIGCHLD` is concerned.

        For :const:`signal.SIGCHLD`, this cooperates with :func:`signal`
        to provide consistent answers.
        """
        ...
    def signal(signalnum: _SIGNUM, handler: _HANDLER) -> _HANDLER:
        """
        Exactly the same as :func:`signal.signal` except where
        :const:`signal.SIGCHLD` is concerned.

        .. note::

           A :const:`signal.SIGCHLD` handler installed with this function
           will only be triggered for children that are forked using
           :func:`gevent.os.fork` (:func:`gevent.os.fork_and_watch`);
           children forked before monkey patching, or otherwise by the raw
           :func:`os.fork`, will not trigger the handler installed by this
           function. (It's unlikely that a SIGCHLD handler installed with
           the builtin :func:`signal.signal` would be triggered either;
           libev typically overwrites such a handler at the C level. At
           the very least, it's full of race conditions.)

        .. note::

            Use of ``SIG_IGN`` and ``SIG_DFL`` may also have race conditions
            with libev child watchers and the :mod:`gevent.subprocess` module.

        .. versionchanged:: 1.2a1
             If ``SIG_IGN`` or ``SIG_DFL`` are used to ignore ``SIGCHLD``, a
             future use of ``gevent.subprocess`` and libev child watchers
             will once again work. However, on Python 2, use of ``os.popen``
             will fail.

        .. versionchanged:: 1.1rc2
             Allow using ``SIG_IGN`` and ``SIG_DFL`` to reset and ignore ``SIGCHLD``.
             However, this allows the possibility of a race condition if ``gevent.subprocess``
             had already been used.
        """
        ...

    __all__ = ["signal", "getsignal"]
