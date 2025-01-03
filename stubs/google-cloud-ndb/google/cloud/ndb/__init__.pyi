"""
``ndb`` is a library for Google Cloud Firestore in Datastore Mode and Google Cloud Datastore.

It was originally included in the Google App Engine runtime as a "new"
version of the ``db`` API (hence ``ndb``).

.. autodata:: __version__
.. autodata:: __all__
"""

from google.cloud.ndb._datastore_api import EVENTUAL as EVENTUAL, EVENTUAL_CONSISTENCY as EVENTUAL_CONSISTENCY, STRONG as STRONG
from google.cloud.ndb._datastore_query import Cursor as Cursor, QueryIterator as QueryIterator
from google.cloud.ndb._transaction import (
    in_transaction as in_transaction,
    non_transactional as non_transactional,
    transaction as transaction,
    transaction_async as transaction_async,
    transactional as transactional,
    transactional_async as transactional_async,
    transactional_tasklet as transactional_tasklet,
)
from google.cloud.ndb.client import Client as Client
from google.cloud.ndb.context import (
    AutoBatcher as AutoBatcher,
    Context as Context,
    ContextOptions as ContextOptions,
    TransactionOptions as TransactionOptions,
    get_context as get_context,
    get_toplevel_context as get_toplevel_context,
)
from google.cloud.ndb.global_cache import GlobalCache as GlobalCache, MemcacheCache as MemcacheCache, RedisCache as RedisCache
from google.cloud.ndb.key import Key as Key
from google.cloud.ndb.model import (
    BadProjectionError as BadProjectionError,
    BlobKey as BlobKey,
    BlobKeyProperty as BlobKeyProperty,
    BlobProperty as BlobProperty,
    BooleanProperty as BooleanProperty,
    ComputedProperty as ComputedProperty,
    ComputedPropertyError as ComputedPropertyError,
    DateProperty as DateProperty,
    DateTimeProperty as DateTimeProperty,
    Expando as Expando,
    FloatProperty as FloatProperty,
    GenericProperty as GenericProperty,
    GeoPt as GeoPt,
    GeoPtProperty as GeoPtProperty,
    Index as Index,
    IndexProperty as IndexProperty,
    IndexState as IndexState,
    IntegerProperty as IntegerProperty,
    InvalidPropertyError as InvalidPropertyError,
    JsonProperty as JsonProperty,
    KeyProperty as KeyProperty,
    KindError as KindError,
    LocalStructuredProperty as LocalStructuredProperty,
    MetaModel as MetaModel,
    Model as Model,
    ModelAdapter as ModelAdapter,
    ModelAttribute as ModelAttribute,
    ModelKey as ModelKey,
    PickleProperty as PickleProperty,
    Property as Property,
    ReadonlyPropertyError as ReadonlyPropertyError,
    Rollback as Rollback,
    StringProperty as StringProperty,
    StructuredProperty as StructuredProperty,
    TextProperty as TextProperty,
    TimeProperty as TimeProperty,
    UnprojectedPropertyError as UnprojectedPropertyError,
    User as User,
    UserNotFoundError as UserNotFoundError,
    UserProperty as UserProperty,
    delete_multi as delete_multi,
    delete_multi_async as delete_multi_async,
    get_indexes as get_indexes,
    get_indexes_async as get_indexes_async,
    get_multi as get_multi,
    get_multi_async as get_multi_async,
    make_connection as make_connection,
    put_multi as put_multi,
    put_multi_async as put_multi_async,
)
from google.cloud.ndb.polymodel import PolyModel as PolyModel
from google.cloud.ndb.query import (
    AND as AND,
    OR as OR,
    ConjunctionNode as ConjunctionNode,
    DisjunctionNode as DisjunctionNode,
    FalseNode as FalseNode,
    FilterNode as FilterNode,
    Node as Node,
    Parameter as Parameter,
    ParameterizedFunction as ParameterizedFunction,
    ParameterizedThing as ParameterizedThing,
    ParameterNode as ParameterNode,
    PostFilterNode as PostFilterNode,
    Query as Query,
    QueryOptions as QueryOptions,
    RepeatedStructuredPropertyPredicate as RepeatedStructuredPropertyPredicate,
    gql as gql,
)
from google.cloud.ndb.tasklets import (
    Future as Future,
    QueueFuture as QueueFuture,
    ReducingFuture as ReducingFuture,
    Return as Return,
    SerialQueueFuture as SerialQueueFuture,
    add_flow_exception as add_flow_exception,
    make_context as make_context,
    make_default_context as make_default_context,
    set_context as set_context,
    sleep as sleep,
    synctasklet as synctasklet,
    tasklet as tasklet,
    toplevel as toplevel,
    wait_all as wait_all,
    wait_any as wait_any,
)
from google.cloud.ndb.version import __version__ as __version__

__all__ = [
    "__version__",
    "AutoBatcher",
    "Client",
    "Context",
    "ContextOptions",
    "EVENTUAL",
    "EVENTUAL_CONSISTENCY",
    "STRONG",
    "TransactionOptions",
    "Key",
    "BlobKey",
    "BlobKeyProperty",
    "BlobProperty",
    "BooleanProperty",
    "ComputedProperty",
    "ComputedPropertyError",
    "DateProperty",
    "DateTimeProperty",
    "delete_multi",
    "delete_multi_async",
    "Expando",
    "FloatProperty",
    "GenericProperty",
    "GeoPt",
    "GeoPtProperty",
    "get_indexes",
    "get_indexes_async",
    "get_multi",
    "get_multi_async",
    "GlobalCache",
    "in_transaction",
    "Index",
    "IndexProperty",
    "IndexState",
    "IntegerProperty",
    "InvalidPropertyError",
    "BadProjectionError",
    "JsonProperty",
    "KeyProperty",
    "KindError",
    "LocalStructuredProperty",
    "make_connection",
    "MemcacheCache",
    "MetaModel",
    "Model",
    "ModelAdapter",
    "ModelAttribute",
    "ModelKey",
    "non_transactional",
    "PickleProperty",
    "PolyModel",
    "Property",
    "put_multi",
    "put_multi_async",
    "ReadonlyPropertyError",
    "RedisCache",
    "Rollback",
    "StringProperty",
    "StructuredProperty",
    "TextProperty",
    "TimeProperty",
    "transaction",
    "transaction_async",
    "transactional",
    "transactional_async",
    "transactional_tasklet",
    "UnprojectedPropertyError",
    "User",
    "UserNotFoundError",
    "UserProperty",
    "ConjunctionNode",
    "AND",
    "Cursor",
    "DisjunctionNode",
    "OR",
    "FalseNode",
    "FilterNode",
    "gql",
    "Node",
    "Parameter",
    "ParameterizedFunction",
    "ParameterizedThing",
    "ParameterNode",
    "PostFilterNode",
    "Query",
    "QueryIterator",
    "QueryOptions",
    "RepeatedStructuredPropertyPredicate",
    "add_flow_exception",
    "Future",
    "get_context",
    "get_toplevel_context",
    "make_context",
    "make_default_context",
    "QueueFuture",
    "ReducingFuture",
    "Return",
    "SerialQueueFuture",
    "set_context",
    "sleep",
    "synctasklet",
    "tasklet",
    "toplevel",
    "wait_all",
    "wait_any",
]
