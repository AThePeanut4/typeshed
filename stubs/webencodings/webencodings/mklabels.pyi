"""
webencodings.mklabels
~~~~~~~~~~~~~~~~~~~~~

Regenarate the webencodings.labels module.

:copyright: Copyright 2012 by Simon Sapin
:license: BSD, see LICENSE for details.
"""

from typing import AnyStr
from urllib.request import Request

def assert_lower(string: AnyStr) -> AnyStr: ...
def generate(url: str | Request) -> str: ...
