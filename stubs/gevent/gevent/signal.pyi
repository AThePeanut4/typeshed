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
    def getsignal(signalnum: _SIGNUM) -> _HANDLER: ...
    def signal(signalnum: _SIGNUM, handler: _HANDLER) -> _HANDLER: ...

    __all__ = ["signal", "getsignal"]
