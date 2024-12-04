"""
Parsing and reformatting of usage messages.

The :mod:`~humanfriendly.usage` module parses and reformats usage messages:

- The :func:`format_usage()` function takes a usage message and inserts ANSI
  escape sequences that highlight items of special significance like command
  line options, meta variables, etc. The resulting usage message is (intended
  to be) easier to read on a terminal.

- The :func:`render_usage()` function takes a usage message and rewrites it to
  reStructuredText_ suitable for inclusion in the documentation of a Python
  package. This provides a DRY solution to keeping a single authoritative
  definition of the usage message while making it easily available in
  documentation. As a cherry on the cake it's not just a pre-formatted dump of
  the usage message but a nicely formatted reStructuredText_ fragment.

- The remaining functions in this module support the two functions above.

Usage messages in general are free format of course, however the functions in
this module assume a certain structure from usage messages in order to
successfully parse and reformat them, refer to :func:`parse_usage()` for
details.

.. _DRY: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
.. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
"""

USAGE_MARKER: str

def format_usage(usage_text):
    """
    Highlight special items in a usage message.

    :param usage_text: The usage message to process (a string).
    :returns: The usage message with special items highlighted.

    This function highlights the following special items:

    - The initial line of the form "Usage: ..."
    - Short and long command line options
    - Environment variables
    - Meta variables (see :func:`find_meta_variables()`)

    All items are highlighted in the color defined by
    :data:`.HIGHLIGHT_COLOR`.
    """
    ...
def find_meta_variables(usage_text):
    """
    Find the meta variables in the given usage message.

    :param usage_text: The usage message to parse (a string).
    :returns: A list of strings with any meta variables found in the usage
              message.

    When a command line option requires an argument, the convention is to
    format such options as ``--option=ARG``. The text ``ARG`` in this example
    is the meta variable.
    """
    ...
def parse_usage(text):
    """
    Parse a usage message by inferring its structure (and making some assumptions :-).

    :param text: The usage message to parse (a string).
    :returns: A tuple of two lists:

              1. A list of strings with the paragraphs of the usage message's
                 "introduction" (the paragraphs before the documentation of the
                 supported command line options).

              2. A list of strings with pairs of command line options and their
                 descriptions: Item zero is a line listing a supported command
                 line option, item one is the description of that command line
                 option, item two is a line listing another supported command
                 line option, etc.

    Usage messages in general are free format of course, however
    :func:`parse_usage()` assume a certain structure from usage messages in
    order to successfully parse them:

    - The usage message starts with a line ``Usage: ...`` that shows a symbolic
      representation of the way the program is to be invoked.

    - After some free form text a line ``Supported options:`` (surrounded by
      empty lines) precedes the documentation of the supported command line
      options.

    - The command line options are documented as follows::

        -v, --verbose

          Make more noise.

      So all of the variants of the command line option are shown together on a
      separate line, followed by one or more paragraphs describing the option.

    - There are several other minor assumptions, but to be honest I'm not sure if
      anyone other than me is ever going to use this functionality, so for now I
      won't list every intricate detail :-).

      If you're curious anyway, refer to the usage message of the `humanfriendly`
      package (defined in the :mod:`humanfriendly.cli` module) and compare it with
      the usage message you see when you run ``humanfriendly --help`` and the
      generated usage message embedded in the readme.

      Feel free to request more detailed documentation if you're interested in
      using the :mod:`humanfriendly.usage` module outside of the little ecosystem
      of Python packages that I have been building over the past years.
    """
    ...
def render_usage(text):
    """
    Reformat a command line program's usage message to reStructuredText_.

    :param text: The plain text usage message (a string).
    :returns: The usage message rendered to reStructuredText_ (a string).
    """
    ...
def inject_usage(module_name) -> None:
    """
    Use cog_ to inject a usage message into a reStructuredText_ file.

    :param module_name: The name of the module whose ``__doc__`` attribute is
                        the source of the usage message (a string).

    This simple wrapper around :func:`render_usage()` makes it very easy to
    inject a reformatted usage message into your documentation using cog_. To
    use it you add a fragment like the following to your ``*.rst`` file::

       .. [[[cog
       .. from humanfriendly.usage import inject_usage
       .. inject_usage('humanfriendly.cli')
       .. ]]]
       .. [[[end]]]

    The lines in the fragment above are single line reStructuredText_ comments
    that are not copied to the output. Their purpose is to instruct cog_ where
    to inject the reformatted usage message. Once you've added these lines to
    your ``*.rst`` file, updating the rendered usage message becomes really
    simple thanks to cog_:

    .. code-block:: sh

       $ cog.py -r README.rst

    This will inject or replace the rendered usage message in your
    ``README.rst`` file with an up to date copy.

    .. _cog: http://nedbatchelder.com/code/cog/
    """
    ...
