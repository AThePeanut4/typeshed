from typing import Any, ClassVar, Literal

FIELDNAME: Any

class Limit:
    offset: Any
    count: Any
    def __init__(self, offset: int = 0, count: int = 0) -> None: ...
    def build_args(self): ...

class Reducer:
    """
    Base reducer object for all reducers.

    See the `redisearch.reducers` module for the actual reducers.
    """
    NAME: ClassVar[None]
    def __init__(self, *args) -> None: ...
    def alias(self, alias):
        """
        Set the alias for this reducer.

        ### Parameters

        - **alias**: The value of the alias for this reducer. If this is the
            special value `aggregation.FIELDNAME` then this reducer will be
            aliased using the same name as the field upon which it operates.
            Note that using `FIELDNAME` is only possible on reducers which
            operate on a single field value.

        This method returns the `Reducer` object making it suitable for
        chaining.
        """
        ...
    @property
    def args(self): ...

class SortDirection:
    """This special class is used to indicate sort direction."""
    DIRSTRING: ClassVar[str | None]
    field: Any
    def __init__(self, field) -> None: ...

class Asc(SortDirection):
    """Indicate that the given field should be sorted in ascending order"""
    DIRSTRING: ClassVar[Literal["ASC"]]

class Desc(SortDirection):
    """Indicate that the given field should be sorted in descending order"""
    DIRSTRING: ClassVar[Literal["DESC"]]

class AggregateRequest:
    """Aggregation request which can be passed to `Client.aggregate`."""
    def __init__(self, query: str = "*") -> None:
        """
        Create an aggregation request. This request may then be passed to
        `client.aggregate()`.

        In order for the request to be usable, it must contain at least one
        group.

        - **query** Query string for filtering records.

        All member methods (except `build_args()`)
        return the object itself, making them useful for chaining.
        """
        ...
    def load(self, *fields):
        """
        Indicate the fields to be returned in the response. These fields are
        returned in addition to any others implicitly specified.

        ### Parameters

        - **fields**: If fields not specified, all the fields will be loaded.
        Otherwise, fields should be given in the format of `@field`.
        """
        ...
    def group_by(self, fields, *reducers):
        """
        Specify by which fields to group the aggregation.

        ### Parameters

        - **fields**: Fields to group by. This can either be a single string,
            or a list of strings. both cases, the field should be specified as
            `@field`.
        - **reducers**: One or more reducers. Reducers may be found in the
            `aggregation` module.
        """
        ...
    def apply(self, **kwexpr):
        """
        Specify one or more projection expressions to add to each result

        ### Parameters

        - **kwexpr**: One or more key-value pairs for a projection. The key is
            the alias for the projection, and the value is the projection
            expression itself, for example `apply(square_root="sqrt(@foo)")`
        """
        ...
    def limit(self, offset, num):
        """
        Sets the limit for the most recent group or query.

        If no group has been defined yet (via `group_by()`) then this sets
        the limit for the initial pool of results from the query. Otherwise,
        this limits the number of items operated on from the previous group.

        Setting a limit on the initial search results may be useful when
        attempting to execute an aggregation on a sample of a large data set.

        ### Parameters

        - **offset**: Result offset from which to begin paging
        - **num**: Number of results to return


        Example of sorting the initial results:

        ```
        AggregateRequest("@sale_amount:[10000, inf]")            .limit(0, 10)            .group_by("@state", r.count())
        ```

        Will only group by the states found in the first 10 results of the
        query `@sale_amount:[10000, inf]`. On the other hand,

        ```
        AggregateRequest("@sale_amount:[10000, inf]")            .limit(0, 1000)            .group_by("@state", r.count()            .limit(0, 10)
        ```

        Will group all the results matching the query, but only return the
        first 10 groups.

        If you only wish to return a *top-N* style query, consider using
        `sort_by()` instead.
        """
        ...
    def sort_by(self, *fields, **kwargs):
        """
        Indicate how the results should be sorted. This can also be used for
        *top-N* style queries

        ### Parameters

        - **fields**: The fields by which to sort. This can be either a single
            field or a list of fields. If you wish to specify order, you can
            use the `Asc` or `Desc` wrapper classes.
        - **max**: Maximum number of results to return. This can be
            used instead of `LIMIT` and is also faster.


        Example of sorting by `foo` ascending and `bar` descending:

        ```
        sort_by(Asc("@foo"), Desc("@bar"))
        ```

        Return the top 10 customers:

        ```
        AggregateRequest()            .group_by("@customer", r.sum("@paid").alias(FIELDNAME))            .sort_by(Desc("@paid"), max=10)
        ```
        """
        ...
    def filter(self, expressions):
        """
        Specify filter for post-query results using predicates relating to
        values in the result set.

        ### Parameters

        - **fields**: Fields to group by. This can either be a single string,
            or a list of strings.
        """
        ...
    def with_schema(self):
        """
        If set, the `schema` property will contain a list of `[field, type]`
        entries in the result object.
        """
        ...
    def verbatim(self): ...
    def cursor(self, count: int = 0, max_idle: float = 0.0): ...
    def build_args(self): ...

class Cursor:
    cid: Any
    max_idle: int
    count: int
    def __init__(self, cid) -> None: ...
    def build_args(self): ...

class AggregateResult:
    rows: Any
    cursor: Any
    schema: Any
    def __init__(self, rows, cursor, schema) -> None: ...
