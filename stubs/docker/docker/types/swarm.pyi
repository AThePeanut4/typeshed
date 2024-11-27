from _typeshed import Incomplete
from typing import Any

class SwarmSpec(dict[str, Any]):
    """
    Describe a Swarm's configuration and options. Use
    :py:meth:`~docker.api.swarm.SwarmApiMixin.create_swarm_spec`
    to instantiate.
    """
    def __init__(
        self,
        version,
        task_history_retention_limit: Incomplete | None = None,
        snapshot_interval: Incomplete | None = None,
        keep_old_snapshots: Incomplete | None = None,
        log_entries_for_slow_followers: Incomplete | None = None,
        heartbeat_tick: Incomplete | None = None,
        election_tick: Incomplete | None = None,
        dispatcher_heartbeat_period: Incomplete | None = None,
        node_cert_expiry: Incomplete | None = None,
        external_cas: Incomplete | None = None,
        name: Incomplete | None = None,
        labels: Incomplete | None = None,
        signing_ca_cert: Incomplete | None = None,
        signing_ca_key: Incomplete | None = None,
        ca_force_rotate: Incomplete | None = None,
        autolock_managers: Incomplete | None = None,
        log_driver: Incomplete | None = None,
    ) -> None: ...

class SwarmExternalCA(dict[str, Any]):
    """
    Configuration for forwarding signing requests to an external
    certificate authority.

    Args:
        url (string): URL where certificate signing requests should be
            sent.
        protocol (string): Protocol for communication with the external CA.
        options (dict): An object with key/value pairs that are interpreted
            as protocol-specific options for the external CA driver.
        ca_cert (string): The root CA certificate (in PEM format) this
            external CA uses to issue TLS certificates (assumed to be to
            the current swarm root CA certificate if not provided).
    """
    def __init__(
        self, url, protocol: Incomplete | None = None, options: Incomplete | None = None, ca_cert: Incomplete | None = None
    ) -> None: ...
