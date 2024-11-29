"""
Implementation of the JSON adaptation objects

This module exists to avoid a circular import problem: pyscopg2.extras depends
on psycopg2.extension, so I can't create the default JSON typecasters in
extensions importing register_json from extras.
"""

from collections.abc import Callable
from typing import Any
from typing_extensions import Self

from psycopg2._psycopg import _type, connection, cursor

JSON_OID: int
JSONARRAY_OID: int
JSONB_OID: int
JSONBARRAY_OID: int

class Json:
    """
    An `~psycopg2.extensions.ISQLQuote` wrapper to adapt a Python object to
    :sql:`json` data type.

    `!Json` can be used to wrap any object supported by the provided *dumps*
    function. If none is provided, the standard :py:func:`json.dumps()` is
    used.
    """
    adapted: Any
    def __init__(self, adapted: Any, dumps: Callable[..., str] | None = None) -> None: ...
    def __conform__(self, proto) -> Self | None: ...
    def dumps(self, obj: Any) -> str:
        """
        Serialize *obj* in JSON format.

        The default is to call `!json.dumps()` or the *dumps* function
        provided in the constructor. You can override this method to create a
        customized JSON wrapper.
        """
        ...
    def prepare(self, conn: connection | None) -> None: ...
    def getquoted(self) -> bytes: ...

def register_json(
    conn_or_curs: connection | cursor | None = None,
    globally: bool = False,
    loads: Callable[..., Any] | None = None,
    oid: int | None = None,
    array_oid: int | None = None,
    name: str = "json",
) -> tuple[_type, _type | None]:
    """
    Create and register typecasters converting :sql:`json` type to Python objects.

    :param conn_or_curs: a connection or cursor used to find the :sql:`json`
        and :sql:`json[]` oids; the typecasters are registered in a scope
        limited to this object, unless *globally* is set to `!True`. It can be
        `!None` if the oids are provided
    :param globally: if `!False` register the typecasters only on
        *conn_or_curs*, otherwise register them globally
    :param loads: the function used to parse the data into a Python object. If
        `!None` use `!json.loads()`, where `!json` is the module chosen
        according to the Python version (see above)
    :param oid: the OID of the :sql:`json` type if known; If not, it will be
        queried on *conn_or_curs*
    :param array_oid: the OID of the :sql:`json[]` array type if known;
        if not, it will be queried on *conn_or_curs*
    :param name: the name of the data type to look for in *conn_or_curs*

    The connection or cursor passed to the function will be used to query the
    database and look for the OID of the :sql:`json` type (or an alternative
    type if *name* if provided). No query is performed if *oid* and *array_oid*
    are provided.  Raise `~psycopg2.ProgrammingError` if the type is not found.
    """
    ...
def register_default_json(
    conn_or_curs: connection | cursor | None = None, globally: bool = False, loads: Callable[..., Any] | None = None
) -> tuple[_type, _type | None]:
    """
    Create and register :sql:`json` typecasters for PostgreSQL 9.2 and following.

    Since PostgreSQL 9.2 :sql:`json` is a builtin type, hence its oid is known
    and fixed. This function allows specifying a customized *loads* function
    for the default :sql:`json` type without querying the database.
    All the parameters have the same meaning of `register_json()`.
    """
    ...
def register_default_jsonb(
    conn_or_curs: connection | cursor | None = None, globally: bool = False, loads: Callable[..., Any] | None = None
) -> tuple[_type, _type | None]:
    """
    Create and register :sql:`jsonb` typecasters for PostgreSQL 9.4 and following.

    As in `register_default_json()`, the function allows to register a
    customized *loads* function for the :sql:`jsonb` type at its known oid for
    PostgreSQL 9.4 and following versions.  All the parameters have the same
    meaning of `register_json()`.
    """
    ...
