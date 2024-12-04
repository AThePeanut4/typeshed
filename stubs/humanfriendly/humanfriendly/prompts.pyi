"""
Interactive terminal prompts.

The :mod:`~humanfriendly.prompts` module enables interaction with the user
(operator) by asking for confirmation (:func:`prompt_for_confirmation()`) and
asking to choose from a list of options (:func:`prompt_for_choice()`). It works
by rendering interactive prompts on the terminal.
"""

from _typeshed import Incomplete
from typing import Any

MAX_ATTEMPTS: int
logger: Any

def prompt_for_confirmation(question, default: Incomplete | None = None, padding: bool = True):
    """
    Prompt the user for confirmation.

    :param question: The text that explains what the user is confirming (a string).
    :param default: The default value (a boolean) or :data:`None`.
    :param padding: Refer to the documentation of :func:`prompt_for_input()`.
    :returns: - If the user enters 'yes' or 'y' then :data:`True` is returned.
              - If the user enters 'no' or 'n' then :data:`False`  is returned.
              - If the user doesn't enter any text or standard input is not
                connected to a terminal (which makes it impossible to prompt
                the user) the value of the keyword argument ``default`` is
                returned (if that value is not :data:`None`).
    :raises: - Any exceptions raised by :func:`retry_limit()`.
             - Any exceptions raised by :func:`prompt_for_input()`.

    When `default` is :data:`False` and the user doesn't enter any text an
    error message is printed and the prompt is repeated:

    >>> prompt_for_confirmation("Are you sure?")
     <BLANKLINE>
     Are you sure? [y/n]
     <BLANKLINE>
     Error: Please enter 'yes' or 'no' (there's no default choice).
     <BLANKLINE>
     Are you sure? [y/n]

    The same thing happens when the user enters text that isn't recognized:

    >>> prompt_for_confirmation("Are you sure?")
     <BLANKLINE>
     Are you sure? [y/n] about what?
     <BLANKLINE>
     Error: Please enter 'yes' or 'no' (the text 'about what?' is not recognized).
     <BLANKLINE>
     Are you sure? [y/n]
    """
    ...
def prompt_for_choice(choices, default: Incomplete | None = None, padding: bool = True):
    """
    Prompt the user to select a choice from a group of options.

    :param choices: A sequence of strings with available options.
    :param default: The default choice if the user simply presses Enter
                    (expected to be a string, defaults to :data:`None`).
    :param padding: Refer to the documentation of
                    :func:`~humanfriendly.prompts.prompt_for_input()`.
    :returns: The string corresponding to the user's choice.
    :raises: - :exc:`~exceptions.ValueError` if `choices` is an empty sequence.
             - Any exceptions raised by
               :func:`~humanfriendly.prompts.retry_limit()`.
             - Any exceptions raised by
               :func:`~humanfriendly.prompts.prompt_for_input()`.

    When no options are given an exception is raised:

    >>> prompt_for_choice([])
    Traceback (most recent call last):
      File "humanfriendly/prompts.py", line 148, in prompt_for_choice
        raise ValueError("Can't prompt for choice without any options!")
    ValueError: Can't prompt for choice without any options!

    If a single option is given the user isn't prompted:

    >>> prompt_for_choice(['only one choice'])
    'only one choice'

    Here's what the actual prompt looks like by default:

    >>> prompt_for_choice(['first option', 'second option'])
    <BLANKLINE>
      1. first option
      2. second option
    <BLANKLINE>
     Enter your choice as a number or unique substring (Control-C aborts): second
    <BLANKLINE>
    'second option'

    If you don't like the whitespace (empty lines and indentation):

    >>> prompt_for_choice(['first option', 'second option'], padding=False)
     1. first option
     2. second option
    Enter your choice as a number or unique substring (Control-C aborts): first
    'first option'
    """
    ...
def prompt_for_input(question, default: Incomplete | None = None, padding: bool = True, strip: bool = True):
    """
    Prompt the user for input (free form text).

    :param question: An explanation of what is expected from the user (a string).
    :param default: The return value if the user doesn't enter any text or
                    standard input is not connected to a terminal (which
                    makes it impossible to prompt the user).
    :param padding: Render empty lines before and after the prompt to make it
                    stand out from the surrounding text? (a boolean, defaults
                    to :data:`True`)
    :param strip: Strip leading/trailing whitespace from the user's reply?
    :returns: The text entered by the user (a string) or the value of the
              `default` argument.
    :raises: - :exc:`~exceptions.KeyboardInterrupt` when the program is
               interrupted_ while the prompt is active, for example
               because the user presses Control-C_.
             - :exc:`~exceptions.EOFError` when reading from `standard input`_
               fails, for example because the user presses Control-D_ or
               because the standard input stream is redirected (only if
               `default` is :data:`None`).

    .. _Control-C: https://en.wikipedia.org/wiki/Control-C#In_command-line_environments
    .. _Control-D: https://en.wikipedia.org/wiki/End-of-transmission_character#Meaning_in_Unix
    .. _interrupted: https://en.wikipedia.org/wiki/Unix_signal#SIGINT
    .. _standard input: https://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29
    """
    ...
def prepare_prompt_text(prompt_text, **options):
    """
    Wrap a text to be rendered as an interactive prompt in ANSI escape sequences.

    :param prompt_text: The text to render on the prompt (a string).
    :param options: Any keyword arguments are passed on to :func:`.ansi_wrap()`.
    :returns: The resulting prompt text (a string).

    ANSI escape sequences are only used when the standard output stream is
    connected to a terminal. When the standard input stream is connected to a
    terminal any escape sequences are wrapped in "readline hints".
    """
    ...
def prepare_friendly_prompts() -> None:
    """
    Make interactive prompts more user friendly.

    The prompts presented by :func:`python2:raw_input()` (in Python 2) and
    :func:`python3:input()` (in Python 3) are not very user friendly by
    default, for example the cursor keys (:kbd:`←`, :kbd:`↑`, :kbd:`→` and
    :kbd:`↓`) and the :kbd:`Home` and :kbd:`End` keys enter characters instead
    of performing the action you would expect them to. By simply importing the
    :mod:`readline` module these prompts become much friendlier (as mentioned
    in the Python standard library documentation).

    This function is called by the other functions in this module to enable
    user friendly prompts.
    """
    ...
def retry_limit(limit=10) -> None:
    """
    Allow the user to provide valid input up to `limit` times.

    :param limit: The maximum number of attempts (a number,
                  defaults to :data:`MAX_ATTEMPTS`).
    :returns: A generator of numbers starting from one.
    :raises: :exc:`TooManyInvalidReplies` when an interactive prompt
             receives repeated invalid input (:data:`MAX_ATTEMPTS`).

    This function returns a generator for interactive prompts that want to
    repeat on invalid input without getting stuck in infinite loops.
    """
    ...

class TooManyInvalidReplies(Exception):
    """Raised by interactive prompts when they've received too many invalid inputs."""
    ...
