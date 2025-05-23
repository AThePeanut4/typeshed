"""c-ares based hostname resolver."""

from collections.abc import Sequence
from typing import TypedDict

from gevent._types import _Watcher
from gevent.hub import Hub
from gevent.resolver import AbstractResolver
from gevent.resolver.cares import channel

class _ChannelArgs(TypedDict):
    flags: str | int | None
    timeout: str | float | None
    tries: str | int | None
    ndots: str | int | None
    udp_port: str | int | None
    tcp_port: str | int | None
    servers: Sequence[str] | str | None

class Resolver(AbstractResolver):
    """
    Implementation of the resolver API using the `c-ares`_ library.

    This implementation uses the c-ares library to handle name
    resolution. c-ares is natively asynchronous at the socket level
    and so integrates well into gevent's event loop.

    In comparison to :class:`gevent.resolver_thread.Resolver` (which
    delegates to the native system resolver), the implementation is
    much more complex. In addition, there have been reports of it not
    properly honoring certain system configurations (for example, the
    order in which IPv4 and IPv6 results are returned may not match
    the threaded resolver). However, because it does not use threads,
    it may scale better for applications that make many lookups.

    There are some known differences from the system resolver.

    - ``gethostbyname_ex`` and ``gethostbyaddr`` may return
      different for the ``aliaslist`` tuple member. (Sometimes the
      same, sometimes in a different order, sometimes a different
      alias altogether.)

    - ``gethostbyname_ex`` may return the ``ipaddrlist`` in a
      different order.

    - ``getaddrinfo`` does not return ``SOCK_RAW`` results.

    - ``getaddrinfo`` may return results in a different order.

    - Handling of ``.local`` (mDNS) names may be different, even
      if they are listed in the hosts file.

    - c-ares will not resolve ``broadcasthost``, even if listed in
      the hosts file prior to 2020-04-30.

    - This implementation may raise ``gaierror(4)`` where the
      system implementation would raise ``herror(1)`` or vice versa,
      with different error numbers. However, after 2020-04-30, this should be
      much reduced.

    - The results for ``localhost`` may be different. In
      particular, some system resolvers will return more results
      from ``getaddrinfo`` than c-ares does, such as SOCK_DGRAM
      results, and c-ares may report more ips on a multi-homed
      host.

    - The system implementation may return some names fully qualified, where
      this implementation returns only the host name. This appears to be
      the case only with entries found in ``/etc/hosts``.

    - c-ares supports a limited set of flags for ``getnameinfo`` and
      ``getaddrinfo``; unknown flags are ignored. System-specific flags
      such as ``AI_V4MAPPED_CFG`` are not supported.

    - ``getaddrinfo`` may return canonical names even without the ``AI_CANONNAME``
      being set.

    - ``getaddrinfo`` does not appear to support IPv6 symbolic scope IDs.

    .. caution::

        This module is considered extremely experimental on PyPy, and
        due to its implementation in cython, it may be slower. It may also lead to
        interpreter crashes.

    .. versionchanged:: 1.5.0
       This version of gevent typically embeds c-ares 1.15.0 or newer. In
       that version of c-ares, domains ending in ``.onion`` `are never
       resolved <https://github.com/c-ares/c-ares/issues/196>`_ or even
       sent to the DNS server.

    .. versionchanged:: 20.5.0
       ``getaddrinfo`` is now implemented using the native c-ares function
       from c-ares 1.16 or newer.

    .. versionchanged:: 20.5.0
       Now ``herror`` and ``gaierror`` are raised more consistently with
       the standard library resolver, and have more consistent errno values.

       Handling of localhost and broadcast names is now more consistent.

    .. versionchanged:: 22.10.1
       Now has a ``__del__`` method that warns if the object is destroyed
       without being properly closed.

    .. _c-ares: http://c-ares.haxx.se
    """
    cares_class: type[channel]
    hub: Hub
    cares: channel
    pid: int
    params: _ChannelArgs
    fork_watcher: _Watcher
    def __init__(
        self,
        hub: Hub | None = None,
        use_environ: bool = True,
        *,
        flags: str | int | None = None,
        timeout: str | float | None = None,
        tries: str | int | None = None,
        ndots: str | int | None = None,
        udp_port: str | int | None = None,
        tcp_port: str | int | None = None,
        servers: Sequence[str] | str | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...

__all__ = ["Resolver"]
