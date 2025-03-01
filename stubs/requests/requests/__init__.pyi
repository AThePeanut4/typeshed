"""
Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
"""

from . import __version__ as version_mod, packages as packages, utils as utils
from .api import (
    delete as delete,
    get as get,
    head as head,
    options as options,
    patch as patch,
    post as post,
    put as put,
    request as request,
)
from .exceptions import (
    ConnectionError as ConnectionError,
    ConnectTimeout as ConnectTimeout,
    FileModeWarning as FileModeWarning,
    HTTPError as HTTPError,
    JSONDecodeError as JSONDecodeError,
    ReadTimeout as ReadTimeout,
    RequestException as RequestException,
    Timeout as Timeout,
    TooManyRedirects as TooManyRedirects,
    URLRequired as URLRequired,
)
from .models import PreparedRequest as PreparedRequest, Request as Request, Response as Response
from .sessions import Session as Session, session as session
from .status_codes import codes as codes

__author__ = version_mod.__author__
__author_email__ = version_mod.__author_email__
__build__ = version_mod.__build__
__cake__ = version_mod.__cake__
__copyright__ = version_mod.__copyright__
__description__ = version_mod.__description__
__license__ = version_mod.__license__
__title__ = version_mod.__title__
__url__ = version_mod.__url__
__version__ = version_mod.__version__

def check_compatibility(urllib3_version: str, chardet_version: str | None, charset_normalizer_version: str | None) -> None: ...
