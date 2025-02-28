from _typeshed import ReadableBuffer, SupportsRead
from typing import Any, NoReturn
from typing_extensions import TypeAlias
from xml.dom.minidom import Document, DocumentFragment, DOMImplementation, Element, Node, TypeInfo
from xml.dom.xmlbuilder import DOMBuilderFilter, Options
from xml.parsers.expat import XMLParserType

_Model: TypeAlias = tuple[int, int, str | None, tuple[Any, ...]]  # same as in pyexpat

TEXT_NODE = Node.TEXT_NODE
CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
DOCUMENT_NODE = Node.DOCUMENT_NODE
FILTER_ACCEPT = DOMBuilderFilter.FILTER_ACCEPT
FILTER_REJECT = DOMBuilderFilter.FILTER_REJECT
FILTER_SKIP = DOMBuilderFilter.FILTER_SKIP
FILTER_INTERRUPT = DOMBuilderFilter.FILTER_INTERRUPT
theDOMImplementation: DOMImplementation

class ElementInfo:
    tagName: str
    def __init__(self, tagName: str, model: _Model | None = None) -> None: ...
    def getAttributeType(self, aname: str) -> TypeInfo: ...
    def getAttributeTypeNS(self, namespaceURI: str | None, localName: str) -> TypeInfo: ...
    def isElementContent(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isId(self, aname: str) -> bool: ...
    def isIdNS(self, euri: str, ename: str, auri: str, aname: str) -> bool: ...

class ExpatBuilder:
    """
    Document builder that uses Expat to build a ParsedXML.DOM document
    instance.
    """
    document: Document  # Created in self.reset()
    curNode: DocumentFragment | Element | Document  # Created in self.reset()
    def __init__(self, options: Options | None = None) -> None: ...
    def createParser(self) -> XMLParserType: ...
    def getParser(self) -> XMLParserType: ...
    def reset(self) -> None: ...
    def install(self, parser: XMLParserType) -> None: ...
    def parseFile(self, file: SupportsRead[ReadableBuffer | str]) -> Document: ...
    def parseString(self, string: str | ReadableBuffer) -> Document: ...
    def start_doctype_decl_handler(
        self, doctypeName: str, systemId: str | None, publicId: str | None, has_internal_subset: bool
    ) -> None: ...
    def end_doctype_decl_handler(self) -> None: ...
    def pi_handler(self, target: str, data: str) -> None: ...
    def character_data_handler_cdata(self, data: str) -> None: ...
    def character_data_handler(self, data: str) -> None: ...
    def start_cdata_section_handler(self) -> None: ...
    def end_cdata_section_handler(self) -> None: ...
    def entity_decl_handler(
        self,
        entityName: str,
        is_parameter_entity: bool,
        value: str | None,
        base: str | None,
        systemId: str,
        publicId: str | None,
        notationName: str | None,
    ) -> None: ...
    def notation_decl_handler(self, notationName: str, base: str | None, systemId: str, publicId: str | None) -> None: ...
    def comment_handler(self, data: str) -> None: ...
    def external_entity_ref_handler(self, context: str, base: str | None, systemId: str | None, publicId: str | None) -> int: ...
    def first_element_handler(self, name: str, attributes: list[str]) -> None: ...
    def start_element_handler(self, name: str, attributes: list[str]) -> None: ...
    def end_element_handler(self, name: str) -> None: ...
    def element_decl_handler(self, name: str, model: _Model) -> None: ...
    def attlist_decl_handler(self, elem: str, name: str, type: str, default: str | None, required: bool) -> None: ...
    def xml_decl_handler(self, version: str, encoding: str | None, standalone: int) -> None: ...

class FilterVisibilityController:
    """
    Wrapper around a DOMBuilderFilter which implements the checks
    to make the whatToShow filter attribute work.
    """
    filter: DOMBuilderFilter
    def __init__(self, filter: DOMBuilderFilter) -> None: ...
    def startContainer(self, node: Node) -> int: ...
    def acceptNode(self, node: Node) -> int: ...

class FilterCrutch:
    def __init__(self, builder: ExpatBuilder) -> None: ...

class Rejecter(FilterCrutch):
    def start_element_handler(self, *args: Any) -> None: ...
    def end_element_handler(self, *args: Any) -> None: ...

class Skipper(FilterCrutch):
    def start_element_handler(self, *args: Any) -> None: ...
    def end_element_handler(self, *args: Any) -> None: ...

class FragmentBuilder(ExpatBuilder):
    fragment: DocumentFragment | None
    originalDocument: Document
    context: Node
    def __init__(self, context: Node, options: Options | None = None) -> None: ...
    def reset(self) -> None: ...
    def parseFile(self, file: SupportsRead[ReadableBuffer | str]) -> DocumentFragment: ...  # type: ignore[override]
    def parseString(self, string: ReadableBuffer | str) -> DocumentFragment: ...  # type: ignore[override]
    def external_entity_ref_handler(self, context: str, base: str | None, systemId: str | None, publicId: str | None) -> int: ...

class Namespaces:
    def createParser(self) -> XMLParserType: ...
    def install(self, parser: XMLParserType) -> None: ...
    def start_namespace_decl_handler(self, prefix: str | None, uri: str) -> None: ...
    def start_element_handler(self, name: str, attributes: list[str]) -> None: ...
    def end_element_handler(self, name: str) -> None: ...  # only exists if __debug__

class ExpatBuilderNS(Namespaces, ExpatBuilder):
    """Document builder that supports namespaces."""
    ...
class FragmentBuilderNS(Namespaces, FragmentBuilder):
    """Fragment builder that supports namespaces."""
    ...
class ParseEscape(Exception):
    """Exception raised to short-circuit parsing in InternalSubsetExtractor."""
    ...

class InternalSubsetExtractor(ExpatBuilder):
    subset: str | list[str] | None = None
    def getSubset(self) -> str: ...
    def parseFile(self, file: SupportsRead[ReadableBuffer | str]) -> None: ...  # type: ignore[override]
    def parseString(self, string: str | ReadableBuffer) -> None: ...  # type: ignore[override]
    def start_doctype_decl_handler(  # type: ignore[override]
        self, name: str, publicId: str | None, systemId: str | None, has_internal_subset: bool
    ) -> None: ...
    def end_doctype_decl_handler(self) -> NoReturn: ...
    def start_element_handler(self, name: str, attrs: list[str]) -> NoReturn: ...

def parse(file: str | SupportsRead[ReadableBuffer | str], namespaces: bool = True) -> Document: ...
def parseString(string: str | ReadableBuffer, namespaces: bool = True) -> Document: ...
def parseFragment(file: str | SupportsRead[ReadableBuffer | str], context: Node, namespaces: bool = True) -> DocumentFragment: ...
def parseFragmentString(string: str | ReadableBuffer, context: Node, namespaces: bool = True) -> DocumentFragment: ...
def makeBuilder(options: Options) -> ExpatBuilderNS | ExpatBuilder: ...
