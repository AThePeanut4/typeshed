"""Implementation of the ipaddres-based network types adaptation"""

import ipaddress as ipaddress
from _typeshed import Unused

from psycopg2._psycopg import QuotedString, connection, cursor

def register_ipaddress(conn_or_curs: connection | cursor | None = None) -> None:
    """
    Register conversion support between `ipaddress` objects and `network types`__.

    :param conn_or_curs: the scope where to register the type casters.
        If `!None` register them globally.

    After the function is called, PostgreSQL :sql:`inet` values will be
    converted into `~ipaddress.IPv4Interface` or `~ipaddress.IPv6Interface`
    objects, :sql:`cidr` values into into `~ipaddress.IPv4Network` or
    `~ipaddress.IPv6Network`.

    .. __: https://www.postgresql.org/docs/current/static/datatype-net-types.html
    """
    ...
def cast_interface(s: str, cur: Unused = None) -> ipaddress.IPv4Interface | ipaddress.IPv6Interface | None: ...
def cast_network(s: str, cur: Unused = None) -> ipaddress.IPv4Network | ipaddress.IPv6Network | None: ...
def adapt_ipaddress(obj: object) -> QuotedString: ...
