"""Routines common to all posix systems."""

from _typeshed import Incomplete

def pid_exists(pid):
    """Check whether pid exists in the current process table."""
    ...
def wait_pid(
    pid,
    timeout: Incomplete | None = None,
    proc_name: Incomplete | None = None,
    _waitpid=...,
    _timer=...,
    _min=...,
    _sleep=...,
    _pid_exists=...,
): ...
def disk_usage(path): ...
def get_terminal_map(): ...

__all__ = ["pid_exists", "wait_pid", "disk_usage", "get_terminal_map"]
