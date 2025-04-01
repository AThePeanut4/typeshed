"""
Backwards compatibility alias for :mod:`gevent.resolver.ares`.

.. deprecated:: 1.3
   Use :mod:`gevent.resolver.ares`
"""

import sys

from gevent.resolver.ares import *

if sys.platform != "win32":
    __all__ = ["Resolver"]
