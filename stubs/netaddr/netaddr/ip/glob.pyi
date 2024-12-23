"""
Routines and classes for supporting and expressing IP address ranges using a
glob style syntax.
"""

from typing_extensions import TypeGuard

from netaddr.ip import IPAddress, IPNetwork, IPRange, _IPAddressAddr, _IPNetworkAddr

def valid_glob(ipglob: object) -> TypeGuard[str]:
    """
    :param ipglob: An IP address range in a glob-style format.

    :return: ``True`` if IP range glob is valid, ``False`` otherwise.
    """
    ...
def glob_to_iptuple(ipglob: str) -> tuple[IPAddress, IPAddress]:
    """
    A function that accepts a glob-style IP range and returns the component
    lower and upper bound IP address.

    :param ipglob: an IP address range in a glob-style format.

    :return: a tuple contain lower and upper bound IP objects.
    """
    ...
def glob_to_iprange(ipglob: str) -> IPRange:
    """
    A function that accepts a glob-style IP range and returns the equivalent
    IP range.

    :param ipglob: an IP address range in a glob-style format.

    :return: an IPRange object.
    """
    ...
def iprange_to_globs(start: _IPAddressAddr, end: _IPAddressAddr) -> list[str]:
    """
    A function that accepts an arbitrary start and end IP address or subnet
    and returns one or more glob-style IP ranges.

    :param start: the start IP address or subnet.

    :param end: the end IP address or subnet.

    :return: a list containing one or more IP globs.
    """
    ...
def glob_to_cidrs(ipglob: str) -> list[IPNetwork]:
    """
    A function that accepts a glob-style IP range and returns a list of one
    or more IP CIDRs that exactly matches it.

    :param ipglob: an IP address range in a glob-style format.

    :return: a list of one or more IP objects.
    """
    ...
def cidr_to_glob(cidr: _IPNetworkAddr) -> str:
    """
    A function that accepts an IP subnet in a glob-style format and returns
    a list of CIDR subnets that exactly matches the specified glob.

    :param cidr: an IP object CIDR subnet.

    :return: a list of one or more IP addresses and subnets.
    """
    ...

class IPGlob(IPRange):
    """
    Represents an IP address range using a glob-style syntax ``x.x.x-y.*``

    Individual octets can be represented using the following shortcuts :

        1. ``*`` - the asterisk octet (represents values ``0`` through ``255``)
        2. ``x-y`` - the hyphenated octet (represents values ``x`` through ``y``)

    A few basic rules also apply :

        1. ``x`` must always be less than ``y``, therefore :

        - ``x`` can only be ``0`` through ``254``
        - ``y`` can only be ``1`` through ``255``

        2. only one hyphenated octet per IP glob is allowed
        3. only asterisks are permitted after a hyphenated octet

    Examples:

    +------------------+------------------------------+
    | IP glob          | Description                  |
    +==================+==============================+
    | ``192.0.2.1``    | a single address             |
    +------------------+------------------------------+
    | ``192.0.2.0-31`` | 32 addresses                 |
    +------------------+------------------------------+
    | ``192.0.2.*``    | 256 addresses                |
    +------------------+------------------------------+
    | ``192.0.2-3.*``  | 512 addresses                |
    +------------------+------------------------------+
    | ``192.0-1.*.*``  | 131,072 addresses            |
    +------------------+------------------------------+
    | ``*.*.*.*``      | the whole IPv4 address space |
    +------------------+------------------------------+

    .. note ::     IP glob ranges are not directly equivalent to CIDR blocks.     They can represent address ranges that do not fall on strict bit mask     boundaries. They are suitable for use in configuration files, being     more obvious and readable than their CIDR counterparts, especially for     admins and end users with little or no networking knowledge or     experience. All CIDR addresses can always be represented as IP globs     but the reverse is not always true.
    """
    def __init__(self, ipglob: str) -> None: ...
    @property
    def glob(self) -> str:
        """an arbitrary IP address range in glob format."""
        ...
    @glob.setter
    def glob(self, value: str) -> None:
        """an arbitrary IP address range in glob format."""
        ...
