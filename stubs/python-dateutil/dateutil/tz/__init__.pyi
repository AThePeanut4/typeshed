"""
This module offers timezone implementations subclassing the abstract
:py:class:`datetime.tzinfo` type. There are classes to handle tzfile format
files (usually are in :file:`/etc/localtime`, :file:`/usr/share/zoneinfo`,
etc), TZ environment string (in all known formats), given ranges (with help
from relative deltas), local machine timezone, fixed offset timezone, and UTC
timezone.
"""

from .tz import (
    datetime_ambiguous as datetime_ambiguous,
    datetime_exists as datetime_exists,
    gettz as gettz,
    resolve_imaginary as resolve_imaginary,
    tzfile as tzfile,
    tzical as tzical,
    tzlocal as tzlocal,
    tzoffset as tzoffset,
    tzrange as tzrange,
    tzstr as tzstr,
    tzutc as tzutc,
)

UTC: tzutc
