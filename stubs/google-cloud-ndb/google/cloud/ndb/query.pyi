"""
High-level wrapper for datastore queries.

The fundamental API here overloads the 6 comparison operators to represent
filters on property values, and supports AND and OR operations (implemented as
functions -- Python's 'and' and 'or' operators cannot be overloaded, and the
'&' and '|' operators have a priority that conflicts with the priority of
comparison operators).

For example::

    class Employee(Model):
        name = StringProperty()
        age = IntegerProperty()
        rank = IntegerProperty()

      @classmethod
      def demographic(cls, min_age, max_age):
          return cls.query().filter(AND(cls.age >= min_age,
                                        cls.age <= max_age))

      @classmethod
      def ranked(cls, rank):
          return cls.query(cls.rank == rank).order(cls.age)

    for emp in Employee.seniors(42, 5):
        print(emp.name, emp.age, emp.rank)

The 'in' operator cannot be overloaded, but is supported through the IN()
method. For example::

    Employee.query().filter(Employee.rank.IN([4, 5, 6]))

Sort orders are supported through the order() method; unary minus is
overloaded on the Property class to represent a descending order::

    Employee.query().order(Employee.name, -Employee.age)

Besides using AND() and OR(), filters can also be combined by repeatedly
calling .filter()::

    query1 = Employee.query()  # A query that returns all employees
    query2 = query1.filter(Employee.age >= 30)  # Only those over 30
    query3 = query2.filter(Employee.age < 40)  # Only those in their 30s

A further shortcut is calling .filter() with multiple arguments; this implies
AND()::

  query1 = Employee.query()  # A query that returns all employees
  query3 = query1.filter(Employee.age >= 30,
                         Employee.age < 40)  # Only those in their 30s

And finally you can also pass one or more filter expressions directly to the
.query() method::

  query3 = Employee.query(Employee.age >= 30,
                          Employee.age < 40)  # Only those in their 30s

Query objects are immutable, so these methods always return a new Query object;
the above calls to filter() do not affect query1. On the other hand, operations
that are effectively no-ops may return the original Query object.

Sort orders can also be combined this way, and .filter() and .order() calls may
be intermixed::

    query4 = query3.order(-Employee.age)
    query5 = query4.order(Employee.name)
    query6 = query5.filter(Employee.rank == 5)

Again, multiple .order() calls can be combined::

    query5 = query3.order(-Employee.age, Employee.name)

The simplest way to retrieve Query results is a for-loop::

    for emp in query3:
        print emp.name, emp.age

Some other methods to run a query and access its results::

    :meth:`Query.iter`() # Return an iterator; same as iter(q) but more
        flexible.
    :meth:`Query.fetch`(N) # Return a list of the first N results
    :meth:`Query.get`() # Return the first result
    :meth:`Query.count`(N) # Return the number of results, with a maximum of N
    :meth:`Query.fetch_page`(N, start_cursor=cursor) # Return (results, cursor,
        has_more)

All of the above methods take a standard set of additional query options,
in the form of keyword arguments such as keys_only=True. You can also pass
a QueryOptions object options=QueryOptions(...), but this is deprecated.

The most important query options are:

- keys_only: bool, if set the results are keys instead of entities.
- limit: int, limits the number of results returned.
- offset: int, skips this many results first.
- start_cursor: Cursor, start returning results after this position.
- end_cursor: Cursor, stop returning results after this position.

The following query options have been deprecated or are not supported in
datastore queries:

- batch_size: int, hint for the number of results returned per RPC.
- prefetch_size: int, hint for the number of results in the first RPC.
- produce_cursors: bool, return Cursor objects with the results.

All of the above methods except for iter() have asynchronous variants as well,
which return a Future; to get the operation's ultimate result, yield the Future
(when inside a tasklet) or call the Future's get_result() method (outside a
tasklet)::

    :meth:`Query.fetch_async`(N)
    :meth:`Query.get_async`()
    :meth:`Query.count_async`(N)
    :meth:`Query.fetch_page_async`(N, start_cursor=cursor)

Finally, there's an idiom to efficiently loop over the Query results in a
tasklet, properly yielding when appropriate::

    it = query1.iter()
    while (yield it.has_next_async()):
        emp = it.next()
        print(emp.name, emp.age)
"""

from _typeshed import Incomplete

from google.cloud.ndb import _options

class PropertyOrder:
    name: Incomplete
    reverse: Incomplete
    def __init__(self, name, reverse: bool = ...) -> None: ...
    def __neg__(self): ...

class RepeatedStructuredPropertyPredicate:
    name: Incomplete
    match_keys: Incomplete
    match_values: Incomplete
    def __init__(self, name, match_keys, entity_pb) -> None: ...
    def __call__(self, entity_pb): ...

class ParameterizedThing:
    """
    Base class for :class:`Parameter` and :class:`ParameterizedFunction`.

    This exists purely for :func:`isinstance` checks.
    """
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Parameter(ParameterizedThing):
    """
    Represents a bound variable in a GQL query.

    ``Parameter(1)`` corresponds to a slot labeled ``:1`` in a GQL query.
    ``Parameter('something')`` corresponds to a slot labeled ``:something``.

    The value must be set (bound) separately.

    Args:
        key (Union[str, int]): The parameter key.

    Raises:
        TypeError: If the ``key`` is not a string or integer.
    """
    def __init__(self, key) -> None: ...
    def __eq__(self, other): ...
    @property
    def key(self):
        """Retrieve the key."""
        ...
    def resolve(self, bindings, used):
        """
        Resolve the current parameter from the parameter bindings.

        Args:
            bindings (dict): A mapping of parameter bindings.
            used (Dict[Union[str, int], bool]): A mapping of already used
                parameters. This will be modified if the current parameter
                is in ``bindings``.

        Returns:
            Any: The bound value for the current parameter.

        Raises:
            exceptions.BadArgumentError: If the current parameter is not in ``bindings``.
        """
        ...

class ParameterizedFunction(ParameterizedThing):
    func: Incomplete
    values: Incomplete
    def __init__(self, func, values) -> None: ...
    def __eq__(self, other): ...
    def is_parameterized(self): ...
    def resolve(self, bindings, used): ...

class Node:
    """
    Base class for filter expression tree nodes.

    Tree nodes are considered immutable, even though they can contain
    Parameter instances, which are not. In particular, two identical
    trees may be represented by the same Node object in different
    contexts.

    Raises:
        TypeError: Always, only subclasses are allowed.
    """
    def __new__(cls): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __le__(self, unused_other): ...
    def __lt__(self, unused_other): ...
    def __ge__(self, unused_other): ...
    def __gt__(self, unused_other): ...
    def resolve(self, bindings, used):
        """
        Return a node with parameters replaced by the selected values.

        .. note::

            Both ``bindings`` and ``used`` are unused by this base class
            implementation.

        Args:
            bindings (dict): A mapping of parameter bindings.
            used (Dict[Union[str, int], bool]): A mapping of already used
                parameters. This will be modified if the current parameter
                is in ``bindings``.

        Returns:
            Node: The current node.
        """
        ...

class FalseNode(Node):
    """Tree node for an always-failing filter."""
    def __eq__(self, other):
        """
        Equality check.

        An instance will always equal another :class:`FalseNode` instance. This
        is because they hold no state.
        """
        ...

class ParameterNode(Node):
    """
    Tree node for a parameterized filter.

    Args:
        prop (~google.cloud.ndb.model.Property): A property describing a value
            type.
        op (str): The comparison operator. One of ``=``, ``!=``, ``<``, ``<=``,
            ``>``, ``>=`` or ``in``.
        param (ParameterizedThing): The parameter corresponding to the node.

    Raises:
        TypeError: If ``prop`` is not a
            :class:`~google.cloud.ndb.model.Property`.
        TypeError: If ``op`` is not one of the accepted operators.
        TypeError: If ``param`` is not a :class:`.Parameter` or
            :class:`.ParameterizedFunction`.
    """
    def __new__(cls, prop, op, param): ...
    def __getnewargs__(self):
        """
        Private API used to specify ``__new__`` arguments when unpickling.

        .. note::

            This method only applies if the ``pickle`` protocol is 2 or
            greater.

        Returns:
            Tuple[~google.cloud.ndb.model.Property, str, ParameterizedThing]:
            A tuple containing the internal state: the property, operation and
            parameter.
        """
        ...
    def __eq__(self, other): ...
    def resolve(self, bindings, used):
        """
        Return a node with parameters replaced by the selected values.

        Args:
            bindings (dict): A mapping of parameter bindings.
            used (Dict[Union[str, int], bool]): A mapping of already used
                parameters.

        Returns:
            Union[~google.cloud.ndb.query.DisjunctionNode,                 ~google.cloud.ndb.query.FilterNode,                 ~google.cloud.ndb.query.FalseNode]: A node corresponding to
            the value substituted.
        """
        ...

class FilterNode(Node):
    """
    Tree node for a single filter expression.

    For example ``FilterNode("a", ">", 3)`` filters for entities where the
    value ``a`` is greater than ``3``.

    .. warning::

        The constructor for this type may not always return a
        :class:`FilterNode`. For example:

        * The filter ``name in (value1, ..., valueN)`` is converted into
          ``(name = value1) OR ... OR (name = valueN)`` (also a
          :class:`DisjunctionNode`)
        * The filter ``name in ()`` (i.e. a property is among an empty list
          of values) is converted into a :class:`FalseNode`
        * The filter ``name in (value1,)`` (i.e. a list with one element) is
          converted into ``name = value1``, a related :class:`FilterNode`
          with a different ``opsymbol`` and ``value`` than what was passed
          to the constructor

    Args:
        name (str): The name of the property being filtered.
        opsymbol (str): The comparison operator. One of ``=``, ``!=``, ``<``,
            ``<=``, ``>``, ``>=`` or ``in``.
        value (Any): The value to filter on / relative to.
        server_op (bool): Force the operator to use a server side filter.

    Raises:
        TypeError: If ``opsymbol`` is ``"in"`` but ``value`` is not a
            basic container (:class:`list`, :class:`tuple`, :class:`set` or
            :class:`frozenset`)
    """
    def __new__(cls, name, opsymbol, value, server_op: bool = False): ...
    def __getnewargs__(self):
        """
        Private API used to specify ``__new__`` arguments when unpickling.

        .. note::

            This method only applies if the ``pickle`` protocol is 2 or
            greater.

        Returns:
            Tuple[str, str, Any]: A tuple containing the
            internal state: the name, ``opsymbol`` and value.
        """
        ...
    def __eq__(self, other): ...

class PostFilterNode(Node):
    """
    Tree node representing an in-memory filtering operation.

    This is used to represent filters that cannot be executed by the
    datastore, for example a query for a structured value.

    Args:
        predicate (Callable[[Any], bool]): A filter predicate that
            takes a datastore entity (typically as a protobuf) and
            returns :data:`True` or :data:`False` if the entity matches
            the given filter.
    """
    def __new__(cls, predicate): ...
    def __getnewargs__(self):
        """
        Private API used to specify ``__new__`` arguments when unpickling.

        .. note::

            This method only applies if the ``pickle`` protocol is 2 or
            greater.

        Returns:
            Tuple[Callable[[Any], bool],]: A tuple containing a single value,
            the ``predicate`` attached to this node.
        """
        ...
    def __eq__(self, other): ...

class _BooleanClauses:
    name: Incomplete
    combine_or: Incomplete
    or_parts: Incomplete
    def __init__(self, name, combine_or) -> None: ...
    def add_node(self, node) -> None:
        """
        Update the current boolean expression.

        This uses the distributive law for sets to combine as follows:

        - ``(A or B or C or ...) or  D`` -> ``A or B or C or ... or D``
        - ``(A or B or C or ...) and D`` ->
          ``(A and D) or (B and D) or (C and D) or ...``

        Args:
            node (Node): A node to add to the list of clauses.

        Raises:
            TypeError: If ``node`` is not a :class:`.Node`.
        """
        ...

class ConjunctionNode(Node):
    """
    Tree node representing a boolean ``AND`` operator on multiple nodes.

    .. warning::

        The constructor for this type may not always return a
        :class:`ConjunctionNode`. For example:

        * If the passed in ``nodes`` has only one entry, that single node
          will be returned by the constructor
        * If the resulting boolean expression has an ``OR`` in it, then a
          :class:`DisjunctionNode` will be returned; e.g.
          ``AND(OR(A, B), C)`` becomes ``OR(AND(A, C), AND(B, C))``

    Args:
        nodes (Tuple[Node, ...]): A list of nodes to be joined.

    Raises:
        TypeError: If ``nodes`` is empty.
        RuntimeError: If the ``nodes`` combine to an "empty" boolean
            expression.
    """
    def __new__(cls, *nodes): ...
    def __getnewargs__(self):
        """
        Private API used to specify ``__new__`` arguments when unpickling.

        .. note::

            This method only applies if the ``pickle`` protocol is 2 or
            greater.

        Returns:
            Tuple[Node, ...]: The list of stored nodes, converted to a
            :class:`tuple`.
        """
        ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def resolve(self, bindings, used):
        """
        Return a node with parameters replaced by the selected values.

        Args:
            bindings (dict): A mapping of parameter bindings.
            used (Dict[Union[str, int], bool]): A mapping of already used
                parameters. This will be modified for each parameter found
                in ``bindings``.

        Returns:
            Node: The current node, if all nodes are already resolved.
            Otherwise returns a modified :class:`ConjunctionNode` with
            each individual node resolved.
        """
        ...

class DisjunctionNode(Node):
    """
    Tree node representing a boolean ``OR`` operator on multiple nodes.

    .. warning::

        This constructor may not always return a :class:`DisjunctionNode`.
        If the passed in ``nodes`` has only one entry, that single node
        will be returned by the constructor.

    Args:
        nodes (Tuple[Node, ...]): A list of nodes to be joined.

    Raises:
        TypeError: If ``nodes`` is empty.
    """
    def __new__(cls, *nodes): ...
    def __getnewargs__(self):
        """
        Private API used to specify ``__new__`` arguments when unpickling.

        .. note::

            This method only applies if the ``pickle`` protocol is 2 or
            greater.

        Returns:
            Tuple[Node, ...]: The list of stored nodes, converted to a
            :class:`tuple`.
        """
        ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def resolve(self, bindings, used):
        """
        Return a node with parameters replaced by the selected values.

        Args:
            bindings (dict): A mapping of parameter bindings.
            used (Dict[Union[str, int], bool]): A mapping of already used
                parameters. This will be modified for each parameter found
                in ``bindings``.

        Returns:
            Node: The current node, if all nodes are already resolved.
            Otherwise returns a modified :class:`DisjunctionNode` with
            each individual node resolved.
        """
        ...

AND = ConjunctionNode
OR = DisjunctionNode

class QueryOptions(_options.ReadOptions):
    project: Incomplete
    namespace: Incomplete
    database: str | None
    def __init__(self, config: Incomplete | None = ..., context: Incomplete | None = ..., **kwargs) -> None: ...

class Query:
    default_options: Incomplete
    kind: Incomplete
    ancestor: Incomplete
    filters: Incomplete
    order_by: Incomplete
    project: Incomplete
    namespace: Incomplete
    limit: Incomplete
    offset: Incomplete
    keys_only: Incomplete
    projection: Incomplete
    distinct_on: Incomplete
    database: str | None
    def __init__(
        self,
        kind: Incomplete | None = ...,
        filters: Incomplete | None = ...,
        ancestor: Incomplete | None = ...,
        order_by: Incomplete | None = ...,
        orders: Incomplete | None = ...,
        project: Incomplete | None = ...,
        app: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
        projection: Incomplete | None = ...,
        distinct_on: Incomplete | None = ...,
        group_by: Incomplete | None = ...,
        limit: Incomplete | None = ...,
        offset: Incomplete | None = ...,
        keys_only: Incomplete | None = ...,
        default_options: Incomplete | None = ...,
    ) -> None: ...
    @property
    def is_distinct(self): ...
    def filter(self, *filters): ...
    def order(self, *props): ...
    def analyze(self): ...
    def bind(self, *positional, **keyword): ...
    def fetch(self, limit: Incomplete | None = ..., **kwargs): ...
    def fetch_async(self, limit: Incomplete | None = ..., **kwargs): ...
    def run_to_queue(self, queue, conn, options: Incomplete | None = ..., dsquery: Incomplete | None = ...) -> None: ...
    def iter(self, **kwargs): ...
    __iter__: Incomplete
    def map(self, callback, **kwargs): ...
    def map_async(self, callback, **kwargs) -> None: ...
    def get(self, **kwargs): ...
    def get_async(self, **kwargs) -> None: ...
    def count(self, limit: Incomplete | None = ..., **kwargs): ...
    def count_async(self, limit: Incomplete | None = ..., **kwargs): ...
    def fetch_page(self, page_size, **kwargs): ...
    def fetch_page_async(self, page_size, **kwargs) -> None: ...

def gql(query_string: str, *args, **kwds) -> Query: ...
