""""""

from _typeshed import Incomplete

class AttrDef:
    """
    Hold the definition of an attribute

    :param name: the real attribute name
    :type name: string
    :param key: the friendly name to use in queries and when accessing the attribute, default to the real attribute name
    :type key: string
    :param validate: called to check if the value in the query is valid, the callable is called with the value parameter
    :type validate: callable
    :param pre_query: called to transform values returned by search
    :type pre_query: callable
    :param post_query: called to transform values returned by search
    :type post_query: callable
    :param default: value returned when the attribute is absent (defaults to NotImplemented to allow use of None as default)
    :type default: string, integer
    :param dereference_dn: reference to an ObjectDef instance. When the attribute value contains a dn it will be searched and substituted in the entry
    :type dereference_dn: ObjectDef
    :param description: custom attribute description
    :type description: string
    :param mandatory: specify if attribute is defined as mandatory in LDAP schema
    :type mandatory: boolean
    """
    name: Incomplete
    key: Incomplete
    validate: Incomplete
    pre_query: Incomplete
    post_query: Incomplete
    default: Incomplete
    dereference_dn: Incomplete
    description: Incomplete
    mandatory: Incomplete
    single_value: Incomplete
    oid_info: Incomplete
    other_names: Incomplete
    def __init__(
        self,
        name,
        key=None,
        validate=None,
        pre_query=None,
        post_query=None,
        default=...,
        dereference_dn=None,
        description=None,
        mandatory: bool = False,
        single_value=None,
        alias=None,
    ) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self) -> int: ...
    def __setattr__(self, key: str, value) -> None: ...
