"""
Utility classes and functions that make it easy to write :mod:`unittest` compatible test suites.

Over the years I've developed the habit of writing test suites for Python
projects using the :mod:`unittest` module. During those years I've come to know
:pypi:`pytest` and in fact I use :pypi:`pytest` to run my test suites (due to
its much better error reporting) but I've yet to publish a test suite that
*requires* :pypi:`pytest`. I have several reasons for doing so:

- It's nice to keep my test suites as simple and accessible as possible and
  not requiring a specific test runner is part of that attitude.

- Whereas :mod:`unittest` is quite explicit, :pypi:`pytest` contains a lot of
  magic, which kind of contradicts the Python mantra "explicit is better than
  implicit" (IMHO).
"""

import unittest
from _typeshed import Incomplete
from types import TracebackType
from typing import Any

from humanfriendly.compat import StringIO

def configure_logging(log_level=10) -> None:
    """
    configure_logging(log_level=logging.DEBUG)
    Automatically configure logging to the terminal.

    :param log_level: The log verbosity (a number, defaults
                      to :mod:`logging.DEBUG <logging>`).

    When :mod:`coloredlogs` is installed :func:`coloredlogs.install()` will be
    used to configure logging to the terminal. When this fails with an
    :exc:`~exceptions.ImportError` then :func:`logging.basicConfig()` is used
    as a fall back.
    """
    ...
def make_dirs(pathname) -> None:
    """
    Create missing directories.

    :param pathname: The pathname of a directory (a string).
    """
    ...
def retry(func, timeout: int = 60, exc_type=...):
    """
    retry(func, timeout=60, exc_type=AssertionError)
    Retry a function until assertions no longer fail.

    :param func: A callable. When the callable returns
                 :data:`False` it will also be retried.
    :param timeout: The number of seconds after which to abort (a number,
                    defaults to 60).
    :param exc_type: The type of exceptions to retry (defaults
                     to :exc:`~exceptions.AssertionError`).
    :returns: The value returned by `func`.
    :raises: Once the timeout has expired :func:`retry()` will raise the
             previously retried assertion error. When `func` keeps returning
             :data:`False` until `timeout` expires :exc:`CallableTimedOut`
             will be raised.

    This function sleeps between retries to avoid claiming CPU cycles we don't
    need. It starts by sleeping for 0.1 second but adjusts this to one second
    as the number of retries grows.
    """
    ...
def run_cli(entry_point, *arguments, **options):
    """
    Test a command line entry point.

    :param entry_point: The function that implements the command line interface
                        (a callable).
    :param arguments: Any positional arguments (strings) become the command
                      line arguments (:data:`sys.argv` items 1-N).
    :param options: The following keyword arguments are supported:

                    **capture**
                     Whether to use :class:`CaptureOutput`. Defaults
                     to :data:`True` but can be disabled by passing
                     :data:`False` instead.
                    **input**
                     Refer to :class:`CaptureOutput`.
                    **merged**
                     Refer to :class:`CaptureOutput`.
                    **program_name**
                     Used to set :data:`sys.argv` item 0.
    :returns: A tuple with two values:

              1. The return code (an integer).
              2. The captured output (a string).
    """
    ...
def skip_on_raise(*exc_types):
    """
    Decorate a test function to translation specific exception types to :exc:`unittest.SkipTest`.

    :param exc_types: One or more positional arguments give the exception
                      types to be translated to :exc:`unittest.SkipTest`.
    :returns: A decorator function specialized to `exc_types`.
    """
    ...
def touch(filename) -> None:
    """
    The equivalent of the UNIX :man:`touch` program in Python.

    :param filename: The pathname of the file to touch (a string).

    Note that missing directories are automatically created using
    :func:`make_dirs()`.
    """
    ...

class CallableTimedOut(Exception):
    """Raised by :func:`retry()` when the timeout expires."""
    ...

class ContextManager:
    """Base class to enable composition of context managers."""
    def __enter__(self):
        """Enable use as context managers."""
        ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None:
        """Enable use as context managers."""
        ...

class PatchedAttribute(ContextManager):
    """Context manager that temporary replaces an object attribute using :func:`setattr()`."""
    object_to_patch: Any
    attribute_to_patch: Any
    patched_value: Any
    original_value: Any
    def __init__(self, obj, name, value) -> None:
        """
        Initialize a :class:`PatchedAttribute` object.

        :param obj: The object to patch.
        :param name: An attribute name.
        :param value: The value to set.
        """
        ...
    def __enter__(self):
        """
        Replace (patch) the attribute.

        :returns: The object whose attribute was patched.
        """
        ...

class PatchedItem(ContextManager):
    """Context manager that temporary replaces an object item using :meth:`~object.__setitem__()`."""
    object_to_patch: Any
    item_to_patch: Any
    patched_value: Any
    original_value: Any
    def __init__(self, obj, item, value) -> None:
        """
        Initialize a :class:`PatchedItem` object.

        :param obj: The object to patch.
        :param item: The item to patch.
        :param value: The value to set.
        """
        ...
    def __enter__(self):
        """
        Replace (patch) the item.

        :returns: The object whose item was patched.
        """
        ...

class TemporaryDirectory(ContextManager):
    """
    Easy temporary directory creation & cleanup using the :keyword:`with` statement.

    Here's an example of how to use this:

    .. code-block:: python

       with TemporaryDirectory() as directory:
           # Do something useful here.
           assert os.path.isdir(directory)
    """
    mkdtemp_options: Any
    temporary_directory: Any
    def __init__(self, **options) -> None:
        """
        Initialize a :class:`TemporaryDirectory` object.

        :param options: Any keyword arguments are passed on to
                        :func:`tempfile.mkdtemp()`.
        """
        ...
    def __enter__(self):
        """
        Create the temporary directory using :func:`tempfile.mkdtemp()`.

        :returns: The pathname of the directory (a string).
        """
        ...

class MockedHomeDirectory(PatchedItem, TemporaryDirectory):
    """
    Context manager to temporarily change ``$HOME`` (the current user's profile directory).

    This class is a composition of the :class:`PatchedItem` and
    :class:`TemporaryDirectory` context managers.
    """
    def __init__(self) -> None:
        """Initialize a :class:`MockedHomeDirectory` object."""
        ...
    patched_value: Any
    def __enter__(self):
        """
        Activate the custom ``$PATH``.

        :returns: The pathname of the directory that has
                  been added to ``$PATH`` (a string).
        """
        ...

class CustomSearchPath(PatchedItem, TemporaryDirectory):
    """
    Context manager to temporarily customize ``$PATH`` (the executable search path).

    This class is a composition of the :class:`PatchedItem` and
    :class:`TemporaryDirectory` context managers.
    """
    isolated_search_path: Any
    def __init__(self, isolated: bool = False) -> None:
        """
        Initialize a :class:`CustomSearchPath` object.

        :param isolated: :data:`True` to clear the original search path,
                         :data:`False` to add the temporary directory to the
                         start of the search path.
        """
        ...
    patched_value: Any
    def __enter__(self):
        """
        Activate the custom ``$PATH``.

        :returns: The pathname of the directory that has
                  been added to ``$PATH`` (a string).
        """
        ...
    @property
    def current_search_path(self):
        """The value of ``$PATH`` or :data:`os.defpath` (a string)."""
        ...

class MockedProgram(CustomSearchPath):
    """
    Context manager to mock the existence of a program (executable).

    This class extends the functionality of :class:`CustomSearchPath`.
    """
    program_name: Any
    program_returncode: Any
    program_script: Any
    program_signal_file: Any
    def __init__(self, name, returncode: int = 0, script: Incomplete | None = None) -> None:
        """
        Initialize a :class:`MockedProgram` object.

        :param name: The name of the program (a string).
        :param returncode: The return code that the program should emit (a
                           number, defaults to zero).
        :param script: Shell script code to include in the mocked program (a
                       string or :data:`None`). This can be used to mock a
                       program that is expected to generate specific output.
        """
        ...
    def __enter__(self):
        """
        Create the mock program.

        :returns: The pathname of the directory that has
                  been added to ``$PATH`` (a string).
        """
        ...
    def __exit__(self, *args: object, **kw: object):
        """
        Ensure that the mock program was run.

        :raises: :exc:`~exceptions.AssertionError` when
                 the mock program hasn't been run.
        """
        ...

class CaptureOutput(ContextManager):
    """
    Context manager that captures what's written to :data:`sys.stdout` and :data:`sys.stderr`.

    .. attribute:: stdin

       The :class:`~humanfriendly.compat.StringIO` object used to feed the standard input stream.

    .. attribute:: stdout

       The :class:`CaptureBuffer` object used to capture the standard output stream.

    .. attribute:: stderr

       The :class:`CaptureBuffer` object used to capture the standard error stream.
    """
    stdin: Any
    stdout: Any
    stderr: Any
    patched_attributes: Any
    def __init__(self, merged: bool = False, input: str = "", enabled: bool = True) -> None:
        """
        Initialize a :class:`CaptureOutput` object.

        :param merged: :data:`True` to merge the streams,
                       :data:`False` to capture them separately.
        :param input: The data that reads from :data:`sys.stdin`
                      should return (a string).
        :param enabled: :data:`True` to enable capturing (the default),
                        :data:`False` otherwise. This makes it easy to
                        unconditionally use :class:`CaptureOutput` in
                        a :keyword:`with` block while preserving the
                        choice to opt out of capturing output.
        """
        ...
    def __enter__(self):
        """Start capturing what's written to :data:`sys.stdout` and :data:`sys.stderr`."""
        ...
    def get_lines(self):
        """Get the contents of :attr:`stdout` split into separate lines."""
        ...
    def get_text(self):
        """Get the contents of :attr:`stdout` as a Unicode string."""
        ...
    def getvalue(self):
        """Get the text written to :data:`sys.stdout`."""
        ...

class CaptureBuffer(StringIO):
    """
    Helper for :class:`CaptureOutput` to provide an easy to use API.

    The two methods defined by this subclass were specifically chosen to match
    the names of the methods provided by my :pypi:`capturer` package which
    serves a similar role as :class:`CaptureOutput` but knows how to simulate
    an interactive terminal (tty).
    """
    def get_lines(self):
        """Get the contents of the buffer split into separate lines."""
        ...
    def get_text(self):
        """Get the contents of the buffer as a Unicode string."""
        ...

class TestCase(unittest.TestCase):
    """Subclass of :class:`unittest.TestCase` with automatic logging and other miscellaneous features."""
    def __init__(self, *args, **kw) -> None:
        """
        Initialize a :class:`TestCase` object.

        Any positional and/or keyword arguments are passed on to the
        initializer of the superclass.
        """
        ...
    def setUp(self, log_level=10) -> None:
        """
        setUp(log_level=logging.DEBUG)
        Automatically configure logging to the terminal.

        :param log_level: Refer to :func:`configure_logging()`.

        The :func:`setUp()` method is automatically called by
        :class:`unittest.TestCase` before each test method starts.
        It does two things:

        - Logging to the terminal is configured using
          :func:`configure_logging()`.

        - Before the test method starts a newline is emitted, to separate the
          name of the test method (which will be printed to the terminal by
          :mod:`unittest` or :pypi:`pytest`) from the first line of logging
          output that the test method is likely going to generate.
        """
        ...
