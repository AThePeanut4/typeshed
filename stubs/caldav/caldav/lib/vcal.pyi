def fix(event):
    """
    This function receives some ical as it's given from the server, checks for
    breakages with the standard, and attempts to fix up known issues:

    1) COMPLETED MUST be a datetime in UTC according to the RFC, but sometimes
    a date is given. (Google Calendar?)

    2) The RFC does not specify any range restrictions on the dates,
    but clearly it doesn't make sense with a CREATED-timestamp that is
    centuries or decades before RFC2445 was published in 1998.
    Apparently some calendar servers generate nonsensical CREATED
    timestamps while other calendar servers can't handle CREATED
    timestamps prior to 1970.  Probably it would make more sense to
    drop the CREATED line completely rather than moving it from the
    end of year 0AD to the beginning of year 1970. (Google Calendar)

    3) iCloud apparently duplicates the DTSTAMP property sometimes -
    keep the first DTSTAMP encountered (arguably the DTSTAMP with earliest value
    should be kept).

    4) ref https://github.com/python-caldav/caldav/issues/37,
    X-APPLE-STRUCTURED-EVENT attribute sometimes comes with trailing
    white space.  I've decided to remove all trailing spaces, since
    they seem to cause a traceback with vobject and those lines are
    simply ignored by icalendar.

    5) Zimbra can apparently create events with both dtstart, dtend
    and duration set - which is forbidden according to the RFC.  We
    should probably verify that the data is consistent.  As for now,
    we'll just drop DURATION or DTEND (whatever comes last).
    """
    ...
