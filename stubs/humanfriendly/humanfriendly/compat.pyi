"""
Compatibility with Python 2 and 3.

This module exposes aliases and functions that make it easier to write Python
code that is compatible with Python 2 and Python 3.

.. data:: basestring

   Alias for :func:`python2:basestring` (in Python 2) or :class:`python3:str`
   (in Python 3). See also :func:`is_string()`.

.. data:: HTMLParser

   Alias for :class:`python2:HTMLParser.HTMLParser` (in Python 2) or
   :class:`python3:html.parser.HTMLParser` (in Python 3).

.. data:: interactive_prompt

   Alias for :func:`python2:raw_input()` (in Python 2) or
   :func:`python3:input()` (in Python 3).

.. data:: StringIO

   Alias for :class:`python2:StringIO.StringIO` (in Python 2) or
   :class:`python3:io.StringIO` (in Python 3).

.. data:: unicode

   Alias for :func:`python2:unicode` (in Python 2) or :class:`python3:str` (in
   Python 3). See also :func:`coerce_string()`.

.. data:: monotonic

   Alias for :func:`python3:time.monotonic()` (in Python 3.3 and higher) or
   `monotonic.monotonic()` (a `conditional dependency
   <https://pypi.org/project/monotonic/>`_ on older Python versions).
"""

from html.parser import HTMLParser as HTMLParser
from io import StringIO as StringIO

unicode = str
unichr = chr
basestring = str
interactive_prompt = input

def coerce_string(value):
    """
    Coerce any value to a Unicode string (:func:`python2:unicode` in Python 2 and :class:`python3:str` in Python 3).

    :param value: The value to coerce.
    :returns: The value coerced to a Unicode string.
    """
    ...
def is_string(value):
    """
    Check if a value is a :func:`python2:basestring` (in Python 2) or :class:`python3:str` (in Python 3) object.

    :param value: The value to check.
    :returns: :data:`True` if the value is a string, :data:`False` otherwise.
    """
    ...
def is_unicode(value):
    """
    Check if a value is a :func:`python2:unicode` (in Python 2) or :class:`python2:str` (in Python 3) object.

    :param value: The value to check.
    :returns: :data:`True` if the value is a Unicode string, :data:`False` otherwise.
    """
    ...
def on_macos():
    """
    Check if we're running on Apple MacOS.

    :returns: :data:`True` if running MacOS, :data:`False` otherwise.
    """
    ...
def on_windows():
    """
    Check if we're running on the Microsoft Windows OS.

    :returns: :data:`True` if running Windows, :data:`False` otherwise.
    """
    ...
