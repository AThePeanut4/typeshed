"""
This class extends pexpect.spawn to specialize setting up SSH connections.
This adds methods for login, logout, and expecting the shell prompt.

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

from _typeshed import FileDescriptorOrPath
from os import _Environ
from typing import AnyStr, Literal

from .exceptions import ExceptionPexpect
from .pty_spawn import spawn
from .spawnbase import _Logfile

__all__ = ["ExceptionPxssh", "pxssh"]

class ExceptionPxssh(ExceptionPexpect):
    """
    Raised for pxssh exceptions.
    
    """
    ...

class pxssh(spawn[AnyStr]):
    """
    This class extends pexpect.spawn to specialize setting up SSH
    connections. This adds methods for login, logout, and expecting the shell
    prompt. It does various tricky things to handle many situations in the SSH
    login process. For example, if the session is your first login, then pxssh
    automatically accepts the remote certificate; or if you have public key
    authentication setup then pxssh won't wait for the password prompt.

    pxssh uses the shell prompt to synchronize output from the remote host. In
    order to make this more robust it sets the shell prompt to something more
    unique than just $ or #. This should work on most Borne/Bash or Csh style
    shells.

    Example that runs a few commands on a remote server and prints the result::

        from pexpect import pxssh
        import getpass
        try:
            s = pxssh.pxssh()
            hostname = raw_input('hostname: ')
            username = raw_input('username: ')
            password = getpass.getpass('password: ')
            s.login(hostname, username, password)
            s.sendline('uptime')   # run a command
            s.prompt()             # match the prompt
            print(s.before)        # print everything before the prompt.
            s.sendline('ls -l')
            s.prompt()
            print(s.before)
            s.sendline('df')
            s.prompt()
            print(s.before)
            s.logout()
        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)

    Example showing how to specify SSH options::

        from pexpect import pxssh
        s = pxssh.pxssh(options={
                            "StrictHostKeyChecking": "no",
                            "UserKnownHostsFile": "/dev/null"})
        ...

    Note that if you have ssh-agent running while doing development with pxssh
    then this can lead to a lot of confusion. Many X display managers (xdm,
    gdm, kdm, etc.) will automatically start a GUI agent. You may see a GUI
    dialog box popup asking for a password during development. You should turn
    off any key agents during testing. The 'force_password' attribute will turn
    off public key authentication. This will only work if the remote SSH server
    is configured to allow password logins. Example of using 'force_password'
    attribute::

            s = pxssh.pxssh()
            s.force_password = True
            hostname = raw_input('hostname: ')
            username = raw_input('username: ')
            password = getpass.getpass('password: ')
            s.login (hostname, username, password)

    `debug_command_string` is only for the test suite to confirm that the string
    generated for SSH is correct, using this will not allow you to do
    anything other than get a string back from `pxssh.pxssh.login()`.
    """
    name: str
    UNIQUE_PROMPT: str
    PROMPT: str
    PROMPT_SET_SH: str
    PROMPT_SET_CSH: str
    PROMPT_SET_ZSH: str
    SSH_OPTS: str
    force_password: bool
    debug_command_string: bool
    options: dict[str, str]
    def __init__(
        self,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        cwd: FileDescriptorOrPath | None = None,
        env: _Environ[str] | None = None,
        ignore_sighup: bool = True,
        echo: bool = True,
        options: dict[str, str] = {},
        encoding: str | None = None,
        codec_errors: str = "strict",
        debug_command_string: bool = False,
        use_poll: bool = False,
    ) -> None: ...
    def levenshtein_distance(self, a, b):
        """
        This calculates the Levenshtein distance between a and b.
        
        """
        ...
    def try_read_prompt(self, timeout_multiplier):
        """
        This facilitates using communication timeouts to perform
        synchronization as quickly as possible, while supporting high latency
        connections with a tunable worst case performance. Fast connections
        should be read almost immediately. Worst case performance for this
        method is timeout_multiplier * 3 seconds.
        """
        ...
    def sync_original_prompt(self, sync_multiplier: float = 1.0):
        """
        This attempts to find the prompt. Basically, press enter and record
        the response; press enter again and record the response; if the two
        responses are similar then assume we are at the original prompt.
        This can be a slow function. Worst case with the default sync_multiplier
        can take 12 seconds. Low latency connections are more likely to fail
        with a low sync_multiplier. Best case sync time gets worse with a
        high sync multiplier (500 ms with default). 
        """
        ...
    def login(
        self,
        server,
        username: str | None = None,
        password: str = "",
        terminal_type: str = "ansi",
        original_prompt: str = "[#$]",
        login_timeout: float | None = 10,
        port: int | None = None,
        auto_prompt_reset: bool = True,
        ssh_key: FileDescriptorOrPath | Literal[True] | None = None,
        quiet: bool = True,
        sync_multiplier: int = 1,
        check_local_ip: bool = True,
        password_regex: str = "(?i)(?:password:)|(?:passphrase for key)",
        ssh_tunnels: dict[str, list[str | int]] = {},
        spawn_local_ssh: bool = True,
        sync_original_prompt: bool = True,
        ssh_config: FileDescriptorOrPath | None = None,
        cmd: str = "ssh",
    ):
        """
        This logs the user into the given server.

        It uses 'original_prompt' to try to find the prompt right after login.
        When it finds the prompt it immediately tries to reset the prompt to
        something more easily matched. The default 'original_prompt' is very
        optimistic and is easily fooled. It's more reliable to try to match the original
        prompt as exactly as possible to prevent false matches by server
        strings such as the "Message Of The Day". On many systems you can
        disable the MOTD on the remote server by creating a zero-length file
        called :file:`~/.hushlogin` on the remote server. If a prompt cannot be found
        then this will not necessarily cause the login to fail. In the case of
        a timeout when looking for the prompt we assume that the original
        prompt was so weird that we could not match it, so we use a few tricks
        to guess when we have reached the prompt. Then we hope for the best and
        blindly try to reset the prompt to something more unique. If that fails
        then login() raises an :class:`ExceptionPxssh` exception.

        In some situations it is not possible or desirable to reset the
        original prompt. In this case, pass ``auto_prompt_reset=False`` to
        inhibit setting the prompt to the UNIQUE_PROMPT. Remember that pxssh
        uses a unique prompt in the :meth:`prompt` method. If the original prompt is
        not reset then this will disable the :meth:`prompt` method unless you
        manually set the :attr:`PROMPT` attribute.

        Set ``password_regex`` if there is a MOTD message with `password` in it.
        Changing this is like playing in traffic, don't (p)expect it to match straight
        away.

        If you require to connect to another SSH server from the your original SSH
        connection set ``spawn_local_ssh`` to `False` and this will use your current
        session to do so. Setting this option to `False` and not having an active session
        will trigger an error.

        Set ``ssh_key`` to a file path to an SSH private key to use that SSH key
        for the session authentication.
        Set ``ssh_key`` to `True` to force passing the current SSH authentication socket
        to the desired ``hostname``.

        Set ``ssh_config`` to a file path string of an SSH client config file to pass that
        file to the client to handle itself. You may set any options you wish in here, however
        doing so will require you to post extra information that you may not want to if you
        run into issues.

        Alter the ``cmd`` to change the ssh client used, or to prepend it with network
        namespaces. For example ```cmd="ip netns exec vlan2 ssh"``` to execute the ssh in
        network namespace named ```vlan```.
        """
        ...
    def logout(self) -> None:
        """
        Sends exit to the remote shell.

        If there are stopped jobs then this automatically sends exit twice.
        """
        ...
    def prompt(self, timeout: float | None = -1):
        """
        Match the next shell prompt.

        This is little more than a short-cut to the :meth:`~pexpect.spawn.expect`
        method. Note that if you called :meth:`login` with
        ``auto_prompt_reset=False``, then before calling :meth:`prompt` you must
        set the :attr:`PROMPT` attribute to a regex that it will use for
        matching the prompt.

        Calling :meth:`prompt` will erase the contents of the :attr:`before`
        attribute even if no prompt is ever matched. If timeout is not given or
        it is set to -1 then self.timeout is used.

        :return: True if the shell prompt was matched, False if the timeout was
                 reached.
        """
        ...
    def set_unique_prompt(self):
        """
        This sets the remote prompt to something more unique than ``#`` or ``$``.
        This makes it easier for the :meth:`prompt` method to match the shell prompt
        unambiguously. This method is called automatically by the :meth:`login`
        method, but you may want to call it manually if you somehow reset the
        shell prompt. For example, if you 'su' to a different user then you
        will need to manually reset the prompt. This sends shell commands to
        the remote host to set the prompt, so this assumes the remote host is
        ready to receive commands.

        Alternatively, you may use your own prompt pattern. In this case you
        should call :meth:`login` with ``auto_prompt_reset=False``; then set the
        :attr:`PROMPT` attribute to a regular expression. After that, the
        :meth:`prompt` method will try to match your prompt pattern.
        """
        ...
