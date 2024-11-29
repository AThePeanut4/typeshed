"""
A basic utility module for parsing math like strings relating to dates

This is inspired by Date Math features in elasticsearch and aims to replicate the same functionality for python.

DateMath (datemath or dm) suppor addition, subtraction and rounding at various granularities of "units" (a map of units to their shorthand is below for reference).
Expressions can be chanied together and are read left to right.  '+' and '-' denote addition and subtraction while '/' denotes 'round', in this case is a 'round down' or floor.
Round requires a unit (/d), while addition and subtraction require an integer value and a unit (+1d).  Whitespace is not allowed in the expression.  Absolute datetimes with datemath 
can be made as well, with the datetime and datemath expressions delinated by '||' - example '2015-01-01||+1d' == '2015-01-02'


Maps:

y or Y      =   'year'
M           =   'month'
m           =   'minute'
d or D      =   'day'
w           =   'week'
h or H      =   'hour'
s or S      =   'second'

Examples:

Assuming our datetime is currently: '2016-01-01T00:00:00-00:00'

Expression:                 Result:
now-1h                      2015-12-31T23:00:00+00:00
now-1y                      2015-01-01T00:00:00+00:00
now+1y+2d                   2017-01-03T00:00:00+00:00
now+12h                     2016-01-01T12:00:00+00:00
now+1d/d                    2016-01-03T00:00:00+00:00
+2h                         2016-01-01T02:00:00+00:00
+1h/h                       2016-01-01T02:00:00+00:00
now+1w/w                    2016-01-11T00:00:00+00:00
now/d+7d+12h                2016-01-08T12:00:00+00:00
2016-01-01||+1d             2016-01-02T00:00:00+00:00
2015-01-01||+2w             2015-01-15T00:00:00+00:00
"""

from _typeshed import Incomplete

import arrow

class DateMathException(Exception): ...

def parse(
    expression: str, now: arrow.Arrow | None = None, tz: str = "UTC", type: str | None = None, roundDown: bool = True
) -> arrow.Arrow:
    """
    the main meat and potatoes of this this whole thing
    takes our datemath expression and does our date math
    :param expression - the datemath expression
    :param now - what time is now; when will now be then?  soon
    :param type - if we are dealing with a arrow or datetime object
    :param roundDown - wether or not we should round up or round down on this.  default is roundDown=True, which means if it was 12:00:00, `/d` would be '00:00:00', and with roundDown=False, `/d` would be '29:59:59'
    """
    ...
def __getattr__(name: str) -> Incomplete: ...
