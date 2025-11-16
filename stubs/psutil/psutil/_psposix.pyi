"""Routines common to all posix systems."""

import sys
from _typeshed import FileDescriptorOrPath, StrOrBytesPath

from ._common import sdiskusage

def pid_exists(pid: int) -> bool:
    """Check whether pid exists in the current process table."""
    ...
def wait_pid(
    pid: int,
    timeout: float | None = None,
    proc_name: str | None = None,
    _waitpid=...,
    _timer=...,
    _min=...,
    _sleep=...,
    _pid_exists=...,
):
    """
    Wait for a process PID to terminate.

    If the process terminated normally by calling exit(3) or _exit(2),
    or by returning from main(), the return value is the positive integer
    passed to *exit().

    If it was terminated by a signal it returns the negated value of the
    signal which caused the termination (e.g. -SIGTERM).

    If PID is not a children of os.getpid() (current process) just
    wait until the process disappears and return None.

    If PID does not exist at all return None immediately.

    If *timeout* != None and process is still alive raise TimeoutExpired.
    timeout=0 is also possible (either return immediately or raise).
    """
    ...

if sys.platform == "darwin":
    def disk_usage(path: StrOrBytesPath) -> sdiskusage: ...

else:
    def disk_usage(path: FileDescriptorOrPath) -> sdiskusage:
        """
        Return disk usage associated with path.
        Note: UNIX usually reserves 5% disk space which is not accessible
        by user. In this function "total" and "used" values reflect the
        total and used disk space whereas "free" and "percent" represent
        the "free" and "used percent" user disk space.
        """
        ...

def get_terminal_map() -> dict[int, str]:
    """
    Get a map of device-id -> path as a dict.
    Used by Process.terminal().
    """
    ...

__all__ = ["pid_exists", "wait_pid", "disk_usage", "get_terminal_map"]
