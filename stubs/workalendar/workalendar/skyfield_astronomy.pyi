"""Astronomical functions"""

from _typeshed import Incomplete

hour: Incomplete
minute: Incomplete
second: Incomplete
newton_precision: Incomplete

def calculate_equinoxes(year, timezone: str = ...):
    """calculate equinox with time zone """
    ...
def get_current_longitude(current_date, earth, sun):
    """Return the ecliptic longitude, in radians."""
    ...
def newton(f, x0, x1, precision=..., **func_kwargs):
    """
    Return an x-value at which the given function reaches zero.

    Stops and declares victory once the x-value is within ``precision``
    of the solution, which defaults to a half-second of clock time.
    """
    ...
def newton_angle_function(t, ts, target_angle, body1, body2):
    """
    Compute the longitude of body2 relative to body1

    In our case, it's Earth & Sun, but it could be used as any other
    combination of solar system planets/bodies.
    """
    ...
def solar_term(year, degrees, timezone: str = ...):
    """
    Returns the date of the solar term for the given longitude
    and the given year.

    Solar terms are used for Chinese and Taiwanese holidays
    (e.g. Qingming Festival in Taiwan).

    More information:
    - https://en.wikipedia.org/wiki/Solar_term
    - https://en.wikipedia.org/wiki/Qingming

    This function is adapted from the following topic:
    https://answers.launchpad.net/pyephem/+question/110832
    """
    ...
