from _typeshed import Incomplete

CS_ESCAPE: Incomplete
FIRST_ELEMENT: Incomplete

def make_charset(letters): ...
def regex_opt_inner(strings, open_paren):
    """Return a regex that matches any string in the sorted list of strings."""
    ...
def regex_opt(strings, prefix: str = "", suffix: str = ""):
    """
    Return a compiled regex that matches any string in the given list.

    The strings to match must be literal strings, not regexes.  They will be
    regex-escaped.

    *prefix* and *suffix* are pre- and appended to the final regex.
    """
    ...
