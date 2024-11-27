"""Translate an ics file's events to a different timezone."""

from collections.abc import Sequence

def change_tz(cal, new_timezone, default, utc_only: bool = False, utc_tz=...) -> None:
    """
    Change the timezone of the specified component.

    Args:
        cal (Component): the component to change
        new_timezone (tzinfo): the timezone to change to
        default (tzinfo): a timezone to assume if the dtstart or dtend in cal doesn't have an existing timezone
        utc_only (bool): only convert dates that are in utc
        utc_tz (tzinfo): the tzinfo to compare to for UTC when processing utc_only=True
    """
    ...
def show_timezones() -> None: ...
def convert_events(utc_only: bool, args: Sequence[str]) -> None: ...
def main() -> None: ...

version: str

def get_options(): ...
