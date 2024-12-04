from typing import Final, Literal

AF_12844: Final[int]
AF_APPLETALK: Final[int]
AF_ASH: Final[int]
AF_ATM: Final[int]
AF_ATMPVC: Final[int]
AF_ATMSVC: Final[int]
AF_AX25: Final[int]
AF_BAN: Final[int]
AF_BLUETOOTH: Final[int]
AF_BRIDGE: Final[int]
AF_DATAKIT: Final[int]
AF_DECnet: Final[int]
AF_CCITT: Final[int]
AF_CHAOS: Final[int]
AF_CLUSTER: Final[int]
AF_CNT: Final[int]
AF_COIP: Final[int]
AF_DLI: Final[int]
AF_ECONET: Final[int]
AF_ECMA: Final[int]
AF_FILE: Final[int]
AF_FIREFOX: Final[int]
AF_HYLINK: Final[int]
AF_IMPLINK: Final[int]
AF_INET: Final[int]
AF_INET6: Final[int]
AF_IPX: Final[int]
AF_IRDA: Final[int]
AF_ISDN: Final[int]
AF_ISO: Final[int]
AF_KEY: Final[int]
AF_LAT: Final[int]
AF_LINK: Final[int]
AF_NATM: Final[int]
AF_NETBEUI: Final[int]
AF_NETBIOS: Final[int]
AF_NETDES: Final[int]
AF_NETGRAPH: Final[int]
AF_NETLINK: Final[int]
AF_NETROM: Final[int]
AF_NDRV: Final[int]
AF_NS: Final[int]
AF_PACKET: Final[int]
AF_PPP: Final[int]
AF_PPPOX: Final[int]
AF_PUP: Final[int]
AF_ROSE: Final[int]
AF_ROUTE: Final[int]
AF_SECURITY: Final[int]
AF_SIP: Final[int]
AF_SNA: Final[int]
AF_SYSTEM: Final[int]
AF_UNIX: Final[int]
AF_UNKNOWN1: Final[int]
AF_UNSPEC: Final[int]
AF_VOICEVIEW: Final[int]
AF_WANPIPE: Final[int]
AF_X25: Final[int]
IN6_IFF_AUTOCONF: Final[int]
IN6_IFF_TEMPORARY: Final[int]
IN6_IFF_DYNAMIC: Final[int]
IN6_IFF_OPTIMISTIC: Final[int]
IN6_IFF_SECURED: Final[int]

address_families: Final[dict[int, str]]
version: Final[str]

def gateways() -> dict[int | Literal["default"], list[tuple[str, str, bool] | tuple[str, str]] | dict[int, tuple[str, str]]]:
    """
    Obtain a list of the gateways on this machine.

    Returns a dict whose keys are equal to the address family constants,
    e.g. netifaces.AF_INET, and whose values are a list of tuples of the
    format (<address>, <interface>, <is_default>).

    There is also a special entry with the key 'default', which you can use
    to quickly obtain the default gateway for a particular address family.

    There may in general be multiple gateways; different address
    families may have different gateway settings (e.g. AF_INET vs AF_INET6)
    and on some systems it's also possible to have interface-specific
    default gateways.
    """
    ...
def ifaddresses(ifname: str, /) -> dict[int, list[dict[str, str]]]:
    """
    Obtain information about the specified network interface.

    Returns a dict whose keys are equal to the address family constants,
    e.g. netifaces.AF_INET, and whose values are a list of addresses in
    that family that are attached to the network interface.
    """
    ...
def interfaces() -> list[str]:
    """Obtain a list of the interfaces available on this machine."""
    ...
