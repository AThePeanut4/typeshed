"""
As a programming ecosystem grows, so do the chances of runtime
variability.

Python boasts one of the widest deployments for a high-level
programming environment, making it a viable target for all manner of
application. But with breadth comes variance, so it's important to
know what you're working with.

Some basic variations that are common among development machines:

* **Executable runtime**: CPython, PyPy, Jython, etc., plus build date and compiler
* **Language version**: 2.7 through 3.12
* **Host operating system**: Windows, OS X, Ubuntu, Debian, CentOS, RHEL, etc.
* **Features**: 64-bit, IPv6, Unicode character support (UCS-2/UCS-4)
* **Built-in library support**: OpenSSL, threading, SQLite, zlib
* **User environment**: umask, ulimit, working directory path
* **Machine info**: CPU count, hostname, filesystem encoding

See the full example profile below for more.

ecoutils was created to quantify that variability. ecoutils quickly
produces an information-dense description of critical runtime factors,
with minimal side effects. In short, ecoutils is like browser and user
agent analytics, but for Python environments.

Transmission and collection
---------------------------

The data is all JSON serializable, and is suitable for sending to a
central analytics server. An HTTP-backed service for this can be found
at: https://github.com/mahmoud/espymetrics/

Notable omissions
-----------------

Due to space constraints (and possibly latency constraints), the
following information is deemed not dense enough, and thus omitted:

* :data:`sys.path`
* full :mod:`sysconfig`
* environment variables (:data:`os.environ`)

Compatibility
-------------

So far ecoutils has has been tested on Python 3.7+ and PyPy3. 
Various versions have been tested on Ubuntu, Debian,
RHEL, OS X, FreeBSD, and Windows 7.

.. note:: 

   ``boltons.ecoutils`` historically supported back to Python 2.4, but in 2024, 
    due to increasing testing burden, ecoutils support tracks the same 
    versions of Python as the rest of the boltons package. 
    For older Pythons, see `this version`_ from boltons 23.0.0.

.. _this version: https://github.com/mahmoud/boltons/blob/4b1d728f31a8378b193be9c966c853be0a57527d/boltons/ecoutils.py

Profile generation
------------------

Profiles are generated by :func:`ecoutils.get_profile`.

When run as a module, ecoutils will call :func:`~ecoutils.get_profile`
and print a profile in JSON format::

    $ python -m boltons.ecoutils
    {
      "_eco_version": "1.0.0",
      "cpu_count": 4,
      "cwd": "/home/mahmoud/projects/boltons",
      "fs_encoding": "UTF-8",
      "guid": "6b139e7bbf5ad4ed8d4063bf6235b4d2",
      "hostfqdn": "mahmoud-host",
      "hostname": "mahmoud-host",
      "linux_dist_name": "Ubuntu",
      "linux_dist_version": "14.04",
      "python": {
        "argv": "boltons/ecoutils.py",
        "bin": "/usr/bin/python",
        "build_date": "Jun 22 2015 17:58:13",
        "compiler": "GCC 4.8.2",
        "features": {
          "64bit": true,
          "expat": "expat_2.1.0",
          "ipv6": true,
          "openssl": "OpenSSL 1.0.1f 6 Jan 2014",
          "readline": true,
          "sqlite": "3.8.2",
          "threading": true,
          "tkinter": "8.6",
          "unicode_wide": true,
          "zlib": "1.2.8"
        },
        "version": "2.7.6 (default, Jun 22 2015, 17:58:13) [GCC 4.8.2]",
        "version_info": [
          2,
          7,
          6,
          "final",
          0
        ]
      },
      "time_utc": "2016-05-24 07:59:40.473140",
      "time_utc_offset": -8.0,
      "ulimit_hard": 4096,
      "ulimit_soft": 1024,
      "umask": "002",
      "uname": {
        "machine": "x86_64",
        "node": "mahmoud-host",
        "processor": "x86_64",
        "release": "3.13.0-85-generic",
        "system": "Linux",
        "version": "#129-Ubuntu SMP Thu Mar 17 20:50:15 UTC 2016"
      },
      "username": "mahmoud"
    }

``pip install boltons`` and try it yourself!
"""

from typing import Any

ECO_VERSION: str
HAVE_URANDOM: bool
INSTANCE_ID: str
IS_64BIT: bool
HAVE_UCS4: bool
HAVE_READLINE: bool
SQLITE_VERSION: str
OPENSSL_VERSION: str
TKINTER_VERSION: str
ZLIB_VERSION: str
EXPAT_VERSION: str
CPU_COUNT: int
HAVE_THREADING: bool
HAVE_IPV6: bool
RLIMIT_FDS_SOFT: int
RLIMIT_FDS_HARD: int
START_TIME_INFO: dict[str, str | float]

def getrandbits(k: int) -> int:
    """getrandbits(k) -> x.  Generates an int with k random bits."""
    ...
def get_python_info() -> dict[str, Any]: ...
def get_profile(**kwargs) -> dict[str, Any]:
    """
    The main entrypoint to ecoutils. Calling this will return a
    JSON-serializable dictionary of information about the current
    process.

    It is very unlikely that the information returned will change
    during the lifetime of the process, and in most cases the majority
    of the information stays the same between runs as well.

    :func:`get_profile` takes one optional keyword argument, *scrub*,
    a :class:`bool` that, if True, blanks out identifiable
    information. This includes current working directory, hostname,
    Python executable path, command-line arguments, and
    username. Values are replaced with '-', but for compatibility keys
    remain in place.
    """
    ...
def get_profile_json(indent: bool = False) -> str: ...
def main() -> None: ...
def dumps(val: Any, indent: int) -> str: ...
