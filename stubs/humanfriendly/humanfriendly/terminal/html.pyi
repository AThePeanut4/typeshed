"""Convert HTML with simple text formatting to text with ANSI escape sequences."""

from _typeshed import Incomplete
from typing import Any

from humanfriendly.compat import HTMLParser

def html_to_ansi(data, callback: Incomplete | None = None):
    """
    Convert HTML with simple text formatting to text with ANSI escape sequences.

    :param data: The HTML to convert (a string).
    :param callback: Optional callback to pass to :class:`HTMLConverter`.
    :returns: Text with ANSI escape sequences (a string).

    Please refer to the documentation of the :class:`HTMLConverter` class for
    details about the conversion process (like which tags are supported) and an
    example with a screenshot.
    """
    ...

class HTMLConverter(HTMLParser):
    """
    Convert HTML with simple text formatting to text with ANSI escape sequences.

    The following text styles are supported:

    - Bold: ``<b>``, ``<strong>`` and ``<span style="font-weight: bold;">``
    - Italic: ``<i>``, ``<em>`` and ``<span style="font-style: italic;">``
    - Strike-through: ``<del>``, ``<s>`` and ``<span style="text-decoration: line-through;">``
    - Underline: ``<ins>``, ``<u>`` and ``<span style="text-decoration: underline">``

    Colors can be specified as follows:

    - Foreground color: ``<span style="color: #RRGGBB;">``
    - Background color: ``<span style="background-color: #RRGGBB;">``

    Here's a small demonstration:

    .. code-block:: python

       from humanfriendly.text import dedent
       from humanfriendly.terminal import html_to_ansi

       print(html_to_ansi(dedent('''
         <b>Hello world!</b>
         <i>Is this thing on?</i>
         I guess I can <u>underline</u> or <s>strike-through</s> text?
         And what about <span style="color: red">color</span>?
       ''')))

       rainbow_colors = [
           '#FF0000', '#E2571E', '#FF7F00', '#FFFF00', '#00FF00',
           '#96BF33', '#0000FF', '#4B0082', '#8B00FF', '#FFFFFF',
       ]
       html_rainbow = "".join('<span style="color: %s">o</span>' % c for c in rainbow_colors)
       print(html_to_ansi("Let's try a rainbow: %s" % html_rainbow))

    Here's what the results look like:

      .. image:: images/html-to-ansi.png

    Some more details:

    - Nested tags are supported, within reasonable limits.

    - Text in ``<code>`` and ``<pre>`` tags will be highlighted in a
      different color from the main text (currently this is yellow).

    - ``<a href="URL">TEXT</a>`` is converted to the format "TEXT (URL)" where
      the uppercase symbols are highlighted in light blue with an underline.

    - ``<div>``, ``<p>`` and ``<pre>`` tags are considered block level tags
      and are wrapped in vertical whitespace to prevent their content from
      "running into" surrounding text. This may cause runs of multiple empty
      lines to be emitted. As a *workaround* the :func:`__call__()` method
      will automatically call :func:`.compact_empty_lines()` on the generated
      output before returning it to the caller. Of course this won't work
      when `output` is set to something like :data:`sys.stdout`.

    - ``<br>`` is converted to a single plain text line break.

    Implementation notes:

    - A list of dictionaries with style information is used as a stack where
      new styling can be pushed and a pop will restore the previous styling.
      When new styling is pushed, it is merged with (but overrides) the current
      styling.

    - If you're going to be converting a lot of HTML it might be useful from
      a performance standpoint to re-use an existing :class:`HTMLConverter`
      object for unrelated HTML fragments, in this case take a look at the
      :func:`__call__()` method (it makes this use case very easy).

    .. versionadded:: 4.15
       :class:`humanfriendly.terminal.HTMLConverter` was added to the
       `humanfriendly` package during the initial development of my new
       `chat-archive <https://chat-archive.readthedocs.io/>`_ project, whose
       command line interface makes for a great demonstration of the
       flexibility that this feature provides (hint: check out how the search
       keyword highlighting combines with the regular highlighting).
    """
    BLOCK_TAGS: Any
    callback: Any
    output: Any
    def __init__(self, *args, **kw) -> None:
        """
        Initialize an :class:`HTMLConverter` object.

        :param callback: Optional keyword argument to specify a function that
                         will be called to process text fragments before they
                         are emitted on the output stream. Note that link text
                         and preformatted text fragments are not processed by
                         this callback.
        :param output: Optional keyword argument to redirect the output to the
                       given file-like object. If this is not given a new
                       :class:`~python3:io.StringIO` object is created.
        """
        ...
    def __call__(self, data):
        """
        Reset the parser, convert some HTML and get the text with ANSI escape sequences.

        :param data: The HTML to convert to text (a string).
        :returns: The converted text (only in case `output` is
                  a :class:`~python3:io.StringIO` object).
        """
        ...
    @property
    def current_style(self):
        """Get the current style from the top of the stack (a dictionary)."""
        ...
    stack: Any
    def close(self) -> None:
        """
        Close previously opened ANSI escape sequences.

        This method overrides the same method in the superclass to ensure that
        an :data:`.ANSI_RESET` code is emitted when parsing reaches the end of
        the input but a style is still active. This is intended to prevent
        malformed HTML from messing up terminal output.
        """
        ...
    def emit_style(self, style: Incomplete | None = None) -> None:
        """
        Emit an ANSI escape sequence for the given or current style to the output stream.

        :param style: A dictionary with arguments for :func:`.ansi_style()` or
                      :data:`None`, in which case the style at the top of the
                      stack is emitted.
        """
        ...
    def handle_charref(self, value) -> None:
        """
        Process a decimal or hexadecimal numeric character reference.

        :param value: The decimal or hexadecimal value (a string).
        """
        ...
    link_text: Any
    def handle_data(self, data) -> None:
        """
        Process textual data.

        :param data: The decoded text (a string).
        """
        ...
    def handle_endtag(self, tag) -> None:
        """
        Process the end of an HTML tag.

        :param tag: The name of the tag (a string).
        """
        ...
    def handle_entityref(self, name) -> None:
        """
        Process a named character reference.

        :param name: The name of the character reference (a string).
        """
        ...
    link_url: Any
    def handle_starttag(self, tag, attrs) -> None:
        """
        Process the start of an HTML tag.

        :param tag: The name of the tag (a string).
        :param attrs: A list of tuples with two strings each.
        """
        ...
    def normalize_url(self, url):
        """
        Normalize a URL to enable string equality comparison.

        :param url: The URL to normalize (a string).
        :returns: The normalized URL (a string).
        """
        ...
    def parse_color(self, value):
        """
        Convert a CSS color to something that :func:`.ansi_style()` understands.

        :param value: A string like ``rgb(1,2,3)``, ``#AABBCC`` or ``yellow``.
        :returns: A color value supported by :func:`.ansi_style()` or :data:`None`.
        """
        ...
    def push_styles(self, **changes) -> None:
        """
        Push new style information onto the stack.

        :param changes: Any keyword arguments are passed on to :func:`.ansi_style()`.

        This method is a helper for :func:`handle_starttag()`
        that does the following:

        1. Make a copy of the current styles (from the top of the stack),
        2. Apply the given `changes` to the copy of the current styles,
        3. Add the new styles to the stack,
        4. Emit the appropriate ANSI escape sequence to the output stream.
        """
        ...
    def render_url(self, url):
        """
        Prepare a URL for rendering on the terminal.

        :param url: The URL to simplify (a string).
        :returns: The simplified URL (a string).

        This method pre-processes a URL before rendering on the terminal. The
        following modifications are made:

        - The ``mailto:`` prefix is stripped.
        - Spaces are converted to ``%20``.
        - A trailing parenthesis is converted to ``%29``.
        """
        ...
    preformatted_text_level: int
    def reset(self) -> None:
        """
        Reset the state of the HTML parser and ANSI converter.

        When `output` is a :class:`~python3:io.StringIO` object a new
        instance will be created (and the old one garbage collected).
        """
        ...
    def urls_match(self, a, b):
        """
        Compare two URLs for equality using :func:`normalize_url()`.

        :param a: A string containing a URL.
        :param b: A string containing a URL.
        :returns: :data:`True` if the URLs are the same, :data:`False` otherwise.

        This method is used by :func:`handle_endtag()` to omit the URL of a
        hyperlink (``<a href="...">``) when the link text is that same URL.
        """
        ...
