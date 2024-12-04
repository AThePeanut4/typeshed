"""SQL composition utility module"""

from collections.abc import Iterable, Iterator
from typing import Any, Generic, TypeVar

from psycopg2._psycopg import connection, cursor

_T = TypeVar("_T")

class Composable:
    """
    Abstract base class for objects that can be used to compose an SQL string.

    `!Composable` objects can be passed directly to `~cursor.execute()`,
    `~cursor.executemany()`, `~cursor.copy_expert()` in place of the query
    string.

    `!Composable` objects can be joined using the ``+`` operator: the result
    will be a `Composed` instance containing the objects joined. The operator
    ``*`` is also supported with an integer argument: the result is a
    `!Composed` instance containing the left argument repeated as many times as
    requested.
    """
    def __init__(self, wrapped: Any) -> None: ...
    def as_string(self, context: connection | cursor) -> str:
        """
        Return the string value of the object.

        :param context: the context to evaluate the string into.
        :type context: `connection` or `cursor`

        The method is automatically invoked by `~cursor.execute()`,
        `~cursor.executemany()`, `~cursor.copy_expert()` if a `!Composable` is
        passed instead of the query string.
        """
        ...
    def __add__(self, other: Composable) -> Composed: ...
    def __mul__(self, n: int) -> Composed: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Composed(Composable):
    """
    A `Composable` object made of a sequence of `!Composable`.

    The object is usually created using `!Composable` operators and methods.
    However it is possible to create a `!Composed` directly specifying a
    sequence of `!Composable` as arguments.

    Example::

        >>> comp = sql.Composed(
        ...     [sql.SQL("insert into "), sql.Identifier("table")])
        >>> print(comp.as_string(conn))
        insert into "table"

    `!Composed` objects are iterable (so they can be used in `SQL.join` for
    instance).
    """
    def __init__(self, seq: Iterable[Composable]) -> None: ...
    @property
    def seq(self) -> list[Composable]:
        """The list of the content of the `!Composed`."""
        ...
    def __iter__(self) -> Iterator[Composable]: ...
    def __add__(self, other: Composable) -> Composed: ...
    def join(self, joiner: str | SQL) -> Composed:
        """
        Return a new `!Composed` interposing the *joiner* with the `!Composed` items.

        The *joiner* must be a `SQL` or a string which will be interpreted as
        an `SQL`.

        Example::

            >>> fields = sql.Identifier('foo') + sql.Identifier('bar')  # a Composed
            >>> print(fields.join(', ').as_string(conn))
            "foo", "bar"
        """
        ...

class SQL(Composable):
    """
    A `Composable` representing a snippet of SQL statement.

    `!SQL` exposes `join()` and `format()` methods useful to create a template
    where to merge variable parts of a query (for instance field or table
    names).

    The *string* doesn't undergo any form of escaping, so it is not suitable to
    represent variable identifiers or values: you should only use it to pass
    constant strings representing templates or snippets of SQL statements; use
    other objects such as `Identifier` or `Literal` to represent variable
    parts.

    Example::

        >>> query = sql.SQL("select {0} from {1}").format(
        ...    sql.SQL(', ').join([sql.Identifier('foo'), sql.Identifier('bar')]),
        ...    sql.Identifier('table'))
        >>> print(query.as_string(conn))
        select "foo", "bar" from "table"
    """
    def __init__(self, string: str) -> None: ...
    @property
    def string(self) -> str:
        """The string wrapped by the `!SQL` object."""
        ...
    def format(self, *args: Composable, **kwargs: Composable) -> Composed:
        """
        Merge `Composable` objects into a template.

        :param `Composable` args: parameters to replace to numbered
            (``{0}``, ``{1}``) or auto-numbered (``{}``) placeholders
        :param `Composable` kwargs: parameters to replace to named (``{name}``)
            placeholders
        :return: the union of the `!SQL` string with placeholders replaced
        :rtype: `Composed`

        The method is similar to the Python `str.format()` method: the string
        template supports auto-numbered (``{}``), numbered (``{0}``,
        ``{1}``...), and named placeholders (``{name}``), with positional
        arguments replacing the numbered placeholders and keywords replacing
        the named ones. However placeholder modifiers (``{0!r}``, ``{0:<10}``)
        are not supported. Only `!Composable` objects can be passed to the
        template.

        Example::

            >>> print(sql.SQL("select * from {} where {} = %s")
            ...     .format(sql.Identifier('people'), sql.Identifier('id'))
            ...     .as_string(conn))
            select * from "people" where "id" = %s

            >>> print(sql.SQL("select * from {tbl} where {pkey} = %s")
            ...     .format(tbl=sql.Identifier('people'), pkey=sql.Identifier('id'))
            ...     .as_string(conn))
            select * from "people" where "id" = %s
        """
        ...
    def join(self, seq: Iterable[Composable]) -> Composed:
        """
        Join a sequence of `Composable`.

        :param seq: the elements to join.
        :type seq: iterable of `!Composable`

        Use the `!SQL` object's *string* to separate the elements in *seq*.
        Note that `Composed` objects are iterable too, so they can be used as
        argument for this method.

        Example::

            >>> snip = sql.SQL(', ').join(
            ...     sql.Identifier(n) for n in ['foo', 'bar', 'baz'])
            >>> print(snip.as_string(conn))
            "foo", "bar", "baz"
        """
        ...

class Identifier(Composable):
    """
    A `Composable` representing an SQL identifier or a dot-separated sequence.

    Identifiers usually represent names of database objects, such as tables or
    fields. PostgreSQL identifiers follow `different rules`__ than SQL string
    literals for escaping (e.g. they use double quotes instead of single).

    .. __: https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#         SQL-SYNTAX-IDENTIFIERS

    Example::

        >>> t1 = sql.Identifier("foo")
        >>> t2 = sql.Identifier("ba'r")
        >>> t3 = sql.Identifier('ba"z')
        >>> print(sql.SQL(', ').join([t1, t2, t3]).as_string(conn))
        "foo", "ba'r", "ba""z"

    Multiple strings can be passed to the object to represent a qualified name,
    i.e. a dot-separated sequence of identifiers.

    Example::

        >>> query = sql.SQL("select {} from {}").format(
        ...     sql.Identifier("table", "field"),
        ...     sql.Identifier("schema", "table"))
        >>> print(query.as_string(conn))
        select "table"."field" from "schema"."table"
    """
    def __init__(self, *strings: str) -> None: ...
    @property
    def strings(self) -> tuple[str, ...]:
        """A tuple with the strings wrapped by the `Identifier`."""
        ...
    @property
    def string(self) -> str:
        """
        The string wrapped by the `Identifier`.
        
        """
        ...

class Literal(Composable, Generic[_T]):
    """
    A `Composable` representing an SQL value to include in a query.

    Usually you will want to include placeholders in the query and pass values
    as `~cursor.execute()` arguments. If however you really really need to
    include a literal value in the query you can use this object.

    The string returned by `!as_string()` follows the normal :ref:`adaptation
    rules <python-types-adaptation>` for Python objects.

    Example::

        >>> s1 = sql.Literal("foo")
        >>> s2 = sql.Literal("ba'r")
        >>> s3 = sql.Literal(42)
        >>> print(sql.SQL(', ').join([s1, s2, s3]).as_string(conn))
        'foo', 'ba''r', 42
    """
    def __init__(self, wrapped: _T) -> None: ...
    @property
    def wrapped(self) -> _T:
        """The object wrapped by the `!Literal`."""
        ...

class Placeholder(Composable):
    """
    A `Composable` representing a placeholder for query parameters.

    If the name is specified, generate a named placeholder (e.g. ``%(name)s``),
    otherwise generate a positional placeholder (e.g. ``%s``).

    The object is useful to generate SQL queries with a variable number of
    arguments.

    Examples::

        >>> names = ['foo', 'bar', 'baz']

        >>> q1 = sql.SQL("insert into table ({}) values ({})").format(
        ...     sql.SQL(', ').join(map(sql.Identifier, names)),
        ...     sql.SQL(', ').join(sql.Placeholder() * len(names)))
        >>> print(q1.as_string(conn))
        insert into table ("foo", "bar", "baz") values (%s, %s, %s)

        >>> q2 = sql.SQL("insert into table ({}) values ({})").format(
        ...     sql.SQL(', ').join(map(sql.Identifier, names)),
        ...     sql.SQL(', ').join(map(sql.Placeholder, names)))
        >>> print(q2.as_string(conn))
        insert into table ("foo", "bar", "baz") values (%(foo)s, %(bar)s, %(baz)s)
    """
    def __init__(self, name: str | None = None) -> None: ...
    @property
    def name(self) -> str | None:
        """The name of the `!Placeholder`."""
        ...

NULL: SQL
DEFAULT: SQL
