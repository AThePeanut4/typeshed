from _typeshed import Incomplete
from typing import Any

ANSI_CSI: str
ANSI_SGR: str
ANSI_ERASE_LINE: Any
ANSI_RESET: Any
ANSI_HIDE_CURSOR: Any
ANSI_SHOW_CURSOR: Any
ANSI_COLOR_CODES: Any
ANSI_TEXT_STYLES: Any
CLEAN_OUTPUT_PATTERN: Any
DEFAULT_LINES: int
DEFAULT_COLUMNS: int
DEFAULT_ENCODING: str
HIGHLIGHT_COLOR: Any

def ansi_strip(text, readline_hints: bool = True):
    """
    Strip ANSI escape sequences from the given string.

    :param text: The text from which ANSI escape sequences should be removed (a
                 string).
    :param readline_hints: If :data:`True` then :func:`readline_strip()` is
                           used to remove `readline hints`_ from the string.
    :returns: The text without ANSI escape sequences (a string).
    """
    ...
def ansi_style(**kw):
    """
    Generate ANSI escape sequences for the given color and/or style(s).

    :param color: The foreground color. Three types of values are supported:

                  - The name of a color (one of the strings 'black', 'red',
                    'green', 'yellow', 'blue', 'magenta', 'cyan' or 'white').
                  - An integer that refers to the 256 color mode palette.
                  - A tuple or list with three integers representing an RGB
                    (red, green, blue) value.

                  The value :data:`None` (the default) means no escape
                  sequence to switch color will be emitted.
    :param background: The background color (see the description
                       of the `color` argument).
    :param bright: Use high intensity colors instead of default colors
                   (a boolean, defaults to :data:`False`).
    :param readline_hints: If :data:`True` then :func:`readline_wrap()` is
                           applied to the generated ANSI escape sequences (the
                           default is :data:`False`).
    :param kw: Any additional keyword arguments are expected to match a key
               in the :data:`ANSI_TEXT_STYLES` dictionary. If the argument's
               value evaluates to :data:`True` the respective style will be
               enabled.
    :returns: The ANSI escape sequences to enable the requested text styles or
              an empty string if no styles were requested.
    :raises: :exc:`~exceptions.ValueError` when an invalid color name is given.

    Even though only eight named colors are supported, the use of `bright=True`
    and `faint=True` increases the number of available colors to around 24 (it
    may be slightly lower, for example because faint black is just black).

    **Support for 8-bit colors**

    In `release 4.7`_ support for 256 color mode was added. While this
    significantly increases the available colors it's not very human friendly
    in usage because you need to look up color codes in the `256 color mode
    palette <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`_.

    You can use the ``humanfriendly --demo`` command to get a demonstration of
    the available colors, see also the screen shot below. Note that the small
    font size in the screen shot was so that the demonstration of 256 color
    mode support would fit into a single screen shot without scrolling :-)
    (I wasn't feeling very creative).

      .. image:: images/ansi-demo.png

    **Support for 24-bit colors**

    In `release 4.14`_ support for 24-bit colors was added by accepting a tuple
    or list with three integers representing the RGB (red, green, blue) value
    of a color. This is not included in the demo because rendering millions of
    colors was deemed unpractical ;-).

    .. _release 4.7: http://humanfriendly.readthedocs.io/en/latest/changelog.html#release-4-7-2018-01-14
    .. _release 4.14: http://humanfriendly.readthedocs.io/en/latest/changelog.html#release-4-14-2018-07-13
    """
    ...
def ansi_width(text):
    """
    Calculate the effective width of the given text (ignoring ANSI escape sequences).

    :param text: The text whose width should be calculated (a string).
    :returns: The width of the text without ANSI escape sequences (an
              integer).

    This function uses :func:`ansi_strip()` to strip ANSI escape sequences from
    the given string and returns the length of the resulting string.
    """
    ...
def ansi_wrap(text, **kw):
    """
    Wrap text in ANSI escape sequences for the given color and/or style(s).

    :param text: The text to wrap (a string).
    :param kw: Any keyword arguments are passed to :func:`ansi_style()`.
    :returns: The result of this function depends on the keyword arguments:

              - If :func:`ansi_style()` generates an ANSI escape sequence based
                on the keyword arguments, the given text is prefixed with the
                generated ANSI escape sequence and suffixed with
                :data:`ANSI_RESET`.

              - If :func:`ansi_style()` returns an empty string then the text
                given by the caller is returned unchanged.
    """
    ...
def auto_encode(stream, text, *args, **kw) -> None:
    """
    Reliably write Unicode strings to the terminal.

    :param stream: The file-like object to write to (a value like
                   :data:`sys.stdout` or :data:`sys.stderr`).
    :param text: The text to write to the stream (a string).
    :param args: Refer to :func:`~humanfriendly.text.format()`.
    :param kw: Refer to :func:`~humanfriendly.text.format()`.

    Renders the text using :func:`~humanfriendly.text.format()` and writes it
    to the given stream. If an :exc:`~exceptions.UnicodeEncodeError` is
    encountered in doing so, the text is encoded using :data:`DEFAULT_ENCODING`
    and the write is retried. The reasoning behind this rather blunt approach
    is that it's preferable to get output on the command line in the wrong
    encoding then to have the Python program blow up with a
    :exc:`~exceptions.UnicodeEncodeError` exception.
    """
    ...
def clean_terminal_output(text):
    """
    Clean up the terminal output of a command.

    :param text: The raw text with special characters (a Unicode string).
    :returns: A list of Unicode strings (one for each line).

    This function emulates the effect of backspace (0x08), carriage return
    (0x0D) and line feed (0x0A) characters and the ANSI 'erase line' escape
    sequence on interactive terminals. It's intended to clean up command output
    that was originally meant to be rendered on an interactive terminal and
    that has been captured using e.g. the :man:`script` program [#]_ or the
    :mod:`pty` module [#]_.

    .. [#] My coloredlogs_ package supports the ``coloredlogs --to-html``
           command which uses :man:`script` to fool a subprocess into thinking
           that it's connected to an interactive terminal (in order to get it
           to emit ANSI escape sequences).

    .. [#] My capturer_ package uses the :mod:`pty` module to fool the current
           process and subprocesses into thinking they are connected to an
           interactive terminal (in order to get them to emit ANSI escape
           sequences).

    **Some caveats about the use of this function:**

    - Strictly speaking the effect of carriage returns cannot be emulated
      outside of an actual terminal due to the interaction between overlapping
      output, terminal widths and line wrapping. The goal of this function is
      to sanitize noise in terminal output while preserving useful output.
      Think of it as a useful and pragmatic but possibly lossy conversion.

    - The algorithm isn't smart enough to properly handle a pair of ANSI escape
      sequences that open before a carriage return and close after the last
      carriage return in a linefeed delimited string; the resulting string will
      contain only the closing end of the ANSI escape sequence pair. Tracking
      this kind of complexity requires a state machine and proper parsing.

    .. _capturer: https://pypi.org/project/capturer
    .. _coloredlogs: https://pypi.org/project/coloredlogs
    """
    ...
def connected_to_terminal(stream: Incomplete | None = None):
    """
    Check if a stream is connected to a terminal.

    :param stream: The stream to check (a file-like object,
                   defaults to :data:`sys.stdout`).
    :returns: :data:`True` if the stream is connected to a terminal,
              :data:`False` otherwise.

    See also :func:`terminal_supports_colors()`.
    """
    ...
def enable_ansi_support():
    """
    Try to enable support for ANSI escape sequences (required on Windows).

    :returns: :data:`True` if ANSI is supported, :data:`False` otherwise.

    This functions checks for the following supported configurations, in the
    given order:

    1. On Windows, if :func:`have_windows_native_ansi_support()` confirms
       native support for ANSI escape sequences :mod:`ctypes` will be used to
       enable this support.

    2. On Windows, if the environment variable ``$ANSICON`` is set nothing is
       done because it is assumed that support for ANSI escape sequences has
       already been enabled via `ansicon <https://github.com/adoxa/ansicon>`_.

    3. On Windows, an attempt is made to import and initialize the Python
       package :pypi:`colorama` instead (of course for this to work
       :pypi:`colorama` has to be installed).

    4. On other platforms this function calls :func:`connected_to_terminal()`
       to determine whether ANSI escape sequences are supported (that is to
       say all platforms that are not Windows are assumed to support ANSI
       escape sequences natively, without weird contortions like above).

       This makes it possible to call :func:`enable_ansi_support()`
       unconditionally without checking the current platform.

    The :func:`~humanfriendly.decorators.cached` decorator is used to ensure
    that this function is only executed once, but its return value remains
    available on later calls.
    """
    ...
def find_terminal_size():
    """
    Determine the number of lines and columns visible in the terminal.

    :returns: A tuple of two integers with the line and column count.

    The result of this function is based on the first of the following three
    methods that works:

    1. First :func:`find_terminal_size_using_ioctl()` is tried,
    2. then :func:`find_terminal_size_using_stty()` is tried,
    3. finally :data:`DEFAULT_LINES` and :data:`DEFAULT_COLUMNS` are returned.

    .. note:: The :func:`find_terminal_size()` function performs the steps
              above every time it is called, the result is not cached. This is
              because the size of a virtual terminal can change at any time and
              the result of :func:`find_terminal_size()` should be correct.

              `Pre-emptive snarky comment`_: It's possible to cache the result
              of this function and use :mod:`signal.SIGWINCH <signal>` to
              refresh the cached values!

              Response: As a library I don't consider it the role of the
              :mod:`humanfriendly.terminal` module to install a process wide
              signal handler ...

    .. _Pre-emptive snarky comment: http://blogs.msdn.com/b/oldnewthing/archive/2008/01/30/7315957.aspx
    """
    ...
def find_terminal_size_using_ioctl(stream):
    """
    Find the terminal size using :func:`fcntl.ioctl()`.

    :param stream: A stream connected to the terminal (a file object with a
                   ``fileno`` attribute).
    :returns: A tuple of two integers with the line and column count.
    :raises: This function can raise exceptions but I'm not going to document
             them here, you should be using :func:`find_terminal_size()`.

    Based on an `implementation found on StackOverflow <http://stackoverflow.com/a/3010495/788200>`_.
    """
    ...
def find_terminal_size_using_stty():
    """
    Find the terminal size using the external command ``stty size``.

    :param stream: A stream connected to the terminal (a file object).
    :returns: A tuple of two integers with the line and column count.
    :raises: This function can raise exceptions but I'm not going to document
             them here, you should be using :func:`find_terminal_size()`.
    """
    ...
def get_pager_command(text: Incomplete | None = None):
    """
    Get the command to show a text on the terminal using a pager.

    :param text: The text to print to the terminal (a string).
    :returns: A list of strings with the pager command and arguments.

    The use of a pager helps to avoid the wall of text effect where the user
    has to scroll up to see where the output began (not very user friendly).

    If the given text contains ANSI escape sequences the command ``less
    --RAW-CONTROL-CHARS`` is used, otherwise the environment variable
    ``$PAGER`` is used (if ``$PAGER`` isn't set :man:`less` is used).

    When the selected pager is :man:`less`, the following options are used to
    make the experience more user friendly:

    - ``--quit-if-one-screen`` causes :man:`less` to automatically exit if the
      entire text can be displayed on the first screen. This makes the use of a
      pager transparent for smaller texts (because the operator doesn't have to
      quit the pager).

    - ``--no-init`` prevents :man:`less` from clearing the screen when it
      exits. This ensures that the operator gets a chance to review the text
      (for example a usage message) after quitting the pager, while composing
      the next command.
    """
    ...
def have_windows_native_ansi_support():
    """
    Check if we're running on a Windows 10 release with native support for ANSI escape sequences.

    :returns: :data:`True` if so, :data:`False` otherwise.

    The :func:`~humanfriendly.decorators.cached` decorator is used as a minor
    performance optimization. Semantically this should have zero impact because
    the answer doesn't change in the lifetime of a computer process.
    """
    ...
def message(text, *args, **kw) -> None:
    """
    Print a formatted message to the standard error stream.

    For details about argument handling please refer to
    :func:`~humanfriendly.text.format()`.

    Renders the message using :func:`~humanfriendly.text.format()` and writes
    the resulting string (followed by a newline) to :data:`sys.stderr` using
    :func:`auto_encode()`.
    """
    ...
def output(text, *args, **kw) -> None:
    """
    Print a formatted message to the standard output stream.

    For details about argument handling please refer to
    :func:`~humanfriendly.text.format()`.

    Renders the message using :func:`~humanfriendly.text.format()` and writes
    the resulting string (followed by a newline) to :data:`sys.stdout` using
    :func:`auto_encode()`.
    """
    ...
def readline_strip(expr):
    """
    Remove `readline hints`_ from a string.

    :param text: The text to strip (a string).
    :returns: The stripped text.
    """
    ...
def readline_wrap(expr):
    """
    Wrap an ANSI escape sequence in `readline hints`_.

    :param text: The text with the escape sequence to wrap (a string).
    :returns: The wrapped text.

    .. _readline hints: http://superuser.com/a/301355
    """
    ...
def show_pager(formatted_text, encoding="UTF-8") -> None:
    """
    Print a large text to the terminal using a pager.

    :param formatted_text: The text to print to the terminal (a string).
    :param encoding: The name of the text encoding used to encode the formatted
                     text if the formatted text is a Unicode string (a string,
                     defaults to :data:`DEFAULT_ENCODING`).

    When :func:`connected_to_terminal()` returns :data:`True` a pager is used
    to show the text on the terminal, otherwise the text is printed directly
    without invoking a pager.

    The use of a pager helps to avoid the wall of text effect where the user
    has to scroll up to see where the output began (not very user friendly).

    Refer to :func:`get_pager_command()` for details about the command line
    that's used to invoke the pager.
    """
    ...
def terminal_supports_colors(stream: Incomplete | None = None):
    """
    Check if a stream is connected to a terminal that supports ANSI escape sequences.

    :param stream: The stream to check (a file-like object,
                   defaults to :data:`sys.stdout`).
    :returns: :data:`True` if the terminal supports ANSI escape sequences,
              :data:`False` otherwise.

    This function was originally inspired by the implementation of
    `django.core.management.color.supports_color()
    <https://github.com/django/django/blob/master/django/core/management/color.py>`_
    but has since evolved significantly.
    """
    ...
def usage(usage_text) -> None:
    """
    Print a human friendly usage message to the terminal.

    :param text: The usage message to print (a string).

    This function does two things:

    1. If :data:`sys.stdout` is connected to a terminal (see
       :func:`connected_to_terminal()`) then the usage message is formatted
       using :func:`.format_usage()`.
    2. The usage message is shown using a pager (see :func:`show_pager()`).
    """
    ...
def warning(text, *args, **kw) -> None:
    """
    Show a warning message on the terminal.

    For details about argument handling please refer to
    :func:`~humanfriendly.text.format()`.

    Renders the message using :func:`~humanfriendly.text.format()` and writes
    the resulting string (followed by a newline) to :data:`sys.stderr` using
    :func:`auto_encode()`.

    If :data:`sys.stderr` is connected to a terminal that supports colors,
    :func:`ansi_wrap()` is used to color the message in a red font (to make
    the warning stand out from surrounding text).
    """
    ...
