def getSortKey(component): ...
def sortByUID(components): ...
def deleteExtraneous(component, ignore_dtstamp: bool = False) -> None:
    """
    Recursively walk the component's children, deleting extraneous details like
    X-VOBJ-ORIGINAL-TZID.
    """
    ...
def diff(left, right):
    """
    Take two VCALENDAR components, compare VEVENTs and VTODOs in them,
    return a list of object pairs containing just UID and the bits
    that didn't match, using None for objects that weren't present in one
    version or the other.

    When there are multiple ContentLines in one VEVENT, for instance many
    DESCRIPTION lines, such lines original order is assumed to be
    meaningful.  Order is also preserved when comparing (the unlikely case
    of) multiple parameters of the same type in a ContentLine
    """
    ...
def prettyDiff(leftObj, rightObj) -> None: ...
def main() -> None: ...
def getOptions(): ...
