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
    __slots__ = ("_glob",)
    def __init__(self, ipglob: str) -> None: ...
    @property
    def glob(self) -> str:
        """an arbitrary IP address range in glob format."""
        ...
    @glob.setter
    def glob(self, value: str) -> None:
        """an arbitrary IP address range in glob format."""
        ...
