"""
This is like :mod:`pexpect`, but it will work with any file descriptor that you
pass it. You are responsible for opening and close the file descriptor.
This allows you to use Pexpect with sockets and named pipes (FIFOs).

.. note::
    socket.fileno() does not give a readable file descriptor on windows.
    Use :mod:`pexpect.socket_pexpect` for cross-platform socket support

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from _typeshed import FileDescriptorLike
from collections.abc import Iterable
from typing import AnyStr

from .spawnbase import SpawnBase, _Logfile

__all__ = ["fdspawn"]

class fdspawn(SpawnBase[AnyStr]):
    """
    This is like pexpect.spawn but allows you to supply your own open file
    descriptor. For example, you could use it to read through a file looking
    for patterns, or to control a modem or serial device. 
    """
    args: None
    command: None
    child_fd: int
    own_fd: bool
    closed: bool
    name: str
    use_poll: bool
    def __init__(
        self,
        fd: FileDescriptorLike,
        args: None = None,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ) -> None:
        """
        This takes a file descriptor (an int) or an object that support the
        fileno() method (returning an int). All Python file-like objects
        support fileno(). 
        """
        ...
    def close(self) -> None:
        """
        Close the file descriptor.

        Calling this method a second time does nothing, but if the file
        descriptor was closed elsewhere, :class:`OSError` will be raised.
        """
        ...
    def isalive(self) -> bool:
        """
        This checks if the file descriptor is still valid. If :func:`os.fstat`
        does not raise an exception then we assume it is alive. 
        """
        ...
    def terminate(self, force: bool = False) -> None:
        """Deprecated and invalid. Just raises an exception."""
        ...
    def send(self, s: str | bytes) -> int:
        """Write to fd, return number of bytes written"""
        ...
    def sendline(self, s: str | bytes) -> int:
        """Write to fd with trailing newline, return number of bytes written"""
        ...
    def write(self, s) -> None:
        """Write to fd, return None"""
        ...
    def writelines(self, sequence: Iterable[str | bytes]) -> None:
        """Call self.write() for each item in sequence"""
        ...
    def read_nonblocking(self, size: int = 1, timeout: float | None = -1) -> AnyStr:
        """
        Read from the file descriptor and return the result as a string.

        The read_nonblocking method of :class:`SpawnBase` assumes that a call
        to os.read will not block (timeout parameter is ignored). This is not
        the case for POSIX file-like objects such as sockets and serial ports.

        Use :func:`select.select`, timeout is implemented conditionally for
        POSIX systems.

        :param int size: Read at most *size* bytes.
        :param int timeout: Wait timeout seconds for file descriptor to be
            ready to read. When -1 (default), use self.timeout. When 0, poll.
        :return: String containing the bytes read
        """
        ...
