from _typeshed import Incomplete, Unused
from abc import ABCMeta, abstractmethod
from collections.abc import Callable

from pyasn1.type import base, char, univ, useful
from pyasn1.type.base import Asn1Type
from pyasn1.type.tag import TagSet

__all__ = ["StreamingDecoder", "Decoder", "decode"]

class AbstractPayloadDecoder:
    protoComponent: Asn1Type | None
    @abstractmethod
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Incomplete | None = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ) -> None:
        """
        Decode value with fixed byte length.

        The decoder is allowed to consume as many bytes as necessary.
        """
        ...
    # Abstract, but implementation is optional
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Incomplete | None = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ) -> None:
        """
        Decode value with undefined length.

        The decoder is allowed to consume as many bytes as necessary.
        """
        ...

class AbstractSimplePayloadDecoder(AbstractPayloadDecoder, metaclass=ABCMeta):
    @staticmethod
    def substrateCollector(asn1Object, substrate, length, options): ...

class RawPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.Any
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

class IntegerPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.Integer
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Unused = None,
        substrateFun: Unused = None,
        **options,
    ): ...

class BooleanPayloadDecoder(IntegerPayloadDecoder):
    protoComponent: univ.Boolean

class BitStringPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.BitString
    supportConstructedForm: bool
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

class OctetStringPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.OctetString
    supportConstructedForm: bool
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

class NullPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.Null
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Unused = None,
        substrateFun: Unused = None,
        **options,
    ): ...

class ObjectIdentifierPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.ObjectIdentifier
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Unused = None,
        substrateFun: Unused = None,
        **options,
    ): ...

class RealPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.Real
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Unused = None,
        substrateFun: Unused = None,
        **options,
    ): ...

class AbstractConstructedPayloadDecoder(AbstractPayloadDecoder, metaclass=ABCMeta):
    protoComponent: base.ConstructedAsn1Type | None

class ConstructedPayloadDecoderBase(AbstractConstructedPayloadDecoder):
    protoRecordComponent: univ.SequenceAndSetBase | None
    protoSequenceComponent: univ.SequenceOfAndSetOfBase | None
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

class SequenceOrSequenceOfPayloadDecoder(ConstructedPayloadDecoderBase):
    protoRecordComponent: univ.Sequence
    protoSequenceComponent: univ.SequenceOf

class SequencePayloadDecoder(SequenceOrSequenceOfPayloadDecoder):
    protoComponent: univ.Sequence

class SequenceOfPayloadDecoder(SequenceOrSequenceOfPayloadDecoder):
    protoComponent: univ.SequenceOf

class SetOrSetOfPayloadDecoder(ConstructedPayloadDecoderBase):
    protoRecordComponent: univ.Set
    protoSequenceComponent: univ.SetOf

class SetPayloadDecoder(SetOrSetOfPayloadDecoder):
    protoComponent: univ.Set

class SetOfPayloadDecoder(SetOrSetOfPayloadDecoder):
    protoComponent: univ.SetOf

class ChoicePayloadDecoder(AbstractConstructedPayloadDecoder):
    protoComponent: univ.Choice
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Incomplete | None = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Incomplete | None = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

class AnyPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent: univ.Any
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Unused = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state: Unused = None,
        decodeFun: Callable[..., Incomplete] | None = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

class UTF8StringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.UTF8String

class NumericStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.NumericString

class PrintableStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.PrintableString

class TeletexStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.TeletexString

class VideotexStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.VideotexString

class IA5StringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.IA5String

class GraphicStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.GraphicString

class VisibleStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.VisibleString

class GeneralStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.GeneralString

class UniversalStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.UniversalString

class BMPStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: char.BMPString

class ObjectDescriptorPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: useful.ObjectDescriptor

class GeneralizedTimePayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: useful.GeneralizedTime

class UTCTimePayloadDecoder(OctetStringPayloadDecoder):
    protoComponent: useful.UTCTime

TAG_MAP: dict[TagSet, AbstractPayloadDecoder]
TYPE_MAP: dict[int, AbstractPayloadDecoder]
# deprecated aliases
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemDecoder:
    defaultErrorState: int
    defaultRawDecoder: AnyPayloadDecoder
    supportIndefLength: bool
    TAG_MAP: dict[TagSet, AbstractPayloadDecoder]
    TYPE_MAP: dict[int, AbstractPayloadDecoder]
    def __init__(self, tagMap=..., typeMap=..., **ignored: Unused) -> None: ...
    def __call__(
        self,
        substrate,
        asn1Spec: Asn1Type | None = None,
        tagSet: TagSet | None = None,
        length: int | None = None,
        state=0,
        decodeFun: Unused = None,
        substrateFun: Callable[..., Incomplete] | None = None,
        **options,
    ): ...

decode: Decoder

class StreamingDecoder:
    "Create an iterator that turns BER/CER/DER byte stream into ASN.1 objects.\n\nOn each iteration, consume whatever BER/CER/DER serialization is\navailable in the `substrate` stream-like object and turns it into\none or more, possibly nested, ASN.1 objects.\n\nParameters\n----------\nsubstrate: :py:class:`file`, :py:class:`io.BytesIO`\n    BER/CER/DER serialization in form of a byte stream\n\nKeyword Args\n------------\nasn1Spec: :py:class:`~pyasn1.type.base.PyAsn1Item`\n    A pyasn1 type object to act as a template guiding the decoder.\n    Depending on the ASN.1 structure being decoded, `asn1Spec` may\n    or may not be required. One of the reasons why `asn1Spec` may\n    me required is that ASN.1 structure is encoded in the *IMPLICIT*\n    tagging mode.\n\nYields\n------\n: :py:class:`~pyasn1.type.base.PyAsn1Item`, :py:class:`~pyasn1.error.SubstrateUnderrunError`\n    Decoded ASN.1 object (possibly, nested) or\n    :py:class:`~pyasn1.error.SubstrateUnderrunError` object indicating\n    insufficient BER/CER/DER serialization on input to fully recover ASN.1\n    objects from it.\n    \n    In the latter case the caller is advised to ensure some more data in\n    the input stream, then call the iterator again. The decoder will resume\n    the decoding process using the newly arrived data.\n\n    The `context` property of :py:class:`~pyasn1.error.SubstrateUnderrunError`\n    object might hold a reference to the partially populated ASN.1 object\n    being reconstructed.\n\nRaises\n------\n~pyasn1.error.PyAsn1Error, ~pyasn1.error.EndOfStreamError\n    `PyAsn1Error` on deserialization error, `EndOfStreamError` on\n     premature stream closure.\n\nExamples\n--------\nDecode BER serialisation without ASN.1 schema\n\n.. code-block:: pycon\n\n    >>> stream = io.BytesIO(\n    ...    b'0      \x02\x01\x01\x02\x01\x02\x02\x01\x03')\n    >>>\n    >>> for asn1Object in StreamingDecoder(stream):\n    ...     print(asn1Object)\n    >>>\n    SequenceOf:\n     1 2 3\n\nDecode BER serialisation with ASN.1 schema\n\n.. code-block:: pycon\n\n    >>> stream = io.BytesIO(\n    ...    b'0      \x02\x01\x01\x02\x01\x02\x02\x01\x03')\n    >>>\n    >>> schema = SequenceOf(componentType=Integer())\n    >>>\n    >>> decoder = StreamingDecoder(stream, asn1Spec=schema)\n    >>> for asn1Object in decoder:\n    ...     print(asn1Object)\n    >>>\n    SequenceOf:\n     1 2 3"
    SINGLE_ITEM_DECODER: type[SingleItemDecoder]

    def __init__(self, substrate, asn1Spec=None, *, tagMap=..., typeMap=..., **ignored: Unused) -> None: ...
    def __iter__(self): ...

class Decoder:
    """
    Create a BER decoder object.

    Parse BER/CER/DER octet-stream into one, possibly nested, ASN.1 object.
    """
    STREAMING_DECODER: type[StreamingDecoder]

    @classmethod
    def __call__(cls, substrate, asn1Spec=None, *, tagMap=..., typeMap=..., **ignored: Unused):
        "Turns BER/CER/DER octet stream into an ASN.1 object.\n\nTakes BER/CER/DER octet-stream in form of :py:class:`bytes`\nand decode it into an ASN.1 object\n(e.g. :py:class:`~pyasn1.type.base.PyAsn1Item` derivative) which\nmay be a scalar or an arbitrary nested structure.\n\nParameters\n----------\nsubstrate: :py:class:`bytes`\n    BER/CER/DER octet-stream to parse\n\nKeyword Args\n------------\nasn1Spec: :py:class:`~pyasn1.type.base.PyAsn1Item`\n    A pyasn1 type object (:py:class:`~pyasn1.type.base.PyAsn1Item`\n    derivative) to act as a template guiding the decoder.\n    Depending on the ASN.1 structure being decoded, `asn1Spec` may or\n    may not be required. Most common reason for it to require is that\n    ASN.1 structure is encoded in *IMPLICIT* tagging mode.\n\nsubstrateFun: :py:class:`Union[\n        Callable[[pyasn1.type.base.PyAsn1Item, bytes, int],\n                 Tuple[pyasn1.type.base.PyAsn1Item, bytes]],\n        Callable[[pyasn1.type.base.PyAsn1Item, io.BytesIO, int, dict],\n                 Generator[Union[pyasn1.type.base.PyAsn1Item,\n                                 pyasn1.error.SubstrateUnderrunError],\n                           None, None]]\n    ]`\n    User callback meant to generalize special use cases like non-recursive or\n    partial decoding. A 3-arg non-streaming variant is supported for backwards\n    compatiblilty in addition to the newer 4-arg streaming variant.\n    The callback will receive the uninitialized object recovered from substrate\n    as 1st argument, the uninterpreted payload as 2nd argument, and the length\n    of the uninterpreted payload as 3rd argument. The streaming variant will\n    additionally receive the decode(..., **options) kwargs as 4th argument.\n    The non-streaming variant shall return an object that will be propagated\n    as decode() return value as 1st item, and the remainig payload for further\n    decode passes as 2nd item.\n    The streaming variant shall yield an object that will be propagated as\n    decode() return value, and leave the remaining payload in the stream.\n\nReturns\n-------\n: :py:class:`tuple`\n    A tuple of :py:class:`~pyasn1.type.base.PyAsn1Item` object\n    recovered from BER/CER/DER substrate and the unprocessed trailing\n    portion of the `substrate` (may be empty)\n\nRaises\n------\n: :py:class:`~pyasn1.error.PyAsn1Error`\n    :py:class:`~pyasn1.error.SubstrateUnderrunError` on insufficient\n    input or :py:class:`~pyasn1.error.PyAsn1Error` on decoding error.\n\nExamples\n--------\nDecode BER/CER/DER serialisation without ASN.1 schema\n\n.. code-block:: pycon\n\n   >>> s, unprocessed = decode(b'0      \x02\x01\x01\x02\x01\x02\x02\x01\x03')\n   >>> str(s)\n   SequenceOf:\n    1 2 3\n\nDecode BER/CER/DER serialisation with ASN.1 schema\n\n.. code-block:: pycon\n\n   >>> seq = SequenceOf(componentType=Integer())\n   >>> s, unprocessed = decode(\n        b'0     \x02\x01\x01\x02\x01\x02\x02\x01\x03', asn1Spec=seq)\n   >>> str(s)\n   SequenceOf:\n    1 2 3"
        ...
