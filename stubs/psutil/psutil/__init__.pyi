"""
psutil is a cross-platform library for retrieving information on
running processes and system utilization (CPU, memory, disks, network,
sensors) in Python. Supported platforms:

 - Linux
 - Windows
 - macOS
 - FreeBSD
 - OpenBSD
 - NetBSD
 - Sun Solaris
 - AIX

Supported Python versions are cPython 3.6+ and PyPy.
"""

import sys
from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Iterator
from contextlib import AbstractContextManager
from types import TracebackType
from typing import Any, Literal, Protocol, overload, type_check_only
from typing_extensions import Self, TypeAlias, deprecated

from psutil._common import (
    AIX as AIX,
    BSD as BSD,
    CONN_CLOSE as CONN_CLOSE,
    CONN_CLOSE_WAIT as CONN_CLOSE_WAIT,
    CONN_CLOSING as CONN_CLOSING,
    CONN_ESTABLISHED as CONN_ESTABLISHED,
    CONN_FIN_WAIT1 as CONN_FIN_WAIT1,
    CONN_FIN_WAIT2 as CONN_FIN_WAIT2,
    CONN_LAST_ACK as CONN_LAST_ACK,
    CONN_LISTEN as CONN_LISTEN,
    CONN_NONE as CONN_NONE,
    CONN_SYN_RECV as CONN_SYN_RECV,
    CONN_SYN_SENT as CONN_SYN_SENT,
    CONN_TIME_WAIT as CONN_TIME_WAIT,
    FREEBSD as FREEBSD,
    LINUX as LINUX,
    MACOS as MACOS,
    NETBSD as NETBSD,
    NIC_DUPLEX_FULL as NIC_DUPLEX_FULL,
    NIC_DUPLEX_HALF as NIC_DUPLEX_HALF,
    NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN,
    OPENBSD as OPENBSD,
    OSX as OSX,
    POSIX as POSIX,
    POWER_TIME_UNKNOWN as POWER_TIME_UNKNOWN,
    POWER_TIME_UNLIMITED as POWER_TIME_UNLIMITED,
    STATUS_DEAD as STATUS_DEAD,
    STATUS_DISK_SLEEP as STATUS_DISK_SLEEP,
    STATUS_IDLE as STATUS_IDLE,
    STATUS_LOCKED as STATUS_LOCKED,
    STATUS_PARKED as STATUS_PARKED,
    STATUS_RUNNING as STATUS_RUNNING,
    STATUS_SLEEPING as STATUS_SLEEPING,
    STATUS_STOPPED as STATUS_STOPPED,
    STATUS_TRACING_STOP as STATUS_TRACING_STOP,
    STATUS_WAITING as STATUS_WAITING,
    STATUS_WAKING as STATUS_WAKING,
    STATUS_ZOMBIE as STATUS_ZOMBIE,
    SUNOS as SUNOS,
    WINDOWS as WINDOWS,
    AccessDenied as AccessDenied,
    Error as Error,
    NoSuchProcess as NoSuchProcess,
    TimeoutExpired as TimeoutExpired,
    ZombieProcess as ZombieProcess,
)

from . import _ntuples as _ntp

if sys.platform == "linux":
    from ._pslinux import (
        IOPRIO_CLASS_BE as IOPRIO_CLASS_BE,
        IOPRIO_CLASS_IDLE as IOPRIO_CLASS_IDLE,
        IOPRIO_CLASS_NONE as IOPRIO_CLASS_NONE,
        IOPRIO_CLASS_RT as IOPRIO_CLASS_RT,
    )
    def sensors_temperatures(fahrenheit: bool = False) -> dict[str, list[_ntp.shwtemp]]: ...
    def sensors_fans() -> dict[str, list[_ntp.sfan]]: ...
    PROCFS_PATH: str
    RLIMIT_AS: int
    RLIMIT_CORE: int
    RLIMIT_CPU: int
    RLIMIT_DATA: int
    RLIMIT_FSIZE: int
    RLIMIT_LOCKS: int
    RLIMIT_MEMLOCK: int
    RLIMIT_MSGQUEUE: int
    RLIMIT_NICE: int
    RLIMIT_NOFILE: int
    RLIMIT_NPROC: int
    RLIMIT_RSS: int
    RLIMIT_RTPRIO: int
    RLIMIT_RTTIME: int
    RLIMIT_SIGPENDING: int
    RLIMIT_STACK: int
    RLIM_INFINITY: int
if sys.platform == "win32":
    from ._psutil_windows import (
        ABOVE_NORMAL_PRIORITY_CLASS as ABOVE_NORMAL_PRIORITY_CLASS,
        BELOW_NORMAL_PRIORITY_CLASS as BELOW_NORMAL_PRIORITY_CLASS,
        HIGH_PRIORITY_CLASS as HIGH_PRIORITY_CLASS,
        IDLE_PRIORITY_CLASS as IDLE_PRIORITY_CLASS,
        NORMAL_PRIORITY_CLASS as NORMAL_PRIORITY_CLASS,
        REALTIME_PRIORITY_CLASS as REALTIME_PRIORITY_CLASS,
    )
    from ._pswindows import (
        CONN_DELETE_TCB as CONN_DELETE_TCB,
        IOPRIO_HIGH as IOPRIO_HIGH,
        IOPRIO_LOW as IOPRIO_LOW,
        IOPRIO_NORMAL as IOPRIO_NORMAL,
        IOPRIO_VERYLOW as IOPRIO_VERYLOW,
        win_service_get as win_service_get,
        win_service_iter as win_service_iter,
    )

# Linux + glibc, Windows, macOS, FreeBSD, NetBSD:
def heap_info() -> _ntp.pheap: ...
def heap_trim() -> None: ...

if sys.platform == "linux":
    from ._pslinux import sensors_battery as sensors_battery
elif sys.platform == "darwin":
    from ._psosx import sensors_battery as sensors_battery
elif sys.platform == "win32":
    from ._pswindows import sensors_battery as sensors_battery
else:
    def sensors_battery(): ...

AF_LINK: int
version_info: tuple[int, int, int]
__version__: str
__author__: str

_Status: TypeAlias = Literal[
    "running",
    "sleeping",
    "disk-sleep",
    "stopped",
    "tracing-stop",
    "zombie",
    "dead",
    "wake-kill",
    "waking",
    "idle",
    "locked",
    "waiting",
    "suspended",
    "parked",
]

class Process:
    """
    Represents an OS process with the given PID.
    If PID is omitted current process PID (os.getpid()) is used.
    Raise NoSuchProcess if PID does not exist.

    Note that most of the methods of this class do not make sure that
    the PID of the process being queried has been reused. That means
    that you may end up retrieving information for another process.

    The only exceptions for which process identity is pre-emptively
    checked and guaranteed are:

     - parent()
     - children()
     - nice() (set)
     - ionice() (set)
     - rlimit() (set)
     - cpu_affinity (set)
     - suspend()
     - resume()
     - send_signal()
     - terminate()
     - kill()

    To prevent this problem for all other methods you can use
    is_running() before querying the process.
    """
    def __init__(self, pid: int | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def pid(self) -> int:
        """The process PID."""
        ...
    # Only present if attrs argument is passed to process_iter
    info: dict[str, Incomplete]
    def oneshot(self) -> AbstractContextManager[None]:
        """
        Utility context manager which considerably speeds up the
        retrieval of multiple process information at the same time.

        Internally different process info (e.g. name, ppid, uids,
        gids, ...) may be fetched by using the same routine, but
        only one information is returned and the others are discarded.
        When using this context manager the internal routine is
        executed once (in the example below on name()) and the
        other info are cached.

        The cache is cleared when exiting the context manager block.
        The advice is to use this every time you retrieve more than
        one information about the process. If you're lucky, you'll
        get a hell of a speedup.

        >>> import psutil
        >>> p = psutil.Process()
        >>> with p.oneshot():
        ...     p.name()  # collect multiple info
        ...     p.cpu_times()  # return cached value
        ...     p.cpu_percent()  # return cached value
        ...     p.create_time()  # return cached value
        ...
        >>>
        """
        ...
    def as_dict(
        self, attrs: list[str] | tuple[str, ...] | set[str] | frozenset[str] | None = None, ad_value=None
    ) -> dict[str, Incomplete]:
        """
        Utility method returning process information as a
        hashable dictionary.
        If *attrs* is specified it must be a list of strings
        reflecting available Process class' attribute names
        (e.g. ['cpu_times', 'name']) else all public (read
        only) attributes are assumed.
        *ad_value* is the value which gets assigned in case
        AccessDenied or ZombieProcess exception is raised when
        retrieving that particular process information.
        """
        ...
    def parent(self) -> Process | None:
        """
        Return the parent process as a Process object pre-emptively
        checking whether PID has been reused.
        If no parent is known return None.
        """
        ...
    def parents(self) -> list[Process]:
        """
        Return the parents of this process as a list of Process
        instances. If no parents are known return an empty list.
        """
        ...
    def is_running(self) -> bool:
        """
        Return whether this process is running.

        It also checks if PID has been reused by another process, in
        which case it will remove the process from `process_iter()`
        internal cache and return False.
        """
        ...
    def ppid(self) -> int:
        """
        The process parent PID.
        On Windows the return value is cached after first call.
        """
        ...
    def name(self) -> str:
        """The process name. The return value is cached after first call."""
        ...
    def exe(self) -> str:
        """
        The process executable as an absolute path.
        May also be an empty string.
        The return value is cached after first call.
        """
        ...
    def cmdline(self) -> list[str]:
        """The command line this process has been called with."""
        ...
    def status(self) -> _Status:
        """The process current status as a STATUS_* constant."""
        ...
    def username(self) -> str:
        """
        The name of the user that owns the process.
        On UNIX this is calculated by using *real* process uid.
        """
        ...
    def create_time(self) -> float:
        """
        The process creation time as a floating point number
        expressed in seconds since the epoch (seconds since January 1,
        1970, at midnight UTC). The return value, which is cached after
        first call, is based on the system clock, which means it may be
        affected by changes such as manual adjustments or time
        synchronization (e.g. NTP).
        """
        ...
    def cwd(self) -> str:
        """Process current working directory as an absolute path."""
        ...
    def nice(self, value: int | None = None) -> int:
        """Get or set process niceness (priority)."""
        ...
    if sys.platform != "win32":
        def uids(self) -> _ntp.puids: ...
        def gids(self) -> _ntp.pgids: ...
        def terminal(self) -> str: ...
        def num_fds(self) -> int: ...
    if sys.platform != "darwin":
        def io_counters(self) -> _ntp.pio: ...
        def ionice(self, ioclass: int | None = None, value: int | None = None) -> _ntp.pionice: ...
        @overload
        def cpu_affinity(self, cpus: None = None) -> list[int]:
            """
            Get or set process CPU affinity.
            If specified, *cpus* must be a list of CPUs for which you
            want to set the affinity (e.g. [0, 1]).
            If an empty list is passed, all egible CPUs are assumed
            (and set).
            (Windows, Linux and BSD only).
            """
            ...
        @overload
        def cpu_affinity(self, cpus: list[int]) -> None:
            """
            Get or set process CPU affinity.
            If specified, *cpus* must be a list of CPUs for which you
            want to set the affinity (e.g. [0, 1]).
            If an empty list is passed, all egible CPUs are assumed
            (and set).
            (Windows, Linux and BSD only).
            """
            ...
        def memory_maps(self, grouped: bool = True) -> list[Incomplete]:
            """
            Return process' mapped memory regions as a list of namedtuples
            whose fields are variable depending on the platform.

            If *grouped* is True the mapped regions with the same 'path'
            are grouped together and the different memory fields are summed.

            If *grouped* is False every mapped region is shown as a single
            entity and the namedtuple will also include the mapped region's
            address space ('addr') and permission set ('perms').
            """
            ...
    if sys.platform == "linux":
        def rlimit(self, resource: int, limits: tuple[int, int] | None = None) -> tuple[int, int]: ...
        def cpu_num(self) -> int: ...

    def environ(self) -> dict[str, str]:
        """
        The environment variables of the process as a dict.  Note: this
        might not reflect changes made after the process started.
        """
        ...
    if sys.platform == "win32":
        def num_handles(self) -> int: ...

    def num_ctx_switches(self) -> _ntp.pctxsw: ...
    def num_threads(self) -> int: ...
    def threads(self) -> list[_ntp.pthread]: ...
    def children(self, recursive: bool = False) -> list[Process]: ...
    def cpu_percent(self, interval: float | None = None) -> float: ...
    def cpu_times(self) -> _ntp.pcputimes: ...
    def memory_info(self) -> _ntp.pmem: ...
    def memory_full_info(self) -> _ntp.pfullmem: ...
    def memory_percent(self, memtype: str = "rss") -> float: ...
    def open_files(self) -> list[_ntp.popenfile]: ...
    @deprecated('use "net_connections" method instead')
    def connections(self, kind: str = "inet") -> list[_ntp.pconn]: ...
    def send_signal(self, sig: int) -> None: ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def wait(self, timeout: float | None = None) -> int: ...
    def net_connections(self, kind: str = "inet") -> list[_ntp.pconn]: ...

class Popen(Process):
    """
    Same as subprocess.Popen, but in addition it provides all
    psutil.Process methods in a single class.
    For the following methods which are common to both classes, psutil
    implementation takes precedence:

    * send_signal()
    * terminate()
    * kill()

    This is done in order to avoid killing another process in case its
    PID has been reused, fixing BPO-6973.

      >>> import psutil
      >>> from subprocess import PIPE
      >>> p = psutil.Popen(["python", "-c", "print 'hi'"], stdout=PIPE)
      >>> p.name()
      'python'
      >>> p.uids()
      user(real=1000, effective=1000, saved=1000)
      >>> p.username()
      'giampaolo'
      >>> p.communicate()
      ('hi', None)
      >>> p.terminate()
      >>> p.wait(timeout=2)
      0
      >>>
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __getattribute__(self, name: str) -> Any: ...
    def __dir__(self) -> list[str]: ...

@type_check_only
class _ProcessIterCallable(Protocol):
    def __call__(
        self, attrs: list[str] | tuple[str, ...] | set[str] | frozenset[str] | None = None, ad_value=None
    ) -> Iterator[Process]: ...
    def cache_clear(self) -> None: ...

def pids() -> list[int]:
    """Return a list of current running PIDs."""
    ...
def pid_exists(pid: int) -> bool:
    """
    Return True if given PID exists in the current process list.
    This is faster than doing "pid in psutil.pids()" and
    should be preferred.
    """
    ...

process_iter: _ProcessIterCallable

def wait_procs(
    procs: Iterable[Process], timeout: float | None = None, callback: Callable[[Process], object] | None = None
) -> tuple[list[Process], list[Process]]:
    """
    Convenience function which waits for a list of processes to
    terminate.

    Return a (gone, alive) tuple indicating which processes
    are gone and which ones are still alive.

    The gone ones will have a new *returncode* attribute indicating
    process exit status (may be None).

    *callback* is a function which gets called every time a process
    terminates (a Process instance is passed as callback argument).

    Function will return as soon as all processes terminate or when
    *timeout* occurs.
    Differently from Process.wait() it will not raise TimeoutExpired if
    *timeout* occurs.

    Typical use case is:

     - send SIGTERM to a list of processes
     - give them some time to terminate
     - send SIGKILL to those ones which are still alive

    Example:

    >>> def on_terminate(proc):
    ...     print("process {} terminated".format(proc))
    ...
    >>> for p in procs:
    ...    p.terminate()
    ...
    >>> gone, alive = wait_procs(procs, timeout=3, callback=on_terminate)
    >>> for p in alive:
    ...     p.kill()
    """
    ...
def cpu_count(logical: bool = True) -> int | None:
    """
    Return the number of logical CPUs in the system (same as
    os.cpu_count()).

    If *logical* is False return the number of physical cores only
    (e.g. hyper thread CPUs are excluded).

    Return None if undetermined.

    The return value is cached after first call.
    If desired cache can be cleared like this:

    >>> psutil.cpu_count.cache_clear()
    """
    ...
@overload
def cpu_freq(percpu: Literal[False] = False) -> _ntp.scpufreq: ...
@overload
def cpu_freq(percpu: Literal[True]) -> list[_ntp.scpufreq]: ...
@overload
def cpu_times(percpu: Literal[False] = False) -> _ntp.scputimes: ...
@overload
def cpu_times(percpu: Literal[True]) -> list[_ntp.scputimes]: ...
@overload
def cpu_percent(interval: float | None = None, percpu: Literal[False] = False) -> float:
    """
    Return a float representing the current system-wide CPU
    utilization as a percentage.

    When *interval* is > 0.0 compares system CPU times elapsed before
    and after the interval (blocking).

    When *interval* is 0.0 or None compares system CPU times elapsed
    since last call or module import, returning immediately (non
    blocking). That means the first time this is called it will
    return a meaningless 0.0 value which you should ignore.
    In this case is recommended for accuracy that this function be
    called with at least 0.1 seconds between calls.

    When *percpu* is True returns a list of floats representing the
    utilization as a percentage for each CPU.
    First element of the list refers to first CPU, second element
    to second CPU and so on.
    The order of the list is consistent across calls.

    Examples:

      >>> # blocking, system-wide
      >>> psutil.cpu_percent(interval=1)
      2.0
      >>>
      >>> # blocking, per-cpu
      >>> psutil.cpu_percent(interval=1, percpu=True)
      [2.0, 1.0]
      >>>
      >>> # non-blocking (percentage since last call)
      >>> psutil.cpu_percent(interval=None)
      2.9
      >>>
    """
    ...
@overload
def cpu_percent(interval: float | None, percpu: Literal[True]) -> list[float]:
    """
    Return a float representing the current system-wide CPU
    utilization as a percentage.

    When *interval* is > 0.0 compares system CPU times elapsed before
    and after the interval (blocking).

    When *interval* is 0.0 or None compares system CPU times elapsed
    since last call or module import, returning immediately (non
    blocking). That means the first time this is called it will
    return a meaningless 0.0 value which you should ignore.
    In this case is recommended for accuracy that this function be
    called with at least 0.1 seconds between calls.

    When *percpu* is True returns a list of floats representing the
    utilization as a percentage for each CPU.
    First element of the list refers to first CPU, second element
    to second CPU and so on.
    The order of the list is consistent across calls.

    Examples:

      >>> # blocking, system-wide
      >>> psutil.cpu_percent(interval=1)
      2.0
      >>>
      >>> # blocking, per-cpu
      >>> psutil.cpu_percent(interval=1, percpu=True)
      [2.0, 1.0]
      >>>
      >>> # non-blocking (percentage since last call)
      >>> psutil.cpu_percent(interval=None)
      2.9
      >>>
    """
    ...
@overload
def cpu_percent(*, percpu: Literal[True]) -> list[float]:
    """
    Return a float representing the current system-wide CPU
    utilization as a percentage.

    When *interval* is > 0.0 compares system CPU times elapsed before
    and after the interval (blocking).

    When *interval* is 0.0 or None compares system CPU times elapsed
    since last call or module import, returning immediately (non
    blocking). That means the first time this is called it will
    return a meaningless 0.0 value which you should ignore.
    In this case is recommended for accuracy that this function be
    called with at least 0.1 seconds between calls.

    When *percpu* is True returns a list of floats representing the
    utilization as a percentage for each CPU.
    First element of the list refers to first CPU, second element
    to second CPU and so on.
    The order of the list is consistent across calls.

    Examples:

      >>> # blocking, system-wide
      >>> psutil.cpu_percent(interval=1)
      2.0
      >>>
      >>> # blocking, per-cpu
      >>> psutil.cpu_percent(interval=1, percpu=True)
      [2.0, 1.0]
      >>>
      >>> # non-blocking (percentage since last call)
      >>> psutil.cpu_percent(interval=None)
      2.9
      >>>
    """
    ...
@overload
def cpu_times_percent(interval: float | None = None, percpu: Literal[False] = False) -> _ntp.scputimes: ...
@overload
def cpu_times_percent(interval: float | None, percpu: Literal[True]) -> list[_ntp.scputimes]: ...
@overload
def cpu_times_percent(*, percpu: Literal[True]) -> list[_ntp.scputimes]: ...
def cpu_stats() -> _ntp.scpustats: ...
def getloadavg() -> tuple[float, float, float]: ...
def virtual_memory() -> _ntp.svmem: ...
def swap_memory() -> _ntp.sswap: ...
def disk_usage(path: str) -> _ntp.sdiskusage: ...
def disk_partitions(all: bool = False) -> list[_ntp.sdiskpart]: ...

# TODO: Incorrect sdiskio for BSD systems:
@overload
def disk_io_counters(perdisk: Literal[False] = False, nowrap: bool = True) -> _ntp.sdiskio | None: ...
@overload
def disk_io_counters(perdisk: Literal[True], nowrap: bool = True) -> dict[str, _ntp.sdiskio]: ...
@overload
def net_io_counters(pernic: Literal[False] = False, nowrap: bool = True) -> _ntp.snetio: ...
@overload
def net_io_counters(pernic: Literal[True], nowrap: bool = True) -> dict[str, _ntp.snetio]: ...
def net_connections(kind: str = "inet") -> list[_ntp.sconn]: ...
def net_if_addrs() -> dict[str, list[_ntp.snicaddr]]: ...
def net_if_stats() -> dict[str, _ntp.snicstats]: ...
def boot_time() -> float: ...
def users() -> list[_ntp.suser]: ...
