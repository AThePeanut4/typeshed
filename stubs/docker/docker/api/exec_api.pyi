class ExecApiMixin:
    def exec_create(
        self,
        container,
        cmd,
        stdout: bool = True,
        stderr: bool = True,
        stdin: bool = False,
        tty: bool = False,
        privileged: bool = False,
        user: str = "",
        environment=None,
        workdir=None,
        detach_keys=None,
    ): ...
    def exec_inspect(self, exec_id): ...
    def exec_resize(self, exec_id, height=None, width=None) -> None: ...
    def exec_start(
        self, exec_id, detach: bool = False, tty: bool = False, stream: bool = False, socket: bool = False, demux: bool = False
    ):
        """
        Start a previously set up exec instance.

        Args:
            exec_id (str): ID of the exec instance
            detach (bool): If true, detach from the exec command.
                Default: False
            tty (bool): Allocate a pseudo-TTY. Default: False
            stream (bool): Return response data progressively as an iterator
                of strings, rather than a single string.
            socket (bool): Return the connection socket to allow custom
                read/write operations. Must be closed by the caller when done.
            demux (bool): Return stdout and stderr separately

        Returns:

            (generator or str or tuple): If ``stream=True``, a generator
            yielding response chunks. If ``socket=True``, a socket object for
            the connection. A string containing response data otherwise. If
            ``demux=True``, a tuple with two elements of type byte: stdout and
            stderr.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
