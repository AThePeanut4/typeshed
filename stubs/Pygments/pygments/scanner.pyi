from _typeshed import Incomplete

class EndOfText(RuntimeError):
    """
    Raise if end of text is reached and the user
    tried to call a match function.
    """
    ...

class Scanner:
    data: Incomplete
    data_length: Incomplete
    start_pos: int
    pos: int
    flags: Incomplete
    last: Incomplete
    match: Incomplete
    def __init__(self, text, flags: int = 0) -> None: ...
    @property
    def eos(self):
        """`True` if the scanner reached the end of text."""
        ...
    def check(self, pattern):
        """
        Apply `pattern` on the current position and return
        the match object. (Doesn't touch pos). Use this for
        lookahead.
        """
        ...
    def test(self, pattern):
        """
        Apply a pattern on the current position and check
        if it patches. Doesn't touch pos.
        """
        ...
    def scan(self, pattern):
        """
        Scan the text for the given pattern and update pos/match
        and related fields. The return value is a boolean that
        indicates if the pattern matched. The matched value is
        stored on the instance as ``match``, the last value is
        stored as ``last``. ``start_pos`` is the position of the
        pointer before the pattern was matched, ``pos`` is the
        end position.
        """
        ...
    def get_char(self) -> None:
        """Scan exactly one char."""
        ...
