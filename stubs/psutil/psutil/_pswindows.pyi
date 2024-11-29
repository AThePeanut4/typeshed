"""Windows platform implementation."""

import enum
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any, NamedTuple

from psutil import _psutil_windows
from psutil._common import (
    ENCODING as ENCODING,
    ENCODING_ERRS as ENCODING_ERRS,
    AccessDenied as AccessDenied,
    NoSuchProcess as NoSuchProcess,
    TimeoutExpired as TimeoutExpired,
    conn_tmap as conn_tmap,
    conn_to_ntuple as conn_to_ntuple,
    debug as debug,
    isfile_strict as isfile_strict,
    memoize as memoize,
    parse_environ_block as parse_environ_block,
    usage_percent as usage_percent,
)
from psutil._compat import PY3 as PY3
from psutil._psutil_windows import (
    ABOVE_NORMAL_PRIORITY_CLASS as ABOVE_NORMAL_PRIORITY_CLASS,
    BELOW_NORMAL_PRIORITY_CLASS as BELOW_NORMAL_PRIORITY_CLASS,
    HIGH_PRIORITY_CLASS as HIGH_PRIORITY_CLASS,
    IDLE_PRIORITY_CLASS as IDLE_PRIORITY_CLASS,
    NORMAL_PRIORITY_CLASS as NORMAL_PRIORITY_CLASS,
    REALTIME_PRIORITY_CLASS as REALTIME_PRIORITY_CLASS,
)

__extra__all__: Any
CONN_DELETE_TCB: str
ERROR_PARTIAL_COPY: int
PYPY: Any
AF_LINK: int
AddressFamily: Any
TCP_STATUSES: Any

# These noqas workaround https://github.com/astral-sh/ruff/issues/10874
class Priority(enum.IntEnum):
    """An enumeration."""
    ABOVE_NORMAL_PRIORITY_CLASS = _psutil_windows.ABOVE_NORMAL_PRIORITY_CLASS  # noqa: F811
    BELOW_NORMAL_PRIORITY_CLASS = _psutil_windows.BELOW_NORMAL_PRIORITY_CLASS  # noqa: F811
    HIGH_PRIORITY_CLASS = _psutil_windows.HIGH_PRIORITY_CLASS  # noqa: F811
    IDLE_PRIORITY_CLASS = _psutil_windows.IDLE_PRIORITY_CLASS  # noqa: F811
    NORMAL_PRIORITY_CLASS = _psutil_windows.NORMAL_PRIORITY_CLASS  # noqa: F811
    REALTIME_PRIORITY_CLASS = _psutil_windows.REALTIME_PRIORITY_CLASS  # noqa: F811

IOPRIO_VERYLOW: int
IOPRIO_LOW: int
IOPRIO_NORMAL: int
IOPRIO_HIGH: int

class IOPriority(enum.IntEnum):
    """An enumeration."""
    IOPRIO_VERYLOW = 0
    IOPRIO_LOW = 1
    IOPRIO_NORMAL = 2
    IOPRIO_HIGH = 3

pinfo_map: Any

class scputimes(NamedTuple):
    """scputimes(user, system, idle, interrupt, dpc)"""
    user: float
    system: float
    idle: float
    interrupt: float
    dpc: float

class svmem(NamedTuple):
    """svmem(total, available, percent, used, free)"""
    total: int
    available: int
    percent: float
    used: int
    free: int

class pmem(NamedTuple):
    """pmem(rss, vms, num_page_faults, peak_wset, wset, peak_paged_pool, paged_pool, peak_nonpaged_pool, nonpaged_pool, pagefile, peak_pagefile, private)"""
    rss: Any
    vms: Any
    num_page_faults: Any
    peak_wset: Any
    wset: Any
    peak_paged_pool: Any
    paged_pool: Any
    peak_nonpaged_pool: Any
    nonpaged_pool: Any
    pagefile: Any
    peak_pagefile: Any
    private: Any

class pfullmem(NamedTuple):
    """pfullmem(rss, vms, num_page_faults, peak_wset, wset, peak_paged_pool, paged_pool, peak_nonpaged_pool, nonpaged_pool, pagefile, peak_pagefile, private, uss)"""
    rss: Incomplete
    vms: Incomplete
    num_page_faults: Incomplete
    peak_wset: Incomplete
    wset: Incomplete
    peak_paged_pool: Incomplete
    paged_pool: Incomplete
    peak_nonpaged_pool: Incomplete
    nonpaged_pool: Incomplete
    pagefile: Incomplete
    peak_pagefile: Incomplete
    private: Incomplete
    uss: Incomplete

class pmmap_grouped(NamedTuple):
    """pmmap_grouped(path, rss)"""
    path: Any
    rss: Any

pmmap_ext: Any

class pio(NamedTuple):
    """pio(read_count, write_count, read_bytes, write_bytes, other_count, other_bytes)"""
    read_count: Any
    write_count: Any
    read_bytes: Any
    write_bytes: Any
    other_count: Any
    other_bytes: Any

def convert_dos_path(s):
    r"""
    Convert paths using native DOS format like:
        "\Device\HarddiskVolume1\Windows\systemew\file.txt"
    into:
        "C:\Windows\systemew\file.txt".
    """
    ...
def py2_strencode(s):
    """
    Encode a unicode string to a byte string by using the default fs
    encoding + "replace" error handler.
    """
    ...
def getpagesize(): ...
def virtual_memory() -> svmem:
    """System virtual memory as a namedtuple."""
    ...
def swap_memory():
    """Swap system memory as a (total, used, free, sin, sout) tuple."""
    ...

disk_io_counters: Any

def disk_usage(path):
    """Return disk usage associated with path."""
    ...
def disk_partitions(all):
    """Return disk partitions."""
    ...
def cpu_times():
    """Return system CPU times as a named tuple."""
    ...
def per_cpu_times():
    """Return system per-CPU times as a list of named tuples."""
    ...
def cpu_count_logical():
    """Return the number of logical CPUs in the system."""
    ...
def cpu_count_cores() -> int | None:
    """Return the number of CPU cores in the system."""
    ...
def cpu_stats():
    """Return CPU statistics."""
    ...
def cpu_freq():
    """
    Return CPU frequency.
    On Windows per-cpu frequency is not supported.
    """
    ...
def getloadavg():
    """
    Return the number of processes in the system run queue averaged
    over the last 1, 5, and 15 minutes respectively as a tuple.
    """
    ...
def net_connections(kind, _pid: int = -1):
    """
    Return socket connections.  If pid == -1 return system-wide
    connections (as opposed to connections opened by one process only).
    """
    ...
def net_if_stats():
    """Get NIC stats (isup, duplex, speed, mtu)."""
    ...
def net_io_counters():
    """
    Return network I/O statistics for every network interface
    installed on the system as a dict of raw tuples.
    """
    ...
def net_if_addrs():
    """Return the addresses associated to each NIC."""
    ...
def sensors_battery():
    """Return battery information."""
    ...
def boot_time():
    """The system boot time expressed in seconds since the epoch."""
    ...
def users():
    """Return currently connected users as a list of namedtuples."""
    ...
def win_service_iter() -> Iterable[WindowsService]:
    """Yields a list of WindowsService instances."""
    ...
def win_service_get(name):
    """Open a Windows service and return it as a WindowsService instance."""
    ...

class WindowsService:
    """Represents an installed Windows service."""
    def __init__(self, name, display_name) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def name(self):
        """
        The service name. This string is how a service is referenced
        and can be passed to win_service_get() to get a new
        WindowsService instance.
        """
        ...
    def display_name(self):
        """
        The service display name. The value is cached when this class
        is instantiated.
        """
        ...
    def binpath(self):
        """
        The fully qualified path to the service binary/exe file as
        a string, including command line arguments.
        """
        ...
    def username(self):
        """The name of the user that owns this service."""
        ...
    def start_type(self):
        """
        A string which can either be "automatic", "manual" or
        "disabled".
        """
        ...
    def pid(self):
        """
        The process PID, if any, else None. This can be passed
        to Process class to control the service's process.
        """
        ...
    def status(self):
        """Service status as a string."""
        ...
    def description(self):
        """Service long description."""
        ...
    def as_dict(self):
        """
        Utility method retrieving all the information above as a
        dictionary.
        """
        ...

pids: Any
pid_exists: Any
ppid_map: Any

def is_permission_err(exc):
    """Return True if this is a permission error."""
    ...
def convert_oserror(exc, pid: Incomplete | None = None, name: Incomplete | None = None):
    """Convert OSError into NoSuchProcess or AccessDenied."""
    ...
def wrap_exceptions(fun):
    """Decorator which converts OSError into NoSuchProcess or AccessDenied."""
    ...
def retry_error_partial_copy(fun):
    """
    Workaround for https://github.com/giampaolo/psutil/issues/875.
    See: https://stackoverflow.com/questions/4457745#4457745.
    """
    ...

class Process:
    """Wrapper class around underlying C implementation."""
    pid: Any
    def __init__(self, pid) -> None: ...
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self):
        """
        Return process name, which on Windows is always the final
        part of the executable.
        """
        ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def ppid(self): ...
    def memory_info(self): ...
    def memory_full_info(self): ...
    def memory_maps(self) -> None: ...
    def kill(self): ...
    def send_signal(self, sig) -> None: ...
    def wait(self, timeout: Incomplete | None = None): ...
    def username(self): ...
    def create_time(self, fast_only: bool = False): ...
    def num_threads(self): ...
    def threads(self): ...
    def cpu_times(self): ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def cwd(self): ...
    def open_files(self): ...
    def net_connections(self, kind: str = "inet"): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def ionice_get(self): ...
    def ionice_set(self, ioclass, value) -> None: ...
    def io_counters(self) -> pio: ...
    def status(self): ...
    def cpu_affinity_get(self): ...
    def cpu_affinity_set(self, value): ...
    def num_handles(self): ...
    def num_ctx_switches(self): ...
