"""
Common objects shared by __init__.py and _ps*.py modules.

Note: this module is imported by setup.py, so it should not import
psutil or third-party modules.
"""

import enum
import io
import threading
from _typeshed import ConvertibleToFloat, FileDescriptorOrPath, Incomplete, StrOrBytesPath, SupportsWrite
from collections.abc import Callable
from socket import AF_INET6 as AF_INET6, AddressFamily, SocketKind
from typing import BinaryIO, Final, NamedTuple, SupportsIndex, TypeVar, overload
from typing_extensions import ParamSpec

POSIX: Final[bool]
WINDOWS: Final[bool]
LINUX: Final[bool]
MACOS: Final[bool]
OSX: Final[bool]
FREEBSD: Final[bool]
OPENBSD: Final[bool]
NETBSD: Final[bool]
BSD: Final[bool]
SUNOS: Final[bool]
AIX: Final[bool]

STATUS_RUNNING: Final = "running"
STATUS_SLEEPING: Final = "sleeping"
STATUS_DISK_SLEEP: Final = "disk-sleep"
STATUS_STOPPED: Final = "stopped"
STATUS_TRACING_STOP: Final = "tracing-stop"
STATUS_ZOMBIE: Final = "zombie"
STATUS_DEAD: Final = "dead"
STATUS_WAKE_KILL: Final = "wake-kill"
STATUS_WAKING: Final = "waking"
STATUS_IDLE: Final = "idle"
STATUS_LOCKED: Final = "locked"
STATUS_WAITING: Final = "waiting"
STATUS_SUSPENDED: Final = "suspended"
STATUS_PARKED: Final = "parked"

CONN_ESTABLISHED: Final = "ESTABLISHED"
CONN_SYN_SENT: Final = "SYN_SENT"
CONN_SYN_RECV: Final = "SYN_RECV"
CONN_FIN_WAIT1: Final = "FIN_WAIT1"
CONN_FIN_WAIT2: Final = "FIN_WAIT2"
CONN_TIME_WAIT: Final = "TIME_WAIT"
CONN_CLOSE: Final = "CLOSE"
CONN_CLOSE_WAIT: Final = "CLOSE_WAIT"
CONN_LAST_ACK: Final = "LAST_ACK"
CONN_LISTEN: Final = "LISTEN"
CONN_CLOSING: Final = "CLOSING"
CONN_NONE: Final = "NONE"

class NicDuplex(enum.IntEnum):
    """An enumeration."""
    NIC_DUPLEX_FULL = 2
    NIC_DUPLEX_HALF = 1
    NIC_DUPLEX_UNKNOWN = 0

NIC_DUPLEX_FULL: Final = NicDuplex.NIC_DUPLEX_FULL
NIC_DUPLEX_HALF: Final = NicDuplex.NIC_DUPLEX_HALF
NIC_DUPLEX_UNKNOWN: Final = NicDuplex.NIC_DUPLEX_UNKNOWN

class BatteryTime(enum.IntEnum):
    """An enumeration."""
    POWER_TIME_UNKNOWN = -1
    POWER_TIME_UNLIMITED = -2

POWER_TIME_UNKNOWN: Final = BatteryTime.POWER_TIME_UNKNOWN
POWER_TIME_UNLIMITED: Final = BatteryTime.POWER_TIME_UNLIMITED

ENCODING: Final[str]
ENCODING_ERRS: Final[str]

class sswap(NamedTuple):
    """sswap(total, used, free, percent, sin, sout)"""
    total: int
    used: int
    free: int
    percent: float
    sin: int
    sout: int

class sdiskusage(NamedTuple):
    """sdiskusage(total, used, free, percent)"""
    total: int
    used: int
    free: int
    percent: float

class sdiskio(NamedTuple):
    """sdiskio(read_count, write_count, read_bytes, write_bytes, read_time, write_time)"""
    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int
    read_time: int
    write_time: int

class sdiskpart(NamedTuple):
    """sdiskpart(device, mountpoint, fstype, opts)"""
    device: str
    mountpoint: str
    fstype: str
    opts: str

class snetio(NamedTuple):
    """snetio(bytes_sent, bytes_recv, packets_sent, packets_recv, errin, errout, dropin, dropout)"""
    bytes_sent: int
    bytes_recv: int
    packets_sent: int
    packets_recv: int
    errin: int
    errout: int
    dropin: int
    dropout: int

class suser(NamedTuple):
    """suser(name, terminal, host, started, pid)"""
    name: str
    terminal: str | None
    host: str | None
    started: float
    pid: str

class sconn(NamedTuple):
    """sconn(fd, family, type, laddr, raddr, status, pid)"""
    fd: int
    family: AddressFamily
    type: SocketKind
    laddr: addr | tuple[()]
    raddr: addr | tuple[()]
    status: str
    pid: int | None

class snicaddr(NamedTuple):
    """snicaddr(family, address, netmask, broadcast, ptp)"""
    family: AddressFamily
    address: str
    netmask: str | None
    broadcast: str | None
    ptp: str | None

class snicstats(NamedTuple):
    """snicstats(isup, duplex, speed, mtu, flags)"""
    isup: bool
    duplex: int
    speed: int
    mtu: int
    flags: str

class scpustats(NamedTuple):
    """scpustats(ctx_switches, interrupts, soft_interrupts, syscalls)"""
    ctx_switches: int
    interrupts: int
    soft_interrupts: int
    syscalls: int

class scpufreq(NamedTuple):
    """scpufreq(current, min, max)"""
    current: float
    min: float
    max: float

class shwtemp(NamedTuple):
    """shwtemp(label, current, high, critical)"""
    label: str
    current: float
    high: float | None
    critical: float | None

class sbattery(NamedTuple):
    """sbattery(percent, secsleft, power_plugged)"""
    percent: int
    secsleft: int
    power_plugged: bool

class sfan(NamedTuple):
    """sfan(label, current)"""
    label: str
    current: int

class pcputimes(NamedTuple):
    """pcputimes(user, system, children_user, children_system)"""
    user: float
    system: float
    children_user: float
    children_system: float

class popenfile(NamedTuple):
    """popenfile(path, fd)"""
    path: str
    fd: int

class pthread(NamedTuple):
    """pthread(id, user_time, system_time)"""
    id: int
    user_time: float
    system_time: float

class puids(NamedTuple):
    """puids(real, effective, saved)"""
    real: int
    effective: int
    saved: int

class pgids(NamedTuple):
    """pgids(real, effective, saved)"""
    real: int
    effective: int
    saved: int

class pio(NamedTuple):
    """pio(read_count, write_count, read_bytes, write_bytes)"""
    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int

class pionice(NamedTuple):
    """pionice(ioclass, value)"""
    ioclass: int
    value: int

class pctxsw(NamedTuple):
    """pctxsw(voluntary, involuntary)"""
    voluntary: int
    involuntary: int

class pconn(NamedTuple):
    """pconn(fd, family, type, laddr, raddr, status)"""
    fd: int
    family: AddressFamily
    type: SocketKind
    laddr: addr
    raddr: addr
    status: str

class addr(NamedTuple):
    """addr(ip, port)"""
    ip: str
    port: int

conn_tmap: dict[str, tuple[list[AddressFamily], list[SocketKind]]]

class Error(Exception):
    msg: str
    def __init__(self, msg: str = ...) -> None: ...

class NoSuchProcess(Error):
    pid: int
    name: str | None
    msg: str
    def __init__(self, pid: int, name: str | None = None, msg: str | None = None) -> None: ...

class ZombieProcess(NoSuchProcess):
    ppid: int | None
    def __init__(self, pid: int, name: str | None = None, ppid: int | None = None, msg: str | None = None) -> None: ...

class AccessDenied(Error):
    pid: int | None
    name: str | None
    msg: str
    def __init__(self, pid: int | None = None, name: str | None = None, msg: str | None = None) -> None: ...

class TimeoutExpired(Error):
    seconds: float
    pid: int | None
    name: str | None
    msg: str
    def __init__(self, seconds: float, pid: int | None = None, name: str | None = None) -> None: ...

_P = ParamSpec("_P")
_R = TypeVar("_R")

def usage_percent(used: ConvertibleToFloat, total: float, round_: SupportsIndex | None = None) -> float: ...

# returned function has `cache_clear()` attribute:
def memoize(fun: Callable[_P, _R]) -> Callable[_P, _R]: ...

# returned function has `cache_activate(proc)` and `cache_deactivate(proc)` attributes:
def memoize_when_activated(fun: Callable[_P, _R]) -> Callable[_P, _R]: ...
def isfile_strict(path: StrOrBytesPath) -> bool: ...
def path_exists_strict(path: StrOrBytesPath) -> bool: ...
def supports_ipv6() -> bool: ...
def parse_environ_block(data: str) -> dict[str, str]: ...
def sockfam_to_enum(num: int) -> AddressFamily: ...
def socktype_to_enum(num: int) -> SocketKind: ...
@overload
def conn_to_ntuple(fd: int, fam: int, type_: int, laddr, raddr, status: str, status_map, pid: int) -> sconn:
    """Convert a raw connection tuple to a proper ntuple."""
    ...
@overload
def conn_to_ntuple(fd: int, fam: int, type_: int, laddr, raddr, status: str, status_map, pid: None = None) -> pconn: ...
def deprecated_method(replacement: str) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...

class _WrapNumbers:
    lock: threading.Lock
    cache: dict[Incomplete, Incomplete]
    reminders: dict[Incomplete, Incomplete]
    reminder_keys: dict[Incomplete, Incomplete]
    def __init__(self) -> None: ...
    def run(self, input_dict, name): ...
    def cache_clear(self, name=None) -> None: ...
    def cache_info(self) -> tuple[dict[Incomplete, Incomplete], dict[Incomplete, Incomplete], dict[Incomplete, Incomplete]]: ...

def wrap_numbers(input_dict, name: str): ...
def open_binary(fname: FileDescriptorOrPath) -> BinaryIO: ...
def open_text(fname: FileDescriptorOrPath) -> io.TextIOWrapper: ...
def cat(fname: FileDescriptorOrPath, fallback=..., _open=...): ...
def bcat(fname: FileDescriptorOrPath, fallback=...): ...
def bytes2human(n: int, format: str = "%(value).1f%(symbol)s") -> str: ...
def get_procfs_path() -> str: ...
def decode(s: bytes) -> str: ...
def term_supports_colors(file: SupportsWrite[str] = ...) -> bool: ...
def hilite(s: str, color: str | None = None, bold: bool = False) -> str: ...
def print_color(s: str, color: str | None = None, bold: bool = False, file: SupportsWrite[str] = ...) -> None: ...
def debug(msg: str | Exception) -> None: ...

__all__ = [
    # OS constants
    "FREEBSD",
    "BSD",
    "LINUX",
    "NETBSD",
    "OPENBSD",
    "MACOS",
    "OSX",
    "POSIX",
    "SUNOS",
    "WINDOWS",
    # connection constants
    "CONN_CLOSE",
    "CONN_CLOSE_WAIT",
    "CONN_CLOSING",
    "CONN_ESTABLISHED",
    "CONN_FIN_WAIT1",
    "CONN_FIN_WAIT2",
    "CONN_LAST_ACK",
    "CONN_LISTEN",
    "CONN_NONE",
    "CONN_SYN_RECV",
    "CONN_SYN_SENT",
    "CONN_TIME_WAIT",
    # net constants
    "NIC_DUPLEX_FULL",
    "NIC_DUPLEX_HALF",
    "NIC_DUPLEX_UNKNOWN",
    # process status constants
    "STATUS_DEAD",
    "STATUS_DISK_SLEEP",
    "STATUS_IDLE",
    "STATUS_LOCKED",
    "STATUS_RUNNING",
    "STATUS_SLEEPING",
    "STATUS_STOPPED",
    "STATUS_SUSPENDED",
    "STATUS_TRACING_STOP",
    "STATUS_WAITING",
    "STATUS_WAKE_KILL",
    "STATUS_WAKING",
    "STATUS_ZOMBIE",
    "STATUS_PARKED",
    # other constants
    "ENCODING",
    "ENCODING_ERRS",
    "AF_INET6",
    # named tuples
    "pconn",
    "pcputimes",
    "pctxsw",
    "pgids",
    "pio",
    "pionice",
    "popenfile",
    "pthread",
    "puids",
    "sconn",
    "scpustats",
    "sdiskio",
    "sdiskpart",
    "sdiskusage",
    "snetio",
    "snicaddr",
    "snicstats",
    "sswap",
    "suser",
    # utility functions
    "conn_tmap",
    "deprecated_method",
    "isfile_strict",
    "memoize",
    "parse_environ_block",
    "path_exists_strict",
    "usage_percent",
    "supports_ipv6",
    "sockfam_to_enum",
    "socktype_to_enum",
    "wrap_numbers",
    "open_text",
    "open_binary",
    "cat",
    "bcat",
    "bytes2human",
    "conn_to_ntuple",
    "debug",
    # shell utils
    "hilite",
    "term_supports_colors",
    "print_color",
]
