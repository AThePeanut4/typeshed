"""
SAX driver for the pyexpat C module.  This driver works with
pyexpat.__version__ == '2.22'.
"""

import sys
from _typeshed import Unused
from xml.sax import xmlreader

version: str
AttributesImpl = xmlreader.AttributesImpl
AttributesNSImpl = xmlreader.AttributesNSImpl

class _ClosedParser: ...

class ExpatLocator(xmlreader.Locator):
    """
    Locator for use with the ExpatParser class.

    This uses a weak reference to the parser object to avoid creating
    a circular reference between the parser and the content handler.
    """
    def __init__(self, parser: ExpatParser) -> None: ...
    def getColumnNumber(self) -> int: ...
    def getLineNumber(self) -> int: ...
    def getPublicId(self): ...
    def getSystemId(self): ...

class ExpatParser(xmlreader.IncrementalParser, xmlreader.Locator):
    """SAX driver for the pyexpat C module."""
    def __init__(self, namespaceHandling: int = 0, bufsize: int = 65516) -> None: ...
    def parse(self, source) -> None:
        """Parse an XML document from a URL or an InputSource."""
        ...
    def prepareParser(self, source) -> None: ...
    def setContentHandler(self, handler) -> None: ...
    def getFeature(self, name: str): ...
    def setFeature(self, name: str, state) -> None: ...
    def getProperty(self, name: str): ...
    def setProperty(self, name: str, value) -> None: ...
    if sys.version_info >= (3, 9):
        def feed(self, data, isFinal: bool = False) -> None: ...
    else:
        def feed(self, data, isFinal: int = 0) -> None: ...

    def flush(self) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...
    def getColumnNumber(self) -> int | None: ...
    def getLineNumber(self) -> int: ...
    def getPublicId(self): ...
    def getSystemId(self): ...
    def start_element(self, name: str, attrs: xmlreader.AttributesImpl) -> None: ...
    def end_element(self, name: str) -> None: ...
    def start_element_ns(self, name: str, attrs) -> None: ...
    def end_element_ns(self, name: str) -> None: ...
    def processing_instruction(self, target: str, data: str) -> None: ...
    def character_data(self, data: str) -> None: ...
    def start_namespace_decl(self, prefix: str | None, uri: str) -> None: ...
    def end_namespace_decl(self, prefix: str | None) -> None: ...
    def start_doctype_decl(self, name: str, sysid: str | None, pubid: str | None, has_internal_subset: Unused) -> None: ...
    def unparsed_entity_decl(self, name, base, sysid, pubid, notation_name) -> None: ...
    def notation_decl(self, name, base, sysid, pubid) -> None: ...
    def external_entity_ref(self, context, base, sysid, pubid): ...
    def skipped_entity_handler(self, name: str, is_pe: bool) -> None: ...

def create_parser(namespaceHandling: int = 0, bufsize: int = 65516) -> ExpatParser: ...