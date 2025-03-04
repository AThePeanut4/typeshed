"""Set based operations for IP addresses and subnets."""

from collections.abc import Iterable, Iterator
from typing import NoReturn
from typing_extensions import Self, TypeAlias

from netaddr.ip import IPAddress, IPNetwork, IPRange, _IPNetworkAddr

_IPIterable: TypeAlias = IPNetwork | IPRange | IPSet | Iterable[_IPNetworkAddr | IPRange | int]

class IPSet:
    """
    Represents an unordered collection (set) of unique IP addresses and
    subnets.
    """
    def __init__(self, iterable: _IPIterable | None = None, flags: int = 0) -> None:
        """
        Constructor.

        :param iterable: (optional) an iterable containing IP addresses,
            subnets or ranges.

        :param flags: decides which rules are applied to the interpretation
            of the addr value. See the :class:`IPAddress` documentation
            for supported constant values.
        """
        ...
    def compact(self) -> None:
        """Compact internal list of `IPNetwork` objects using a CIDR merge."""
        ...
    def __hash__(self) -> NoReturn:
        """
        Raises ``TypeError`` if this method is called.

        .. note:: IPSet objects are not hashable and cannot be used as             dictionary keys or as members of other sets.         
        """
        ...
    def __contains__(self, ip: _IPNetworkAddr) -> bool:
        """
        :param ip: An IP address or subnet.

        :return: ``True`` if IP address or subnet is a member of this IP set.
        """
        ...
    def __bool__(self) -> bool:
        """Return True if IPSet contains at least one IP, else False"""
        ...
    def __iter__(self) -> Iterator[IPAddress]:
        """:return: an iterator over the IP addresses within this IP set."""
        ...
    def iter_cidrs(self) -> list[IPNetwork]:
        """:return: an iterator over individual IP subnets within this IP set."""
        ...
    def add(self, addr: IPRange | _IPNetworkAddr | int, flags: int = 0) -> None:
        """
        Adds an IP address or subnet or IPRange to this IP set. Has no effect if
        it is already present.

        Note that where possible the IP address or subnet is merged with other
        members of the set to form more concise CIDR blocks.

        :param addr: An IP address or subnet in either string or object form, or
            an IPRange object.

        :param flags: decides which rules are applied to the interpretation
            of the addr value. See the :class:`IPAddress` documentation
            for supported constant values.
        """
        ...
    def remove(self, addr: IPRange | _IPNetworkAddr | int, flags: int = 0) -> None:
        """
        Removes an IP address or subnet or IPRange from this IP set. Does
        nothing if it is not already a member.

        Note that this method behaves more like discard() found in regular
        Python sets because it doesn't raise KeyError exceptions if the
        IP address or subnet is question does not exist. It doesn't make sense
        to fully emulate that behaviour here as IP sets contain groups of
        individual IP addresses as individual set members using IPNetwork
        objects.

        :param addr: An IP address or subnet, or an IPRange.

        :param flags: decides which rules are applied to the interpretation
            of the addr value. See the :class:`IPAddress` documentation
            for supported constant values.
        """
        ...
    def pop(self) -> IPNetwork:
        """
        Removes and returns an arbitrary IP address or subnet from this IP
        set.

        :return: An IP address or subnet.
        """
        ...
    def isdisjoint(self, other: IPSet) -> bool:
        """
        :param other: an IP set.

        :return: ``True`` if this IP set has no elements (IP addresses
            or subnets) in common with other. Intersection *must* be an
            empty set.
        """
        ...
    def copy(self) -> Self:
        """:return: a shallow copy of this IP set."""
        ...
    def update(self, iterable: _IPIterable, flags: int = 0) -> None:
        """
        Update the contents of this IP set with the union of itself and
        other IP set.

        :param iterable: an iterable containing IP addresses, subnets or ranges.

        :param flags: decides which rules are applied to the interpretation
            of the addr value. See the :class:`IPAddress` documentation
            for supported constant values.
        """
        ...
    def clear(self) -> None:
        """Remove all IP addresses and subnets from this IP set."""
        ...
    def __eq__(self, other: object) -> bool:
        """
        :param other: an IP set

        :return: ``True`` if this IP set is equivalent to the ``other`` IP set,
            ``False`` otherwise.
        """
        ...
    def __ne__(self, other: object) -> bool:
        """
        :param other: an IP set

        :return: ``False`` if this IP set is equivalent to the ``other`` IP set,
            ``True`` otherwise.
        """
        ...
    def __lt__(self, other: IPSet) -> bool:
        """
        :param other: an IP set

        :return: ``True`` if this IP set is less than the ``other`` IP set,
            ``False`` otherwise.
        """
        ...
    def issubset(self, other: IPSet) -> bool:
        """
        :param other: an IP set.

        :return: ``True`` if every IP address and subnet in this IP set
            is found within ``other``.
        """
        ...
    __le__ = issubset
    def __gt__(self, other: IPSet) -> bool:
        """
        :param other: an IP set.

        :return: ``True`` if this IP set is greater than the ``other`` IP set,
            ``False`` otherwise.
        """
        ...
    def issuperset(self, other: IPSet) -> bool:
        """
        :param other: an IP set.

        :return: ``True`` if every IP address and subnet in other IP set
            is found within this one.
        """
        ...
    __ge__ = issuperset
    def union(self, other: IPSet) -> Self:
        """
        :param other: an IP set.

        :return: the union of this IP set and another as a new IP set
            (combines IP addresses and subnets from both sets).
        """
        ...
    __or__ = union
    def intersection(self, other: IPSet) -> IPSet:
        """
        :param other: an IP set.

        :return: the intersection of this IP set and another as a new IP set.
            (IP addresses and subnets common to both sets).
        """
        ...
    __and__ = intersection
    def symmetric_difference(self, other: IPSet) -> IPSet:
        """
        :param other: an IP set.

        :return: the symmetric difference of this IP set and another as a new
            IP set (all IP addresses and subnets that are in exactly one
            of the sets).
        """
        ...
    __xor__ = symmetric_difference
    def difference(self, other: IPSet) -> IPSet:
        """
        :param other: an IP set.

        :return: the difference between this IP set and another as a new IP
            set (all IP addresses and subnets that are in this IP set but
            not found in the other.)
        """
        ...
    __sub__ = difference
    def __len__(self) -> int:
        """:return: the cardinality of this IP set (i.e. sum of individual IP             addresses). Raises ``IndexError`` if size > maxsize (a Python             limitation). Use the .size property for subnets of any size."""
        ...
    @property
    def size(self) -> int:
        """
        The cardinality of this IP set (based on the number of individual IP
        addresses including those implicitly defined in subnets).
        """
        ...
    def iscontiguous(self) -> bool:
        """
        Returns True if the members of the set form a contiguous IP
        address range (with no gaps), False otherwise.

        :return: ``True`` if the ``IPSet`` object is contiguous.
        """
        ...
    def iprange(self) -> IPRange | None:
        """
        Generates an IPRange for this IPSet, if all its members
        form a single contiguous sequence.

        Raises ``ValueError`` if the set is not contiguous.

        :return: An ``IPRange`` for all IPs in the IPSet.
        """
        ...
    def iter_ipranges(self) -> Iterator[IPRange]:
        """
        Generate the merged IPRanges for this IPSet.

        In contrast to self.iprange(), this will work even when the IPSet is
        not contiguous. Adjacent IPRanges will be merged together, so you
        get the minimal number of IPRanges.
        """
        ...
