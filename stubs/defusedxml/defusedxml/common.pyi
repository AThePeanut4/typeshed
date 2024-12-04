"""Common constants, exceptions and helpe functions"""

from _typeshed import Incomplete

PY3: bool

class DefusedXmlException(ValueError):
    """Base exception"""
    ...

class DTDForbidden(DefusedXmlException):
    """Document type definition is forbidden"""
    name: Incomplete
    sysid: Incomplete
    pubid: Incomplete
    def __init__(self, name, sysid, pubid) -> None: ...

class EntitiesForbidden(DefusedXmlException):
    """Entity definition is forbidden"""
    name: Incomplete
    value: Incomplete
    base: Incomplete
    sysid: Incomplete
    pubid: Incomplete
    notation_name: Incomplete
    def __init__(self, name, value, base, sysid, pubid, notation_name) -> None: ...

class ExternalReferenceForbidden(DefusedXmlException):
    """Resolving an external reference is forbidden"""
    context: Incomplete
    base: Incomplete
    sysid: Incomplete
    pubid: Incomplete
    def __init__(self, context, base, sysid, pubid) -> None: ...

class NotSupportedError(DefusedXmlException):
    """The operation is not supported"""
    ...
