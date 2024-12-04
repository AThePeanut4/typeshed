"""
flask_cors
~~~~
Flask-CORS is a simple extension to Flask allowing you to support cross
origin resource sharing (CORS) using a simple decorator.

:copyright: (c) 2016 by Cory Dolphin.
:license: MIT, see LICENSE for more details.
"""

from logging import Logger

from .decorator import cross_origin as cross_origin
from .extension import CORS as CORS
from .version import __version__ as __version__

rootlogger: Logger
