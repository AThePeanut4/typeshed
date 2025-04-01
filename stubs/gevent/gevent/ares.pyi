"""
Backwards compatibility alias for :mod:`gevent.resolver.cares`.

.. deprecated:: 1.3
   Use :mod:`gevent.resolver.cares`
"""

import sys

from gevent.resolver.cares import *

if sys.platform != "win32":
    __all__ = ["channel"]
