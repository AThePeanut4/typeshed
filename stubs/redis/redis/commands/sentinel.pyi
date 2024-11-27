class SentinelCommands:
    """
    A class containing the commands specific to redis sentinel. This class is
    to be used as a mixin.
    """
    def sentinel(self, *args):
        """Redis Sentinel's SENTINEL command."""
        ...
    def sentinel_get_master_addr_by_name(self, service_name):
        """Returns a (host, port) pair for the given ``service_name``"""
        ...
    def sentinel_master(self, service_name):
        """Returns a dictionary containing the specified masters state."""
        ...
    def sentinel_masters(self):
        """Returns a list of dictionaries containing each master's state."""
        ...
    def sentinel_monitor(self, name, ip, port, quorum):
        """Add a new master to Sentinel to be monitored"""
        ...
    def sentinel_remove(self, name):
        """Remove a master from Sentinel's monitoring"""
        ...
    def sentinel_sentinels(self, service_name):
        """Returns a list of sentinels for ``service_name``"""
        ...
    def sentinel_set(self, name, option, value):
        """Set Sentinel monitoring parameters for a given master"""
        ...
    def sentinel_slaves(self, service_name):
        """Returns a list of slaves for ``service_name``"""
        ...
    def sentinel_reset(self, pattern):
        """
        This command will reset all the masters with matching name.
        The pattern argument is a glob-style pattern.

        The reset process clears any previous state in a master (including a
        failover in progress), and removes every slave and sentinel already
        discovered and associated with the master.
        """
        ...
    def sentinel_failover(self, new_master_name):
        """
        Force a failover as if the master was not reachable, and without
        asking for agreement to other Sentinels (however a new version of the
        configuration will be published so that the other Sentinels will
        update their configurations).
        """
        ...
    def sentinel_ckquorum(self, new_master_name):
        """
        Check if the current Sentinel configuration is able to reach the
        quorum needed to failover a master, and the majority needed to
        authorize the failover.

        This command should be used in monitoring systems to check if a
        Sentinel deployment is ok.
        """
        ...
    def sentinel_flushconfig(self):
        """
        Force Sentinel to rewrite its configuration on disk, including the
        current Sentinel state.

        Normally Sentinel rewrites the configuration every time something
        changes in its state (in the context of the subset of the state which
        is persisted on disk across restart).
        However sometimes it is possible that the configuration file is lost
        because of operation errors, disk failures, package upgrade scripts or
        configuration managers. In those cases a way to to force Sentinel to
        rewrite the configuration file is handy.

        This command works even if the previous configuration file is
        completely missing.
        """
        ...

class AsyncSentinelCommands(SentinelCommands):
    async def sentinel(self, *args) -> None:
        """Redis Sentinel's SENTINEL command."""
        ...
