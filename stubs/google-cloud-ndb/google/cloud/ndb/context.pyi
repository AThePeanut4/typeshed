"""Context for currently running tasks and transactions."""

from _typeshed import Incomplete
from collections.abc import Callable
from typing import NamedTuple

from google.cloud.ndb import Key, exceptions as exceptions

class _LocalState:
    """Thread local state."""
    def __init__(self) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, value) -> None: ...
    @property
    def toplevel_context(self): ...
    @toplevel_context.setter
    def toplevel_context(self, value) -> None: ...

def get_context(raise_context_error: bool = ...):
    """
    Get the current context.

    This function should be called within a context established by
    :meth:`google.cloud.ndb.client.Client.context`.

    Args:
        raise_context_error (bool): If set to :data:`True`, will raise an
            exception if called outside of a context. Set this to :data:`False`
            in order to have it just return :data:`None` if called outside of a
            context. Default: :data:`True`

    Returns:
        Context: The current context.

    Raises:
        exceptions.ContextError: If called outside of a context
            established by :meth:`google.cloud.ndb.client.Client.context` and
            ``raise_context_error`` is :data:`True`.
    """
    ...
def get_toplevel_context(raise_context_error: bool = ...):
    """
    Get the current top level context.

    This function should be called within a context established by
    :meth:`google.cloud.ndb.client.Client.context`.

    The toplevel context is the context created by the call to
    :meth:`google.cloud.ndb.client.Client.context`. At times, this context will
    be superseded by subcontexts, which are used, for example, during
    transactions. This function will always return the top level context
    regardless of whether one of these subcontexts is the current one.

    Args:
        raise_context_error (bool): If set to :data:`True`, will raise an
            exception if called outside of a context. Set this to :data:`False`
            in order to have it just return :data:`None` if called outside of a
            context. Default: :data:`True`

    Returns:
        Context: The current context.

    Raises:
        exceptions.ContextError: If called outside of a context
            established by :meth:`google.cloud.ndb.client.Client.context` and
            ``raise_context_error`` is :data:`True`.
    """
    ...

class _ContextTuple(NamedTuple):
    id: Incomplete
    client: Incomplete
    namespace: Incomplete
    eventloop: Incomplete
    batches: Incomplete
    commit_batches: Incomplete
    transaction: Incomplete
    cache: Incomplete
    global_cache: Incomplete
    on_commit_callbacks: Incomplete
    transaction_complete_callbacks: Incomplete
    legacy_data: Incomplete

class _Context(_ContextTuple):
    """
    Current runtime state.

    Instances of this class hold on to runtime state such as the current event
    loop, current transaction, etc. Instances are shallowly immutable, but
    contain references to data structures which are mutable, such as the event
    loop. A new context can be derived from an existing context using
    :meth:`new`.

    :class:`Context` is a subclass of :class:`_Context` which provides only
    publicly facing interface. The use of two classes is only to provide a
    distinction between public and private API.

    Arguments:
        client (client.Client): The NDB client for this context.
    """
    def __new__(
        cls,
        client,
        id: Incomplete | None = ...,
        namespace=...,
        eventloop: Incomplete | None = ...,
        batches: Incomplete | None = ...,
        commit_batches: Incomplete | None = ...,
        transaction: Incomplete | None = ...,
        cache: Incomplete | None = ...,
        cache_policy: Incomplete | None = ...,
        global_cache: Incomplete | None = ...,
        global_cache_policy: Callable[[Key], bool] | None = ...,
        global_cache_timeout_policy: Incomplete | None = ...,
        datastore_policy: Incomplete | None = ...,
        on_commit_callbacks: Incomplete | None = ...,
        transaction_complete_callbacks: Incomplete | None = ...,
        legacy_data: bool = ...,
        retry: Incomplete | None = ...,
        rpc_time: Incomplete | None = ...,
        wait_time: Incomplete | None = ...,
    ): ...
    def new(self, **kwargs):
        """
        Create a new :class:`_Context` instance.

        New context will be the same as context except values from ``kwargs``
        will be substituted.
        """
        ...
    rpc_time: int
    wait_time: int
    def use(self) -> None:
        """
        Use this context as the current context.

        This method returns a context manager for use with the ``with``
        statement. Code inside the ``with`` context will see this context as
        the current context.
        """
        ...

class Context(_Context):
    def clear_cache(self) -> None: ...
    def flush(self) -> None: ...
    def get_namespace(self): ...
    def get_cache_policy(self): ...
    def get_datastore_policy(self) -> None: ...
    def get_global_cache_policy(self): ...
    get_memcache_policy: Incomplete
    def get_global_cache_timeout_policy(self): ...
    get_memcache_timeout_policy: Incomplete
    cache_policy: Incomplete
    def set_cache_policy(self, policy): ...
    datastore_policy: Incomplete
    def set_datastore_policy(self, policy): ...
    global_cache_policy: Incomplete
    def set_global_cache_policy(self, policy): ...
    set_memcache_policy: Incomplete
    global_cache_timeout_policy: Incomplete
    def set_global_cache_timeout_policy(self, policy): ...
    set_memcache_timeout_policy: Incomplete
    def get_retry_state(self): ...
    def set_retry_state(self, state) -> None: ...
    def clear_retry_state(self) -> None: ...
    def call_on_commit(self, callback) -> None:
        """
        Call a callback upon successful commit of a transaction.

        If not in a transaction, the callback is called immediately.

        In a transaction, multiple callbacks may be registered and will be
        called once the transaction commits, in the order in which they
        were registered.  If the transaction fails, the callbacks will not
        be called.

        If the callback raises an exception, it bubbles up normally.  This
        means: If the callback is called immediately, any exception it
        raises will bubble up immediately.  If the call is postponed until
        commit, remaining callbacks will be skipped and the exception will
        bubble up through the transaction() call.  (However, the
        transaction is already committed at that point.)

        Args:
            callback (Callable): The callback function.
        """
        ...
    def in_transaction(self):
        """
        Get whether a transaction is currently active.

        Returns:
            bool: :data:`True` if currently in a transaction, otherwise
                :data:`False`.
        """
        ...
    def in_retry(self):
        """
        Get whether we are already in a retry block.

        Returns:
            bool: :data:`True` if currently in a retry block, otherwise
                :data:`False`.
        """
        ...
    def memcache_add(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_cas(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_decr(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_delete(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_get(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_gets(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_incr(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_replace(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def memcache_set(self, *args, **kwargs) -> None:
        """Direct pass-through to memcache client. No longer implemented."""
        ...
    def urlfetch(self, *args, **kwargs) -> None:
        """Fetch a resource using HTTP. No longer implemented."""
        ...

class ContextOptions:
    def __init__(self, *args, **kwargs) -> None: ...

class TransactionOptions:
    NESTED: int
    MANDATORY: int
    ALLOWED: int
    INDEPENDENT: int

class AutoBatcher:
    def __init__(self, *args, **kwargs) -> None: ...
