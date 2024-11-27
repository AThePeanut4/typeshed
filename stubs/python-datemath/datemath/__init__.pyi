from datetime import datetime

import arrow

from .helpers import DateMathException as DateMathException, parse as parse

def dm(
    expr: str, *, now: arrow.Arrow | None = ..., tz: str = ..., type: str | None = ..., roundDown: bool = ...
) -> arrow.Arrow:
    """does our datemath and returns an arrow object """
    ...
def datemath(
    expr: str, *, now: arrow.Arrow | None = ..., tz: str = ..., type: str | None = ..., roundDown: bool = ...
) -> datetime:
    """does our datemath and returns a datetime object """
    ...
