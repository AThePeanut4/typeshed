from _typeshed import Incomplete

from google.cloud.ndb import model

class BaseStatistic(model.Model):
    """
    Base Statistic Model class.

    Attributes:
        bytes (int): the total number of bytes taken up in Cloud Datastore for
            the statistic instance.
        count (int): attribute is the total number of occurrences of the
            statistic in Cloud Datastore.
        timestamp (datetime.datetime): the time the statistic instance was
            written to Cloud Datastore.
    """
    STORED_KIND_NAME: str
    bytes: Incomplete
    count: Incomplete
    timestamp: Incomplete

class BaseKindStatistic(BaseStatistic):
    """
    Base Statistic Model class for stats associated with kinds.

    Attributes:
        kind_name (str): the name of the kind associated with the statistic
            instance.
        entity_bytes (int): the number of bytes taken up to store the statistic
            in Cloud Datastore minus the cost of storing indices.
    """
    STORED_KIND_NAME: str
    kind_name: Incomplete
    entity_bytes: Incomplete

class GlobalStat(BaseStatistic):
    """
    An aggregate of all entities across the entire application.

    This statistic only has a single instance in Cloud Datastore that contains
    the total number of entities stored and the total number of bytes they take
    up.

    Attributes:
        entity_bytes (int): the number of bytes taken up to store the statistic
            in Cloud Datastore minus the cost of storing indices.
        builtin_index_bytes (int): the number of bytes taken up to store
            built-in index entries.
        builtin_index_count (int): the number of built-in index entries.
        composite_index_bytes (int): the number of bytes taken up to store
            composite index entries.
        composite_index_count (int): the number of composite index entries.
    """
    STORED_KIND_NAME: str
    entity_bytes: Incomplete
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete
    composite_index_bytes: Incomplete
    composite_index_count: Incomplete

class NamespaceStat(BaseStatistic):
    """
    An aggregate of all entities across an entire namespace.

    This statistic has one instance per namespace.  The key_name is the
    represented namespace. NamespaceStat entities will only be found
    in the namespace "" (empty string). It contains the total
    number of entities stored and the total number of bytes they take up.

    Attributes:
        subject_namespace (str): the namespace associated with the statistic
            instance.
        entity_bytes (int): the number of bytes taken up to store the statistic
            in Cloud Datastore minus the cost of storing indices.
        builtin_index_bytes (int): the number of bytes taken up to store
            builtin-in index entries.
        builtin_index_count (int): the number of built-in index entries.
        composite_index_bytes (int): the number of bytes taken up to store
            composite index entries.
        composite_index_count (int): the number of composite index entries.
    """
    STORED_KIND_NAME: str
    subject_namespace: Incomplete
    entity_bytes: Incomplete
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete
    composite_index_bytes: Incomplete
    composite_index_count: Incomplete

class KindStat(BaseKindStatistic):
    """
    An aggregate of all entities at the granularity of their Kind.

    There is an instance of the KindStat for every Kind that is in the
    application's datastore.  This stat contains per-Kind statistics.

    Attributes:
        builtin_index_bytes (int): the number of bytes taken up to store
            built-in index entries.
        builtin_index_count (int): the number of built-in index entries.
        composite_index_bytes (int): the number of bytes taken up to store
            composite index entries.
        composite_index_count (int): the number of composite index entries.
    """
    STORED_KIND_NAME: str
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete
    composite_index_bytes: Incomplete
    composite_index_count: Incomplete

class KindRootEntityStat(BaseKindStatistic):
    """
    Statistics of the number of root entities in Cloud Datastore by Kind.

    There is an instance of the KindRootEntityState for every Kind that is in
    the application's datastore and has an instance that is a root entity. This
    stat contains statistics regarding these root entity instances.
    """
    STORED_KIND_NAME: str

class KindNonRootEntityStat(BaseKindStatistic):
    """
    Statistics of the number of non root entities in Cloud Datastore by Kind.

    There is an instance of the KindNonRootEntityStat for every Kind that is in
    the application's datastore that is a not a root entity.  This stat
    contains statistics regarding these non root entity instances.
    """
    STORED_KIND_NAME: str

class PropertyTypeStat(BaseStatistic):
    """
    An aggregate of all properties across the entire application by type.

    There is an instance of the PropertyTypeStat for every property type
    (google.appengine.api.datastore_types._PROPERTY_TYPES) in use by the
    application in its datastore.

    Attributes:
        property_type (str): the property type associated with the statistic
            instance.
        entity_bytes (int): the number of bytes taken up to store the statistic
            in Cloud Datastore minus the cost of storing indices.
        builtin_index_bytes (int): the number of bytes taken up to store
        built-in index entries.
        builtin_index_count (int): the number of built-in index entries.
    """
    STORED_KIND_NAME: str
    property_type: Incomplete
    entity_bytes: Incomplete
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete

class KindPropertyTypeStat(BaseKindStatistic):
    """
    Statistics on (kind, property_type) tuples in the app's datastore.

    There is an instance of the KindPropertyTypeStat for every
    (kind, property_type) tuple in the application's datastore.

    Attributes:
        property_type (str): the property type associated with the statistic
            instance.
        builtin_index_bytes (int): the number of bytes taken up to store            built-in index entries.
        builtin_index_count (int): the number of built-in index entries.
    """
    STORED_KIND_NAME: str
    property_type: Incomplete
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete

class KindPropertyNameStat(BaseKindStatistic):
    """
    Statistics on (kind, property_name) tuples in the app's datastore.

    There is an instance of the KindPropertyNameStat for every
    (kind, property_name) tuple in the application's datastore.

    Attributes:
        property_name (str): the name of the property associated with the
            statistic instance.
        builtin_index_bytes (int): the number of bytes taken up to store
            built-in index entries.
        builtin_index_count (int): the number of built-in index entries.
    """
    STORED_KIND_NAME: str
    property_name: Incomplete
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete

class KindPropertyNamePropertyTypeStat(BaseKindStatistic):
    """
    Statistic on (kind, property_name, property_type) tuples in Cloud
    Datastore.

    There is an instance of the KindPropertyNamePropertyTypeStat for every
    (kind, property_name, property_type) tuple in the application's datastore.

    Attributes:
      property_type (str): the property type associated with the statistic
          instance.
      property_name (str): the name of the property associated with the
          statistic instance.
      builtin_index_bytes (int): the number of bytes taken up to store
          built-in index entries
      builtin_index_count (int): the number of built-in index entries.
    """
    STORED_KIND_NAME: str
    property_type: Incomplete
    property_name: Incomplete
    builtin_index_bytes: Incomplete
    builtin_index_count: Incomplete

class KindCompositeIndexStat(BaseStatistic):
    """
    Statistic on (kind, composite_index_id) tuples in Cloud Datastore.

    There is an instance of the KindCompositeIndexStat for every unique
    (kind, composite_index_id) tuple in the application's datastore indexes.

    Attributes:
        index_id (int): the id of the composite index associated with the
            statistic instance.
        kind_name (str): the name of the kind associated with the statistic
            instance.
    """
    STORED_KIND_NAME: str
    index_id: Incomplete
    kind_name: Incomplete

class NamespaceGlobalStat(GlobalStat):
    """
    GlobalStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindStat(KindStat):
    """
    KindStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindRootEntityStat(KindRootEntityStat):
    """
    KindRootEntityStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindNonRootEntityStat(KindNonRootEntityStat):
    """
    KindNonRootEntityStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespacePropertyTypeStat(PropertyTypeStat):
    """
    PropertyTypeStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindPropertyTypeStat(KindPropertyTypeStat):
    """
    KindPropertyTypeStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindPropertyNameStat(KindPropertyNameStat):
    """
    KindPropertyNameStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindPropertyNamePropertyTypeStat(KindPropertyNamePropertyTypeStat):
    """
    KindPropertyNamePropertyTypeStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str

class NamespaceKindCompositeIndexStat(KindCompositeIndexStat):
    """
    KindCompositeIndexStat equivalent for a specific namespace.

    These may be found in each specific namespace and represent stats for that
    particular namespace.
    """
    STORED_KIND_NAME: str
