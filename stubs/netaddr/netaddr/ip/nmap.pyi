"""
Routines for dealing with nmap-style IPv4 address ranges.

Based on nmap's Target Specification :-

    http://nmap.org/book/man-target-specification.html
"""

from collections.abc import Iterator

from netaddr.ip import IPAddress

def valid_nmap_range(target_spec: str) -> bool:
    """
    :param target_spec: an nmap-style IP range target specification.

    :return: ``True`` if IP range target spec is valid, ``False`` otherwise.
    """
    ...
def iter_nmap_range(*nmap_target_spec: str) -> Iterator[IPAddress]:
    """
    An generator that yields IPAddress objects from defined by nmap target
    specifications.

    See https://nmap.org/book/man-target-specification.html for details.

    :param nmap_target_spec: one or more nmap IP range target specification.

    :return: an iterator producing IPAddress objects for each IP in the target spec(s).
    """
    ...
