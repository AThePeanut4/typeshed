"""Event Log Utilities - helper for win32evtlog.pyd"""

from _typeshed import Incomplete
from collections.abc import Iterable

import _win32typing
import win32api

error = win32api.error
langid: Incomplete

def AddSourceToRegistry(
    appName, msgDLL=None, eventLogType: str = "Application", eventLogFlags=None, categoryDLL=None, categoryCount: int = 0
) -> None: ...
def RemoveSourceFromRegistry(appName, eventLogType: str = ...) -> None: ...
def ReportEvent(
    appName: str,
    eventID: int,
    eventCategory: int = ...,
    eventType: int = ...,
    strings: Iterable[str] | None = ...,
    data: bytes | None = ...,
    sid: _win32typing.PySID | None = ...,
) -> None:
    """Report an event for a previously added event source."""
    ...
def FormatMessage(eventLogRecord: _win32typing.PyEventLogRecord, logType: str = ...):
    """
    Given a tuple from ReadEventLog, and optionally where the event
    record came from, load the message, and process message inserts.

    Note that this function may raise win32api.error.  See also the
    function SafeFormatMessage which will return None if the message can
    not be processed.
    """
    ...
def SafeFormatMessage(eventLogRecord, logType: Incomplete | None = ...):
    """
    As for FormatMessage, except returns an error message if
    the message can not be processed.
    """
    ...
def FeedEventLogRecords(feeder, machineName: Incomplete | None = ..., logName: str = ..., readFlags: Incomplete | None = ...): ...
