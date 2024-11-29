"""
This module provides primitive operations to write multi-threaded programs.
The 'threading' module provides a more convenient interface.
"""

import sys

if sys.version_info >= (3, 9):
    from _thread import *
else:
    from _dummy_thread import *
