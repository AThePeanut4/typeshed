"""
Defused xmlrpclib

Also defuses gzip bomb
"""

from _typeshed import Incomplete
from xmlrpc.client import ExpatParser

__origin__: str
MAX_DATA: int = 31457280

def defused_gzip_decode(data, limit: int | None = None):
    """
    gzip encoded data -> unencoded data

    Decode data using the gzip content encoding as described in RFC 1952
    """
    ...

# Couldn't type this as a class deriving from gzip.GzipFile
# since overwriting `read` method does not define an optional argument
# for size when the underlying class does.
DefusedGzipDecodedResponse = Incomplete

class DefusedExpatParser(ExpatParser):
    forbid_dtd: bool
    forbid_entities: bool
    forbid_external: bool
    def __init__(self, target, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True) -> None: ...
    def defused_start_doctype_decl(self, name, sysid, pubid, has_internal_subset) -> None: ...
    def defused_entity_decl(self, name, is_parameter_entity, value, base, sysid, pubid, notation_name) -> None: ...
    def defused_unparsed_entity_decl(self, name, base, sysid, pubid, notation_name) -> None: ...
    def defused_external_entity_ref_handler(self, context, base, sysid, pubid) -> None: ...

def monkey_patch() -> None: ...
def unmonkey_patch() -> None: ...
