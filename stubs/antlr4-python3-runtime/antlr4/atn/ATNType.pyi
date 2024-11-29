from enum import IntEnum

class ATNType(IntEnum):
    """An enumeration."""
    LEXER = 0
    PARSER = 1
    @classmethod
    def fromOrdinal(cls, i: int): ...
