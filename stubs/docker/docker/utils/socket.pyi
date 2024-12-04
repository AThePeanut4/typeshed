from _typeshed import Incomplete
from collections.abc import Generator

STDOUT: int
STDERR: int

class SocketError(Exception): ...

NPIPE_ENDED: int

def read(socket, n: int = 4096):
    """Reads at most n bytes from socket"""
    ...
def read_exactly(socket, n):
    """
    Reads exactly n bytes from socket
    Raises SocketError if there isn't enough data
    """
    ...
def next_frame_header(socket):
    """
    Returns the stream and size of the next frame of data waiting to be read
    from socket, according to the protocol defined here:

    https://docs.docker.com/engine/api/v1.24/#attach-to-a-container
    """
    ...
def frames_iter(socket, tty):
    """
    Return a generator of frames read from socket. A frame is a tuple where
    the first item is the stream number and the second item is a chunk of data.

    If the tty setting is enabled, the streams are multiplexed into the stdout
    stream.
    """
    ...
def frames_iter_no_tty(socket) -> Generator[Incomplete, None, None]:
    """
    Returns a generator of data read from the socket when the tty setting is
    not enabled.
    """
    ...
def frames_iter_tty(socket) -> Generator[Incomplete, None, None]:
    """
    Return a generator of data read from the socket when the tty setting is
    enabled.
    """
    ...
def consume_socket_output(frames, demux: bool = False):
    """
    Iterate through frames read from the socket and return the result.

    Args:

        demux (bool):
            If False, stdout and stderr are multiplexed, and the result is the
            concatenation of all the frames. If True, the streams are
            demultiplexed, and the result is a 2-tuple where each item is the
            concatenation of frames belonging to the same stream.
    """
    ...
def demux_adaptor(stream_id, data):
    """
    Utility to demultiplex stdout and stderr when reading frames from the
    socket.
    """
    ...
