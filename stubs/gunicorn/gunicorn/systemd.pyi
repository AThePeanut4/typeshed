from typing import Final

from gunicorn.glogging import Logger as GLogger

SD_LISTEN_FDS_START: Final[int]

def listen_fds(unset_environment: bool = True) -> int:
    """
    Get the number of sockets inherited from systemd socket activation.

    :param unset_environment: clear systemd environment variables unless False
    :type unset_environment: bool
    :return: the number of sockets to inherit from systemd socket activation
    :rtype: int

    Returns zero immediately if $LISTEN_PID is not set to the current pid.
    Otherwise, returns the number of systemd activation sockets specified by
    $LISTEN_FDS.

    When $LISTEN_PID matches the current pid, unsets the environment variables
    unless the ``unset_environment`` flag is ``False``.

    .. note::
        Unlike the sd_listen_fds C function, this implementation does not set
        the FD_CLOEXEC flag because the gunicorn arbiter never needs to do this.

    .. seealso::
        `<https://www.freedesktop.org/software/systemd/man/sd_listen_fds.html>`_
    """
    ...
def sd_notify(state: str, logger: GLogger, unset_environment: bool = False) -> None:
    """
    Send a notification to systemd. state is a string; see
    the man page of sd_notify (http://www.freedesktop.org/software/systemd/man/sd_notify.html)
    for a description of the allowable values.

    If the unset_environment parameter is True, sd_notify() will unset
    the $NOTIFY_SOCKET environment variable before returning (regardless of
    whether the function call itself succeeded or not). Further calls to
    sd_notify() will then fail, but the variable is no longer inherited by
    child processes.
    """
    ...
