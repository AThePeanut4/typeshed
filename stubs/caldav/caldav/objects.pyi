"""
A "DAV object" is anything we get from the caldav server or push into the
caldav server, notably principal, calendars and calendar events.

(This file has become huge and will be split up prior to the next
release.  I think it makes sense moving the CalendarObjectResource
class hierarchy into a separate file)
"""

import datetime
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Callable, Container, Iterable, Iterator, Mapping, Sequence
from typing import Any, Literal, TypeVar, overload
from typing_extensions import Self, TypeAlias
from urllib.parse import ParseResult, SplitResult

from vobject.base import VBase

from .davclient import DAVClient
from .elements.cdav import CalendarData, CalendarQuery, CompFilter, ScheduleInboxURL, ScheduleOutboxURL
from .lib.url import URL

_CC = TypeVar("_CC", bound=CalendarObjectResource)
# Actually "type[Todo] | type[Event] | type[Journal]", but mypy doesn't like that.
_CompClass: TypeAlias = type[CalendarObjectResource]
_VCalAddress: TypeAlias = Incomplete  # actually icalendar.vCalAddress

class DAVObject:
    """
    Base class for all DAV objects.  Can be instantiated by a client
    and an absolute or relative URL, or from the parent object.
    """
    id: str | None
    url: URL | None
    client: DAVClient | None
    parent: DAVObject | None
    name: str | None
    props: Mapping[Incomplete, Incomplete]
    extra_init_options: dict[str, Incomplete]
    def __init__(
        self,
        client: DAVClient | None = None,
        url: str | ParseResult | SplitResult | URL | None = None,
        parent: DAVObject | None = None,
        name: str | None = None,
        id: str | None = None,
        props: Mapping[Incomplete, Incomplete] | None = None,
        **extra,
    ) -> None:
        """
        Default constructor.

        Parameters:
         * client: A DAVClient instance
         * url: The url for this object.  May be a full URL or a relative URL.
         * parent: The parent object - used when creating objects
         * name: A displayname - to be removed in 1.0, see https://github.com/python-caldav/caldav/issues/128 for details
         * props: a dict with known properties for this object (as of 2020-12, only used for etags, and only when fetching CalendarObjectResource using the .objects or .objects_by_sync_token methods).
         * id: The resource id (UID for an Event)
        """
        ...
    @property
    def canonical_url(self) -> str: ...
    def children(self, type: str | None = None) -> list[tuple[URL, Incomplete, Incomplete]]:
        """
        List children, using a propfind (resourcetype) on the parent object,
        at depth = 1.

        TODO: This is old code, it's querying for DisplayName and
        ResourceTypes prop and returning a tuple of those.  Those two
        are relatively arbitrary.  I think it's mostly only calendars
        having DisplayName, but it may make sense to ask for the
        children of a calendar also as an alternative way to get all
        events?  It should be redone into a more generic method, and
        it should probably return a dict rather than a tuple.  We
        should also look over to see if there is any code duplication.
        """
        ...
    def get_property(self, prop, use_cached: bool = False, **passthrough) -> Incomplete | None: ...
    def get_properties(self, props=None, depth: int = 0, parse_response_xml: bool = True, parse_props: bool = True): ...
    def set_properties(self, props=None) -> Self: ...
    def save(self) -> Self: ...
    def delete(self) -> None: ...

class CalendarSet(DAVObject):
    """A CalendarSet is a set of calendars."""
    def calendars(self) -> list[Calendar]:
        """
        List all calendar collections in this set.

        Returns:
         * [Calendar(), ...]
        """
        ...
    def make_calendar(
        self, name: str | None = None, cal_id: str | None = None, supported_calendar_component_set=None
    ) -> Calendar: ...
    def calendar(self, name: str | None = None, cal_id: str | None = None) -> Calendar: ...

class Principal(DAVObject):
    """
    This class represents a DAV Principal. It doesn't do much, except
    keep track of the URLs for the calendar-home-set, etc.

    A principal MUST have a non-empty DAV:displayname property
    (defined in Section 13.2 of [RFC2518]),
    and a DAV:resourcetype property (defined in Section 13.9 of [RFC2518]).
    Additionally, a principal MUST report the DAV:principal XML element
    in the value of the DAV:resourcetype property.

    (TODO: the resourcetype is actually never checked, and the DisplayName
    is not stored anywhere)
    """
    def __init__(self, client: DAVClient | None = None, url: str | ParseResult | SplitResult | URL | None = None) -> None:
        """
        Returns a Principal.

        Parameters:
         * client: a DAVClient() object
         * url: Deprecated - for backwards compatibility purposes only.

        If url is not given, deduct principal path as well as calendar home set
        path from doing propfinds.
        """
        ...
    def calendars(self) -> list[Calendar]:
        """Return the principials calendars"""
        ...
    def make_calendar(
        self, name: str | None = None, cal_id: str | None = None, supported_calendar_component_set=None
    ) -> Calendar: ...
    def calendar(self, name: str | None = None, cal_id: str | None = None, cal_url: str | None = None) -> Calendar: ...
    def get_vcal_address(self) -> _VCalAddress: ...
    calendar_home_set: CalendarSet  # can also be set to anything URL.objectify() accepts
    def freebusy_request(self, dtstart, dtend, attendees): ...
    def calendar_user_address_set(self) -> list[str]:
        """defined in RFC6638"""
        ...
    def schedule_inbox(self) -> ScheduleInbox: ...
    def schedule_outbox(self) -> ScheduleOutbox: ...

class Calendar(DAVObject):
    """
    The `Calendar` object is used to represent a calendar collection.
    Refer to the RFC for details:
    https://tools.ietf.org/html/rfc4791#section-5.3.1
    """
    def get_supported_components(self) -> list[Incomplete]:
        """
        returns a list of component types supported by the calendar, in
        string format (typically ['VJOURNAL', 'VTODO', 'VEVENT'])
        """
        ...
    def save_with_invites(self, ical: str, attendees, **attendeeoptions) -> None:
        """
        sends a schedule request to the server.  Equivalent with save_event, save_todo, etc,
        but the attendees will be added to the ical object before sending it to the server.
        """
        ...
    def save_event(self, ical: str | None = None, no_overwrite: bool = False, no_create: bool = False, **ical_data) -> Event:
        """
        Add a new event to the calendar, with the given ical.

        Parameters:
         * ical - ical object (text)
         * no_overwrite - existing calendar objects should not be overwritten
         * no_create - don't create a new object, existing calendar objects should be updated
         * ical_data - passed to lib.vcal.create_ical
        """
        ...
    def save_todo(self, ical: str | None = None, no_overwrite: bool = False, no_create: bool = False, **ical_data) -> Todo:
        """
        Add a new task to the calendar, with the given ical.

        Parameters:
         * ical - ical object (text)
        """
        ...
    def save_journal(
        self, ical: str | None = None, no_overwrite: bool = False, no_create: bool = False, **ical_data
    ) -> Journal:
        """
        Add a new journal entry to the calendar, with the given ical.

        Parameters:
         * ical - ical object (text)
        """
        ...
    add_event = save_event
    add_todo = save_todo
    add_journal = save_journal
    def calendar_multiget(self, event_urls: Iterable[URL]) -> list[Event]:
        """
        get multiple events' data
        @author mtorange@gmail.com
        @type events list of Event
        """
        ...
    def build_date_search_query(
        self,
        start,
        end: datetime.datetime | None = None,
        compfilter: Literal["VEVENT"] | None = "VEVENT",
        expand: bool | Literal["maybe"] = "maybe",
    ):
        """WARNING: DEPRECATED"""
        ...
    @overload
    def date_search(
        self,
        start: datetime.datetime,
        end: datetime.datetime | None = None,
        compfilter: Literal["VEVENT"] = "VEVENT",
        expand: bool | Literal["maybe"] = "maybe",
        verify_expand: bool = False,
    ) -> list[Event]:
        """
        Deprecated.  Use self.search() instead.

        Search events by date in the calendar. Recurring events are
        expanded if they are occurring during the specified time frame
        and if an end timestamp is given.

        Parameters:
         * start = datetime.today().
         * end = same as above.
         * compfilter = defaults to events only.  Set to None to fetch all
           calendar components.
         * expand - should recurrent events be expanded?  (to preserve
           backward-compatibility the default "maybe" will be changed into True
           unless the date_search is open-ended)
         * verify_expand - not in use anymore, but kept for backward compatibility

        Returns:
         * [CalendarObjectResource(), ...]
        """
        ...
    @overload
    def date_search(
        self,
        start: datetime.datetime,
        *,
        compfilter: None,
        expand: bool | Literal["maybe"] = "maybe",
        verify_expand: bool = False,
    ) -> list[CalendarObjectResource]:
        """
        Deprecated.  Use self.search() instead.

        Search events by date in the calendar. Recurring events are
        expanded if they are occurring during the specified time frame
        and if an end timestamp is given.

        Parameters:
         * start = datetime.today().
         * end = same as above.
         * compfilter = defaults to events only.  Set to None to fetch all
           calendar components.
         * expand - should recurrent events be expanded?  (to preserve
           backward-compatibility the default "maybe" will be changed into True
           unless the date_search is open-ended)
         * verify_expand - not in use anymore, but kept for backward compatibility

        Returns:
         * [CalendarObjectResource(), ...]
        """
        ...
    @overload
    def date_search(
        self,
        start: datetime.datetime,
        end: datetime.datetime | None,
        compfilter: None,
        expand: bool | Literal["maybe"] = "maybe",
        verify_expand: bool = False,
    ) -> list[CalendarObjectResource]:
        """
        Deprecated.  Use self.search() instead.

        Search events by date in the calendar. Recurring events are
        expanded if they are occurring during the specified time frame
        and if an end timestamp is given.

        Parameters:
         * start = datetime.today().
         * end = same as above.
         * compfilter = defaults to events only.  Set to None to fetch all
           calendar components.
         * expand - should recurrent events be expanded?  (to preserve
           backward-compatibility the default "maybe" will be changed into True
           unless the date_search is open-ended)
         * verify_expand - not in use anymore, but kept for backward compatibility

        Returns:
         * [CalendarObjectResource(), ...]
        """
        ...
    @overload
    def search(
        self,
        xml: None = None,
        comp_class: None = None,
        todo: bool | None = None,
        include_completed: bool = False,
        sort_keys: Sequence[str] = (),
        split_expanded: bool = True,
        props: list[CalendarData] | None = None,
        **kwargs,
    ) -> list[CalendarObjectResource]:
        """
        Creates an XML query, does a REPORT request towards the
        server and returns objects found, eventually sorting them
        before delivery.

        This method contains some special logics to ensure that it can
        consistently return a list of pending tasks on any server
        implementation.  In the future it may also include workarounds
        and client side filtering to make sure other search results
        are consistent on different server implementations.

        Parameters supported:

        * xml - use this search query, and ignore other filter parameters
        * comp_class - set to event, todo or journal to restrict search to this
          resource type.  Some server implementations require this to be set.
        * todo - sets comp_class to Todo, and restricts search to pending tasks,
          unless the next parameter is set ...
        * include_completed - include completed tasks
        * event - sets comp_class to event
        * text attribute search parameters: category, uid, summary, omment,
          description, location, status
        * no-category, no-summary, etc ... search for objects that does not
          have those attributes.  TODO: WRITE TEST CODE!
        * expand - do server side expanding of recurring events/tasks
        * start, end: do a time range search
        * filters - other kind of filters (in lxml tree format)
        * sort_keys - list of attributes to use when sorting

        not supported yet:
        * negated text match
        * attribute not set
        """
        ...
    @overload
    def search(
        self,
        xml,
        comp_class: type[_CC],
        todo: bool | None = None,
        include_completed: bool = False,
        sort_keys: Sequence[str] = (),
        split_expanded: bool = True,
        props: list[CalendarData] | None = None,
        **kwargs,
    ) -> list[_CC]:
        """
        Creates an XML query, does a REPORT request towards the
        server and returns objects found, eventually sorting them
        before delivery.

        This method contains some special logics to ensure that it can
        consistently return a list of pending tasks on any server
        implementation.  In the future it may also include workarounds
        and client side filtering to make sure other search results
        are consistent on different server implementations.

        Parameters supported:

        * xml - use this search query, and ignore other filter parameters
        * comp_class - set to event, todo or journal to restrict search to this
          resource type.  Some server implementations require this to be set.
        * todo - sets comp_class to Todo, and restricts search to pending tasks,
          unless the next parameter is set ...
        * include_completed - include completed tasks
        * event - sets comp_class to event
        * text attribute search parameters: category, uid, summary, omment,
          description, location, status
        * no-category, no-summary, etc ... search for objects that does not
          have those attributes.  TODO: WRITE TEST CODE!
        * expand - do server side expanding of recurring events/tasks
        * start, end: do a time range search
        * filters - other kind of filters (in lxml tree format)
        * sort_keys - list of attributes to use when sorting

        not supported yet:
        * negated text match
        * attribute not set
        """
        ...
    @overload
    def search(
        self,
        *,
        comp_class: type[_CC],
        todo: bool | None = None,
        include_completed: bool = False,
        sort_keys: Sequence[str] = (),
        split_expanded: bool = True,
        props: list[CalendarData] | None = None,
        **kwargs,
    ) -> list[_CC]:
        """
        Creates an XML query, does a REPORT request towards the
        server and returns objects found, eventually sorting them
        before delivery.

        This method contains some special logics to ensure that it can
        consistently return a list of pending tasks on any server
        implementation.  In the future it may also include workarounds
        and client side filtering to make sure other search results
        are consistent on different server implementations.

        Parameters supported:

        * xml - use this search query, and ignore other filter parameters
        * comp_class - set to event, todo or journal to restrict search to this
          resource type.  Some server implementations require this to be set.
        * todo - sets comp_class to Todo, and restricts search to pending tasks,
          unless the next parameter is set ...
        * include_completed - include completed tasks
        * event - sets comp_class to event
        * text attribute search parameters: category, uid, summary, omment,
          description, location, status
        * no-category, no-summary, etc ... search for objects that does not
          have those attributes.  TODO: WRITE TEST CODE!
        * expand - do server side expanding of recurring events/tasks
        * start, end: do a time range search
        * filters - other kind of filters (in lxml tree format)
        * sort_keys - list of attributes to use when sorting

        not supported yet:
        * negated text match
        * attribute not set
        """
        ...
    def build_search_xml_query(
        self,
        comp_class: _CompClass | None = None,
        todo: bool | None = None,
        ignore_completed1: bool | None = None,
        ignore_completed2: bool | None = None,
        ignore_completed3: bool | None = None,
        event: bool | None = None,
        filters: list[Incomplete] | None = None,
        expand: bool | None = None,
        start: datetime.datetime | None = None,
        end: datetime.datetime | None = None,
        props: list[CalendarData] | None = None,
        *,
        uid=...,
        summary=...,
        comment=...,
        description=...,
        location=...,
        status=...,
        **kwargs: str,
    ) -> tuple[CalendarQuery, _CompClass]:
        """
        This method will produce a caldav search query as an etree object.

        It is primarily to be used from the search method.  See the
        documentation for the search method for more information.
        """
        ...
    def freebusy_request(self, start: datetime.datetime, end: datetime.datetime) -> FreeBusy:
        """
        Search the calendar, but return only the free/busy information.

        Parameters:
         * start = datetime.today().
         * end = same as above.

        Returns:
         * [FreeBusy(), ...]
        """
        ...
    def todos(
        self, sort_keys: Iterable[str] = ("due", "priority"), include_completed: bool = False, sort_key: str | None = None
    ) -> list[Todo]: ...
    def event_by_url(self, href, data=None) -> Event: ...
    def object_by_uid(self, uid: str, comp_filter: CompFilter | None = None, comp_class: _CompClass | None = None) -> Event: ...
    def todo_by_uid(self, uid: str) -> CalendarObjectResource: ...
    def event_by_uid(self, uid: str) -> CalendarObjectResource: ...
    def journal_by_uid(self, uid: str) -> CalendarObjectResource: ...
    event = event_by_uid
    def events(self) -> list[Event]: ...
    def objects_by_sync_token(self, sync_token=None, load_objects: bool = False) -> SynchronizableCalendarObjectCollection: ...
    objects = objects_by_sync_token
    def journals(self) -> list[Journal]:
        """
        List all journals from the calendar.

        Returns:
         * [Journal(), ...]
        """
        ...

class ScheduleMailbox(Calendar):
    """
    RFC6638 defines an inbox and an outbox for handling event scheduling.

    TODO: As ScheduleMailboxes works a bit like calendars, I've chosen
    to inheritate the Calendar class, but this is a bit incorrect, a
    ScheduleMailbox is a collection, but not really a calendar.  We
    should create a common base class for ScheduleMailbox and Calendar
    eventually.
    """
    def __init__(
        self,
        client: DAVClient | None = None,
        principal: Principal | None = None,
        url: str | ParseResult | SplitResult | URL | None = None,
    ) -> None:
        """Will locate the mbox if no url is given"""
        ...
    def get_items(self):
        """
        TODO: work in progress
        TODO: perhaps this belongs to the super class?
        """
        ...

class ScheduleInbox(ScheduleMailbox):
    findprop = ScheduleInboxURL

class ScheduleOutbox(ScheduleMailbox):
    findprop = ScheduleOutboxURL

class SynchronizableCalendarObjectCollection:
    """
    This class may hold a cached snapshot of a calendar, and changes
    in the calendar can easily be copied over through the sync method.

    To create a SynchronizableCalendarObjectCollection object, use
    calendar.objects(load_objects=True)
    """
    def __init__(self, calendar, objects, sync_token) -> None: ...
    def __iter__(self) -> Iterator[Incomplete]: ...
    def __len__(self) -> int: ...
    def objects_by_url(self):
        """returns a dict of the contents of the SynchronizableCalendarObjectCollection, URLs -> objects."""
        ...
    def sync(self) -> tuple[Incomplete, Incomplete]:
        """
        This method will contact the caldav server,
        request all changes from it, and sync up the collection
        """
        ...

class CalendarObjectResource(DAVObject):
    """
    Ref RFC 4791, section 4.1, a "Calendar Object Resource" can be an
    event, a todo-item, a journal entry, or a free/busy entry
    """
    def __init__(
        self,
        client: DAVClient | None = None,
        url: str | ParseResult | SplitResult | URL | None = None,
        data=None,
        parent=None,
        id=None,
        props=None,
    ) -> None: ...
    def add_organizer(self) -> None: ...
    def split_expanded(self) -> list[Self]: ...
    def expand_rrule(self, start: datetime.datetime, end: datetime.datetime) -> None:
        """
        This method will transform the calendar content of the
        event and expand the calendar data from a "master copy" with
        RRULE set and into a "recurrence set" with RECURRENCE-ID set
        and no RRULE set.  The main usage is for client-side expansion
        in case the calendar server does not support server-side
        expansion.  It should be safe to save back to the server, the
        server should recognize it as recurrences and should not edit
        the "master copy".  If doing a `self.load`, the calendar
        content will be replaced with the "master copy".  However, as
        of 2022-10 there is no test code verifying this.

        :param event: Event
        :param start: datetime.datetime
        :param end: datetime.datetime
        """
        ...
    def get_relatives(
        self,
        reltypes: Container[str] | None = None,
        relfilter: Callable[[Any], bool] | None = None,
        fetch_objects: bool = True,
        ignore_missing: bool = True,
    ) -> defaultdict[str, set[str]]:
        """
        By default, loads all objects pointed to by the RELATED-TO
        property and loads the related objects.

        It's possible to filter, either by passing a set or a list of
        acceptable relation types in reltypes, or by passing a lambda
        function in relfilter.

        TODO: Make it possible to  also check up reverse relationships

        TODO: this is partially overlapped by plann.lib._relships_by_type
        in the plann tool.  Should consolidate the code.
        """
        ...
    def add_attendee(self, attendee, no_default_parameters: bool = False, **parameters) -> None:
        """
        For the current (event/todo/journal), add an attendee.

        The attendee can be any of the following:
        * A principal
        * An email address prepended with "mailto:"
        * An email address without the "mailto:"-prefix
        * A two-item tuple containing a common name and an email address
        * (not supported, but planned: an ical text line starting with the word "ATTENDEE")

        Any number of attendee parameters can be given, those will be used
        as defaults unless no_default_parameters is set to True:

        partstat=NEEDS-ACTION
        cutype=UNKNOWN (unless a principal object is given)
        rsvp=TRUE
        role=REQ-PARTICIPANT
        schedule-agent is not set
        """
        ...
    def is_invite_request(self) -> bool: ...
    def accept_invite(self, calendar=None) -> None: ...
    def decline_invite(self, calendar=None) -> None: ...
    def tentatively_accept_invite(self, calendar=None) -> None: ...
    def copy(self, keep_uid: bool = False, new_parent=None) -> Self: ...
    def load(self, only_if_unloaded: bool = False) -> Self: ...
    def change_attendee_status(self, attendee=None, **kwargs) -> None: ...
    def save(
        self,
        no_overwrite: bool = False,
        no_create: bool = False,
        obj_type: str | None = None,
        increase_seqno: bool = True,
        if_schedule_tag_match: bool = False,
    ) -> Self:
        """
        Save the object, can be used for creation and update.

        no_overwrite and no_create will check if the object exists.
        Those two are mutually exclusive.  Some servers don't support
        searching for an object uid without explicitly specifying what
        kind of object it should be, hence obj_type can be passed.
        obj_type is only used in conjunction with no_overwrite and
        no_create.

        Returns:
         * self
        """
        ...
    def get_duration(self) -> datetime.timedelta:
        """
        According to the RFC, either DURATION or DUE should be set
        for a task, but never both - implicitly meaning that DURATION
        is the difference between DTSTART and DUE (personally I
        believe that's stupid.  If a task takes five minutes to
        complete - say, fill in some simple form that should be
        delivered before midnight at new years eve, then it feels
        natural for me to define "duration" as five minutes, DTSTART
        to "some days before new years eve" and DUE to 20xx-01-01
        00:00:00 - but I digress.

        This method will return DURATION if set, otherwise the
        difference between DUE and DTSTART (if both of them are set).

        TODO: should be fixed for Event class as well (only difference
        is that DTEND is used rather than DUE) and possibly also for
        Journal (defaults to one day, probably?)

        WARNING: this method is likely to be deprecated and moved to
        the icalendar library.  If you decide to use it, please put
        caldav<2.0 in the requirements.
        """
        ...
    data: Incomplete
    vobject_instance: VBase
    icalendar_instance: Incomplete
    instance: VBase

class Event(CalendarObjectResource):
    """
    The `Event` object is used to represent an event (VEVENT).

    As of 2020-12 it adds nothing to the inheritated class.  (I have
    frequently asked myself if we need those subclasses ... perhaps
    not)
    """
    ...
class Journal(CalendarObjectResource):
    """
    The `Journal` object is used to represent a journal entry (VJOURNAL).

    As of 2020-12 it adds nothing to the inheritated class.  (I have
    frequently asked myself if we need those subclasses ... perhaps
    not)
    """
    ...

class FreeBusy(CalendarObjectResource):
    def __init__(self, parent, data, url: str | ParseResult | SplitResult | URL | None = None, id=None) -> None: ...

class Todo(CalendarObjectResource):
    """
    The `Todo` object is used to represent a todo item (VTODO).  A
    Todo-object can be completed.  Extra logic for different ways to
    complete one recurrence of a recurrent todo.  Extra logic to
    handle due vs duration.
    """
    def complete(
        self,
        completion_timestamp: datetime.datetime | None = None,
        handle_rrule: bool = False,
        rrule_mode: Literal["safe", "this_and_future"] = "safe",
    ) -> None:
        """
        Marks the task as completed.

        Parameters:
         * completion_timestamp - datetime object.  Defaults to
           datetime.now().
         * handle_rrule - if set to True, the library will try to be smart if
           the task is recurring.  The default is False, for backward
           compatibility.  I may consider making this one mandatory.
         * rrule_mode -   The RFC leaves a lot of room for interpretation on how
           to handle recurring tasks, and what works on one server may break at
           another.  The following modes are accepted:
           * this_and_future - see doc for _complete_recurring_thisandfuture for details
           * safe - see doc for _complete_recurring_safe for details
        """
        ...
