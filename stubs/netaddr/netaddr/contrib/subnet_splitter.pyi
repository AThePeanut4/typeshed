from netaddr.ip import IPNetwork, _IPAddressAddr

class SubnetSplitter:
    """
    A handy utility class that takes a single (large) subnet and allows
    smaller subnet within its range to be extracted by CIDR prefix. Any
    leaving address space is available for subsequent extractions until
    all space is exhausted.
    """
    def __init__(self, base_cidr: _IPAddressAddr) -> None:
        """
        Constructor.

        :param base_cidr: an IPv4 or IPv6 address with a CIDR prefix.
            (see IPNetwork.__init__ for full details).
        """
        ...
    def extract_subnet(self, prefix: int, count: int | None = None) -> list[IPNetwork]:
        """Extract 1 or more subnets of size specified by CIDR prefix."""
        ...
    def available_subnets(self) -> list[IPNetwork]:
        """Returns a list of the currently available subnets."""
        ...
    def remove_subnet(self, ip_network: IPNetwork) -> None:
        """Remove a specified IPNetwork from available address space."""
        ...
