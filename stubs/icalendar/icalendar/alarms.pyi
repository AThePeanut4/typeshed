"""
Compute the times and states of alarms.

This takes different calendar software into account and the RFC 9074 (Alarm Extension).

- RFC 9074 defines an ACKNOWLEDGED property in the VALARM.
- Outlook does not export VALARM information.
- Google Calendar uses the DTSTAMP to acknowledge the alarms.
- Thunderbird snoozes the alarms with a X-MOZ-SNOOZE-TIME attribute in the event.
- Thunderbird acknowledges the alarms with a X-MOZ-LASTACK attribute in the event.
- Etar deletes alarms that are acknowledged.
- Nextcloud's Webinterface does not do anything with the alarms when the time passes.
"""

import datetime
from typing_extensions import TypeAlias

from .cal import Alarm, Event, Todo
from .error import (
    ComponentEndMissing as ComponentEndMissing,
    ComponentStartMissing as ComponentStartMissing,
    IncompleteAlarmInformation as IncompleteAlarmInformation,
    LocalTimezoneMissing as LocalTimezoneMissing,
)

__all__ = ["Alarms", "AlarmTime", "IncompleteAlarmInformation", "ComponentEndMissing", "ComponentStartMissing"]

Parent: TypeAlias = Event | Todo

class AlarmTime:
    """An alarm time with all the information."""
    def __init__(
        self,
        alarm: Alarm,
        trigger: datetime.datetime,
        acknowledged_until: datetime.datetime | None = None,
        snoozed_until: datetime.datetime | None = None,
        parent: Parent | None = None,
    ) -> None: ...
    @property
    def acknowledged(self) -> datetime.datetime | None:
        """
        The time in UTC at which this alarm was last acknowledged.

        If the alarm was not acknowledged (dismissed), then this is None.
        """
        ...
    @property
    def alarm(self) -> Alarm:
        """The alarm component."""
        ...
    @property
    def parent(self) -> Parent | None:
        """
        This is the component that contains the alarm.

        This is None if you did not use Alarms.set_component().
        """
        ...
    def is_active(self) -> bool:
        """
        Whether this alarm is active (True) or acknowledged (False).

        For example, in some calendar software, this is True until the user looks
        at the alarm message and clicked the dismiss button.

        Alarms can be in local time (without a timezone).
        To calculate if the alarm really happened, we need it to be in a timezone.
        If a timezone is required but not given, we throw an IncompleteAlarmInformation.
        """
        ...
    @property
    def trigger(self) -> datetime.date:
        """
        This is the time to trigger the alarm.

        If the alarm has been snoozed, this can differ from the TRIGGER property.
        """
        ...

class Alarms:
    def __init__(self, component: Alarm | Event | Todo | None = None) -> None: ...
    def add_component(self, component: Alarm | Parent) -> None: ...
    def set_parent(self, parent: Parent) -> None: ...
    def add_alarm(self, alarm: Alarm) -> None: ...
    def set_start(self, dt: datetime.date | None) -> None: ...
    def set_end(self, dt: datetime.date | None) -> None: ...
    def acknowledge_until(self, dt: datetime.date | None) -> None: ...
    def snooze_until(self, dt: datetime.date | None) -> None: ...
    def set_local_timezone(self, tzinfo: datetime.tzinfo | str | None) -> None: ...
    @property
    def times(self) -> list[AlarmTime]:
        """
        Compute and return the times of the alarms given.

        If the information for calculation is incomplete, this will raise a
        IncompleteAlarmInformation exception.

        Please make sure to set all the required parameters before calculating.
        If you forget to set the acknowledged times, that is not problem.
        """
        ...
    @property
    def active(self) -> list[AlarmTime]:
        """
        The alarm times that are still active and not acknowledged.

        This considers snoozed alarms.

        Alarms can be in local time (without a timezone).
        To calculate if the alarm really happened, we need it to be in a timezone.
        If a timezone is required but not given, we throw an IncompleteAlarmInformation.
        """
        ...
