import builtins
from _typeshed import Incomplete, SupportsItems
from collections.abc import AsyncIterator, Awaitable, Callable, Iterable, Iterator, Mapping, Sequence
from datetime import datetime, timedelta
from typing import Any, Generic, Literal, TypeVar, overload

from ..asyncio.client import Redis as AsyncRedis
from ..client import _CommandOptions, _Key, _Value
from ..typing import ChannelT, EncodableT, KeyT, PatternT, ScriptTextT, StreamIdT

_ScoreCastFuncReturn = TypeVar("_ScoreCastFuncReturn")
_StrType = TypeVar("_StrType", bound=str | bytes)

class ACLCommands(Generic[_StrType]):
    """
    Redis Access Control List (ACL) commands.
    see: https://redis.io/topics/acl
    """
    def acl_cat(self, category: str | None = None, **kwargs: _CommandOptions) -> list[str]:
        """
        Returns a list of categories or commands within a category.

        If ``category`` is not supplied, returns a list of all categories.
        If ``category`` is supplied, returns a list of all commands within
        that category.

        For more information see https://redis.io/commands/acl-cat
        """
        ...
    def acl_deluser(self, *username: str, **kwargs: _CommandOptions) -> int:
        """
        Delete the ACL for the specified ``username``s

        For more information see https://redis.io/commands/acl-deluser
        """
        ...
    def acl_genpass(self, bits: int | None = None, **kwargs: _CommandOptions) -> str:
        """
        Generate a random password value.
        If ``bits`` is supplied then use this number of bits, rounded to
        the next multiple of 4.
        See: https://redis.io/commands/acl-genpass
        """
        ...
    def acl_getuser(self, username: str, **kwargs: _CommandOptions) -> Any | None:
        """
        Get the ACL details for the specified ``username``.

        If ``username`` does not exist, return None

        For more information see https://redis.io/commands/acl-getuser
        """
        ...
    def acl_help(self, **kwargs: _CommandOptions):
        """
        The ACL HELP command returns helpful text describing
        the different subcommands.

        For more information see https://redis.io/commands/acl-help
        """
        ...
    def acl_list(self, **kwargs: _CommandOptions) -> list[str]:
        """
        Return a list of all ACLs on the server

        For more information see https://redis.io/commands/acl-list
        """
        ...
    def acl_log(self, count: int | None = None, **kwargs: _CommandOptions):
        """
        Get ACL logs as a list.
        :param int count: Get logs[0:count].
        :rtype: List.

        For more information see https://redis.io/commands/acl-log
        """
        ...
    def acl_log_reset(self, **kwargs: _CommandOptions):
        """
        Reset ACL logs.
        :rtype: Boolean.

        For more information see https://redis.io/commands/acl-log
        """
        ...
    def acl_load(self, **kwargs: _CommandOptions) -> bool:
        """
        Load ACL rules from the configured ``aclfile``.

        Note that the server must be configured with the ``aclfile``
        directive to be able to load ACL rules from an aclfile.

        For more information see https://redis.io/commands/acl-load
        """
        ...
    def acl_save(self, **kwargs: _CommandOptions):
        """
        Save ACL rules to the configured ``aclfile``.

        Note that the server must be configured with the ``aclfile``
        directive to be able to save ACL rules to an aclfile.

        For more information see https://redis.io/commands/acl-save
        """
        ...
    def acl_setuser(
        self,
        username: str,
        enabled: bool = False,
        nopass: bool = False,
        passwords: Sequence[str] | None = None,
        hashed_passwords: Sequence[str] | None = None,
        categories: Sequence[str] | None = None,
        commands: Sequence[str] | None = None,
        keys: Sequence[str] | None = None,
        channels: Iterable[ChannelT] | None = None,
        selectors: Iterable[tuple[str, KeyT]] | None = None,
        reset: bool = False,
        reset_keys: bool = False,
        reset_channels: bool = False,
        reset_passwords: bool = False,
        **kwargs: _CommandOptions,
    ) -> bool:
        """
        Create or update an ACL user.

        Create or update the ACL for ``username``. If the user already exists,
        the existing ACL is completely overwritten and replaced with the
        specified values.

        ``enabled`` is a boolean indicating whether the user should be allowed
        to authenticate or not. Defaults to ``False``.

        ``nopass`` is a boolean indicating whether the can authenticate without
        a password. This cannot be True if ``passwords`` are also specified.

        ``passwords`` if specified is a list of plain text passwords
        to add to or remove from the user. Each password must be prefixed with
        a '+' to add or a '-' to remove. For convenience, the value of
        ``passwords`` can be a simple prefixed string when adding or
        removing a single password.

        ``hashed_passwords`` if specified is a list of SHA-256 hashed passwords
        to add to or remove from the user. Each hashed password must be
        prefixed with a '+' to add or a '-' to remove. For convenience,
        the value of ``hashed_passwords`` can be a simple prefixed string when
        adding or removing a single password.

        ``categories`` if specified is a list of strings representing category
        permissions. Each string must be prefixed with either a '+' to add the
        category permission or a '-' to remove the category permission.

        ``commands`` if specified is a list of strings representing command
        permissions. Each string must be prefixed with either a '+' to add the
        command permission or a '-' to remove the command permission.

        ``keys`` if specified is a list of key patterns to grant the user
        access to. Keys patterns allow '*' to support wildcard matching. For
        example, '*' grants access to all keys while 'cache:*' grants access
        to all keys that are prefixed with 'cache:'. ``keys`` should not be
        prefixed with a '~'.

        ``reset`` is a boolean indicating whether the user should be fully
        reset prior to applying the new ACL. Setting this to True will
        remove all existing passwords, flags and privileges from the user and
        then apply the specified rules. If this is False, the user's existing
        passwords, flags and privileges will be kept and any new specified
        rules will be applied on top.

        ``reset_keys`` is a boolean indicating whether the user's key
        permissions should be reset prior to applying any new key permissions
        specified in ``keys``. If this is False, the user's existing
        key permissions will be kept and any new specified key permissions
        will be applied on top.

        ``reset_channels`` is a boolean indicating whether the user's channel
        permissions should be reset prior to applying any new channel permissions
        specified in ``channels``.If this is False, the user's existing
        channel permissions will be kept and any new specified channel permissions
        will be applied on top.

        ``reset_passwords`` is a boolean indicating whether to remove all
        existing passwords and the 'nopass' flag from the user prior to
        applying any new passwords specified in 'passwords' or
        'hashed_passwords'. If this is False, the user's existing passwords
        and 'nopass' status will be kept and any new specified passwords
        or hashed_passwords will be applied on top.

        For more information see https://redis.io/commands/acl-setuser
        """
        ...
    def acl_users(self, **kwargs: _CommandOptions) -> list[str]:
        """
        Returns a list of all registered users on the server.

        For more information see https://redis.io/commands/acl-users
        """
        ...
    def acl_whoami(self, **kwargs: _CommandOptions) -> str:
        """
        Get the username for the current connection

        For more information see https://redis.io/commands/acl-whoami
        """
        ...

class AsyncACLCommands(Generic[_StrType]):
    """
    Redis Access Control List (ACL) commands.
    see: https://redis.io/topics/acl
    """
    async def acl_cat(self, category: str | None = None, **kwargs: _CommandOptions) -> list[str]:
        """
        Returns a list of categories or commands within a category.

        If ``category`` is not supplied, returns a list of all categories.
        If ``category`` is supplied, returns a list of all commands within
        that category.

        For more information see https://redis.io/commands/acl-cat
        """
        ...
    async def acl_deluser(self, *username: str, **kwargs: _CommandOptions) -> int:
        """
        Delete the ACL for the specified ``username``s

        For more information see https://redis.io/commands/acl-deluser
        """
        ...
    async def acl_genpass(self, bits: int | None = None, **kwargs: _CommandOptions) -> str:
        """
        Generate a random password value.
        If ``bits`` is supplied then use this number of bits, rounded to
        the next multiple of 4.
        See: https://redis.io/commands/acl-genpass
        """
        ...
    async def acl_getuser(self, username: str, **kwargs: _CommandOptions) -> Any | None:
        """
        Get the ACL details for the specified ``username``.

        If ``username`` does not exist, return None

        For more information see https://redis.io/commands/acl-getuser
        """
        ...
    async def acl_help(self, **kwargs: _CommandOptions):
        """
        The ACL HELP command returns helpful text describing
        the different subcommands.

        For more information see https://redis.io/commands/acl-help
        """
        ...
    async def acl_list(self, **kwargs: _CommandOptions) -> list[str]:
        """
        Return a list of all ACLs on the server

        For more information see https://redis.io/commands/acl-list
        """
        ...
    async def acl_log(self, count: int | None = None, **kwargs: _CommandOptions):
        """
        Get ACL logs as a list.
        :param int count: Get logs[0:count].
        :rtype: List.

        For more information see https://redis.io/commands/acl-log
        """
        ...
    async def acl_log_reset(self, **kwargs: _CommandOptions):
        """
        Reset ACL logs.
        :rtype: Boolean.

        For more information see https://redis.io/commands/acl-log
        """
        ...
    async def acl_load(self, **kwargs: _CommandOptions) -> bool:
        """
        Load ACL rules from the configured ``aclfile``.

        Note that the server must be configured with the ``aclfile``
        directive to be able to load ACL rules from an aclfile.

        For more information see https://redis.io/commands/acl-load
        """
        ...
    async def acl_save(self, **kwargs: _CommandOptions):
        """
        Save ACL rules to the configured ``aclfile``.

        Note that the server must be configured with the ``aclfile``
        directive to be able to save ACL rules to an aclfile.

        For more information see https://redis.io/commands/acl-save
        """
        ...
    async def acl_setuser(
        self,
        username: str,
        enabled: bool = False,
        nopass: bool = False,
        passwords: Sequence[str] | None = None,
        hashed_passwords: Sequence[str] | None = None,
        categories: Sequence[str] | None = None,
        commands: Sequence[str] | None = None,
        keys: Sequence[str] | None = None,
        channels: Iterable[ChannelT] | None = None,
        selectors: Iterable[tuple[str, KeyT]] | None = None,
        reset: bool = False,
        reset_keys: bool = False,
        reset_channels: bool = False,
        reset_passwords: bool = False,
        **kwargs: _CommandOptions,
    ) -> bool:
        """
        Create or update an ACL user.

        Create or update the ACL for ``username``. If the user already exists,
        the existing ACL is completely overwritten and replaced with the
        specified values.

        ``enabled`` is a boolean indicating whether the user should be allowed
        to authenticate or not. Defaults to ``False``.

        ``nopass`` is a boolean indicating whether the can authenticate without
        a password. This cannot be True if ``passwords`` are also specified.

        ``passwords`` if specified is a list of plain text passwords
        to add to or remove from the user. Each password must be prefixed with
        a '+' to add or a '-' to remove. For convenience, the value of
        ``passwords`` can be a simple prefixed string when adding or
        removing a single password.

        ``hashed_passwords`` if specified is a list of SHA-256 hashed passwords
        to add to or remove from the user. Each hashed password must be
        prefixed with a '+' to add or a '-' to remove. For convenience,
        the value of ``hashed_passwords`` can be a simple prefixed string when
        adding or removing a single password.

        ``categories`` if specified is a list of strings representing category
        permissions. Each string must be prefixed with either a '+' to add the
        category permission or a '-' to remove the category permission.

        ``commands`` if specified is a list of strings representing command
        permissions. Each string must be prefixed with either a '+' to add the
        command permission or a '-' to remove the command permission.

        ``keys`` if specified is a list of key patterns to grant the user
        access to. Keys patterns allow '*' to support wildcard matching. For
        example, '*' grants access to all keys while 'cache:*' grants access
        to all keys that are prefixed with 'cache:'. ``keys`` should not be
        prefixed with a '~'.

        ``reset`` is a boolean indicating whether the user should be fully
        reset prior to applying the new ACL. Setting this to True will
        remove all existing passwords, flags and privileges from the user and
        then apply the specified rules. If this is False, the user's existing
        passwords, flags and privileges will be kept and any new specified
        rules will be applied on top.

        ``reset_keys`` is a boolean indicating whether the user's key
        permissions should be reset prior to applying any new key permissions
        specified in ``keys``. If this is False, the user's existing
        key permissions will be kept and any new specified key permissions
        will be applied on top.

        ``reset_channels`` is a boolean indicating whether the user's channel
        permissions should be reset prior to applying any new channel permissions
        specified in ``channels``.If this is False, the user's existing
        channel permissions will be kept and any new specified channel permissions
        will be applied on top.

        ``reset_passwords`` is a boolean indicating whether to remove all
        existing passwords and the 'nopass' flag from the user prior to
        applying any new passwords specified in 'passwords' or
        'hashed_passwords'. If this is False, the user's existing passwords
        and 'nopass' status will be kept and any new specified passwords
        or hashed_passwords will be applied on top.

        For more information see https://redis.io/commands/acl-setuser
        """
        ...
    async def acl_users(self, **kwargs: _CommandOptions) -> list[str]:
        """
        Returns a list of all registered users on the server.

        For more information see https://redis.io/commands/acl-users
        """
        ...
    async def acl_whoami(self, **kwargs: _CommandOptions) -> str:
        """
        Get the username for the current connection

        For more information see https://redis.io/commands/acl-whoami
        """
        ...

class ManagementCommands:
    """Redis management commands"""
    def bgrewriteaof(self, **kwargs: _CommandOptions):
        """
        Tell the Redis server to rewrite the AOF file from data in memory.

        For more information see https://redis.io/commands/bgrewriteaof
        """
        ...
    def bgsave(self, schedule: bool = True, **kwargs: _CommandOptions):
        """
        Tell the Redis server to save its data to disk.  Unlike save(),
        this method is asynchronous and returns immediately.

        For more information see https://redis.io/commands/bgsave
        """
        ...
    def role(self):
        """
        Provide information on the role of a Redis instance in
        the context of replication, by returning if the instance
        is currently a master, slave, or sentinel.

        For more information see https://redis.io/commands/role
        """
        ...
    def client_kill(self, address: str, **kwargs: _CommandOptions) -> bool:
        """
        Disconnects the client at ``address`` (ip:port)

        For more information see https://redis.io/commands/client-kill
        """
        ...
    def client_kill_filter(
        self,
        _id: Incomplete | None = None,
        _type: Incomplete | None = None,
        addr: Incomplete | None = None,
        skipme: Incomplete | None = None,
        laddr: Incomplete | None = None,
        user: Incomplete | None = None,
        **kwargs: _CommandOptions,
    ):
        """
        Disconnects client(s) using a variety of filter options
        :param _id: Kills a client by its unique ID field
        :param _type: Kills a client by type where type is one of 'normal',
        'master', 'slave' or 'pubsub'
        :param addr: Kills a client by its 'address:port'
        :param skipme: If True, then the client calling the command
        will not get killed even if it is identified by one of the filter
        options. If skipme is not provided, the server defaults to skipme=True
        :param laddr: Kills a client by its 'local (bind) address:port'
        :param user: Kills a client for a specific user name
        """
        ...
    def client_info(self, **kwargs: _CommandOptions):
        """
        Returns information and statistics about the current
        client connection.

        For more information see https://redis.io/commands/client-info
        """
        ...
    def client_list(
        self, _type: str | None = None, client_id: list[str] = [], **kwargs: _CommandOptions
    ) -> list[dict[str, str]]:
        """
        Returns a list of currently connected clients.
        If type of client specified, only that type will be returned.
        :param _type: optional. one of the client types (normal, master,
         replica, pubsub)
        :param client_id: optional. a list of client ids

        For more information see https://redis.io/commands/client-list
        """
        ...
    def client_getname(self, **kwargs: _CommandOptions) -> str | None:
        """
        Returns the current connection name

        For more information see https://redis.io/commands/client-getname
        """
        ...
    def client_getredir(self, **kwargs: _CommandOptions):
        """
        Returns the ID (an integer) of the client to whom we are
        redirecting tracking notifications.

        see: https://redis.io/commands/client-getredir
        """
        ...
    def client_reply(self, reply, **kwargs: _CommandOptions):
        """
        Enable and disable redis server replies.
        ``reply`` Must be ON OFF or SKIP,
            ON - The default most with server replies to commands
            OFF - Disable server responses to commands
            SKIP - Skip the response of the immediately following command.

        Note: When setting OFF or SKIP replies, you will need a client object
        with a timeout specified in seconds, and will need to catch the
        TimeoutError.
              The test_client_reply unit test illustrates this, and
              conftest.py has a client with a timeout.

        See https://redis.io/commands/client-reply
        """
        ...
    def client_id(self, **kwargs: _CommandOptions) -> int:
        """
        Returns the current connection id

        For more information see https://redis.io/commands/client-id
        """
        ...
    def client_tracking_on(
        self,
        clientid: Incomplete | None = None,
        prefix=[],
        bcast: bool = False,
        optin: bool = False,
        optout: bool = False,
        noloop: bool = False,
    ):
        """
        Turn on the tracking mode.
        For more information about the options look at client_tracking func.

        See https://redis.io/commands/client-tracking
        """
        ...
    def client_tracking_off(
        self,
        clientid: Incomplete | None = None,
        prefix=[],
        bcast: bool = False,
        optin: bool = False,
        optout: bool = False,
        noloop: bool = False,
    ):
        """
        Turn off the tracking mode.
        For more information about the options look at client_tracking func.

        See https://redis.io/commands/client-tracking
        """
        ...
    def client_tracking(
        self,
        on: bool = True,
        clientid: Incomplete | None = None,
        prefix=[],
        bcast: bool = False,
        optin: bool = False,
        optout: bool = False,
        noloop: bool = False,
        **kwargs: _CommandOptions,
    ):
        """
        Enables the tracking feature of the Redis server, that is used
        for server assisted client side caching.

        ``on`` indicate for tracking on or tracking off. The dafualt is on.

        ``clientid`` send invalidation messages to the connection with
        the specified ID.

        ``bcast`` enable tracking in broadcasting mode. In this mode
        invalidation messages are reported for all the prefixes
        specified, regardless of the keys requested by the connection.

        ``optin``  when broadcasting is NOT active, normally don't track
        keys in read only commands, unless they are called immediately
        after a CLIENT CACHING yes command.

        ``optout`` when broadcasting is NOT active, normally track keys in
        read only commands, unless they are called immediately after a
        CLIENT CACHING no command.

        ``noloop`` don't send notifications about keys modified by this
        connection itself.

        ``prefix``  for broadcasting, register a given key prefix, so that
        notifications will be provided only for keys starting with this string.

        See https://redis.io/commands/client-tracking
        """
        ...
    def client_trackinginfo(self, **kwargs: _CommandOptions):
        """
        Returns the information about the current client connection's
        use of the server assisted client side cache.

        See https://redis.io/commands/client-trackinginfo
        """
        ...
    def client_setname(self, name: str, **kwargs: _CommandOptions) -> bool:
        """
        Sets the current connection name

        For more information see https://redis.io/commands/client-setname

        .. note::
           This method sets client name only for **current** connection.

           If you want to set a common name for all connections managed
           by this client, use ``client_name`` constructor argument.
        """
        ...
    def client_unblock(self, client_id, error: bool = False, **kwargs: _CommandOptions):
        """
        Unblocks a connection by its client id.
        If ``error`` is True, unblocks the client with a special error message.
        If ``error`` is False (default), the client is unblocked using the
        regular timeout mechanism.

        For more information see https://redis.io/commands/client-unblock
        """
        ...
    def client_pause(self, timeout, all: bool = True, **kwargs: _CommandOptions):
        """
        Suspend all the Redis clients for the specified amount of time
        :param timeout: milliseconds to pause clients

        For more information see https://redis.io/commands/client-pause
        :param all: If true (default) all client commands are blocked.
             otherwise, clients are only blocked if they attempt to execute
             a write command.
             For the WRITE mode, some commands have special behavior:
                 EVAL/EVALSHA: Will block client for all scripts.
                 PUBLISH: Will block client.
                 PFCOUNT: Will block client.
                 WAIT: Acknowledgments will be delayed, so this command will
                 appear blocked.
        """
        ...
    def client_unpause(self, **kwargs: _CommandOptions):
        """
        Unpause all redis clients

        For more information see https://redis.io/commands/client-unpause
        """
        ...
    def client_no_evict(self, mode: str):
        """
        Sets the client eviction mode for the current connection.

        For more information see https://redis.io/commands/client-no-evict
        """
        ...
    def client_no_touch(self, mode: str):
        """
        # The command controls whether commands sent by the client will alter
        # the LRU/LFU of the keys they access.
        # When turned on, the current client will not change LFU/LRU stats,
        # unless it sends the TOUCH command.

        For more information see https://redis.io/commands/client-no-touch
        """
        ...
    def command(self, **kwargs: _CommandOptions):
        """
        Returns dict reply of details about all Redis commands.

        For more information see https://redis.io/commands/command
        """
        ...
    def command_info(self, **kwargs: _CommandOptions): ...
    def command_count(self, **kwargs: _CommandOptions): ...
    def config_get(self, pattern: PatternT = "*", *args: PatternT, **kwargs: _CommandOptions):
        """
        Return a dictionary of configuration based on the ``pattern``

        For more information see https://redis.io/commands/config-get
        """
        ...
    def config_set(self, name: KeyT, value: EncodableT, *args: KeyT | EncodableT, **kwargs: _CommandOptions):
        """
        Set config item ``name`` with ``value``

        For more information see https://redis.io/commands/config-set
        """
        ...
    def config_resetstat(self, **kwargs: _CommandOptions):
        """
        Reset runtime statistics

        For more information see https://redis.io/commands/config-resetstat
        """
        ...
    def config_rewrite(self, **kwargs: _CommandOptions):
        """
        Rewrite config file with the minimal change to reflect running config.

        For more information see https://redis.io/commands/config-rewrite
        """
        ...
    def dbsize(self, **kwargs: _CommandOptions) -> int:
        """
        Returns the number of keys in the current database

        For more information see https://redis.io/commands/dbsize
        """
        ...
    def debug_object(self, key, **kwargs: _CommandOptions):
        """
        Returns version specific meta information about a given key

        For more information see https://redis.io/commands/debug-object
        """
        ...
    def debug_segfault(self, **kwargs: _CommandOptions): ...
    def echo(self, value: _Value, **kwargs: _CommandOptions) -> bytes:
        """
        Echo the string back from the server

        For more information see https://redis.io/commands/echo
        """
        ...
    def flushall(self, asynchronous: bool = False, **kwargs: _CommandOptions) -> bool:
        """
        Delete all keys in all databases on the current host.

        ``asynchronous`` indicates whether the operation is
        executed asynchronously by the server.

        For more information see https://redis.io/commands/flushall
        """
        ...
    def flushdb(self, asynchronous: bool = False, **kwargs: _CommandOptions) -> bool:
        """
        Delete all keys in the current database.

        ``asynchronous`` indicates whether the operation is
        executed asynchronously by the server.

        For more information see https://redis.io/commands/flushdb
        """
        ...
    def sync(self):
        """
        Initiates a replication stream from the master.

        For more information see https://redis.io/commands/sync
        """
        ...
    def psync(self, replicationid, offset):
        """
        Initiates a replication stream from the master.
        Newer version for `sync`.

        For more information see https://redis.io/commands/sync
        """
        ...
    def swapdb(self, first, second, **kwargs: _CommandOptions):
        """
        Swap two databases

        For more information see https://redis.io/commands/swapdb
        """
        ...
    def select(self, index, **kwargs: _CommandOptions):
        """
        Select the Redis logical database at index.

        See: https://redis.io/commands/select
        """
        ...
    def info(self, section: _Key | None = None, *args: _Key, **kwargs: _CommandOptions) -> Mapping[str, Any]:
        """
        Returns a dictionary containing information about the Redis server

        The ``section`` option can be used to select a specific section
        of information

        The section option is not supported by older versions of Redis Server,
        and will generate ResponseError

        For more information see https://redis.io/commands/info
        """
        ...
    def lastsave(self, **kwargs: _CommandOptions):
        """
        Return a Python datetime object representing the last time the
        Redis database was saved to disk

        For more information see https://redis.io/commands/lastsave
        """
        ...
    def lolwut(self, *version_numbers: _Value, **kwargs: _CommandOptions) -> bytes:
        """
        Get the Redis version and a piece of generative computer art

        See: https://redis.io/commands/lolwut
        """
        ...
    def reset(self) -> None:
        """
        Perform a full reset on the connection's server side contenxt.

        See: https://redis.io/commands/reset
        """
        ...
    def migrate(
        self,
        host,
        port,
        keys,
        destination_db,
        timeout,
        copy: bool = False,
        replace: bool = False,
        auth: Incomplete | None = None,
        **kwargs: _CommandOptions,
    ):
        """
        Migrate 1 or more keys from the current Redis server to a different
        server specified by the ``host``, ``port`` and ``destination_db``.

        The ``timeout``, specified in milliseconds, indicates the maximum
        time the connection between the two servers can be idle before the
        command is interrupted.

        If ``copy`` is True, the specified ``keys`` are NOT deleted from
        the source server.

        If ``replace`` is True, this operation will overwrite the keys
        on the destination server if they exist.

        If ``auth`` is specified, authenticate to the destination server with
        the password provided.

        For more information see https://redis.io/commands/migrate
        """
        ...
    def object(self, infotype, key, **kwargs: _CommandOptions):
        """Return the encoding, idletime, or refcount about the key"""
        ...
    def memory_doctor(self, **kwargs: _CommandOptions): ...
    def memory_help(self, **kwargs: _CommandOptions): ...
    def memory_stats(self, **kwargs: _CommandOptions) -> dict[str, Any]:
        """
        Return a dictionary of memory stats

        For more information see https://redis.io/commands/memory-stats
        """
        ...
    def memory_malloc_stats(self, **kwargs: _CommandOptions):
        """
        Return an internal statistics report from the memory allocator.

        See: https://redis.io/commands/memory-malloc-stats
        """
        ...
    def memory_usage(self, key, samples: Incomplete | None = None, **kwargs: _CommandOptions):
        """
        Return the total memory usage for key, its value and associated
        administrative overheads.

        For nested data structures, ``samples`` is the number of elements to
        sample. If left unspecified, the server's default is 5. Use 0 to sample
        all elements.

        For more information see https://redis.io/commands/memory-usage
        """
        ...
    def memory_purge(self, **kwargs: _CommandOptions):
        """
        Attempts to purge dirty pages for reclamation by allocator

        For more information see https://redis.io/commands/memory-purge
        """
        ...
    def ping(self, **kwargs: _CommandOptions) -> bool:
        """
        Ping the Redis server

        For more information see https://redis.io/commands/ping
        """
        ...
    def quit(self, **kwargs: _CommandOptions):
        """
        Ask the server to close the connection.

        For more information see https://redis.io/commands/quit
        """
        ...
    def replicaof(self, *args, **kwargs: _CommandOptions):
        """
        Update the replication settings of a redis replica, on the fly.
        Examples of valid arguments include:
            NO ONE (set no replication)
            host port (set to the host and port of a redis server)

        For more information see  https://redis.io/commands/replicaof
        """
        ...
    def save(self, **kwargs: _CommandOptions) -> bool:
        """
        Tell the Redis server to save its data to disk,
        blocking until the save is complete

        For more information see https://redis.io/commands/save
        """
        ...
    def shutdown(
        self,
        save: bool = False,
        nosave: bool = False,
        now: bool = False,
        force: bool = False,
        abort: bool = False,
        **kwargs: _CommandOptions,
    ) -> None:
        """
        Shutdown the Redis server.  If Redis has persistence configured,
        data will be flushed before shutdown.
        It is possible to specify modifiers to alter the behavior of the command:
        ``save`` will force a DB saving operation even if no save points are configured.
        ``nosave`` will prevent a DB saving operation even if one or more save points
        are configured.
        ``now`` skips waiting for lagging replicas, i.e. it bypasses the first step in
        the shutdown sequence.
        ``force`` ignores any errors that would normally prevent the server from exiting
        ``abort`` cancels an ongoing shutdown and cannot be combined with other flags.

        For more information see https://redis.io/commands/shutdown
        """
        ...
    def slaveof(self, host: Incomplete | None = None, port: Incomplete | None = None, **kwargs: _CommandOptions):
        """
        Set the server to be a replicated slave of the instance identified
        by the ``host`` and ``port``. If called without arguments, the
        instance is promoted to a master instead.

        For more information see https://redis.io/commands/slaveof
        """
        ...
    def slowlog_get(self, num: Incomplete | None = None, **kwargs: _CommandOptions):
        """
        Get the entries from the slowlog. If ``num`` is specified, get the
        most recent ``num`` items.

        For more information see https://redis.io/commands/slowlog-get
        """
        ...
    def slowlog_len(self, **kwargs: _CommandOptions):
        """
        Get the number of items in the slowlog

        For more information see https://redis.io/commands/slowlog-len
        """
        ...
    def slowlog_reset(self, **kwargs: _CommandOptions):
        """
        Remove all items in the slowlog

        For more information see https://redis.io/commands/slowlog-reset
        """
        ...
    def time(self, **kwargs: _CommandOptions):
        """
        Returns the server time as a 2-item tuple of ints:
        (seconds since epoch, microseconds into this second).

        For more information see https://redis.io/commands/time
        """
        ...
    def wait(self, num_replicas, timeout, **kwargs: _CommandOptions):
        """
        Redis synchronous replication
        That returns the number of replicas that processed the query when
        we finally have at least ``num_replicas``, or when the ``timeout`` was
        reached.

        For more information see https://redis.io/commands/wait
        """
        ...

class AsyncManagementCommands:
    async def bgrewriteaof(self, **kwargs: _CommandOptions):
        """
        Tell the Redis server to rewrite the AOF file from data in memory.

        For more information see https://redis.io/commands/bgrewriteaof
        """
        ...
    async def bgsave(self, schedule: bool = True, **kwargs: _CommandOptions):
        """
        Tell the Redis server to save its data to disk.  Unlike save(),
        this method is asynchronous and returns immediately.

        For more information see https://redis.io/commands/bgsave
        """
        ...
    async def role(self):
        """
        Provide information on the role of a Redis instance in
        the context of replication, by returning if the instance
        is currently a master, slave, or sentinel.

        For more information see https://redis.io/commands/role
        """
        ...
    async def client_kill(self, address: str, **kwargs: _CommandOptions) -> bool:
        """
        Disconnects the client at ``address`` (ip:port)

        For more information see https://redis.io/commands/client-kill
        """
        ...
    async def client_kill_filter(
        self,
        _id: Incomplete | None = None,
        _type: Incomplete | None = None,
        addr: Incomplete | None = None,
        skipme: Incomplete | None = None,
        laddr: Incomplete | None = None,
        user: Incomplete | None = None,
        **kwargs: _CommandOptions,
    ):
        """
        Disconnects client(s) using a variety of filter options
        :param _id: Kills a client by its unique ID field
        :param _type: Kills a client by type where type is one of 'normal',
        'master', 'slave' or 'pubsub'
        :param addr: Kills a client by its 'address:port'
        :param skipme: If True, then the client calling the command
        will not get killed even if it is identified by one of the filter
        options. If skipme is not provided, the server defaults to skipme=True
        :param laddr: Kills a client by its 'local (bind) address:port'
        :param user: Kills a client for a specific user name
        """
        ...
    async def client_info(self, **kwargs: _CommandOptions):
        """
        Returns information and statistics about the current
        client connection.

        For more information see https://redis.io/commands/client-info
        """
        ...
    async def client_list(
        self, _type: str | None = None, client_id: list[str] = [], **kwargs: _CommandOptions
    ) -> list[dict[str, str]]:
        """
        Returns a list of currently connected clients.
        If type of client specified, only that type will be returned.
        :param _type: optional. one of the client types (normal, master,
         replica, pubsub)
        :param client_id: optional. a list of client ids

        For more information see https://redis.io/commands/client-list
        """
        ...
    async def client_getname(self, **kwargs: _CommandOptions) -> str | None:
        """
        Returns the current connection name

        For more information see https://redis.io/commands/client-getname
        """
        ...
    async def client_getredir(self, **kwargs: _CommandOptions):
        """
        Returns the ID (an integer) of the client to whom we are
        redirecting tracking notifications.

        see: https://redis.io/commands/client-getredir
        """
        ...
    async def client_reply(self, reply, **kwargs: _CommandOptions):
        """
        Enable and disable redis server replies.
        ``reply`` Must be ON OFF or SKIP,
            ON - The default most with server replies to commands
            OFF - Disable server responses to commands
            SKIP - Skip the response of the immediately following command.

        Note: When setting OFF or SKIP replies, you will need a client object
        with a timeout specified in seconds, and will need to catch the
        TimeoutError.
              The test_client_reply unit test illustrates this, and
              conftest.py has a client with a timeout.

        See https://redis.io/commands/client-reply
        """
        ...
    async def client_id(self, **kwargs: _CommandOptions) -> int:
        """
        Returns the current connection id

        For more information see https://redis.io/commands/client-id
        """
        ...
    async def client_tracking_on(
        self,
        clientid: Incomplete | None = None,
        prefix=[],
        bcast: bool = False,
        optin: bool = False,
        optout: bool = False,
        noloop: bool = False,
    ):
        """
        Turn on the tracking mode.
        For more information about the options look at client_tracking func.

        See https://redis.io/commands/client-tracking
        """
        ...
    async def client_tracking_off(
        self,
        clientid: Incomplete | None = None,
        prefix=[],
        bcast: bool = False,
        optin: bool = False,
        optout: bool = False,
        noloop: bool = False,
    ):
        """
        Turn off the tracking mode.
        For more information about the options look at client_tracking func.

        See https://redis.io/commands/client-tracking
        """
        ...
    async def client_tracking(
        self,
        on: bool = True,
        clientid: Incomplete | None = None,
        prefix=[],
        bcast: bool = False,
        optin: bool = False,
        optout: bool = False,
        noloop: bool = False,
        **kwargs: _CommandOptions,
    ):
        """
        Enables the tracking feature of the Redis server, that is used
        for server assisted client side caching.

        ``on`` indicate for tracking on or tracking off. The dafualt is on.

        ``clientid`` send invalidation messages to the connection with
        the specified ID.

        ``bcast`` enable tracking in broadcasting mode. In this mode
        invalidation messages are reported for all the prefixes
        specified, regardless of the keys requested by the connection.

        ``optin``  when broadcasting is NOT active, normally don't track
        keys in read only commands, unless they are called immediately
        after a CLIENT CACHING yes command.

        ``optout`` when broadcasting is NOT active, normally track keys in
        read only commands, unless they are called immediately after a
        CLIENT CACHING no command.

        ``noloop`` don't send notifications about keys modified by this
        connection itself.

        ``prefix``  for broadcasting, register a given key prefix, so that
        notifications will be provided only for keys starting with this string.

        See https://redis.io/commands/client-tracking
        """
        ...
    async def client_trackinginfo(self, **kwargs: _CommandOptions):
        """
        Returns the information about the current client connection's
        use of the server assisted client side cache.

        See https://redis.io/commands/client-trackinginfo
        """
        ...
    async def client_setname(self, name: str, **kwargs: _CommandOptions) -> bool:
        """
        Sets the current connection name

        For more information see https://redis.io/commands/client-setname

        .. note::
           This method sets client name only for **current** connection.

           If you want to set a common name for all connections managed
           by this client, use ``client_name`` constructor argument.
        """
        ...
    async def client_unblock(self, client_id, error: bool = False, **kwargs: _CommandOptions):
        """
        Unblocks a connection by its client id.
        If ``error`` is True, unblocks the client with a special error message.
        If ``error`` is False (default), the client is unblocked using the
        regular timeout mechanism.

        For more information see https://redis.io/commands/client-unblock
        """
        ...
    async def client_pause(self, timeout, all: bool = True, **kwargs: _CommandOptions):
        """
        Suspend all the Redis clients for the specified amount of time
        :param timeout: milliseconds to pause clients

        For more information see https://redis.io/commands/client-pause
        :param all: If true (default) all client commands are blocked.
             otherwise, clients are only blocked if they attempt to execute
             a write command.
             For the WRITE mode, some commands have special behavior:
                 EVAL/EVALSHA: Will block client for all scripts.
                 PUBLISH: Will block client.
                 PFCOUNT: Will block client.
                 WAIT: Acknowledgments will be delayed, so this command will
                 appear blocked.
        """
        ...
    async def client_unpause(self, **kwargs: _CommandOptions):
        """
        Unpause all redis clients

        For more information see https://redis.io/commands/client-unpause
        """
        ...
    async def command(self, **kwargs: _CommandOptions):
        """
        Returns dict reply of details about all Redis commands.

        For more information see https://redis.io/commands/command
        """
        ...
    async def command_info(self, **kwargs: _CommandOptions): ...
    async def command_count(self, **kwargs: _CommandOptions): ...
    async def config_get(self, pattern: PatternT = "*", *args: PatternT, **kwargs: _CommandOptions):
        """
        Return a dictionary of configuration based on the ``pattern``

        For more information see https://redis.io/commands/config-get
        """
        ...
    async def config_set(self, name: KeyT, value: EncodableT, *args: KeyT | EncodableT, **kwargs: _CommandOptions):
        """
        Set config item ``name`` with ``value``

        For more information see https://redis.io/commands/config-set
        """
        ...
    async def config_resetstat(self, **kwargs: _CommandOptions):
        """
        Reset runtime statistics

        For more information see https://redis.io/commands/config-resetstat
        """
        ...
    async def config_rewrite(self, **kwargs: _CommandOptions):
        """
        Rewrite config file with the minimal change to reflect running config.

        For more information see https://redis.io/commands/config-rewrite
        """
        ...
    async def dbsize(self, **kwargs: _CommandOptions) -> int:
        """
        Returns the number of keys in the current database

        For more information see https://redis.io/commands/dbsize
        """
        ...
    async def debug_object(self, key, **kwargs: _CommandOptions):
        """
        Returns version specific meta information about a given key

        For more information see https://redis.io/commands/debug-object
        """
        ...
    async def debug_segfault(self, **kwargs: _CommandOptions): ...
    async def echo(self, value: _Value, **kwargs: _CommandOptions) -> bytes:
        """
        Echo the string back from the server

        For more information see https://redis.io/commands/echo
        """
        ...
    async def flushall(self, asynchronous: bool = False, **kwargs: _CommandOptions) -> bool:
        """
        Delete all keys in all databases on the current host.

        ``asynchronous`` indicates whether the operation is
        executed asynchronously by the server.

        For more information see https://redis.io/commands/flushall
        """
        ...
    async def flushdb(self, asynchronous: bool = False, **kwargs: _CommandOptions) -> bool:
        """
        Delete all keys in the current database.

        ``asynchronous`` indicates whether the operation is
        executed asynchronously by the server.

        For more information see https://redis.io/commands/flushdb
        """
        ...
    async def sync(self):
        """
        Initiates a replication stream from the master.

        For more information see https://redis.io/commands/sync
        """
        ...
    async def psync(self, replicationid, offset):
        """
        Initiates a replication stream from the master.
        Newer version for `sync`.

        For more information see https://redis.io/commands/sync
        """
        ...
    async def swapdb(self, first, second, **kwargs: _CommandOptions):
        """
        Swap two databases

        For more information see https://redis.io/commands/swapdb
        """
        ...
    async def select(self, index, **kwargs: _CommandOptions):
        """
        Select the Redis logical database at index.

        See: https://redis.io/commands/select
        """
        ...
    async def info(self, section: _Key | None = None, *args: _Key, **kwargs: _CommandOptions) -> Mapping[str, Any]:
        """
        Returns a dictionary containing information about the Redis server

        The ``section`` option can be used to select a specific section
        of information

        The section option is not supported by older versions of Redis Server,
        and will generate ResponseError

        For more information see https://redis.io/commands/info
        """
        ...
    async def lastsave(self, **kwargs: _CommandOptions):
        """
        Return a Python datetime object representing the last time the
        Redis database was saved to disk

        For more information see https://redis.io/commands/lastsave
        """
        ...
    async def lolwut(self, *version_numbers: _Value, **kwargs: _CommandOptions) -> bytes:
        """
        Get the Redis version and a piece of generative computer art

        See: https://redis.io/commands/lolwut
        """
        ...
    async def reset(self) -> None:
        """
        Perform a full reset on the connection's server side contenxt.

        See: https://redis.io/commands/reset
        """
        ...
    async def migrate(
        self,
        host,
        port,
        keys,
        destination_db,
        timeout,
        copy: bool = False,
        replace: bool = False,
        auth: Incomplete | None = None,
        **kwargs: _CommandOptions,
    ):
        """
        Migrate 1 or more keys from the current Redis server to a different
        server specified by the ``host``, ``port`` and ``destination_db``.

        The ``timeout``, specified in milliseconds, indicates the maximum
        time the connection between the two servers can be idle before the
        command is interrupted.

        If ``copy`` is True, the specified ``keys`` are NOT deleted from
        the source server.

        If ``replace`` is True, this operation will overwrite the keys
        on the destination server if they exist.

        If ``auth`` is specified, authenticate to the destination server with
        the password provided.

        For more information see https://redis.io/commands/migrate
        """
        ...
    async def object(self, infotype, key, **kwargs: _CommandOptions):
        """Return the encoding, idletime, or refcount about the key"""
        ...
    async def memory_doctor(self, **kwargs: _CommandOptions): ...
    async def memory_help(self, **kwargs: _CommandOptions): ...
    async def memory_stats(self, **kwargs: _CommandOptions) -> dict[str, Any]:
        """
        Return a dictionary of memory stats

        For more information see https://redis.io/commands/memory-stats
        """
        ...
    async def memory_malloc_stats(self, **kwargs: _CommandOptions):
        """
        Return an internal statistics report from the memory allocator.

        See: https://redis.io/commands/memory-malloc-stats
        """
        ...
    async def memory_usage(self, key, samples: Incomplete | None = None, **kwargs: _CommandOptions):
        """
        Return the total memory usage for key, its value and associated
        administrative overheads.

        For nested data structures, ``samples`` is the number of elements to
        sample. If left unspecified, the server's default is 5. Use 0 to sample
        all elements.

        For more information see https://redis.io/commands/memory-usage
        """
        ...
    async def memory_purge(self, **kwargs: _CommandOptions):
        """
        Attempts to purge dirty pages for reclamation by allocator

        For more information see https://redis.io/commands/memory-purge
        """
        ...
    async def ping(self, **kwargs: _CommandOptions) -> bool:
        """
        Ping the Redis server

        For more information see https://redis.io/commands/ping
        """
        ...
    async def quit(self, **kwargs: _CommandOptions):
        """
        Ask the server to close the connection.

        For more information see https://redis.io/commands/quit
        """
        ...
    async def replicaof(self, *args, **kwargs: _CommandOptions):
        """
        Update the replication settings of a redis replica, on the fly.
        Examples of valid arguments include:
            NO ONE (set no replication)
            host port (set to the host and port of a redis server)

        For more information see  https://redis.io/commands/replicaof
        """
        ...
    async def save(self, **kwargs: _CommandOptions) -> bool:
        """
        Tell the Redis server to save its data to disk,
        blocking until the save is complete

        For more information see https://redis.io/commands/save
        """
        ...
    async def shutdown(
        self,
        save: bool = False,
        nosave: bool = False,
        now: bool = False,
        force: bool = False,
        abort: bool = False,
        **kwargs: _CommandOptions,
    ) -> None:
        """
        Shutdown the Redis server.  If Redis has persistence configured,
        data will be flushed before shutdown.  If the "save" option is set,
        a data flush will be attempted even if there is no persistence
        configured.  If the "nosave" option is set, no data flush will be
        attempted.  The "save" and "nosave" options cannot both be set.

        For more information see https://redis.io/commands/shutdown
        """
        ...
    async def slaveof(self, host: Incomplete | None = None, port: Incomplete | None = None, **kwargs: _CommandOptions):
        """
        Set the server to be a replicated slave of the instance identified
        by the ``host`` and ``port``. If called without arguments, the
        instance is promoted to a master instead.

        For more information see https://redis.io/commands/slaveof
        """
        ...
    async def slowlog_get(self, num: Incomplete | None = None, **kwargs: _CommandOptions):
        """
        Get the entries from the slowlog. If ``num`` is specified, get the
        most recent ``num`` items.

        For more information see https://redis.io/commands/slowlog-get
        """
        ...
    async def slowlog_len(self, **kwargs: _CommandOptions):
        """
        Get the number of items in the slowlog

        For more information see https://redis.io/commands/slowlog-len
        """
        ...
    async def slowlog_reset(self, **kwargs: _CommandOptions):
        """
        Remove all items in the slowlog

        For more information see https://redis.io/commands/slowlog-reset
        """
        ...
    async def time(self, **kwargs: _CommandOptions):
        """
        Returns the server time as a 2-item tuple of ints:
        (seconds since epoch, microseconds into this second).

        For more information see https://redis.io/commands/time
        """
        ...
    async def wait(self, num_replicas, timeout, **kwargs: _CommandOptions):
        """
        Redis synchronous replication
        That returns the number of replicas that processed the query when
        we finally have at least ``num_replicas``, or when the ``timeout`` was
        reached.

        For more information see https://redis.io/commands/wait
        """
        ...

class BasicKeyCommands(Generic[_StrType]):
    """Redis basic key-based commands"""
    def append(self, key, value):
        """
        Appends the string ``value`` to the value at ``key``. If ``key``
        doesn't already exist, create it with a value of ``value``.
        Returns the new length of the value at ``key``.

        For more information see https://redis.io/commands/append
        """
        ...
    def bitcount(self, key: _Key, start: int | None = None, end: int | None = None, mode: str | None = None) -> int:
        """
        Returns the count of set bits in the value of ``key``.  Optional
        ``start`` and ``end`` parameters indicate which bytes to consider

        For more information see https://redis.io/commands/bitcount
        """
        ...
    def bitfield(self, key, default_overflow: Incomplete | None = None):
        """
        Return a BitFieldOperation instance to conveniently construct one or
        more bitfield operations on ``key``.

        For more information see https://redis.io/commands/bitfield
        """
        ...
    def bitop(self, operation, dest, *keys):
        """
        Perform a bitwise operation using ``operation`` between ``keys`` and
        store the result in ``dest``.

        For more information see https://redis.io/commands/bitop
        """
        ...
    def bitpos(self, key: _Key, bit: int, start: int | None = None, end: int | None = None, mode: str | None = None):
        """
        Return the position of the first bit set to 1 or 0 in a string.
        ``start`` and ``end`` defines search range. The range is interpreted
        as a range of bytes and not a range of bits, so start=0 and end=2
        means to look at the first three bytes.

        For more information see https://redis.io/commands/bitpos
        """
        ...
    def copy(self, source, destination, destination_db: Incomplete | None = None, replace: bool = False):
        """
        Copy the value stored in the ``source`` key to the ``destination`` key.

        ``destination_db`` an alternative destination database. By default,
        the ``destination`` key is created in the source Redis database.

        ``replace`` whether the ``destination`` key should be removed before
        copying the value to it. By default, the value is not copied if
        the ``destination`` key already exists.

        For more information see https://redis.io/commands/copy
        """
        ...
    def decr(self, name, amount: int = 1) -> int:
        """
        Decrements the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as 0 - ``amount``

        For more information see https://redis.io/commands/decrby
        """
        ...
    def decrby(self, name, amount: int = 1) -> int:
        """
        Decrements the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as 0 - ``amount``

        For more information see https://redis.io/commands/decrby
        """
        ...
    def delete(self, *names: _Key) -> int:
        """Delete one or more keys specified by ``names``"""
        ...
    def __delitem__(self, name: _Key) -> None: ...
    def dump(self, name: _Key) -> _StrType | None:
        """
        Return a serialized version of the value stored at the specified key.
        If key does not exist a nil bulk reply is returned.

        For more information see https://redis.io/commands/dump
        """
        ...
    def exists(self, *names: _Key) -> int:
        """
        Returns the number of ``names`` that exist

        For more information see https://redis.io/commands/exists
        """
        ...
    __contains__ = exists
    def expire(
        self, name: _Key, time: int | timedelta, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> bool:
        """
        Set an expire flag on key ``name`` for ``time`` seconds with given
        ``option``. ``time`` can be represented by an integer or a Python timedelta
        object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/expire
        """
        ...
    def expireat(self, name, when, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False):
        """
        Set an expire flag on key ``name`` with given ``option``. ``when``
        can be represented as an integer indicating unix time or a Python
        datetime object.

        Valid options are:
            -> NX -- Set expiry only when the key has no expiry
            -> XX -- Set expiry only when the key has an existing expiry
            -> GT -- Set expiry only when the new expiry is greater than current one
            -> LT -- Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/expireat
        """
        ...
    def get(self, name: _Key) -> _StrType | None:
        """
        Return the value at key ``name``, or None if the key doesn't exist

        For more information see https://redis.io/commands/get
        """
        ...
    def getdel(self, name: _Key) -> _StrType | None:
        """
        Get the value at key ``name`` and delete the key. This command
        is similar to GET, except for the fact that it also deletes
        the key on success (if and only if the key's value type
        is a string).

        For more information see https://redis.io/commands/getdel
        """
        ...
    def getex(
        self,
        name,
        ex: Incomplete | None = None,
        px: Incomplete | None = None,
        exat: Incomplete | None = None,
        pxat: Incomplete | None = None,
        persist: bool = False,
    ):
        """
        Get the value of key and optionally set its expiration.
        GETEX is similar to GET, but is a write command with
        additional options. All time parameters can be given as
        datetime.timedelta or integers.

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
        specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
        specified in unix time.

        ``persist`` remove the time to live associated with ``name``.

        For more information see https://redis.io/commands/getex
        """
        ...
    def __getitem__(self, name: str):
        """
        Return the value at key ``name``, raises a KeyError if the key
        doesn't exist.
        """
        ...
    def getbit(self, name: _Key, offset: int) -> int:
        """
        Returns an integer indicating the value of ``offset`` in ``name``

        For more information see https://redis.io/commands/getbit
        """
        ...
    def getrange(self, key, start, end):
        """
        Returns the substring of the string value stored at ``key``,
        determined by the offsets ``start`` and ``end`` (both are inclusive)

        For more information see https://redis.io/commands/getrange
        """
        ...
    def getset(self, name, value) -> _StrType | None:
        """
        Sets the value at key ``name`` to ``value``
        and returns the old value at key ``name`` atomically.

        As per Redis 6.2, GETSET is considered deprecated.
        Please use SET with GET parameter in new code.

        For more information see https://redis.io/commands/getset
        """
        ...
    def incr(self, name: _Key, amount: int = 1) -> int:
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrby
        """
        ...
    def incrby(self, name: _Key, amount: int = 1) -> int:
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrby
        """
        ...
    def incrbyfloat(self, name: _Key, amount: float = 1.0) -> float:
        """
        Increments the value at key ``name`` by floating ``amount``.
        If no key exists, the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrbyfloat
        """
        ...
    def keys(self, pattern: _Key = "*", **kwargs: _CommandOptions) -> list[_StrType]:
        """
        Returns a list of keys matching ``pattern``

        For more information see https://redis.io/commands/keys
        """
        ...
    def lmove(
        self,
        first_list: _Key,
        second_list: _Key,
        src: Literal["LEFT", "RIGHT"] = "LEFT",
        dest: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> _Value:
        """
        Atomically returns and removes the first/last element of a list,
        pushing it as the first/last element on the destination list.
        Returns the element being popped and pushed.

        For more information see https://redis.io/commands/lmove
        """
        ...
    def blmove(
        self,
        first_list: _Key,
        second_list: _Key,
        timeout: float,
        src: Literal["LEFT", "RIGHT"] = "LEFT",
        dest: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> _Value | None:
        """
        Blocking version of lmove.

        For more information see https://redis.io/commands/blmove
        """
        ...
    def mget(self, keys: _Key | Iterable[_Key], *args: _Key) -> list[_StrType | None]:
        """
        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/mget
        """
        ...
    def mset(self, mapping: Mapping[_Key, _Value]) -> Literal[True]:
        """
        Sets key/values based on a mapping. Mapping is a dictionary of
        key/value pairs. Both keys and values should be strings or types that
        can be cast to a string via str().

        For more information see https://redis.io/commands/mset
        """
        ...
    def msetnx(self, mapping: Mapping[_Key, _Value]) -> bool:
        """
        Sets key/values based on a mapping if none of the keys are already set.
        Mapping is a dictionary of key/value pairs. Both keys and values
        should be strings or types that can be cast to a string via str().
        Returns a boolean indicating if the operation was successful.

        For more information see https://redis.io/commands/msetnx
        """
        ...
    def move(self, name: _Key, db: int) -> bool:
        """
        Moves the key ``name`` to a different Redis database ``db``

        For more information see https://redis.io/commands/move
        """
        ...
    def persist(self, name: _Key) -> bool:
        """
        Removes an expiration on ``name``

        For more information see https://redis.io/commands/persist
        """
        ...
    def pexpire(
        self, name: _Key, time: int | timedelta, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Literal[1, 0]:
        """
        Set an expire flag on key ``name`` for ``time`` milliseconds
        with given ``option``. ``time`` can be represented by an
        integer or a Python timedelta object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/pexpire
        """
        ...
    def pexpireat(
        self, name: _Key, when: int | datetime, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Literal[1, 0]:
        """
        Set an expire flag on key ``name`` with given ``option``. ``when``
        can be represented as an integer representing unix time in
        milliseconds (unix time * 1000) or a Python datetime object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/pexpireat
        """
        ...
    def psetex(self, name, time_ms, value):
        """
        Set the value of key ``name`` to ``value`` that expires in ``time_ms``
        milliseconds. ``time_ms`` can be represented by an integer or a Python
        timedelta object

        For more information see https://redis.io/commands/psetex
        """
        ...
    def pttl(self, name: _Key) -> int:
        """
        Returns the number of milliseconds until the key ``name`` will expire

        For more information see https://redis.io/commands/pttl
        """
        ...
    def hrandfield(self, key, count: Incomplete | None = None, withvalues: bool = False):
        """
        Return a random field from the hash value stored at key.

        count: if the argument is positive, return an array of distinct fields.
        If called with a negative count, the behavior changes and the command
        is allowed to return the same field multiple times. In this case,
        the number of returned fields is the absolute value of the
        specified count.
        withvalues: The optional WITHVALUES modifier changes the reply so it
        includes the respective values of the randomly selected hash fields.

        For more information see https://redis.io/commands/hrandfield
        """
        ...
    def randomkey(self, **kwargs: _CommandOptions):
        """
        Returns the name of a random key

        For more information see https://redis.io/commands/randomkey
        """
        ...
    def rename(self, src, dst):
        """
        Rename key ``src`` to ``dst``

        For more information see https://redis.io/commands/rename
        """
        ...
    def renamenx(self, src, dst):
        """
        Rename key ``src`` to ``dst`` if ``dst`` doesn't already exist

        For more information see https://redis.io/commands/renamenx
        """
        ...
    def restore(
        self,
        name,
        ttl,
        value,
        replace: bool = False,
        absttl: bool = False,
        idletime: Incomplete | None = None,
        frequency: Incomplete | None = None,
    ):
        """
        Create a key using the provided serialized value, previously obtained
        using DUMP.

        ``replace`` allows an existing key on ``name`` to be overridden. If
        it's not specified an error is raised on collision.

        ``absttl`` if True, specified ``ttl`` should represent an absolute Unix
        timestamp in milliseconds in which the key will expire. (Redis 5.0 or
        greater).

        ``idletime`` Used for eviction, this is the number of seconds the
        key must be idle, prior to execution.

        ``frequency`` Used for eviction, this is the frequency counter of
        the object stored at the key, prior to execution.

        For more information see https://redis.io/commands/restore
        """
        ...
    def set(
        self,
        name: _Key,
        value: _Value,
        ex: None | float | timedelta = None,
        px: None | float | timedelta = None,
        nx: bool = False,
        xx: bool = False,
        keepttl: bool = False,
        get: bool = False,
        exat: Incomplete | None = None,
        pxat: Incomplete | None = None,
    ) -> bool | None:
        """
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``keepttl`` if True, retain the time to live associated with the key.
            (Available since Redis 6.0)

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
            specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
            specified in unix time.

        For more information see https://redis.io/commands/set
        """
        ...
    def __setitem__(self, name, value) -> None: ...
    def setbit(self, name: _Key, offset: int, value: int) -> int:
        """
        Flag the ``offset`` in ``name`` as ``value``. Returns an integer
        indicating the previous value of ``offset``.

        For more information see https://redis.io/commands/setbit
        """
        ...
    def setex(self, name: _Key, time: int | timedelta, value: _Value) -> bool:
        """
        Set the value of key ``name`` to ``value`` that expires in ``time``
        seconds. ``time`` can be represented by an integer or a Python
        timedelta object.

        For more information see https://redis.io/commands/setex
        """
        ...
    def setnx(self, name: _Key, value: _Value) -> bool:
        """
        Set the value of key ``name`` to ``value`` if key doesn't exist

        For more information see https://redis.io/commands/setnx
        """
        ...
    def setrange(self, name, offset, value):
        """
        Overwrite bytes in the value of ``name`` starting at ``offset`` with
        ``value``. If ``offset`` plus the length of ``value`` exceeds the
        length of the original value, the new value will be larger than before.
        If ``offset`` exceeds the length of the original value, null bytes
        will be used to pad between the end of the previous value and the start
        of what's being injected.

        Returns the length of the new string.

        For more information see https://redis.io/commands/setrange
        """
        ...
    def stralgo(
        self,
        algo,
        value1,
        value2,
        specific_argument: str = "strings",
        len: bool = False,
        idx: bool = False,
        minmatchlen: Incomplete | None = None,
        withmatchlen: bool = False,
        **kwargs: _CommandOptions,
    ):
        """
        Implements complex algorithms that operate on strings.
        Right now the only algorithm implemented is the LCS algorithm
        (longest common substring). However new algorithms could be
        implemented in the future.

        ``algo`` Right now must be LCS
        ``value1`` and ``value2`` Can be two strings or two keys
        ``specific_argument`` Specifying if the arguments to the algorithm
        will be keys or strings. strings is the default.
        ``len`` Returns just the len of the match.
        ``idx`` Returns the match positions in each string.
        ``minmatchlen`` Restrict the list of matches to the ones of a given
        minimal length. Can be provided only when ``idx`` set to True.
        ``withmatchlen`` Returns the matches with the len of the match.
        Can be provided only when ``idx`` set to True.

        For more information see https://redis.io/commands/stralgo
        """
        ...
    def strlen(self, name):
        """
        Return the number of bytes stored in the value of ``name``

        For more information see https://redis.io/commands/strlen
        """
        ...
    def substr(self, name, start, end: int = -1):
        """
        Return a substring of the string at key ``name``. ``start`` and ``end``
        are 0-based integers specifying the portion of the string to return.
        """
        ...
    def touch(self, *args):
        """
        Alters the last access time of a key(s) ``*args``. A key is ignored
        if it does not exist.

        For more information see https://redis.io/commands/touch
        """
        ...
    def ttl(self, name: _Key) -> int:
        """
        Returns the number of seconds until the key ``name`` will expire

        For more information see https://redis.io/commands/ttl
        """
        ...
    def type(self, name):
        """
        Returns the type of key ``name``

        For more information see https://redis.io/commands/type
        """
        ...
    def watch(self, *names):
        """
        Watches the values at keys ``names``, or None if the key doesn't exist

        For more information see https://redis.io/commands/watch
        """
        ...
    def unwatch(self):
        """
        Unwatches the value at key ``name``, or None of the key doesn't exist

        For more information see https://redis.io/commands/unwatch
        """
        ...
    def unlink(self, *names: _Key) -> int:
        """
        Unlink one or more keys specified by ``names``

        For more information see https://redis.io/commands/unlink
        """
        ...

class AsyncBasicKeyCommands(Generic[_StrType]):
    async def append(self, key, value):
        """
        Appends the string ``value`` to the value at ``key``. If ``key``
        doesn't already exist, create it with a value of ``value``.
        Returns the new length of the value at ``key``.

        For more information see https://redis.io/commands/append
        """
        ...
    async def bitcount(self, key: _Key, start: int | None = None, end: int | None = None, mode: str | None = None) -> int:
        """
        Returns the count of set bits in the value of ``key``.  Optional
        ``start`` and ``end`` parameters indicate which bytes to consider

        For more information see https://redis.io/commands/bitcount
        """
        ...
    async def bitfield(self, key, default_overflow: Incomplete | None = None):
        """
        Return a BitFieldOperation instance to conveniently construct one or
        more bitfield operations on ``key``.

        For more information see https://redis.io/commands/bitfield
        """
        ...
    async def bitop(self, operation, dest, *keys):
        """
        Perform a bitwise operation using ``operation`` between ``keys`` and
        store the result in ``dest``.

        For more information see https://redis.io/commands/bitop
        """
        ...
    async def bitpos(self, key: _Key, bit: int, start: int | None = None, end: int | None = None, mode: str | None = None):
        """
        Return the position of the first bit set to 1 or 0 in a string.
        ``start`` and ``end`` defines search range. The range is interpreted
        as a range of bytes and not a range of bits, so start=0 and end=2
        means to look at the first three bytes.

        For more information see https://redis.io/commands/bitpos
        """
        ...
    async def copy(self, source, destination, destination_db: Incomplete | None = None, replace: bool = False):
        """
        Copy the value stored in the ``source`` key to the ``destination`` key.

        ``destination_db`` an alternative destination database. By default,
        the ``destination`` key is created in the source Redis database.

        ``replace`` whether the ``destination`` key should be removed before
        copying the value to it. By default, the value is not copied if
        the ``destination`` key already exists.

        For more information see https://redis.io/commands/copy
        """
        ...
    async def decr(self, name, amount: int = 1) -> int:
        """
        Decrements the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as 0 - ``amount``

        For more information see https://redis.io/commands/decrby
        """
        ...
    async def decrby(self, name, amount: int = 1) -> int:
        """
        Decrements the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as 0 - ``amount``

        For more information see https://redis.io/commands/decrby
        """
        ...
    async def delete(self, *names: _Key) -> int:
        """Delete one or more keys specified by ``names``"""
        ...
    async def dump(self, name: _Key) -> _StrType | None:
        """
        Return a serialized version of the value stored at the specified key.
        If key does not exist a nil bulk reply is returned.

        For more information see https://redis.io/commands/dump
        """
        ...
    async def exists(self, *names: _Key) -> int:
        """
        Returns the number of ``names`` that exist

        For more information see https://redis.io/commands/exists
        """
        ...
    async def expire(
        self, name: _Key, time: int | timedelta, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> bool:
        """
        Set an expire flag on key ``name`` for ``time`` seconds with given
        ``option``. ``time`` can be represented by an integer or a Python timedelta
        object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/expire
        """
        ...
    async def expireat(self, name, when, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False):
        """
        Set an expire flag on key ``name`` with given ``option``. ``when``
        can be represented as an integer indicating unix time or a Python
        datetime object.

        Valid options are:
            -> NX -- Set expiry only when the key has no expiry
            -> XX -- Set expiry only when the key has an existing expiry
            -> GT -- Set expiry only when the new expiry is greater than current one
            -> LT -- Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/expireat
        """
        ...
    async def get(self, name: _Key) -> _StrType | None:
        """
        Return the value at key ``name``, or None if the key doesn't exist

        For more information see https://redis.io/commands/get
        """
        ...
    async def getdel(self, name: _Key) -> _StrType | None:
        """
        Get the value at key ``name`` and delete the key. This command
        is similar to GET, except for the fact that it also deletes
        the key on success (if and only if the key's value type
        is a string).

        For more information see https://redis.io/commands/getdel
        """
        ...
    async def getex(
        self,
        name,
        ex: Incomplete | None = None,
        px: Incomplete | None = None,
        exat: Incomplete | None = None,
        pxat: Incomplete | None = None,
        persist: bool = False,
    ):
        """
        Get the value of key and optionally set its expiration.
        GETEX is similar to GET, but is a write command with
        additional options. All time parameters can be given as
        datetime.timedelta or integers.

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
        specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
        specified in unix time.

        ``persist`` remove the time to live associated with ``name``.

        For more information see https://redis.io/commands/getex
        """
        ...
    async def getbit(self, name: _Key, offset: int) -> int:
        """
        Returns an integer indicating the value of ``offset`` in ``name``

        For more information see https://redis.io/commands/getbit
        """
        ...
    async def getrange(self, key, start, end):
        """
        Returns the substring of the string value stored at ``key``,
        determined by the offsets ``start`` and ``end`` (both are inclusive)

        For more information see https://redis.io/commands/getrange
        """
        ...
    async def getset(self, name, value) -> _StrType | None:
        """
        Sets the value at key ``name`` to ``value``
        and returns the old value at key ``name`` atomically.

        As per Redis 6.2, GETSET is considered deprecated.
        Please use SET with GET parameter in new code.

        For more information see https://redis.io/commands/getset
        """
        ...
    async def incr(self, name: _Key, amount: int = 1) -> int:
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrby
        """
        ...
    async def incrby(self, name: _Key, amount: int = 1) -> int:
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrby
        """
        ...
    async def incrbyfloat(self, name: _Key, amount: float = 1.0) -> float:
        """
        Increments the value at key ``name`` by floating ``amount``.
        If no key exists, the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrbyfloat
        """
        ...
    async def keys(self, pattern: _Key = "*", **kwargs: _CommandOptions) -> list[_StrType]:
        """
        Returns a list of keys matching ``pattern``

        For more information see https://redis.io/commands/keys
        """
        ...
    async def lmove(
        self,
        first_list: _Key,
        second_list: _Key,
        src: Literal["LEFT", "RIGHT"] = "LEFT",
        dest: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> _Value:
        """
        Atomically returns and removes the first/last element of a list,
        pushing it as the first/last element on the destination list.
        Returns the element being popped and pushed.

        For more information see https://redis.io/commands/lmove
        """
        ...
    async def blmove(
        self,
        first_list: _Key,
        second_list: _Key,
        timeout: float,
        src: Literal["LEFT", "RIGHT"] = "LEFT",
        dest: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> _Value | None:
        """
        Blocking version of lmove.

        For more information see https://redis.io/commands/blmove
        """
        ...
    async def mget(self, keys: _Key | Iterable[_Key], *args: _Key) -> list[_StrType | None]:
        """
        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/mget
        """
        ...
    async def mset(self, mapping: Mapping[_Key, _Value]) -> Literal[True]:
        """
        Sets key/values based on a mapping. Mapping is a dictionary of
        key/value pairs. Both keys and values should be strings or types that
        can be cast to a string via str().

        For more information see https://redis.io/commands/mset
        """
        ...
    async def msetnx(self, mapping: Mapping[_Key, _Value]) -> bool:
        """
        Sets key/values based on a mapping if none of the keys are already set.
        Mapping is a dictionary of key/value pairs. Both keys and values
        should be strings or types that can be cast to a string via str().
        Returns a boolean indicating if the operation was successful.

        For more information see https://redis.io/commands/msetnx
        """
        ...
    async def move(self, name: _Key, db: int) -> bool:
        """
        Moves the key ``name`` to a different Redis database ``db``

        For more information see https://redis.io/commands/move
        """
        ...
    async def persist(self, name: _Key) -> bool:
        """
        Removes an expiration on ``name``

        For more information see https://redis.io/commands/persist
        """
        ...
    async def pexpire(
        self, name: _Key, time: int | timedelta, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Literal[1, 0]:
        """
        Set an expire flag on key ``name`` for ``time`` milliseconds
        with given ``option``. ``time`` can be represented by an
        integer or a Python timedelta object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/pexpire
        """
        ...
    async def pexpireat(
        self, name: _Key, when: int | datetime, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Literal[1, 0]:
        """
        Set an expire flag on key ``name`` with given ``option``. ``when``
        can be represented as an integer representing unix time in
        milliseconds (unix time * 1000) or a Python datetime object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/pexpireat
        """
        ...
    async def psetex(self, name, time_ms, value):
        """
        Set the value of key ``name`` to ``value`` that expires in ``time_ms``
        milliseconds. ``time_ms`` can be represented by an integer or a Python
        timedelta object

        For more information see https://redis.io/commands/psetex
        """
        ...
    async def pttl(self, name: _Key) -> int:
        """
        Returns the number of milliseconds until the key ``name`` will expire

        For more information see https://redis.io/commands/pttl
        """
        ...
    async def hrandfield(self, key, count: Incomplete | None = None, withvalues: bool = False):
        """
        Return a random field from the hash value stored at key.

        count: if the argument is positive, return an array of distinct fields.
        If called with a negative count, the behavior changes and the command
        is allowed to return the same field multiple times. In this case,
        the number of returned fields is the absolute value of the
        specified count.
        withvalues: The optional WITHVALUES modifier changes the reply so it
        includes the respective values of the randomly selected hash fields.

        For more information see https://redis.io/commands/hrandfield
        """
        ...
    async def randomkey(self, **kwargs: _CommandOptions):
        """
        Returns the name of a random key

        For more information see https://redis.io/commands/randomkey
        """
        ...
    async def rename(self, src, dst):
        """
        Rename key ``src`` to ``dst``

        For more information see https://redis.io/commands/rename
        """
        ...
    async def renamenx(self, src, dst):
        """
        Rename key ``src`` to ``dst`` if ``dst`` doesn't already exist

        For more information see https://redis.io/commands/renamenx
        """
        ...
    async def restore(
        self,
        name,
        ttl,
        value,
        replace: bool = False,
        absttl: bool = False,
        idletime: Incomplete | None = None,
        frequency: Incomplete | None = None,
    ):
        """
        Create a key using the provided serialized value, previously obtained
        using DUMP.

        ``replace`` allows an existing key on ``name`` to be overridden. If
        it's not specified an error is raised on collision.

        ``absttl`` if True, specified ``ttl`` should represent an absolute Unix
        timestamp in milliseconds in which the key will expire. (Redis 5.0 or
        greater).

        ``idletime`` Used for eviction, this is the number of seconds the
        key must be idle, prior to execution.

        ``frequency`` Used for eviction, this is the frequency counter of
        the object stored at the key, prior to execution.

        For more information see https://redis.io/commands/restore
        """
        ...
    async def set(
        self,
        name: _Key,
        value: _Value,
        ex: None | float | timedelta = None,
        px: None | float | timedelta = None,
        nx: bool = False,
        xx: bool = False,
        keepttl: bool = False,
        get: bool = False,
        exat: Incomplete | None = None,
        pxat: Incomplete | None = None,
    ) -> bool | None:
        """
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``keepttl`` if True, retain the time to live associated with the key.
            (Available since Redis 6.0)

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
            specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
            specified in unix time.

        For more information see https://redis.io/commands/set
        """
        ...
    async def setbit(self, name: _Key, offset: int, value: int) -> int:
        """
        Flag the ``offset`` in ``name`` as ``value``. Returns an integer
        indicating the previous value of ``offset``.

        For more information see https://redis.io/commands/setbit
        """
        ...
    async def setex(self, name: _Key, time: int | timedelta, value: _Value) -> bool:
        """
        Set the value of key ``name`` to ``value`` that expires in ``time``
        seconds. ``time`` can be represented by an integer or a Python
        timedelta object.

        For more information see https://redis.io/commands/setex
        """
        ...
    async def setnx(self, name: _Key, value: _Value) -> bool:
        """
        Set the value of key ``name`` to ``value`` if key doesn't exist

        For more information see https://redis.io/commands/setnx
        """
        ...
    async def setrange(self, name, offset, value):
        """
        Overwrite bytes in the value of ``name`` starting at ``offset`` with
        ``value``. If ``offset`` plus the length of ``value`` exceeds the
        length of the original value, the new value will be larger than before.
        If ``offset`` exceeds the length of the original value, null bytes
        will be used to pad between the end of the previous value and the start
        of what's being injected.

        Returns the length of the new string.

        For more information see https://redis.io/commands/setrange
        """
        ...
    async def stralgo(
        self,
        algo,
        value1,
        value2,
        specific_argument: str = "strings",
        len: bool = False,
        idx: bool = False,
        minmatchlen: Incomplete | None = None,
        withmatchlen: bool = False,
        **kwargs: _CommandOptions,
    ):
        """
        Implements complex algorithms that operate on strings.
        Right now the only algorithm implemented is the LCS algorithm
        (longest common substring). However new algorithms could be
        implemented in the future.

        ``algo`` Right now must be LCS
        ``value1`` and ``value2`` Can be two strings or two keys
        ``specific_argument`` Specifying if the arguments to the algorithm
        will be keys or strings. strings is the default.
        ``len`` Returns just the len of the match.
        ``idx`` Returns the match positions in each string.
        ``minmatchlen`` Restrict the list of matches to the ones of a given
        minimal length. Can be provided only when ``idx`` set to True.
        ``withmatchlen`` Returns the matches with the len of the match.
        Can be provided only when ``idx`` set to True.

        For more information see https://redis.io/commands/stralgo
        """
        ...
    async def strlen(self, name):
        """
        Return the number of bytes stored in the value of ``name``

        For more information see https://redis.io/commands/strlen
        """
        ...
    async def substr(self, name, start, end: int = -1):
        """
        Return a substring of the string at key ``name``. ``start`` and ``end``
        are 0-based integers specifying the portion of the string to return.
        """
        ...
    async def touch(self, *args):
        """
        Alters the last access time of a key(s) ``*args``. A key is ignored
        if it does not exist.

        For more information see https://redis.io/commands/touch
        """
        ...
    async def ttl(self, name: _Key) -> int:
        """
        Returns the number of seconds until the key ``name`` will expire

        For more information see https://redis.io/commands/ttl
        """
        ...
    async def type(self, name):
        """
        Returns the type of key ``name``

        For more information see https://redis.io/commands/type
        """
        ...
    async def watch(self, *names): ...
    async def unwatch(self): ...
    async def unlink(self, *names: _Key) -> int:
        """
        Unlink one or more keys specified by ``names``

        For more information see https://redis.io/commands/unlink
        """
        ...
    def __getitem__(self, name: str): ...
    def __setitem__(self, name, value) -> None: ...
    def __delitem__(self, name: _Key) -> None: ...
    def __contains__(self, name: _Key) -> None: ...

class ListCommands(Generic[_StrType]):
    """
    Redis commands for List data type.
    see: https://redis.io/topics/data-types#lists
    """
    @overload
    def blpop(self, keys: _Value | Iterable[_Value], timeout: Literal[0] | None = 0) -> tuple[_StrType, _StrType]:
        """
        LPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to LPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/blpop
        """
        ...
    @overload
    def blpop(self, keys: _Value | Iterable[_Value], timeout: float) -> tuple[_StrType, _StrType] | None:
        """
        LPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to LPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/blpop
        """
        ...
    @overload
    def brpop(self, keys: _Value | Iterable[_Value], timeout: Literal[0] | None = 0) -> tuple[_StrType, _StrType]:
        """
        RPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to RPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/brpop
        """
        ...
    @overload
    def brpop(self, keys: _Value | Iterable[_Value], timeout: float) -> tuple[_StrType, _StrType] | None:
        """
        RPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to RPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/brpop
        """
        ...
    def brpoplpush(self, src, dst, timeout: int | None = 0):
        """
        Pop a value off the tail of ``src``, push it on the head of ``dst``
        and then return it.

        This command blocks until a value is in ``src`` or until ``timeout``
        seconds elapse, whichever is first. A ``timeout`` value of 0 blocks
        forever.

        For more information see https://redis.io/commands/brpoplpush
        """
        ...
    def lindex(self, name: _Key, index: int) -> _StrType | None:
        """
        Return the item from list ``name`` at position ``index``

        Negative indexes are supported and will return an item at the
        end of the list

        For more information see https://redis.io/commands/lindex
        """
        ...
    def linsert(
        self, name: _Key, where: Literal["BEFORE", "AFTER", "before", "after"], refvalue: _Value, value: _Value
    ) -> int:
        """
        Insert ``value`` in list ``name`` either immediately before or after
        [``where``] ``refvalue``

        Returns the new length of the list on success or -1 if ``refvalue``
        is not in the list.

        For more information see https://redis.io/commands/linsert
        """
        ...
    def llen(self, name: _Key) -> int:
        """
        Return the length of the list ``name``

        For more information see https://redis.io/commands/llen
        """
        ...
    def lpop(self, name, count: int | None = None):
        """
        Removes and returns the first elements of the list ``name``.

        By default, the command pops a single element from the beginning of
        the list. When provided with the optional ``count`` argument, the reply
        will consist of up to count elements, depending on the list's length.

        For more information see https://redis.io/commands/lpop
        """
        ...
    def lpush(self, name: _Value, *values: _Value) -> int:
        """
        Push ``values`` onto the head of the list ``name``

        For more information see https://redis.io/commands/lpush
        """
        ...
    def lpushx(self, name, value):
        """
        Push ``value`` onto the head of the list ``name`` if ``name`` exists

        For more information see https://redis.io/commands/lpushx
        """
        ...
    def lrange(self, name: _Key, start: int, end: int) -> list[_StrType]:
        """
        Return a slice of the list ``name`` between
        position ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation

        For more information see https://redis.io/commands/lrange
        """
        ...
    def lrem(self, name: _Key, count: int, value: _Value) -> int:
        """
        Remove the first ``count`` occurrences of elements equal to ``value``
        from the list stored at ``name``.

        The count argument influences the operation in the following ways:
            count > 0: Remove elements equal to value moving from head to tail.
            count < 0: Remove elements equal to value moving from tail to head.
            count = 0: Remove all elements equal to value.

            For more information see https://redis.io/commands/lrem
        """
        ...
    def lset(self, name: _Key, index: int, value: _Value) -> bool:
        """
        Set element at ``index`` of list ``name`` to ``value``

        For more information see https://redis.io/commands/lset
        """
        ...
    def ltrim(self, name: _Key, start: int, end: int) -> bool:
        """
        Trim the list ``name``, removing all values not within the slice
        between ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation

        For more information see https://redis.io/commands/ltrim
        """
        ...
    def rpop(self, name, count: int | None = None):
        """
        Removes and returns the last elements of the list ``name``.

        By default, the command pops a single element from the end of the list.
        When provided with the optional ``count`` argument, the reply will
        consist of up to count elements, depending on the list's length.

        For more information see https://redis.io/commands/rpop
        """
        ...
    def rpoplpush(self, src, dst):
        """
        RPOP a value off of the ``src`` list and atomically LPUSH it
        on to the ``dst`` list.  Returns the value.

        For more information see https://redis.io/commands/rpoplpush
        """
        ...
    def rpush(self, name: _Value, *values: _Value) -> int:
        """
        Push ``values`` onto the tail of the list ``name``

        For more information see https://redis.io/commands/rpush
        """
        ...
    def rpushx(self, name, value):
        """
        Push ``value`` onto the tail of the list ``name`` if ``name`` exists

        For more information see https://redis.io/commands/rpushx
        """
        ...
    def lpos(
        self, name, value, rank: Incomplete | None = None, count: Incomplete | None = None, maxlen: Incomplete | None = None
    ):
        """
        Get position of ``value`` within the list ``name``

         If specified, ``rank`` indicates the "rank" of the first element to
         return in case there are multiple copies of ``value`` in the list.
         By default, LPOS returns the position of the first occurrence of
         ``value`` in the list. When ``rank`` 2, LPOS returns the position of
         the second ``value`` in the list. If ``rank`` is negative, LPOS
         searches the list in reverse. For example, -1 would return the
         position of the last occurrence of ``value`` and -2 would return the
         position of the next to last occurrence of ``value``.

         If specified, ``count`` indicates that LPOS should return a list of
         up to ``count`` positions. A ``count`` of 2 would return a list of
         up to 2 positions. A ``count`` of 0 returns a list of all positions
         matching ``value``. When ``count`` is specified and but ``value``
         does not exist in the list, an empty list is returned.

         If specified, ``maxlen`` indicates the maximum number of list
         elements to scan. A ``maxlen`` of 1000 will only return the
         position(s) of items within the first 1000 entries in the list.
         A ``maxlen`` of 0 (the default) will scan the entire list.

         For more information see https://redis.io/commands/lpos
        """
        ...
    @overload
    def sort(
        self,
        name: _Key,
        start: int | None = None,
        num: int | None = None,
        by: _Key | None = None,
        get: _Key | Sequence[_Key] | None = None,
        desc: bool = False,
        alpha: bool = False,
        store: None = None,
        groups: bool = False,
    ) -> list[_StrType]:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...
    @overload
    def sort(
        self,
        name: _Key,
        start: int | None = None,
        num: int | None = None,
        by: _Key | None = None,
        get: _Key | Sequence[_Key] | None = None,
        desc: bool = False,
        alpha: bool = False,
        *,
        store: _Key,
        groups: bool = False,
    ) -> int:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...
    @overload
    def sort(
        self,
        name: _Key,
        start: int | None,
        num: int | None,
        by: _Key | None,
        get: _Key | Sequence[_Key] | None,
        desc: bool,
        alpha: bool,
        store: _Key,
        groups: bool = False,
    ) -> int:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...

class AsyncListCommands(Generic[_StrType]):
    """
    Redis commands for List data type.
    see: https://redis.io/topics/data-types#lists
    """
    @overload
    async def blpop(self, keys: _Value | Iterable[_Value], timeout: Literal[0] | None = 0) -> tuple[_StrType, _StrType]:
        """
        LPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to LPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/blpop
        """
        ...
    @overload
    async def blpop(self, keys: _Value | Iterable[_Value], timeout: float) -> tuple[_StrType, _StrType] | None:
        """
        LPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to LPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/blpop
        """
        ...
    @overload
    async def brpop(self, keys: _Value | Iterable[_Value], timeout: Literal[0] | None = 0) -> tuple[_StrType, _StrType]:
        """
        RPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to RPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/brpop
        """
        ...
    @overload
    async def brpop(self, keys: _Value | Iterable[_Value], timeout: float) -> tuple[_StrType, _StrType] | None:
        """
        RPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to RPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/brpop
        """
        ...
    async def brpoplpush(self, src, dst, timeout: int | None = 0):
        """
        Pop a value off the tail of ``src``, push it on the head of ``dst``
        and then return it.

        This command blocks until a value is in ``src`` or until ``timeout``
        seconds elapse, whichever is first. A ``timeout`` value of 0 blocks
        forever.

        For more information see https://redis.io/commands/brpoplpush
        """
        ...
    async def lindex(self, name: _Key, index: int) -> _StrType | None:
        """
        Return the item from list ``name`` at position ``index``

        Negative indexes are supported and will return an item at the
        end of the list

        For more information see https://redis.io/commands/lindex
        """
        ...
    async def linsert(
        self, name: _Key, where: Literal["BEFORE", "AFTER", "before", "after"], refvalue: _Value, value: _Value
    ) -> int:
        """
        Insert ``value`` in list ``name`` either immediately before or after
        [``where``] ``refvalue``

        Returns the new length of the list on success or -1 if ``refvalue``
        is not in the list.

        For more information see https://redis.io/commands/linsert
        """
        ...
    async def llen(self, name: _Key) -> int:
        """
        Return the length of the list ``name``

        For more information see https://redis.io/commands/llen
        """
        ...
    async def lpop(self, name, count: int | None = None):
        """
        Removes and returns the first elements of the list ``name``.

        By default, the command pops a single element from the beginning of
        the list. When provided with the optional ``count`` argument, the reply
        will consist of up to count elements, depending on the list's length.

        For more information see https://redis.io/commands/lpop
        """
        ...
    async def lpush(self, name: _Value, *values: _Value) -> int:
        """
        Push ``values`` onto the head of the list ``name``

        For more information see https://redis.io/commands/lpush
        """
        ...
    async def lpushx(self, name, value):
        """
        Push ``value`` onto the head of the list ``name`` if ``name`` exists

        For more information see https://redis.io/commands/lpushx
        """
        ...
    async def lrange(self, name: _Key, start: int, end: int) -> list[_StrType]:
        """
        Return a slice of the list ``name`` between
        position ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation

        For more information see https://redis.io/commands/lrange
        """
        ...
    async def lrem(self, name: _Key, count: int, value: _Value) -> int:
        """
        Remove the first ``count`` occurrences of elements equal to ``value``
        from the list stored at ``name``.

        The count argument influences the operation in the following ways:
            count > 0: Remove elements equal to value moving from head to tail.
            count < 0: Remove elements equal to value moving from tail to head.
            count = 0: Remove all elements equal to value.

            For more information see https://redis.io/commands/lrem
        """
        ...
    async def lset(self, name: _Key, index: int, value: _Value) -> bool:
        """
        Set element at ``index`` of list ``name`` to ``value``

        For more information see https://redis.io/commands/lset
        """
        ...
    async def ltrim(self, name: _Key, start: int, end: int) -> bool:
        """
        Trim the list ``name``, removing all values not within the slice
        between ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation

        For more information see https://redis.io/commands/ltrim
        """
        ...
    async def rpop(self, name, count: int | None = None):
        """
        Removes and returns the last elements of the list ``name``.

        By default, the command pops a single element from the end of the list.
        When provided with the optional ``count`` argument, the reply will
        consist of up to count elements, depending on the list's length.

        For more information see https://redis.io/commands/rpop
        """
        ...
    async def rpoplpush(self, src, dst):
        """
        RPOP a value off of the ``src`` list and atomically LPUSH it
        on to the ``dst`` list.  Returns the value.

        For more information see https://redis.io/commands/rpoplpush
        """
        ...
    async def rpush(self, name: _Value, *values: _Value) -> int:
        """
        Push ``values`` onto the tail of the list ``name``

        For more information see https://redis.io/commands/rpush
        """
        ...
    async def rpushx(self, name, value):
        """
        Push ``value`` onto the tail of the list ``name`` if ``name`` exists

        For more information see https://redis.io/commands/rpushx
        """
        ...
    async def lpos(
        self, name, value, rank: Incomplete | None = None, count: Incomplete | None = None, maxlen: Incomplete | None = None
    ):
        """
        Get position of ``value`` within the list ``name``

         If specified, ``rank`` indicates the "rank" of the first element to
         return in case there are multiple copies of ``value`` in the list.
         By default, LPOS returns the position of the first occurrence of
         ``value`` in the list. When ``rank`` 2, LPOS returns the position of
         the second ``value`` in the list. If ``rank`` is negative, LPOS
         searches the list in reverse. For example, -1 would return the
         position of the last occurrence of ``value`` and -2 would return the
         position of the next to last occurrence of ``value``.

         If specified, ``count`` indicates that LPOS should return a list of
         up to ``count`` positions. A ``count`` of 2 would return a list of
         up to 2 positions. A ``count`` of 0 returns a list of all positions
         matching ``value``. When ``count`` is specified and but ``value``
         does not exist in the list, an empty list is returned.

         If specified, ``maxlen`` indicates the maximum number of list
         elements to scan. A ``maxlen`` of 1000 will only return the
         position(s) of items within the first 1000 entries in the list.
         A ``maxlen`` of 0 (the default) will scan the entire list.

         For more information see https://redis.io/commands/lpos
        """
        ...
    @overload
    async def sort(
        self,
        name: _Key,
        start: int | None = None,
        num: int | None = None,
        by: _Key | None = None,
        get: _Key | Sequence[_Key] | None = None,
        desc: bool = False,
        alpha: bool = False,
        store: None = None,
        groups: bool = False,
    ) -> list[_StrType]:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...
    @overload
    async def sort(
        self,
        name: _Key,
        start: int | None = None,
        num: int | None = None,
        by: _Key | None = None,
        get: _Key | Sequence[_Key] | None = None,
        desc: bool = False,
        alpha: bool = False,
        *,
        store: _Key,
        groups: bool = False,
    ) -> int:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...
    @overload
    async def sort(
        self,
        name: _Key,
        start: int | None,
        num: int | None,
        by: _Key | None,
        get: _Key | Sequence[_Key] | None,
        desc: bool,
        alpha: bool,
        store: _Key,
        groups: bool = False,
    ) -> int:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...

class ScanCommands(Generic[_StrType]):
    """
    Redis SCAN commands.
    see: https://redis.io/commands/scan
    """
    def scan(
        self,
        cursor: int = 0,
        match: _Key | None = None,
        count: int | None = None,
        _type: str | None = None,
        **kwargs: _CommandOptions,
    ) -> tuple[int, list[_StrType]]:
        """
        Incrementally return lists of key names. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` provides a hint to Redis about the number of keys to
            return per batch.

        ``_type`` filters the returned values by a particular Redis type.
            Stock Redis instances allow for the following types:
            HASH, LIST, SET, STREAM, STRING, ZSET
            Additionally, Redis modules can expose other types as well.

        For more information see https://redis.io/commands/scan
        """
        ...
    def scan_iter(
        self, match: _Key | None = None, count: int | None = None, _type: str | None = None, **kwargs: _CommandOptions
    ) -> Iterator[_StrType]:
        """
        Make an iterator using the SCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` provides a hint to Redis about the number of keys to
            return per batch.

        ``_type`` filters the returned values by a particular Redis type.
            Stock Redis instances allow for the following types:
            HASH, LIST, SET, STREAM, STRING, ZSET
            Additionally, Redis modules can expose other types as well.
        """
        ...
    def sscan(
        self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None
    ) -> tuple[int, list[_StrType]]:
        """
        Incrementally return lists of elements in a set. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        For more information see https://redis.io/commands/sscan
        """
        ...
    def sscan_iter(self, name: _Key, match: _Key | None = None, count: int | None = None) -> Iterator[_StrType]:
        """
        Make an iterator using the SSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        ...
    def hscan(
        self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None
    ) -> tuple[int, dict[_StrType, _StrType]]:
        """
        Incrementally return key/value slices in a hash. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        For more information see https://redis.io/commands/hscan
        """
        ...
    def hscan_iter(
        self, name: _Key, match: _Key | None = None, count: int | None = None
    ) -> Iterator[tuple[_StrType, _StrType]]:
        """
        Make an iterator using the HSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        ...
    @overload
    def zscan(
        self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None
    ) -> tuple[int, list[tuple[_StrType, float]]]:
        """
        Incrementally return lists of elements in a sorted set. Also return a
        cursor indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zscan
        """
        ...
    @overload
    def zscan(
        self,
        name: _Key,
        cursor: int = 0,
        match: _Key | None = None,
        count: int | None = None,
        *,
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> tuple[int, list[tuple[_StrType, _ScoreCastFuncReturn]]]:
        """
        Incrementally return lists of elements in a sorted set. Also return a
        cursor indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zscan
        """
        ...
    @overload
    def zscan(
        self,
        name: _Key,
        cursor: int,
        match: _Key | None,
        count: int | None,
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> tuple[int, list[tuple[_StrType, _ScoreCastFuncReturn]]]:
        """
        Incrementally return lists of elements in a sorted set. Also return a
        cursor indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zscan
        """
        ...
    @overload
    def zscan_iter(self, name: _Key, match: _Key | None = None, count: int | None = None) -> Iterator[tuple[_StrType, float]]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...
    @overload
    def zscan_iter(
        self,
        name: _Key,
        match: _Key | None = None,
        count: int | None = None,
        *,
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> Iterator[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...
    @overload
    def zscan_iter(
        self, name: _Key, match: _Key | None, count: int | None, score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn]
    ) -> Iterator[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...

class AsyncScanCommands(Generic[_StrType]):
    async def scan(
        self,
        cursor: int = 0,
        match: _Key | None = None,
        count: int | None = None,
        _type: str | None = None,
        **kwargs: _CommandOptions,
    ) -> tuple[int, list[_StrType]]:
        """
        Incrementally return lists of key names. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` provides a hint to Redis about the number of keys to
            return per batch.

        ``_type`` filters the returned values by a particular Redis type.
            Stock Redis instances allow for the following types:
            HASH, LIST, SET, STREAM, STRING, ZSET
            Additionally, Redis modules can expose other types as well.

        For more information see https://redis.io/commands/scan
        """
        ...
    def scan_iter(
        self, match: _Key | None = None, count: int | None = None, _type: str | None = None, **kwargs: _CommandOptions
    ) -> AsyncIterator[_StrType]:
        """
        Make an iterator using the SCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` provides a hint to Redis about the number of keys to
            return per batch.

        ``_type`` filters the returned values by a particular Redis type.
            Stock Redis instances allow for the following types:
            HASH, LIST, SET, STREAM, STRING, ZSET
            Additionally, Redis modules can expose other types as well.
        """
        ...
    async def sscan(
        self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None
    ) -> tuple[int, list[_StrType]]:
        """
        Incrementally return lists of elements in a set. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        For more information see https://redis.io/commands/sscan
        """
        ...
    def sscan_iter(self, name: _Key, match: _Key | None = None, count: int | None = None) -> AsyncIterator[_StrType]:
        """
        Make an iterator using the SSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        ...
    async def hscan(
        self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None
    ) -> tuple[int, dict[_StrType, _StrType]]:
        """
        Incrementally return key/value slices in a hash. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        For more information see https://redis.io/commands/hscan
        """
        ...
    def hscan_iter(
        self, name: _Key, match: _Key | None = None, count: int | None = None
    ) -> AsyncIterator[tuple[_StrType, _StrType]]:
        """
        Make an iterator using the HSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        ...
    @overload
    async def zscan(
        self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None
    ) -> tuple[int, list[tuple[_StrType, float]]]:
        """
        Incrementally return lists of elements in a sorted set. Also return a
        cursor indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zscan
        """
        ...
    @overload
    async def zscan(
        self,
        name: _Key,
        cursor: int = 0,
        match: _Key | None = None,
        count: int | None = None,
        *,
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> tuple[int, list[tuple[_StrType, _ScoreCastFuncReturn]]]:
        """
        Incrementally return lists of elements in a sorted set. Also return a
        cursor indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zscan
        """
        ...
    @overload
    async def zscan(
        self,
        name: _Key,
        cursor: int,
        match: _Key | None,
        count: int | None,
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> tuple[int, list[tuple[_StrType, _ScoreCastFuncReturn]]]:
        """
        Incrementally return lists of elements in a sorted set. Also return a
        cursor indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zscan
        """
        ...
    @overload
    def zscan_iter(
        self, name: _Key, match: _Key | None = None, count: int | None = None
    ) -> AsyncIterator[tuple[_StrType, float]]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...
    @overload
    def zscan_iter(
        self,
        name: _Key,
        match: _Key | None = None,
        count: int | None = None,
        *,
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> AsyncIterator[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...
    @overload
    def zscan_iter(
        self, name: _Key, match: _Key | None, count: int | None, score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn]
    ) -> AsyncIterator[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...

class SetCommands(Generic[_StrType]):
    """
    Redis commands for Set data type.
    see: https://redis.io/topics/data-types#sets
    """
    def sadd(self, name: _Key, *values: _Value) -> int:
        """
        Add ``value(s)`` to set ``name``

        For more information see https://redis.io/commands/sadd
        """
        ...
    def scard(self, name: _Key) -> int:
        """
        Return the number of elements in set ``name``

        For more information see https://redis.io/commands/scard
        """
        ...
    def sdiff(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]:
        """
        Return the difference of sets specified by ``keys``

        For more information see https://redis.io/commands/sdiff
        """
        ...
    def sdiffstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int:
        """
        Store the difference of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sdiffstore
        """
        ...
    def sinter(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]:
        """
        Return the intersection of sets specified by ``keys``

        For more information see https://redis.io/commands/sinter
        """
        ...
    def sinterstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int:
        """
        Store the intersection of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sinterstore
        """
        ...
    def sismember(self, name: _Key, value: _Value) -> bool:
        """
        Return a boolean indicating if ``value`` is a member of set ``name``

        For more information see https://redis.io/commands/sismember
        """
        ...
    def smembers(self, name: _Key) -> builtins.set[_StrType]:
        """
        Return all members of the set ``name``

        For more information see https://redis.io/commands/smembers
        """
        ...
    def smismember(self, name, values, *args):
        """
        Return whether each value in ``values`` is a member of the set ``name``
        as a list of ``int`` in the order of ``values``:
        - 1 if the value is a member of the set.
        - 0 if the value is not a member of the set or if key does not exist.

        For more information see https://redis.io/commands/smismember
        """
        ...
    def smove(self, src: _Key, dst: _Key, value: _Value) -> bool:
        """
        Move ``value`` from set ``src`` to set ``dst`` atomically

        For more information see https://redis.io/commands/smove
        """
        ...
    @overload
    def spop(self, name: _Key, count: None = None) -> _Value | None:
        """
        Remove and return a random member of set ``name``

        For more information see https://redis.io/commands/spop
        """
        ...
    @overload
    def spop(self, name: _Key, count: int) -> list[_Value]:
        """
        Remove and return a random member of set ``name``

        For more information see https://redis.io/commands/spop
        """
        ...
    @overload
    def srandmember(self, name: _Key, number: None = None) -> _Value | None:
        """
        If ``number`` is None, returns a random member of set ``name``.

        If ``number`` is supplied, returns a list of ``number`` random
        members of set ``name``. Note this is only available when running
        Redis 2.6+.

        For more information see https://redis.io/commands/srandmember
        """
        ...
    @overload
    def srandmember(self, name: _Key, number: int) -> list[_Value]:
        """
        If ``number`` is None, returns a random member of set ``name``.

        If ``number`` is supplied, returns a list of ``number`` random
        members of set ``name``. Note this is only available when running
        Redis 2.6+.

        For more information see https://redis.io/commands/srandmember
        """
        ...
    def srem(self, name: _Key, *values: _Value) -> int:
        """
        Remove ``values`` from set ``name``

        For more information see https://redis.io/commands/srem
        """
        ...
    def sunion(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]:
        """
        Return the union of sets specified by ``keys``

        For more information see https://redis.io/commands/sunion
        """
        ...
    def sunionstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int:
        """
        Store the union of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sunionstore
        """
        ...

class AsyncSetCommands(Generic[_StrType]):
    """
    Redis commands for Set data type.
    see: https://redis.io/topics/data-types#sets
    """
    async def sadd(self, name: _Key, *values: _Value) -> int:
        """
        Add ``value(s)`` to set ``name``

        For more information see https://redis.io/commands/sadd
        """
        ...
    async def scard(self, name: _Key) -> int:
        """
        Return the number of elements in set ``name``

        For more information see https://redis.io/commands/scard
        """
        ...
    async def sdiff(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]:
        """
        Return the difference of sets specified by ``keys``

        For more information see https://redis.io/commands/sdiff
        """
        ...
    async def sdiffstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int:
        """
        Store the difference of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sdiffstore
        """
        ...
    async def sinter(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]:
        """
        Return the intersection of sets specified by ``keys``

        For more information see https://redis.io/commands/sinter
        """
        ...
    async def sinterstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int:
        """
        Store the intersection of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sinterstore
        """
        ...
    async def sismember(self, name: _Key, value: _Value) -> bool:
        """
        Return a boolean indicating if ``value`` is a member of set ``name``

        For more information see https://redis.io/commands/sismember
        """
        ...
    async def smembers(self, name: _Key) -> builtins.set[_StrType]:
        """
        Return all members of the set ``name``

        For more information see https://redis.io/commands/smembers
        """
        ...
    async def smismember(self, name, values, *args):
        """
        Return whether each value in ``values`` is a member of the set ``name``
        as a list of ``int`` in the order of ``values``:
        - 1 if the value is a member of the set.
        - 0 if the value is not a member of the set or if key does not exist.

        For more information see https://redis.io/commands/smismember
        """
        ...
    async def smove(self, src: _Key, dst: _Key, value: _Value) -> bool:
        """
        Move ``value`` from set ``src`` to set ``dst`` atomically

        For more information see https://redis.io/commands/smove
        """
        ...
    @overload
    async def spop(self, name: _Key, count: None = None) -> _Value | None:
        """
        Remove and return a random member of set ``name``

        For more information see https://redis.io/commands/spop
        """
        ...
    @overload
    async def spop(self, name: _Key, count: int) -> list[_Value]:
        """
        Remove and return a random member of set ``name``

        For more information see https://redis.io/commands/spop
        """
        ...
    @overload
    async def srandmember(self, name: _Key, number: None = None) -> _Value | None:
        """
        If ``number`` is None, returns a random member of set ``name``.

        If ``number`` is supplied, returns a list of ``number`` random
        members of set ``name``. Note this is only available when running
        Redis 2.6+.

        For more information see https://redis.io/commands/srandmember
        """
        ...
    @overload
    async def srandmember(self, name: _Key, number: int) -> list[_Value]:
        """
        If ``number`` is None, returns a random member of set ``name``.

        If ``number`` is supplied, returns a list of ``number`` random
        members of set ``name``. Note this is only available when running
        Redis 2.6+.

        For more information see https://redis.io/commands/srandmember
        """
        ...
    async def srem(self, name: _Key, *values: _Value) -> int:
        """
        Remove ``values`` from set ``name``

        For more information see https://redis.io/commands/srem
        """
        ...
    async def sunion(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]:
        """
        Return the union of sets specified by ``keys``

        For more information see https://redis.io/commands/sunion
        """
        ...
    async def sunionstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int:
        """
        Store the union of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sunionstore
        """
        ...

class StreamCommands:
    """
    Redis commands for Stream data type.
    see: https://redis.io/topics/streams-intro
    """
    def xack(self, name, groupname, *ids):
        """
        Acknowledges the successful processing of one or more messages.
        name: name of the stream.
        groupname: name of the consumer group.
        *ids: message ids to acknowledge.

        For more information see https://redis.io/commands/xack
        """
        ...
    def xadd(
        self,
        name: KeyT,
        # Only accepts dict objects, but for variance reasons we use a looser annotation
        fields: SupportsItems[bytes | memoryview | str | float, Any],
        id: str | int | bytes | memoryview = "*",
        maxlen=None,
        approximate: bool = True,
        nomkstream: bool = False,
        minid: Incomplete | None = None,
        limit: Incomplete | None = None,
    ):
        """
        Add to a stream.
        name: name of the stream
        fields: dict of field/value pairs to insert into the stream
        id: Location to insert this record. By default it is appended.
        maxlen: truncate old stream members beyond this size.
        Can't be specified with minid.
        approximate: actual stream length may be slightly more than maxlen
        nomkstream: When set to true, do not make a stream
        minid: the minimum id in the stream to query.
        Can't be specified with maxlen.
        limit: specifies the maximum number of entries to retrieve

        For more information see https://redis.io/commands/xadd
        """
        ...
    def xautoclaim(
        self,
        name,
        groupname,
        consumername,
        min_idle_time,
        start_id: StreamIdT = "0-0",
        count: Incomplete | None = None,
        justid: bool = False,
    ):
        """
        Transfers ownership of pending stream entries that match the specified
        criteria. Conceptually, equivalent to calling XPENDING and then XCLAIM,
        but provides a more straightforward way to deal with message delivery
        failures via SCAN-like semantics.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of a consumer that claims the message.
        min_idle_time: filter messages that were idle less than this amount of
        milliseconds.
        start_id: filter messages with equal or greater ID.
        count: optional integer, upper limit of the number of entries that the
        command attempts to claim. Set to 100 by default.
        justid: optional boolean, false by default. Return just an array of IDs
        of messages successfully claimed, without returning the actual message

        For more information see https://redis.io/commands/xautoclaim
        """
        ...
    def xclaim(
        self,
        name,
        groupname,
        consumername,
        min_idle_time,
        message_ids,
        idle=None,
        time=None,
        retrycount=None,
        force=False,
        justid=False,
    ):
        """
        Changes the ownership of a pending message.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of a consumer that claims the message.
        min_idle_time: filter messages that were idle less than this amount of
        milliseconds
        message_ids: non-empty list or tuple of message IDs to claim
        idle: optional. Set the idle time (last time it was delivered) of the
         message in ms
        time: optional integer. This is the same as idle but instead of a
         relative amount of milliseconds, it sets the idle time to a specific
         Unix time (in milliseconds).
        retrycount: optional integer. set the retry counter to the specified
         value. This counter is incremented every time a message is delivered
         again.
        force: optional boolean, false by default. Creates the pending message
         entry in the PEL even if certain specified IDs are not already in the
         PEL assigned to a different client.
        justid: optional boolean, false by default. Return just an array of IDs
         of messages successfully claimed, without returning the actual message

         For more information see https://redis.io/commands/xclaim
        """
        ...
    def xdel(self, name: KeyT, *ids: str | int | bytes | memoryview):
        """
        Deletes one or more messages from a stream.
        name: name of the stream.
        *ids: message ids to delete.

        For more information see https://redis.io/commands/xdel
        """
        ...
    def xgroup_create(self, name, groupname, id: str = "$", mkstream: bool = False, entries_read: int | None = None):
        """
        Create a new consumer group associated with a stream.
        name: name of the stream.
        groupname: name of the consumer group.
        id: ID of the last item in the stream to consider already delivered.

        For more information see https://redis.io/commands/xgroup-create
        """
        ...
    def xgroup_delconsumer(self, name, groupname, consumername):
        """
        Remove a specific consumer from a consumer group.
        Returns the number of pending messages that the consumer had before it
        was deleted.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of consumer to delete

        For more information see https://redis.io/commands/xgroup-delconsumer
        """
        ...
    def xgroup_destroy(self, name, groupname):
        """
        Destroy a consumer group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xgroup-destroy
        """
        ...
    def xgroup_createconsumer(self, name, groupname, consumername):
        """
        Consumers in a consumer group are auto-created every time a new
        consumer name is mentioned by some command.
        They can be explicitly created by using this command.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of consumer to create.

        See: https://redis.io/commands/xgroup-createconsumer
        """
        ...
    def xgroup_setid(self, name, groupname, id, entries_read: int | None = None):
        """
        Set the consumer group last delivered ID to something else.
        name: name of the stream.
        groupname: name of the consumer group.
        id: ID of the last item in the stream to consider already delivered.

        For more information see https://redis.io/commands/xgroup-setid
        """
        ...
    def xinfo_consumers(self, name, groupname):
        """
        Returns general information about the consumers in the group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xinfo-consumers
        """
        ...
    def xinfo_groups(self, name):
        """
        Returns general information about the consumer groups of the stream.
        name: name of the stream.

        For more information see https://redis.io/commands/xinfo-groups
        """
        ...
    def xinfo_stream(self, name, full: bool = False):
        """
        Returns general information about the stream.
        name: name of the stream.
        full: optional boolean, false by default. Return full summary

        For more information see https://redis.io/commands/xinfo-stream
        """
        ...
    def xlen(self, name: _Key) -> int:
        """
        Returns the number of elements in a given stream.

        For more information see https://redis.io/commands/xlen
        """
        ...
    def xpending(self, name, groupname):
        """
        Returns information about pending messages of a group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xpending
        """
        ...
    def xpending_range(
        self, name: _Key, groupname, min, max, count: int, consumername: Incomplete | None = None, idle: int | None = None
    ):
        """
        Returns information about pending messages, in a range.

        name: name of the stream.
        groupname: name of the consumer group.
        idle: available from  version 6.2. filter entries by their
        idle-time, given in milliseconds (optional).
        min: minimum stream ID.
        max: maximum stream ID.
        count: number of messages to return
        consumername: name of a consumer to filter by (optional).
        """
        ...
    def xrange(self, name, min: str = "-", max: str = "+", count: Incomplete | None = None):
        """
        Read stream values within an interval.
        name: name of the stream.
        start: first stream ID. defaults to '-',
               meaning the earliest available.
        finish: last stream ID. defaults to '+',
                meaning the latest available.
        count: if set, only return this many items, beginning with the
               earliest available.

        For more information see https://redis.io/commands/xrange
        """
        ...
    def xread(self, streams, count: Incomplete | None = None, block: Incomplete | None = None):
        """
        Block and monitor multiple streams for new data.
        streams: a dict of stream names to stream IDs, where
                   IDs indicate the last ID already seen.
        count: if set, only return this many items, beginning with the
               earliest available.
        block: number of milliseconds to wait, if nothing already present.

        For more information see https://redis.io/commands/xread
        """
        ...
    def xreadgroup(
        self,
        groupname,
        consumername,
        streams,
        count: Incomplete | None = None,
        block: Incomplete | None = None,
        noack: bool = False,
    ):
        """
        Read from a stream via a consumer group.
        groupname: name of the consumer group.
        consumername: name of the requesting consumer.
        streams: a dict of stream names to stream IDs, where
               IDs indicate the last ID already seen.
        count: if set, only return this many items, beginning with the
               earliest available.
        block: number of milliseconds to wait, if nothing already present.
        noack: do not add messages to the PEL

        For more information see https://redis.io/commands/xreadgroup
        """
        ...
    def xrevrange(self, name, max: str = "+", min: str = "-", count: Incomplete | None = None):
        """
        Read stream values within an interval, in reverse order.
        name: name of the stream
        start: first stream ID. defaults to '+',
               meaning the latest available.
        finish: last stream ID. defaults to '-',
                meaning the earliest available.
        count: if set, only return this many items, beginning with the
               latest available.

        For more information see https://redis.io/commands/xrevrange
        """
        ...
    def xtrim(
        self, name, maxlen: int | None = None, approximate: bool = True, minid: Incomplete | None = None, limit: int | None = None
    ):
        """
        Trims old messages from a stream.
        name: name of the stream.
        maxlen: truncate old stream messages beyond this size
        Can't be specified with minid.
        approximate: actual stream length may be slightly more than maxlen
        minid: the minimum id in the stream to query
        Can't be specified with maxlen.
        limit: specifies the maximum number of entries to retrieve

        For more information see https://redis.io/commands/xtrim
        """
        ...

class AsyncStreamCommands:
    """
    Redis commands for Stream data type.
    see: https://redis.io/topics/streams-intro
    """
    async def xack(self, name, groupname, *ids):
        """
        Acknowledges the successful processing of one or more messages.
        name: name of the stream.
        groupname: name of the consumer group.
        *ids: message ids to acknowledge.

        For more information see https://redis.io/commands/xack
        """
        ...
    async def xadd(
        self,
        name: KeyT,
        # Only accepts dict objects, but for variance reasons we use a looser annotation
        fields: SupportsItems[bytes | memoryview | str | float, Any],
        id: str | int | bytes | memoryview = "*",
        maxlen=None,
        approximate: bool = True,
        nomkstream: bool = False,
        minid: Incomplete | None = None,
        limit: Incomplete | None = None,
    ):
        """
        Add to a stream.
        name: name of the stream
        fields: dict of field/value pairs to insert into the stream
        id: Location to insert this record. By default it is appended.
        maxlen: truncate old stream members beyond this size.
        Can't be specified with minid.
        approximate: actual stream length may be slightly more than maxlen
        nomkstream: When set to true, do not make a stream
        minid: the minimum id in the stream to query.
        Can't be specified with maxlen.
        limit: specifies the maximum number of entries to retrieve

        For more information see https://redis.io/commands/xadd
        """
        ...
    async def xautoclaim(
        self,
        name,
        groupname,
        consumername,
        min_idle_time,
        start_id: StreamIdT = "0-0",
        count: Incomplete | None = None,
        justid: bool = False,
    ):
        """
        Transfers ownership of pending stream entries that match the specified
        criteria. Conceptually, equivalent to calling XPENDING and then XCLAIM,
        but provides a more straightforward way to deal with message delivery
        failures via SCAN-like semantics.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of a consumer that claims the message.
        min_idle_time: filter messages that were idle less than this amount of
        milliseconds.
        start_id: filter messages with equal or greater ID.
        count: optional integer, upper limit of the number of entries that the
        command attempts to claim. Set to 100 by default.
        justid: optional boolean, false by default. Return just an array of IDs
        of messages successfully claimed, without returning the actual message

        For more information see https://redis.io/commands/xautoclaim
        """
        ...
    async def xclaim(
        self,
        name,
        groupname,
        consumername,
        min_idle_time,
        message_ids,
        idle=None,
        time=None,
        retrycount=None,
        force=False,
        justid=False,
    ):
        """
        Changes the ownership of a pending message.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of a consumer that claims the message.
        min_idle_time: filter messages that were idle less than this amount of
        milliseconds
        message_ids: non-empty list or tuple of message IDs to claim
        idle: optional. Set the idle time (last time it was delivered) of the
         message in ms
        time: optional integer. This is the same as idle but instead of a
         relative amount of milliseconds, it sets the idle time to a specific
         Unix time (in milliseconds).
        retrycount: optional integer. set the retry counter to the specified
         value. This counter is incremented every time a message is delivered
         again.
        force: optional boolean, false by default. Creates the pending message
         entry in the PEL even if certain specified IDs are not already in the
         PEL assigned to a different client.
        justid: optional boolean, false by default. Return just an array of IDs
         of messages successfully claimed, without returning the actual message

         For more information see https://redis.io/commands/xclaim
        """
        ...
    async def xdel(self, name: KeyT, *ids: str | int | bytes | memoryview):
        """
        Deletes one or more messages from a stream.
        name: name of the stream.
        *ids: message ids to delete.

        For more information see https://redis.io/commands/xdel
        """
        ...
    async def xgroup_create(self, name, groupname, id: str = "$", mkstream: bool = False, entries_read: int | None = None):
        """
        Create a new consumer group associated with a stream.
        name: name of the stream.
        groupname: name of the consumer group.
        id: ID of the last item in the stream to consider already delivered.

        For more information see https://redis.io/commands/xgroup-create
        """
        ...
    async def xgroup_delconsumer(self, name, groupname, consumername):
        """
        Remove a specific consumer from a consumer group.
        Returns the number of pending messages that the consumer had before it
        was deleted.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of consumer to delete

        For more information see https://redis.io/commands/xgroup-delconsumer
        """
        ...
    async def xgroup_destroy(self, name, groupname):
        """
        Destroy a consumer group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xgroup-destroy
        """
        ...
    async def xgroup_createconsumer(self, name, groupname, consumername):
        """
        Consumers in a consumer group are auto-created every time a new
        consumer name is mentioned by some command.
        They can be explicitly created by using this command.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of consumer to create.

        See: https://redis.io/commands/xgroup-createconsumer
        """
        ...
    async def xgroup_setid(self, name, groupname, id, entries_read: int | None = None):
        """
        Set the consumer group last delivered ID to something else.
        name: name of the stream.
        groupname: name of the consumer group.
        id: ID of the last item in the stream to consider already delivered.

        For more information see https://redis.io/commands/xgroup-setid
        """
        ...
    async def xinfo_consumers(self, name, groupname):
        """
        Returns general information about the consumers in the group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xinfo-consumers
        """
        ...
    async def xinfo_groups(self, name):
        """
        Returns general information about the consumer groups of the stream.
        name: name of the stream.

        For more information see https://redis.io/commands/xinfo-groups
        """
        ...
    async def xinfo_stream(self, name, full: bool = False):
        """
        Returns general information about the stream.
        name: name of the stream.
        full: optional boolean, false by default. Return full summary

        For more information see https://redis.io/commands/xinfo-stream
        """
        ...
    async def xlen(self, name: _Key) -> int:
        """
        Returns the number of elements in a given stream.

        For more information see https://redis.io/commands/xlen
        """
        ...
    async def xpending(self, name, groupname):
        """
        Returns information about pending messages of a group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xpending
        """
        ...
    async def xpending_range(
        self, name: _Key, groupname, min, max, count: int, consumername: Incomplete | None = None, idle: int | None = None
    ):
        """
        Returns information about pending messages, in a range.

        name: name of the stream.
        groupname: name of the consumer group.
        idle: available from  version 6.2. filter entries by their
        idle-time, given in milliseconds (optional).
        min: minimum stream ID.
        max: maximum stream ID.
        count: number of messages to return
        consumername: name of a consumer to filter by (optional).
        """
        ...
    async def xrange(self, name, min: str = "-", max: str = "+", count: Incomplete | None = None):
        """
        Read stream values within an interval.
        name: name of the stream.
        start: first stream ID. defaults to '-',
               meaning the earliest available.
        finish: last stream ID. defaults to '+',
                meaning the latest available.
        count: if set, only return this many items, beginning with the
               earliest available.

        For more information see https://redis.io/commands/xrange
        """
        ...
    async def xread(self, streams, count: Incomplete | None = None, block: Incomplete | None = None):
        """
        Block and monitor multiple streams for new data.
        streams: a dict of stream names to stream IDs, where
                   IDs indicate the last ID already seen.
        count: if set, only return this many items, beginning with the
               earliest available.
        block: number of milliseconds to wait, if nothing already present.

        For more information see https://redis.io/commands/xread
        """
        ...
    async def xreadgroup(
        self,
        groupname,
        consumername,
        streams,
        count: Incomplete | None = None,
        block: Incomplete | None = None,
        noack: bool = False,
    ):
        """
        Read from a stream via a consumer group.
        groupname: name of the consumer group.
        consumername: name of the requesting consumer.
        streams: a dict of stream names to stream IDs, where
               IDs indicate the last ID already seen.
        count: if set, only return this many items, beginning with the
               earliest available.
        block: number of milliseconds to wait, if nothing already present.
        noack: do not add messages to the PEL

        For more information see https://redis.io/commands/xreadgroup
        """
        ...
    async def xrevrange(self, name, max: str = "+", min: str = "-", count: Incomplete | None = None):
        """
        Read stream values within an interval, in reverse order.
        name: name of the stream
        start: first stream ID. defaults to '+',
               meaning the latest available.
        finish: last stream ID. defaults to '-',
                meaning the earliest available.
        count: if set, only return this many items, beginning with the
               latest available.

        For more information see https://redis.io/commands/xrevrange
        """
        ...
    async def xtrim(
        self, name, maxlen: int | None = None, approximate: bool = True, minid: Incomplete | None = None, limit: int | None = None
    ):
        """
        Trims old messages from a stream.
        name: name of the stream.
        maxlen: truncate old stream messages beyond this size
        Can't be specified with minid.
        approximate: actual stream length may be slightly more than maxlen
        minid: the minimum id in the stream to query
        Can't be specified with maxlen.
        limit: specifies the maximum number of entries to retrieve

        For more information see https://redis.io/commands/xtrim
        """
        ...

class SortedSetCommands(Generic[_StrType]):
    """
    Redis commands for Sorted Sets data type.
    see: https://redis.io/topics/data-types-intro#redis-sorted-sets
    """
    def zadd(
        self,
        name: _Key,
        mapping: Mapping[_Key, _Value],
        nx: bool = False,
        xx: bool = False,
        ch: bool = False,
        incr: bool = False,
        gt: Incomplete | None = False,
        lt: Incomplete | None = False,
    ) -> int:
        """
        Set any number of element-name, score pairs to the key ``name``. Pairs
        are specified as a dict of element-names keys to score values.

        ``nx`` forces ZADD to only create new elements and not to update
        scores for elements that already exist.

        ``xx`` forces ZADD to only update scores of elements that already
        exist. New elements will not be added.

        ``ch`` modifies the return value to be the numbers of elements changed.
        Changed elements include new elements that were added and elements
        whose scores changed.

        ``incr`` modifies ZADD to behave like ZINCRBY. In this mode only a
        single element/score pair can be specified and the score is the amount
        the existing score will be incremented by. When using this mode the
        return value of ZADD will be the new score of the element.

        ``LT`` Only update existing elements if the new score is less than
        the current score. This flag doesn't prevent adding new elements.

        ``GT`` Only update existing elements if the new score is greater than
        the current score. This flag doesn't prevent adding new elements.

        The return value of ZADD varies based on the mode specified. With no
        options, ZADD returns the number of new elements added to the sorted
        set.

        ``NX``, ``LT``, and ``GT`` are mutually exclusive options.

        See: https://redis.io/commands/ZADD
        """
        ...
    def zcard(self, name: _Key) -> int:
        """
        Return the number of elements in the sorted set ``name``

        For more information see https://redis.io/commands/zcard
        """
        ...
    def zcount(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Returns the number of elements in the sorted set at key ``name`` with
        a score between ``min`` and ``max``.

        For more information see https://redis.io/commands/zcount
        """
        ...
    def zdiff(self, keys, withscores: bool = False):
        """
        Returns the difference between the first and all successive input
        sorted sets provided in ``keys``.

        For more information see https://redis.io/commands/zdiff
        """
        ...
    def zdiffstore(self, dest, keys):
        """
        Computes the difference between the first and all successive input
        sorted sets provided in ``keys`` and stores the result in ``dest``.

        For more information see https://redis.io/commands/zdiffstore
        """
        ...
    def zincrby(self, name: _Key, amount: float, value: _Value) -> float:
        """
        Increment the score of ``value`` in sorted set ``name`` by ``amount``

        For more information see https://redis.io/commands/zincrby
        """
        ...
    def zinter(self, keys, aggregate: Incomplete | None = None, withscores: bool = False):
        """
        Return the intersect of multiple sorted sets specified by ``keys``.
        With the ``aggregate`` option, it is possible to specify how the
        results of the union are aggregated. This option defaults to SUM,
        where the score of an element is summed across the inputs where it
        exists. When this option is set to either MIN or MAX, the resulting
        set will contain the minimum or maximum score of an element across
        the inputs where it exists.

        For more information see https://redis.io/commands/zinter
        """
        ...
    def zinterstore(self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = None) -> int:
        """
        Intersect multiple sorted sets specified by ``keys`` into a new
        sorted set, ``dest``. Scores in the destination will be aggregated
        based on the ``aggregate``. This option defaults to SUM, where the
        score of an element is summed across the inputs where it exists.
        When this option is set to either MIN or MAX, the resulting set will
        contain the minimum or maximum score of an element across the inputs
        where it exists.

        For more information see https://redis.io/commands/zinterstore
        """
        ...
    def zlexcount(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Return the number of items in the sorted set ``name`` between the
        lexicographical range ``min`` and ``max``.

        For more information see https://redis.io/commands/zlexcount
        """
        ...
    def zpopmax(self, name: _Key, count: int | None = None) -> list[tuple[_StrType, float]]:
        """
        Remove and return up to ``count`` members with the highest scores
        from the sorted set ``name``.

        For more information see https://redis.io/commands/zpopmax
        """
        ...
    def zpopmin(self, name: _Key, count: int | None = None) -> list[tuple[_StrType, float]]:
        """
        Remove and return up to ``count`` members with the lowest scores
        from the sorted set ``name``.

        For more information see https://redis.io/commands/zpopmin
        """
        ...
    def zrandmember(self, key, count: Incomplete | None = None, withscores: bool = False):
        """
        Return a random element from the sorted set value stored at key.

        ``count`` if the argument is positive, return an array of distinct
        fields. If called with a negative count, the behavior changes and
        the command is allowed to return the same field multiple times.
        In this case, the number of returned fields is the absolute value
        of the specified count.

        ``withscores`` The optional WITHSCORES modifier changes the reply so it
        includes the respective scores of the randomly selected elements from
        the sorted set.

        For more information see https://redis.io/commands/zrandmember
        """
        ...
    @overload
    def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: Literal[0] = 0) -> tuple[_StrType, _StrType, float]:
        """
        ZPOPMAX a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMAX,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmax
        """
        ...
    @overload
    def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: float) -> tuple[_StrType, _StrType, float] | None:
        """
        ZPOPMAX a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMAX,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmax
        """
        ...
    @overload
    def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: Literal[0] = 0) -> tuple[_StrType, _StrType, float]:
        """
        ZPOPMIN a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMIN,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmin
        """
        ...
    @overload
    def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: float) -> tuple[_StrType, _StrType, float] | None:
        """
        ZPOPMIN a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMIN,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmin
        """
        ...
    @overload
    def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], float] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], float] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    def zrange(
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = False,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[_StrType]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    def zrevrange(
        self,
        name: _Key,
        start: int,
        end: int,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    @overload
    def zrevrange(  # type: ignore[overload-overlap]
        self, name: _Key, start: int, end: int, withscores: Literal[True]
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    @overload
    def zrevrange(
        self, name: _Key, start: int, end: int, withscores: bool = False, score_cast_func: Callable[[Any], Any] = ...
    ) -> list[_StrType]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    def zrangestore(
        self,
        dest,
        name,
        start,
        end,
        byscore: bool = False,
        bylex: bool = False,
        desc: bool = False,
        offset: Incomplete | None = None,
        num: Incomplete | None = None,
    ):
        """
        Stores in ``dest`` the result of a range of values from sorted set
        ``name`` between ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrangestore
        """
        ...
    def zrangebylex(
        self, name: _Key, min: _Value, max: _Value, start: int | None = None, num: int | None = None
    ) -> list[_StrType]:
        """
        Return the lexicographical range of values from sorted set ``name``
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.

        For more information see https://redis.io/commands/zrangebylex
        """
        ...
    def zrevrangebylex(
        self, name: _Key, max: _Value, min: _Value, start: int | None = None, num: int | None = None
    ) -> list[_StrType]:
        """
        Return the reversed lexicographical range of values from sorted set
        ``name`` between ``max`` and ``min``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.

        For more information see https://redis.io/commands/zrevrangebylex
        """
        ...
    @overload
    def zrangebyscore(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = None,
        num: int | None = None,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    @overload
    def zrangebyscore(  # type: ignore[overload-overlap]
        self, name: _Key, min: _Value, max: _Value, start: int | None = None, num: int | None = None, *, withscores: Literal[True]
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    @overload
    def zrangebyscore(
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = None,
        num: int | None = None,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
    ) -> list[_StrType]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    @overload
    def zrevrangebyscore(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = None,
        num: int | None = None,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    @overload
    def zrevrangebyscore(  # type: ignore[overload-overlap]
        self, name: _Key, max: _Value, min: _Value, start: int | None = None, num: int | None = None, *, withscores: Literal[True]
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    @overload
    def zrevrangebyscore(
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = None,
        num: int | None = None,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
    ) -> list[_StrType]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    def zrank(self, name: _Key, value: _Value, withscore: bool = False) -> int | None:
        """
        Returns a 0-based value indicating the rank of ``value`` in sorted set
        ``name``.
        The optional WITHSCORE argument supplements the command's
        reply with the score of the element returned.

        For more information see https://redis.io/commands/zrank
        """
        ...
    def zrem(self, name: _Key, *values: _Value) -> int:
        """
        Remove member ``values`` from sorted set ``name``

        For more information see https://redis.io/commands/zrem
        """
        ...
    def zremrangebylex(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Remove all elements in the sorted set ``name`` between the
        lexicographical range specified by ``min`` and ``max``.

        Returns the number of elements removed.

        For more information see https://redis.io/commands/zremrangebylex
        """
        ...
    def zremrangebyrank(self, name: _Key, min: int, max: int) -> int:
        """
        Remove all elements in the sorted set ``name`` with ranks between
        ``min`` and ``max``. Values are 0-based, ordered from smallest score
        to largest. Values can be negative indicating the highest scores.
        Returns the number of elements removed

        For more information see https://redis.io/commands/zremrangebyrank
        """
        ...
    def zremrangebyscore(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Remove all elements in the sorted set ``name`` with scores
        between ``min`` and ``max``. Returns the number of elements removed.

        For more information see https://redis.io/commands/zremrangebyscore
        """
        ...
    def zrevrank(self, name: _Key, value: _Value, withscore: bool = False) -> int | None:
        """
        Returns a 0-based value indicating the descending rank of
        ``value`` in sorted set ``name``.
        The optional ``withscore`` argument supplements the command's
        reply with the score of the element returned.

        For more information see https://redis.io/commands/zrevrank
        """
        ...
    def zscore(self, name: _Key, value: _Value) -> float | None:
        """
        Return the score of element ``value`` in sorted set ``name``

        For more information see https://redis.io/commands/zscore
        """
        ...
    def zunion(self, keys, aggregate: Incomplete | None = None, withscores: bool = False):
        """
        Return the union of multiple sorted sets specified by ``keys``.
        ``keys`` can be provided as dictionary of keys and their weights.
        Scores will be aggregated based on the ``aggregate``, or SUM if
        none is provided.

        For more information see https://redis.io/commands/zunion
        """
        ...
    def zunionstore(self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = None) -> int:
        """
        Union multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.

        For more information see https://redis.io/commands/zunionstore
        """
        ...
    def zmscore(self, key, members):
        """
        Returns the scores associated with the specified members
        in the sorted set stored at key.
        ``members`` should be a list of the member name.
        Return type is a list of score.
        If the member does not exist, a None will be returned
        in corresponding position.

        For more information see https://redis.io/commands/zmscore
        """
        ...

class AsyncSortedSetCommands(Generic[_StrType]):
    """
    Redis commands for Sorted Sets data type.
    see: https://redis.io/topics/data-types-intro#redis-sorted-sets
    """
    async def zadd(
        self,
        name: _Key,
        mapping: Mapping[_Key, _Value],
        nx: bool = False,
        xx: bool = False,
        ch: bool = False,
        incr: bool = False,
        gt: Incomplete | None = False,
        lt: Incomplete | None = False,
    ) -> int:
        """
        Set any number of element-name, score pairs to the key ``name``. Pairs
        are specified as a dict of element-names keys to score values.

        ``nx`` forces ZADD to only create new elements and not to update
        scores for elements that already exist.

        ``xx`` forces ZADD to only update scores of elements that already
        exist. New elements will not be added.

        ``ch`` modifies the return value to be the numbers of elements changed.
        Changed elements include new elements that were added and elements
        whose scores changed.

        ``incr`` modifies ZADD to behave like ZINCRBY. In this mode only a
        single element/score pair can be specified and the score is the amount
        the existing score will be incremented by. When using this mode the
        return value of ZADD will be the new score of the element.

        ``LT`` Only update existing elements if the new score is less than
        the current score. This flag doesn't prevent adding new elements.

        ``GT`` Only update existing elements if the new score is greater than
        the current score. This flag doesn't prevent adding new elements.

        The return value of ZADD varies based on the mode specified. With no
        options, ZADD returns the number of new elements added to the sorted
        set.

        ``NX``, ``LT``, and ``GT`` are mutually exclusive options.

        See: https://redis.io/commands/ZADD
        """
        ...
    async def zcard(self, name: _Key) -> int:
        """
        Return the number of elements in the sorted set ``name``

        For more information see https://redis.io/commands/zcard
        """
        ...
    async def zcount(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Returns the number of elements in the sorted set at key ``name`` with
        a score between ``min`` and ``max``.

        For more information see https://redis.io/commands/zcount
        """
        ...
    async def zdiff(self, keys, withscores: bool = False):
        """
        Returns the difference between the first and all successive input
        sorted sets provided in ``keys``.

        For more information see https://redis.io/commands/zdiff
        """
        ...
    async def zdiffstore(self, dest, keys):
        """
        Computes the difference between the first and all successive input
        sorted sets provided in ``keys`` and stores the result in ``dest``.

        For more information see https://redis.io/commands/zdiffstore
        """
        ...
    async def zincrby(self, name: _Key, amount: float, value: _Value) -> float:
        """
        Increment the score of ``value`` in sorted set ``name`` by ``amount``

        For more information see https://redis.io/commands/zincrby
        """
        ...
    async def zinter(self, keys, aggregate: Incomplete | None = None, withscores: bool = False):
        """
        Return the intersect of multiple sorted sets specified by ``keys``.
        With the ``aggregate`` option, it is possible to specify how the
        results of the union are aggregated. This option defaults to SUM,
        where the score of an element is summed across the inputs where it
        exists. When this option is set to either MIN or MAX, the resulting
        set will contain the minimum or maximum score of an element across
        the inputs where it exists.

        For more information see https://redis.io/commands/zinter
        """
        ...
    async def zinterstore(
        self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = None
    ) -> int:
        """
        Intersect multiple sorted sets specified by ``keys`` into a new
        sorted set, ``dest``. Scores in the destination will be aggregated
        based on the ``aggregate``. This option defaults to SUM, where the
        score of an element is summed across the inputs where it exists.
        When this option is set to either MIN or MAX, the resulting set will
        contain the minimum or maximum score of an element across the inputs
        where it exists.

        For more information see https://redis.io/commands/zinterstore
        """
        ...
    async def zlexcount(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Return the number of items in the sorted set ``name`` between the
        lexicographical range ``min`` and ``max``.

        For more information see https://redis.io/commands/zlexcount
        """
        ...
    async def zpopmax(self, name: _Key, count: int | None = None) -> list[tuple[_StrType, float]]:
        """
        Remove and return up to ``count`` members with the highest scores
        from the sorted set ``name``.

        For more information see https://redis.io/commands/zpopmax
        """
        ...
    async def zpopmin(self, name: _Key, count: int | None = None) -> list[tuple[_StrType, float]]:
        """
        Remove and return up to ``count`` members with the lowest scores
        from the sorted set ``name``.

        For more information see https://redis.io/commands/zpopmin
        """
        ...
    async def zrandmember(self, key, count: Incomplete | None = None, withscores: bool = False):
        """
        Return a random element from the sorted set value stored at key.

        ``count`` if the argument is positive, return an array of distinct
        fields. If called with a negative count, the behavior changes and
        the command is allowed to return the same field multiple times.
        In this case, the number of returned fields is the absolute value
        of the specified count.

        ``withscores`` The optional WITHSCORES modifier changes the reply so it
        includes the respective scores of the randomly selected elements from
        the sorted set.

        For more information see https://redis.io/commands/zrandmember
        """
        ...
    @overload
    async def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: Literal[0] = 0) -> tuple[_StrType, _StrType, float]:
        """
        ZPOPMAX a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMAX,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmax
        """
        ...
    @overload
    async def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: float) -> tuple[_StrType, _StrType, float] | None:
        """
        ZPOPMAX a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMAX,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmax
        """
        ...
    @overload
    async def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: Literal[0] = 0) -> tuple[_StrType, _StrType, float]:
        """
        ZPOPMIN a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMIN,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmin
        """
        ...
    @overload
    async def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: float) -> tuple[_StrType, _StrType, float] | None:
        """
        ZPOPMIN a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMIN,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmin
        """
        ...
    @overload
    async def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    async def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], float] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    async def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = False,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    async def zrange(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = False,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], float] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    async def zrange(
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = False,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> list[_StrType]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    @overload
    async def zrevrange(
        self,
        name: _Key,
        start: int,
        end: int,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    @overload
    async def zrevrange(  # type: ignore[overload-overlap]
        self, name: _Key, start: int, end: int, withscores: Literal[True]
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    @overload
    async def zrevrange(
        self, name: _Key, start: int, end: int, withscores: bool = False, score_cast_func: Callable[[Any], Any] = ...
    ) -> list[_StrType]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    async def zrangestore(
        self,
        dest,
        name,
        start,
        end,
        byscore: bool = False,
        bylex: bool = False,
        desc: bool = False,
        offset: Incomplete | None = None,
        num: Incomplete | None = None,
    ):
        """
        Stores in ``dest`` the result of a range of values from sorted set
        ``name`` between ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrangestore
        """
        ...
    async def zrangebylex(
        self, name: _Key, min: _Value, max: _Value, start: int | None = None, num: int | None = None
    ) -> list[_StrType]:
        """
        Return the lexicographical range of values from sorted set ``name``
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.

        For more information see https://redis.io/commands/zrangebylex
        """
        ...
    async def zrevrangebylex(
        self, name: _Key, max: _Value, min: _Value, start: int | None = None, num: int | None = None
    ) -> list[_StrType]:
        """
        Return the reversed lexicographical range of values from sorted set
        ``name`` between ``max`` and ``min``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.

        For more information see https://redis.io/commands/zrevrangebylex
        """
        ...
    @overload
    async def zrangebyscore(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = None,
        num: int | None = None,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    @overload
    async def zrangebyscore(  # type: ignore[overload-overlap]
        self, name: _Key, min: _Value, max: _Value, start: int | None = None, num: int | None = None, *, withscores: Literal[True]
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    @overload
    async def zrangebyscore(
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = None,
        num: int | None = None,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
    ) -> list[_StrType]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    @overload
    async def zrevrangebyscore(  # type: ignore[overload-overlap]
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = None,
        num: int | None = None,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[_StrType], _ScoreCastFuncReturn],
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    @overload
    async def zrevrangebyscore(  # type: ignore[overload-overlap]
        self, name: _Key, max: _Value, min: _Value, start: int | None = None, num: int | None = None, *, withscores: Literal[True]
    ) -> list[tuple[_StrType, float]]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    @overload
    async def zrevrangebyscore(
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = None,
        num: int | None = None,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
    ) -> list[_StrType]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    async def zrank(self, name: _Key, value: _Value, withscore: bool = False) -> int | None:
        """
        Returns a 0-based value indicating the rank of ``value`` in sorted set
        ``name``.
        The optional WITHSCORE argument supplements the command's
        reply with the score of the element returned.

        For more information see https://redis.io/commands/zrank
        """
        ...
    async def zrem(self, name: _Key, *values: _Value) -> int:
        """
        Remove member ``values`` from sorted set ``name``

        For more information see https://redis.io/commands/zrem
        """
        ...
    async def zremrangebylex(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Remove all elements in the sorted set ``name`` between the
        lexicographical range specified by ``min`` and ``max``.

        Returns the number of elements removed.

        For more information see https://redis.io/commands/zremrangebylex
        """
        ...
    async def zremrangebyrank(self, name: _Key, min: int, max: int) -> int:
        """
        Remove all elements in the sorted set ``name`` with ranks between
        ``min`` and ``max``. Values are 0-based, ordered from smallest score
        to largest. Values can be negative indicating the highest scores.
        Returns the number of elements removed

        For more information see https://redis.io/commands/zremrangebyrank
        """
        ...
    async def zremrangebyscore(self, name: _Key, min: _Value, max: _Value) -> int:
        """
        Remove all elements in the sorted set ``name`` with scores
        between ``min`` and ``max``. Returns the number of elements removed.

        For more information see https://redis.io/commands/zremrangebyscore
        """
        ...
    async def zrevrank(self, name: _Key, value: _Value, withscore: bool = False) -> int | None:
        """
        Returns a 0-based value indicating the descending rank of
        ``value`` in sorted set ``name``.
        The optional ``withscore`` argument supplements the command's
        reply with the score of the element returned.

        For more information see https://redis.io/commands/zrevrank
        """
        ...
    async def zscore(self, name: _Key, value: _Value) -> float | None:
        """
        Return the score of element ``value`` in sorted set ``name``

        For more information see https://redis.io/commands/zscore
        """
        ...
    async def zunion(self, keys, aggregate: Incomplete | None = None, withscores: bool = False):
        """
        Return the union of multiple sorted sets specified by ``keys``.
        ``keys`` can be provided as dictionary of keys and their weights.
        Scores will be aggregated based on the ``aggregate``, or SUM if
        none is provided.

        For more information see https://redis.io/commands/zunion
        """
        ...
    async def zunionstore(
        self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = None
    ) -> int:
        """
        Union multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.

        For more information see https://redis.io/commands/zunionstore
        """
        ...
    async def zmscore(self, key, members):
        """
        Returns the scores associated with the specified members
        in the sorted set stored at key.
        ``members`` should be a list of the member name.
        Return type is a list of score.
        If the member does not exist, a None will be returned
        in corresponding position.

        For more information see https://redis.io/commands/zmscore
        """
        ...

class HyperlogCommands:
    """
    Redis commands of HyperLogLogs data type.
    see: https://redis.io/topics/data-types-intro#hyperloglogs
    """
    def pfadd(self, name: _Key, *values: _Value) -> int:
        """
        Adds the specified elements to the specified HyperLogLog.

        For more information see https://redis.io/commands/pfadd
        """
        ...
    def pfcount(self, name: _Key) -> int:
        """
        Return the approximated cardinality of
        the set observed by the HyperLogLog at key(s).

        For more information see https://redis.io/commands/pfcount
        """
        ...
    def pfmerge(self, dest: _Key, *sources: _Key) -> bool:
        """
        Merge N different HyperLogLogs into a single one.

        For more information see https://redis.io/commands/pfmerge
        """
        ...

class AsyncHyperlogCommands:
    """
    Redis commands of HyperLogLogs data type.
    see: https://redis.io/topics/data-types-intro#hyperloglogs
    """
    async def pfadd(self, name: _Key, *values: _Value) -> int:
        """
        Adds the specified elements to the specified HyperLogLog.

        For more information see https://redis.io/commands/pfadd
        """
        ...
    async def pfcount(self, name: _Key) -> int:
        """
        Return the approximated cardinality of
        the set observed by the HyperLogLog at key(s).

        For more information see https://redis.io/commands/pfcount
        """
        ...
    async def pfmerge(self, dest: _Key, *sources: _Key) -> bool:
        """
        Merge N different HyperLogLogs into a single one.

        For more information see https://redis.io/commands/pfmerge
        """
        ...

class HashCommands(Generic[_StrType]):
    """
    Redis commands for Hash data type.
    see: https://redis.io/topics/data-types-intro#redis-hashes
    """
    def hdel(self, name: _Key, *keys: _Key) -> int:
        """
        Delete ``keys`` from hash ``name``

        For more information see https://redis.io/commands/hdel
        """
        ...
    def hexists(self, name: _Key, key: _Key) -> bool:
        """
        Returns a boolean indicating if ``key`` exists within hash ``name``

        For more information see https://redis.io/commands/hexists
        """
        ...
    def hget(self, name: _Key, key: _Key) -> _StrType | None:
        """
        Return the value of ``key`` within the hash ``name``

        For more information see https://redis.io/commands/hget
        """
        ...
    def hgetall(self, name: _Key) -> dict[_StrType, _StrType]:
        """
        Return a Python dict of the hash's name/value pairs

        For more information see https://redis.io/commands/hgetall
        """
        ...
    def hincrby(self, name: _Key, key: _Key, amount: int = 1) -> int:
        """
        Increment the value of ``key`` in hash ``name`` by ``amount``

        For more information see https://redis.io/commands/hincrby
        """
        ...
    def hincrbyfloat(self, name: _Key, key: _Key, amount: float = 1.0) -> float:
        """
        Increment the value of ``key`` in hash ``name`` by floating ``amount``

        For more information see https://redis.io/commands/hincrbyfloat
        """
        ...
    def hkeys(self, name: _Key) -> list[_StrType]:
        """
        Return the list of keys within hash ``name``

        For more information see https://redis.io/commands/hkeys
        """
        ...
    def hlen(self, name: _Key) -> int:
        """
        Return the number of elements in hash ``name``

        For more information see https://redis.io/commands/hlen
        """
        ...
    @overload
    def hset(
        self, name: _Key, key: _Key, value: _Value, mapping: Mapping[_Key, _Value] | None = None, items: Incomplete | None = None
    ) -> int:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    @overload
    def hset(
        self, name: _Key, key: None, value: None, mapping: Mapping[_Key, _Value], items: Incomplete | None = None
    ) -> int:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    @overload
    def hset(self, name: _Key, *, mapping: Mapping[_Key, _Value], items: Incomplete | None = None) -> int:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    def hsetnx(self, name: _Key, key: _Key, value: _Value) -> int:
        """
        Set ``key`` to ``value`` within hash ``name`` if ``key`` does not
        exist.  Returns 1 if HSETNX created a field, otherwise 0.

        For more information see https://redis.io/commands/hsetnx
        """
        ...
    def hmset(self, name: _Key, mapping: Mapping[_Key, _Value]) -> bool:
        """
        Set key to value within hash ``name`` for each corresponding
        key and value from the ``mapping`` dict.

        For more information see https://redis.io/commands/hmset
        """
        ...
    def hmget(self, name: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> list[_StrType | None]:
        """
        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/hmget
        """
        ...
    def hvals(self, name: _Key) -> list[_StrType]:
        """
        Return the list of values within hash ``name``

        For more information see https://redis.io/commands/hvals
        """
        ...
    def hstrlen(self, name, key):
        """
        Return the number of bytes stored in the value of ``key``
        within hash ``name``

        For more information see https://redis.io/commands/hstrlen
        """
        ...

class AsyncHashCommands(Generic[_StrType]):
    """
    Redis commands for Hash data type.
    see: https://redis.io/topics/data-types-intro#redis-hashes
    """
    async def hdel(self, name: _Key, *keys: _Key) -> int:
        """
        Delete ``keys`` from hash ``name``

        For more information see https://redis.io/commands/hdel
        """
        ...
    async def hexists(self, name: _Key, key: _Key) -> bool:
        """
        Returns a boolean indicating if ``key`` exists within hash ``name``

        For more information see https://redis.io/commands/hexists
        """
        ...
    async def hget(self, name: _Key, key: _Key) -> _StrType | None:
        """
        Return the value of ``key`` within the hash ``name``

        For more information see https://redis.io/commands/hget
        """
        ...
    async def hgetall(self, name: _Key) -> dict[_StrType, _StrType]:
        """
        Return a Python dict of the hash's name/value pairs

        For more information see https://redis.io/commands/hgetall
        """
        ...
    async def hincrby(self, name: _Key, key: _Key, amount: int = 1) -> int:
        """
        Increment the value of ``key`` in hash ``name`` by ``amount``

        For more information see https://redis.io/commands/hincrby
        """
        ...
    async def hincrbyfloat(self, name: _Key, key: _Key, amount: float = 1.0) -> float:
        """
        Increment the value of ``key`` in hash ``name`` by floating ``amount``

        For more information see https://redis.io/commands/hincrbyfloat
        """
        ...
    async def hkeys(self, name: _Key) -> list[_StrType]:
        """
        Return the list of keys within hash ``name``

        For more information see https://redis.io/commands/hkeys
        """
        ...
    async def hlen(self, name: _Key) -> int:
        """
        Return the number of elements in hash ``name``

        For more information see https://redis.io/commands/hlen
        """
        ...
    @overload
    async def hset(
        self, name: _Key, key: _Key, value: _Value, mapping: Mapping[_Key, _Value] | None = None, items: Incomplete | None = None
    ) -> int:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    @overload
    async def hset(
        self, name: _Key, key: None, value: None, mapping: Mapping[_Key, _Value], items: Incomplete | None = None
    ) -> int:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    @overload
    async def hset(self, name: _Key, *, mapping: Mapping[_Key, _Value], items: Incomplete | None = None) -> int:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    async def hsetnx(self, name: _Key, key: _Key, value: _Value) -> int:
        """
        Set ``key`` to ``value`` within hash ``name`` if ``key`` does not
        exist.  Returns 1 if HSETNX created a field, otherwise 0.

        For more information see https://redis.io/commands/hsetnx
        """
        ...
    async def hmset(self, name: _Key, mapping: Mapping[_Key, _Value]) -> bool:
        """
        Set key to value within hash ``name`` for each corresponding
        key and value from the ``mapping`` dict.

        For more information see https://redis.io/commands/hmset
        """
        ...
    async def hmget(self, name: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> list[_StrType | None]:
        """
        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/hmget
        """
        ...
    async def hvals(self, name: _Key) -> list[_StrType]:
        """
        Return the list of values within hash ``name``

        For more information see https://redis.io/commands/hvals
        """
        ...
    async def hstrlen(self, name, key):
        """
        Return the number of bytes stored in the value of ``key``
        within hash ``name``

        For more information see https://redis.io/commands/hstrlen
        """
        ...

class AsyncScript:
    """An executable Lua script object returned by ``register_script``"""
    def __init__(self, registered_client: AsyncRedis[Any], script: ScriptTextT) -> None: ...
    async def __call__(
        self, keys: Sequence[KeyT] | None = None, args: Iterable[EncodableT] | None = None, client: AsyncRedis[Any] | None = None
    ):
        """Execute the script, passing any required ``args``"""
        ...

class PubSubCommands:
    """
    Redis PubSub commands.
    see https://redis.io/topics/pubsub
    """
    def publish(self, channel: _Key, message: _Key, **kwargs: _CommandOptions) -> int:
        """
        Publish ``message`` on ``channel``.
        Returns the number of subscribers the message was delivered to.

        For more information see https://redis.io/commands/publish
        """
        ...
    def pubsub_channels(self, pattern: _Key = "*", **kwargs: _CommandOptions) -> list[str]:
        """
        Return a list of channels that have at least one subscriber

        For more information see https://redis.io/commands/pubsub-channels
        """
        ...
    def pubsub_numpat(self, **kwargs: _CommandOptions) -> int:
        """
        Returns the number of subscriptions to patterns

        For more information see https://redis.io/commands/pubsub-numpat
        """
        ...
    def pubsub_numsub(self, *args: _Key, **kwargs: _CommandOptions) -> list[tuple[str, int]]:
        """
        Return a list of (channel, number of subscribers) tuples
        for each channel given in ``*args``

        For more information see https://redis.io/commands/pubsub-numsub
        """
        ...

class AsyncPubSubCommands:
    """
    Redis PubSub commands.
    see https://redis.io/topics/pubsub
    """
    async def publish(self, channel: _Key, message: _Key, **kwargs: _CommandOptions) -> int:
        """
        Publish ``message`` on ``channel``.
        Returns the number of subscribers the message was delivered to.

        For more information see https://redis.io/commands/publish
        """
        ...
    async def pubsub_channels(self, pattern: _Key = "*", **kwargs: _CommandOptions) -> list[str]:
        """
        Return a list of channels that have at least one subscriber

        For more information see https://redis.io/commands/pubsub-channels
        """
        ...
    async def pubsub_numpat(self, **kwargs: _CommandOptions) -> int:
        """
        Returns the number of subscriptions to patterns

        For more information see https://redis.io/commands/pubsub-numpat
        """
        ...
    async def pubsub_numsub(self, *args: _Key, **kwargs: _CommandOptions) -> list[tuple[str, int]]:
        """
        Return a list of (channel, number of subscribers) tuples
        for each channel given in ``*args``

        For more information see https://redis.io/commands/pubsub-numsub
        """
        ...

class ScriptCommands(Generic[_StrType]):
    """
    Redis Lua script commands. see:
    https://redis.com/ebook/part-3-next-steps/chapter-11-scripting-redis-with-lua/
    """
    def eval(self, script, numkeys, *keys_and_args):
        """
        Execute the Lua ``script``, specifying the ``numkeys`` the script
        will touch and the key names and argument values in ``keys_and_args``.
        Returns the result of the script.

        In practice, use the object returned by ``register_script``. This
        function exists purely for Redis API completion.

        For more information see  https://redis.io/commands/eval
        """
        ...
    def evalsha(self, sha, numkeys, *keys_and_args):
        """
        Use the ``sha`` to execute a Lua script already registered via EVAL
        or SCRIPT LOAD. Specify the ``numkeys`` the script will touch and the
        key names and argument values in ``keys_and_args``. Returns the result
        of the script.

        In practice, use the object returned by ``register_script``. This
        function exists purely for Redis API completion.

        For more information see  https://redis.io/commands/evalsha
        """
        ...
    def script_exists(self, *args):
        """
        Check if a script exists in the script cache by specifying the SHAs of
        each script as ``args``. Returns a list of boolean values indicating if
        if each already script exists in the cache.

        For more information see  https://redis.io/commands/script-exists
        """
        ...
    def script_debug(self, *args): ...
    def script_flush(self, sync_type: Incomplete | None = None):
        """
        Flush all scripts from the script cache.
        ``sync_type`` is by default SYNC (synchronous) but it can also be
                      ASYNC.
        For more information see  https://redis.io/commands/script-flush
        """
        ...
    def script_kill(self):
        """
        Kill the currently executing Lua script

        For more information see https://redis.io/commands/script-kill
        """
        ...
    def script_load(self, script):
        """
        Load a Lua ``script`` into the script cache. Returns the SHA.

        For more information see https://redis.io/commands/script-load
        """
        ...
    def register_script(self, script: str | _StrType) -> Script:
        """
        Register a Lua ``script`` specifying the ``keys`` it will touch.
        Returns a Script object that is callable and hides the complexity of
        deal with scripts, keys, and shas. This is the preferred way to work
        with Lua scripts.
        """
        ...

class AsyncScriptCommands(Generic[_StrType]):
    async def eval(self, script, numkeys, *keys_and_args):
        """
        Execute the Lua ``script``, specifying the ``numkeys`` the script
        will touch and the key names and argument values in ``keys_and_args``.
        Returns the result of the script.

        In practice, use the object returned by ``register_script``. This
        function exists purely for Redis API completion.

        For more information see  https://redis.io/commands/eval
        """
        ...
    async def evalsha(self, sha, numkeys, *keys_and_args):
        """
        Use the ``sha`` to execute a Lua script already registered via EVAL
        or SCRIPT LOAD. Specify the ``numkeys`` the script will touch and the
        key names and argument values in ``keys_and_args``. Returns the result
        of the script.

        In practice, use the object returned by ``register_script``. This
        function exists purely for Redis API completion.

        For more information see  https://redis.io/commands/evalsha
        """
        ...
    async def script_exists(self, *args):
        """
        Check if a script exists in the script cache by specifying the SHAs of
        each script as ``args``. Returns a list of boolean values indicating if
        if each already script exists in the cache.

        For more information see  https://redis.io/commands/script-exists
        """
        ...
    async def script_debug(self, *args): ...
    async def script_flush(self, sync_type: Incomplete | None = None):
        """
        Flush all scripts from the script cache.
        ``sync_type`` is by default SYNC (synchronous) but it can also be
                      ASYNC.
        For more information see  https://redis.io/commands/script-flush
        """
        ...
    async def script_kill(self):
        """
        Kill the currently executing Lua script

        For more information see https://redis.io/commands/script-kill
        """
        ...
    async def script_load(self, script):
        """
        Load a Lua ``script`` into the script cache. Returns the SHA.

        For more information see https://redis.io/commands/script-load
        """
        ...
    def register_script(self, script: ScriptTextT) -> AsyncScript:
        """
        Register a Lua ``script`` specifying the ``keys`` it will touch.
        Returns a Script object that is callable and hides the complexity of
        deal with scripts, keys, and shas. This is the preferred way to work
        with Lua scripts.
        """
        ...

class GeoCommands:
    """
    Redis Geospatial commands.
    see: https://redis.com/redis-best-practices/indexing-patterns/geospatial/
    """
    def geoadd(self, name, values, nx: bool = False, xx: bool = False, ch: bool = False):
        """
        Add the specified geospatial items to the specified key identified
        by the ``name`` argument. The Geospatial items are given as ordered
        members of the ``values`` argument, each item or place is formed by
        the triad longitude, latitude and name.

        Note: You can use ZREM to remove elements.

        ``nx`` forces ZADD to only create new elements and not to update
        scores for elements that already exist.

        ``xx`` forces ZADD to only update scores of elements that already
        exist. New elements will not be added.

        ``ch`` modifies the return value to be the numbers of elements changed.
        Changed elements include new elements that were added and elements
        whose scores changed.

        For more information see https://redis.io/commands/geoadd
        """
        ...
    def geodist(self, name, place1, place2, unit: Incomplete | None = None):
        """
        Return the distance between ``place1`` and ``place2`` members of the
        ``name`` key.
        The units must be one of the following : m, km mi, ft. By default
        meters are used.

        For more information see https://redis.io/commands/geodist
        """
        ...
    def geohash(self, name, *values):
        """
        Return the geo hash string for each item of ``values`` members of
        the specified key identified by the ``name`` argument.

        For more information see https://redis.io/commands/geohash
        """
        ...
    def geopos(self, name, *values):
        """
        Return the positions of each item of ``values`` as members of
        the specified key identified by the ``name`` argument. Each position
        is represented by the pairs lon and lat.

        For more information see https://redis.io/commands/geopos
        """
        ...
    def georadius(
        self,
        name,
        longitude,
        latitude,
        radius,
        unit: Incomplete | None = None,
        withdist: bool = False,
        withcoord: bool = False,
        withhash: bool = False,
        count: Incomplete | None = None,
        sort: Incomplete | None = None,
        store: Incomplete | None = None,
        store_dist: Incomplete | None = None,
        any: bool = False,
    ):
        """
        Return the members of the specified key identified by the
        ``name`` argument which are within the borders of the area specified
        with the ``latitude`` and ``longitude`` location and the maximum
        distance from the center specified by the ``radius`` value.

        The units must be one of the following : m, km mi, ft. By default

        ``withdist`` indicates to return the distances of each place.

        ``withcoord`` indicates to return the latitude and longitude of
        each place.

        ``withhash`` indicates to return the geohash string of each place.

        ``count`` indicates to return the number of elements up to N.

        ``sort`` indicates to return the places in a sorted way, ASC for
        nearest to fairest and DESC for fairest to nearest.

        ``store`` indicates to save the places names in a sorted set named
        with a specific key, each element of the destination sorted set is
        populated with the score got from the original geo sorted set.

        ``store_dist`` indicates to save the places names in a sorted set
        named with a specific key, instead of ``store`` the sorted set
        destination score is set with the distance.

        For more information see https://redis.io/commands/georadius
        """
        ...
    def georadiusbymember(
        self,
        name,
        member,
        radius,
        unit: Incomplete | None = None,
        withdist: bool = False,
        withcoord: bool = False,
        withhash: bool = False,
        count: Incomplete | None = None,
        sort: Incomplete | None = None,
        store: Incomplete | None = None,
        store_dist: Incomplete | None = None,
        any: bool = False,
    ):
        """
        This command is exactly like ``georadius`` with the sole difference
        that instead of taking, as the center of the area to query, a longitude
        and latitude value, it takes the name of a member already existing
        inside the geospatial index represented by the sorted set.

        For more information see https://redis.io/commands/georadiusbymember
        """
        ...
    def geosearch(
        self,
        name,
        member: Incomplete | None = None,
        longitude: Incomplete | None = None,
        latitude: Incomplete | None = None,
        unit: str = "m",
        radius: Incomplete | None = None,
        width: Incomplete | None = None,
        height: Incomplete | None = None,
        sort: Incomplete | None = None,
        count: Incomplete | None = None,
        any: bool = False,
        withcoord: bool = False,
        withdist: bool = False,
        withhash: bool = False,
    ):
        """
        Return the members of specified key identified by the
        ``name`` argument, which are within the borders of the
        area specified by a given shape. This command extends the
        GEORADIUS command, so in addition to searching within circular
        areas, it supports searching within rectangular areas.
        This command should be used in place of the deprecated
        GEORADIUS and GEORADIUSBYMEMBER commands.
        ``member`` Use the position of the given existing
         member in the sorted set. Can't be given with ``longitude``
         and ``latitude``.
        ``longitude`` and ``latitude`` Use the position given by
        this coordinates. Can't be given with ``member``
        ``radius`` Similar to GEORADIUS, search inside circular
        area according the given radius. Can't be given with
        ``height`` and ``width``.
        ``height`` and ``width`` Search inside an axis-aligned
        rectangle, determined by the given height and width.
        Can't be given with ``radius``
        ``unit`` must be one of the following : m, km, mi, ft.
        `m` for meters (the default value), `km` for kilometers,
        `mi` for miles and `ft` for feet.
        ``sort`` indicates to return the places in a sorted way,
        ASC for nearest to furthest and DESC for furthest to nearest.
        ``count`` limit the results to the first count matching items.
        ``any`` is set to True, the command will return as soon as
        enough matches are found. Can't be provided without ``count``
        ``withdist`` indicates to return the distances of each place.
        ``withcoord`` indicates to return the latitude and longitude of
        each place.
        ``withhash`` indicates to return the geohash string of each place.

        For more information see https://redis.io/commands/geosearch
        """
        ...
    def geosearchstore(
        self,
        dest,
        name,
        member: Incomplete | None = None,
        longitude: Incomplete | None = None,
        latitude: Incomplete | None = None,
        unit: str = "m",
        radius: Incomplete | None = None,
        width: Incomplete | None = None,
        height: Incomplete | None = None,
        sort: Incomplete | None = None,
        count: Incomplete | None = None,
        any: bool = False,
        storedist: bool = False,
    ):
        """
        This command is like GEOSEARCH, but stores the result in
        ``dest``. By default, it stores the results in the destination
        sorted set with their geospatial information.
        if ``store_dist`` set to True, the command will stores the
        items in a sorted set populated with their distance from the
        center of the circle or box, as a floating-point number.

        For more information see https://redis.io/commands/geosearchstore
        """
        ...

class AsyncGeoCommands:
    """
    Redis Geospatial commands.
    see: https://redis.com/redis-best-practices/indexing-patterns/geospatial/
    """
    async def geoadd(self, name, values, nx: bool = False, xx: bool = False, ch: bool = False):
        """
        Add the specified geospatial items to the specified key identified
        by the ``name`` argument. The Geospatial items are given as ordered
        members of the ``values`` argument, each item or place is formed by
        the triad longitude, latitude and name.

        Note: You can use ZREM to remove elements.

        ``nx`` forces ZADD to only create new elements and not to update
        scores for elements that already exist.

        ``xx`` forces ZADD to only update scores of elements that already
        exist. New elements will not be added.

        ``ch`` modifies the return value to be the numbers of elements changed.
        Changed elements include new elements that were added and elements
        whose scores changed.

        For more information see https://redis.io/commands/geoadd
        """
        ...
    async def geodist(self, name, place1, place2, unit: Incomplete | None = None):
        """
        Return the distance between ``place1`` and ``place2`` members of the
        ``name`` key.
        The units must be one of the following : m, km mi, ft. By default
        meters are used.

        For more information see https://redis.io/commands/geodist
        """
        ...
    async def geohash(self, name, *values):
        """
        Return the geo hash string for each item of ``values`` members of
        the specified key identified by the ``name`` argument.

        For more information see https://redis.io/commands/geohash
        """
        ...
    async def geopos(self, name, *values):
        """
        Return the positions of each item of ``values`` as members of
        the specified key identified by the ``name`` argument. Each position
        is represented by the pairs lon and lat.

        For more information see https://redis.io/commands/geopos
        """
        ...
    async def georadius(
        self,
        name,
        longitude,
        latitude,
        radius,
        unit: Incomplete | None = None,
        withdist: bool = False,
        withcoord: bool = False,
        withhash: bool = False,
        count: Incomplete | None = None,
        sort: Incomplete | None = None,
        store: Incomplete | None = None,
        store_dist: Incomplete | None = None,
        any: bool = False,
    ):
        """
        Return the members of the specified key identified by the
        ``name`` argument which are within the borders of the area specified
        with the ``latitude`` and ``longitude`` location and the maximum
        distance from the center specified by the ``radius`` value.

        The units must be one of the following : m, km mi, ft. By default

        ``withdist`` indicates to return the distances of each place.

        ``withcoord`` indicates to return the latitude and longitude of
        each place.

        ``withhash`` indicates to return the geohash string of each place.

        ``count`` indicates to return the number of elements up to N.

        ``sort`` indicates to return the places in a sorted way, ASC for
        nearest to fairest and DESC for fairest to nearest.

        ``store`` indicates to save the places names in a sorted set named
        with a specific key, each element of the destination sorted set is
        populated with the score got from the original geo sorted set.

        ``store_dist`` indicates to save the places names in a sorted set
        named with a specific key, instead of ``store`` the sorted set
        destination score is set with the distance.

        For more information see https://redis.io/commands/georadius
        """
        ...
    async def georadiusbymember(
        self,
        name,
        member,
        radius,
        unit: Incomplete | None = None,
        withdist: bool = False,
        withcoord: bool = False,
        withhash: bool = False,
        count: Incomplete | None = None,
        sort: Incomplete | None = None,
        store: Incomplete | None = None,
        store_dist: Incomplete | None = None,
        any: bool = False,
    ):
        """
        This command is exactly like ``georadius`` with the sole difference
        that instead of taking, as the center of the area to query, a longitude
        and latitude value, it takes the name of a member already existing
        inside the geospatial index represented by the sorted set.

        For more information see https://redis.io/commands/georadiusbymember
        """
        ...
    async def geosearch(
        self,
        name,
        member: Incomplete | None = None,
        longitude: Incomplete | None = None,
        latitude: Incomplete | None = None,
        unit: str = "m",
        radius: Incomplete | None = None,
        width: Incomplete | None = None,
        height: Incomplete | None = None,
        sort: Incomplete | None = None,
        count: Incomplete | None = None,
        any: bool = False,
        withcoord: bool = False,
        withdist: bool = False,
        withhash: bool = False,
    ):
        """
        Return the members of specified key identified by the
        ``name`` argument, which are within the borders of the
        area specified by a given shape. This command extends the
        GEORADIUS command, so in addition to searching within circular
        areas, it supports searching within rectangular areas.
        This command should be used in place of the deprecated
        GEORADIUS and GEORADIUSBYMEMBER commands.
        ``member`` Use the position of the given existing
         member in the sorted set. Can't be given with ``longitude``
         and ``latitude``.
        ``longitude`` and ``latitude`` Use the position given by
        this coordinates. Can't be given with ``member``
        ``radius`` Similar to GEORADIUS, search inside circular
        area according the given radius. Can't be given with
        ``height`` and ``width``.
        ``height`` and ``width`` Search inside an axis-aligned
        rectangle, determined by the given height and width.
        Can't be given with ``radius``
        ``unit`` must be one of the following : m, km, mi, ft.
        `m` for meters (the default value), `km` for kilometers,
        `mi` for miles and `ft` for feet.
        ``sort`` indicates to return the places in a sorted way,
        ASC for nearest to furthest and DESC for furthest to nearest.
        ``count`` limit the results to the first count matching items.
        ``any`` is set to True, the command will return as soon as
        enough matches are found. Can't be provided without ``count``
        ``withdist`` indicates to return the distances of each place.
        ``withcoord`` indicates to return the latitude and longitude of
        each place.
        ``withhash`` indicates to return the geohash string of each place.

        For more information see https://redis.io/commands/geosearch
        """
        ...
    async def geosearchstore(
        self,
        dest,
        name,
        member: Incomplete | None = None,
        longitude: Incomplete | None = None,
        latitude: Incomplete | None = None,
        unit: str = "m",
        radius: Incomplete | None = None,
        width: Incomplete | None = None,
        height: Incomplete | None = None,
        sort: Incomplete | None = None,
        count: Incomplete | None = None,
        any: bool = False,
        storedist: bool = False,
    ):
        """
        This command is like GEOSEARCH, but stores the result in
        ``dest``. By default, it stores the results in the destination
        sorted set with their geospatial information.
        if ``store_dist`` set to True, the command will stores the
        items in a sorted set populated with their distance from the
        center of the circle or box, as a floating-point number.

        For more information see https://redis.io/commands/geosearchstore
        """
        ...

class ModuleCommands:
    """
    Redis Module commands.
    see: https://redis.io/topics/modules-intro
    """
    def module_load(self, path, *args):
        """
        Loads the module from ``path``.
        Passes all ``*args`` to the module, during loading.
        Raises ``ModuleError`` if a module is not found at ``path``.

        For more information see https://redis.io/commands/module-load
        """
        ...
    def module_unload(self, name):
        """
        Unloads the module ``name``.
        Raises ``ModuleError`` if ``name`` is not in loaded modules.

        For more information see https://redis.io/commands/module-unload
        """
        ...
    def module_list(self):
        """
        Returns a list of dictionaries containing the name and version of
        all loaded modules.

        For more information see https://redis.io/commands/module-list
        """
        ...
    def command_info(self): ...
    def command_count(self): ...
    def command_getkeys(self, *args): ...
    def command(self): ...

class Script:
    """An executable Lua script object returned by ``register_script``"""
    def __init__(self, registered_client, script) -> None: ...
    def __call__(self, keys=[], args=[], client: Incomplete | None = None):
        """Execute the script, passing any required ``args``"""
        ...

class BitFieldOperation:
    """Command builder for BITFIELD commands."""
    def __init__(self, client, key, default_overflow: Incomplete | None = None): ...
    def reset(self) -> None:
        """Reset the state of the instance to when it was constructed"""
        ...
    def overflow(self, overflow):
        """
        Update the overflow algorithm of successive INCRBY operations
        :param overflow: Overflow algorithm, one of WRAP, SAT, FAIL. See the
            Redis docs for descriptions of these algorithmsself.
        :returns: a :py:class:`BitFieldOperation` instance.
        """
        ...
    def incrby(self, fmt, offset, increment, overflow: Incomplete | None = None):
        """
        Increment a bitfield by a given amount.
        :param fmt: format-string for the bitfield being updated, e.g. 'u8'
            for an unsigned 8-bit integer.
        :param offset: offset (in number of bits). If prefixed with a
            '#', this is an offset multiplier, e.g. given the arguments
            fmt='u8', offset='#2', the offset will be 16.
        :param int increment: value to increment the bitfield by.
        :param str overflow: overflow algorithm. Defaults to WRAP, but other
            acceptable values are SAT and FAIL. See the Redis docs for
            descriptions of these algorithms.
        :returns: a :py:class:`BitFieldOperation` instance.
        """
        ...
    def get(self, fmt, offset):
        """
        Get the value of a given bitfield.
        :param fmt: format-string for the bitfield being read, e.g. 'u8' for
            an unsigned 8-bit integer.
        :param offset: offset (in number of bits). If prefixed with a
            '#', this is an offset multiplier, e.g. given the arguments
            fmt='u8', offset='#2', the offset will be 16.
        :returns: a :py:class:`BitFieldOperation` instance.
        """
        ...
    def set(self, fmt, offset, value):
        """
        Set the value of a given bitfield.
        :param fmt: format-string for the bitfield being read, e.g. 'u8' for
            an unsigned 8-bit integer.
        :param offset: offset (in number of bits). If prefixed with a
            '#', this is an offset multiplier, e.g. given the arguments
            fmt='u8', offset='#2', the offset will be 16.
        :param int value: value to set at the given position.
        :returns: a :py:class:`BitFieldOperation` instance.
        """
        ...
    @property
    def command(self): ...
    def execute(self):
        """
        Execute the operation(s) in a single BITFIELD command. The return value
        is a list of values corresponding to each operation. If the client
        used to create this instance was a pipeline, the list of values
        will be present within the pipeline's execute.
        """
        ...

class AsyncModuleCommands(ModuleCommands):
    async def command_info(self) -> None: ...

class ClusterCommands:
    """Class for Redis Cluster commands"""
    def cluster(self, cluster_arg: str, *args, **kwargs: _CommandOptions): ...
    def readwrite(self, **kwargs: _CommandOptions) -> bool:
        """
        Disables read queries for a connection to a Redis Cluster slave node.

        For more information see https://redis.io/commands/readwrite
        """
        ...
    def readonly(self, **kwargs: _CommandOptions) -> bool:
        """
        Enables read queries for a connection to a Redis Cluster replica node.

        For more information see https://redis.io/commands/readonly
        """
        ...

class AsyncClusterCommands:
    """Class for Redis Cluster commands"""
    async def cluster(self, cluster_arg: str, *args, **kwargs: _CommandOptions): ...
    async def readwrite(self, **kwargs: _CommandOptions) -> bool:
        """
        Disables read queries for a connection to a Redis Cluster slave node.

        For more information see https://redis.io/commands/readwrite
        """
        ...
    async def readonly(self, **kwargs: _CommandOptions) -> bool:
        """
        Enables read queries for a connection to a Redis Cluster replica node.

        For more information see https://redis.io/commands/readonly
        """
        ...

class FunctionCommands:
    """Redis Function commands"""
    def function_load(self, code: str, replace: bool | None = False) -> Awaitable[str] | str:
        """
        Load a library to Redis.
        :param code: the source code (must start with
        Shebang statement that provides a metadata about the library)
        :param replace: changes the behavior to overwrite the existing library
        with the new contents.
        Return the library name that was loaded.

        For more information see https://redis.io/commands/function-load
        """
        ...
    def function_delete(self, library: str) -> Awaitable[str] | str:
        """
        Delete the library called ``library`` and all its functions.

        For more information see https://redis.io/commands/function-delete
        """
        ...
    def function_flush(self, mode: str = "SYNC") -> Awaitable[str] | str:
        """
        Deletes all the libraries.

        For more information see https://redis.io/commands/function-flush
        """
        ...
    def function_list(self, library: str | None = "*", withcode: bool | None = False) -> Awaitable[list[Any]] | list[Any]:
        """
        Return information about the functions and libraries.
        :param library: pecify a pattern for matching library names
        :param withcode: cause the server to include the libraries source
         implementation in the reply
        """
        ...
    def fcall(self, function, numkeys: int, *keys_and_args: list[Any] | None) -> Awaitable[str] | str:
        """
        Invoke a function.

        For more information see https://redis.io/commands/fcall
        """
        ...
    def fcall_ro(self, function, numkeys: int, *keys_and_args: list[Any] | None) -> Awaitable[str] | str:
        """
        This is a read-only variant of the FCALL command that cannot
        execute commands that modify data.

        For more information see https://redis.io/commands/fcal_ro
        """
        ...
    def function_dump(self) -> Awaitable[str] | str:
        """
        Return the serialized payload of loaded libraries.

        For more information see https://redis.io/commands/function-dump
        """
        ...
    def function_restore(self, payload: str, policy: str | None = "APPEND") -> Awaitable[str] | str:
        """
        Restore libraries from the serialized ``payload``.
        You can use the optional policy argument to provide a policy
        for handling existing libraries.

        For more information see https://redis.io/commands/function-restore
        """
        ...
    def function_kill(self) -> Awaitable[str] | str:
        """
        Kill a function that is currently executing.

        For more information see https://redis.io/commands/function-kill
        """
        ...
    def function_stats(self) -> Awaitable[list[Any]] | list[Any]:
        """
        Return information about the function that's currently running
        and information about the available execution engines.

        For more information see https://redis.io/commands/function-stats
        """
        ...

class AsyncFunctionCommands:
    """Redis Function commands"""
    async def function_load(self, code: str, replace: bool | None = False) -> Awaitable[str] | str:
        """
        Load a library to Redis.
        :param code: the source code (must start with
        Shebang statement that provides a metadata about the library)
        :param replace: changes the behavior to overwrite the existing library
        with the new contents.
        Return the library name that was loaded.

        For more information see https://redis.io/commands/function-load
        """
        ...
    async def function_delete(self, library: str) -> Awaitable[str] | str:
        """
        Delete the library called ``library`` and all its functions.

        For more information see https://redis.io/commands/function-delete
        """
        ...
    async def function_flush(self, mode: str = "SYNC") -> Awaitable[str] | str:
        """
        Deletes all the libraries.

        For more information see https://redis.io/commands/function-flush
        """
        ...
    async def function_list(
        self, library: str | None = "*", withcode: bool | None = False
    ) -> Awaitable[list[Any]] | list[Any]:
        """
        Return information about the functions and libraries.
        :param library: pecify a pattern for matching library names
        :param withcode: cause the server to include the libraries source
         implementation in the reply
        """
        ...
    async def fcall(self, function, numkeys: int, *keys_and_args: list[Any] | None) -> Awaitable[str] | str:
        """
        Invoke a function.

        For more information see https://redis.io/commands/fcall
        """
        ...
    async def fcall_ro(self, function, numkeys: int, *keys_and_args: list[Any] | None) -> Awaitable[str] | str:
        """
        This is a read-only variant of the FCALL command that cannot
        execute commands that modify data.

        For more information see https://redis.io/commands/fcal_ro
        """
        ...
    async def function_dump(self) -> Awaitable[str] | str:
        """
        Return the serialized payload of loaded libraries.

        For more information see https://redis.io/commands/function-dump
        """
        ...
    async def function_restore(self, payload: str, policy: str | None = "APPEND") -> Awaitable[str] | str:
        """
        Restore libraries from the serialized ``payload``.
        You can use the optional policy argument to provide a policy
        for handling existing libraries.

        For more information see https://redis.io/commands/function-restore
        """
        ...
    async def function_kill(self) -> Awaitable[str] | str:
        """
        Kill a function that is currently executing.

        For more information see https://redis.io/commands/function-kill
        """
        ...
    async def function_stats(self) -> Awaitable[list[Any]] | list[Any]:
        """
        Return information about the function that's currently running
        and information about the available execution engines.

        For more information see https://redis.io/commands/function-stats
        """
        ...

class DataAccessCommands(
    BasicKeyCommands[_StrType],
    HyperlogCommands,
    HashCommands[_StrType],
    GeoCommands,
    ListCommands[_StrType],
    ScanCommands[_StrType],
    SetCommands[_StrType],
    StreamCommands,
    SortedSetCommands[_StrType],
):
    """
    A class containing all of the implemented data access redis commands.
    This class is to be used as a mixin for synchronous Redis clients.
    """
    ...
class AsyncDataAccessCommands(
    AsyncBasicKeyCommands[_StrType],
    AsyncHyperlogCommands,
    AsyncHashCommands[_StrType],
    AsyncGeoCommands,
    AsyncListCommands[_StrType],
    AsyncScanCommands[_StrType],
    AsyncSetCommands[_StrType],
    AsyncStreamCommands,
    AsyncSortedSetCommands[_StrType],
):
    """
    A class containing all of the implemented data access redis commands.
    This class is to be used as a mixin for asynchronous Redis clients.
    """
    ...
class CoreCommands(
    ACLCommands[_StrType],
    ClusterCommands,
    DataAccessCommands[_StrType],
    ManagementCommands,
    ModuleCommands,
    PubSubCommands,
    ScriptCommands[_StrType],
):
    """
    A class containing all of the implemented redis commands. This class is
    to be used as a mixin for synchronous Redis clients.
    """
    ...
class AsyncCoreCommands(
    AsyncACLCommands[_StrType],
    AsyncClusterCommands,
    AsyncDataAccessCommands[_StrType],
    AsyncManagementCommands,
    AsyncModuleCommands,
    AsyncPubSubCommands,
    AsyncScriptCommands[_StrType],
    AsyncFunctionCommands,
):
    """
    A class containing all of the implemented redis commands. This class is
    to be used as a mixin for asynchronous Redis clients.
    """
    ...
