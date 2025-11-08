from _typeshed import SupportsWrite
from collections.abc import Callable, Mapping, MutableMapping
from typing import Any
from typing_extensions import TypeAlias
from xml.sax import _Source, handler
from xml.sax.xmlreader import AttributesImpl, InputSource, XMLReader

from netaddr.core import Publisher, Subscriber
from netaddr.ip import IPAddress, IPNetwork, IPRange

_IanaInfoKey: TypeAlias = IPAddress | IPNetwork | IPRange

IANA_INFO: dict[str, dict[_IanaInfoKey, dict[str, str]]]

class SaxRecordParser(handler.ContentHandler):
    def __init__(self, callback: Callable[[Mapping[str, object] | None], object] | None = None) -> None: ...
    def startElement(self, name: str, attrs: AttributesImpl) -> None: ...
    def endElement(self, name: str) -> None: ...
    def characters(self, content: str) -> None: ...

class XMLRecordParser(Publisher):
    """A configurable Parser that understands how to parse XML based records."""
    xmlparser: XMLReader
    fh: InputSource | _Source
    def __init__(self, fh: InputSource | _Source, **kwargs: object) -> None: ...
    def process_record(self, rec: Mapping[str, object]) -> dict[str, str] | None: ...
    def consume_record(self, rec: object) -> None: ...
    def parse(self) -> None:
        """
        Parse and normalises records, notifying registered subscribers with
        record data as it is encountered.
        """
        ...
    # Arbitrary attributes are set in __init__ with `self.__dict__.update(kwargs)`
    def __getattr__(self, name: str, /) -> Any: ...

class IPv4Parser(XMLRecordParser):
    """
    A XMLRecordParser that understands how to parse and retrieve data records
    from the IANA IPv4 address space file.

    It can be found online here :-

        - http://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xml
    """
    def process_record(self, rec: Mapping[str, object]) -> dict[str, str]:
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class IPv6Parser(XMLRecordParser):
    """
    A XMLRecordParser that understands how to parse and retrieve data records
    from the IANA IPv6 address space file.

    It can be found online here :-

        - http://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xml
    """
    def process_record(self, rec: Mapping[str, object]) -> dict[str, str]:
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class IPv6UnicastParser(XMLRecordParser):
    """
    A XMLRecordParser that understands how to parse and retrieve data records
    from the IANA IPv6 unicast address assignments file.

    It can be found online here :-

        - http://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xml
    """
    def process_record(self, rec: Mapping[str, object]) -> dict[str, str]:
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class MulticastParser(XMLRecordParser):
    """
    A XMLRecordParser that knows how to process the IANA IPv4 multicast address
    allocation file.

    It can be found online here :-

        - http://www.iana.org/assignments/multicast-addresses/multicast-addresses.xml
    """
    def normalise_addr(self, addr: str) -> str:
        """Removes variations from address entries found in this particular file."""
        ...

class DictUpdater(Subscriber):
    dct: MutableMapping[_IanaInfoKey, dict[str, Any]]
    topic: str
    unique_key: str
    def __init__(self, dct: MutableMapping[_IanaInfoKey, dict[str, Any]], topic: str, unique_key: str) -> None: ...
    def update(self, data: dict[str, Any]) -> None: ...

        dct - lookup dict or dict like object to insert records into.

        topic - high-level category name of data to be processed.

        unique_key - key name in data dict that uniquely identifies it.
        """
        ...
    def update(self, data) -> None:
        """
        Callback function used by Publisher to notify this Subscriber about
        an update. Stores topic based information into dictionary passed to
        constructor.
        """
        ...

def load_info() -> None:
    """
    Parse and load internal IANA data lookups with the latest information from
    data files.
    """
    ...
def pprint_info(fh: SupportsWrite[str] | None = None) -> None:
    """Pretty prints IANA information to filehandle."""
    ...
def query(ip_addr: IPAddress) -> dict[str, list[dict[str, str]]]:
    """Returns informational data specific to this IP address."""
    ...
