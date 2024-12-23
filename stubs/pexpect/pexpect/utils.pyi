from os import _Environ

InterruptedError: type
string_types: tuple[type, ...]

def is_executable_file(path):
    """
    Checks that path is an executable regular file, or a symlink towards one.

    This is roughly ``os.path isfile(path) and os.access(path, os.X_OK)``.
    """
    ...
def which(filename, env: _Environ[str] | None = None):
    """
    This takes a given filename; tries to find it in the environment path;
    then checks if it is executable. This returns the full path to the filename
    if found and executable. Otherwise this returns None.
    """
    ...
def split_command_line(command_line):
    """
    This splits a command line into a list of arguments. It splits arguments
    on spaces, but handles embedded quotes, doublequotes, and escaped
    characters. It's impossible to do this with a regular expression, so I
    wrote a little state machine to parse the command line. 
    """
    ...
def select_ignore_interrupts(iwtd, owtd, ewtd, timeout: float | None = None):
    """
    This is a wrapper around select.select() that ignores signals. If
    select.select raises a select.error exception and errno is an EINTR
    error then it is ignored. Mainly this is used to ignore sigwinch
    (terminal resize). 
    """
    ...
def poll_ignore_interrupts(fds, timeout: float | None = None):
    """
    Simple wrapper around poll to register file descriptors and
    ignore signals.
    """
    ...
