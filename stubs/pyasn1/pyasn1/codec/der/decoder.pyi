from pyasn1.codec.ber.decoder import AbstractPayloadDecoder
from pyasn1.codec.cer import decoder
from pyasn1.type.tag import TagSet

__all__ = ["decode", "StreamingDecoder"]

class BitStringPayloadDecoder(decoder.BitStringPayloadDecoder):
    supportConstructedForm: bool

class OctetStringPayloadDecoder(decoder.OctetStringPayloadDecoder):
    supportConstructedForm: bool

RealPayloadDecoder = decoder.RealPayloadDecoder

TAG_MAP: dict[TagSet, AbstractPayloadDecoder]
TYPE_MAP: dict[int, AbstractPayloadDecoder]
# deprecated aliases
tagMap = TAG_MAP
typeMap = TYPE_MAP

class SingleItemDecoder(decoder.SingleItemDecoder):
    TAG_MAP: dict[TagSet, AbstractPayloadDecoder]
    TYPE_MAP: dict[int, AbstractPayloadDecoder]

    supportIndefLength: bool

class StreamingDecoder(decoder.StreamingDecoder):
    "Create an iterator that turns BER/CER/DER byte stream into ASN.1 objects.\n\nOn each iteration, consume whatever BER/CER/DER serialization is\navailable in the `substrate` stream-like object and turns it into\none or more, possibly nested, ASN.1 objects.\n\nParameters\n----------\nsubstrate: :py:class:`file`, :py:class:`io.BytesIO`\n    BER/CER/DER serialization in form of a byte stream\n\nKeyword Args\n------------\nasn1Spec: :py:class:`~pyasn1.type.base.PyAsn1Item`\n    A pyasn1 type object to act as a template guiding the decoder.\n    Depending on the ASN.1 structure being decoded, `asn1Spec` may\n    or may not be required. One of the reasons why `asn1Spec` may\n    me required is that ASN.1 structure is encoded in the *IMPLICIT*\n    tagging mode.\n\nYields\n------\n: :py:class:`~pyasn1.type.base.PyAsn1Item`, :py:class:`~pyasn1.error.SubstrateUnderrunError`\n    Decoded ASN.1 object (possibly, nested) or\n    :py:class:`~pyasn1.error.SubstrateUnderrunError` object indicating\n    insufficient BER/CER/DER serialization on input to fully recover ASN.1\n    objects from it.\n    \n    In the latter case the caller is advised to ensure some more data in\n    the input stream, then call the iterator again. The decoder will resume\n    the decoding process using the newly arrived data.\n\n    The `context` property of :py:class:`~pyasn1.error.SubstrateUnderrunError`\n    object might hold a reference to the partially populated ASN.1 object\n    being reconstructed.\n\nRaises\n------\n~pyasn1.error.PyAsn1Error, ~pyasn1.error.EndOfStreamError\n    `PyAsn1Error` on deserialization error, `EndOfStreamError` on\n     premature stream closure.\n\nExamples\n--------\nDecode BER serialisation without ASN.1 schema\n\n.. code-block:: pycon\n\n    >>> stream = io.BytesIO(\n    ...    b'0      \x02\x01\x01\x02\x01\x02\x02\x01\x03')\n    >>>\n    >>> for asn1Object in StreamingDecoder(stream):\n    ...     print(asn1Object)\n    >>>\n    SequenceOf:\n     1 2 3\n\nDecode BER serialisation with ASN.1 schema\n\n.. code-block:: pycon\n\n    >>> stream = io.BytesIO(\n    ...    b'0      \x02\x01\x01\x02\x01\x02\x02\x01\x03')\n    >>>\n    >>> schema = SequenceOf(componentType=Integer())\n    >>>\n    >>> decoder = StreamingDecoder(stream, asn1Spec=schema)\n    >>> for asn1Object in decoder:\n    ...     print(asn1Object)\n    >>>\n    SequenceOf:\n     1 2 3"
    SINGLE_ITEM_DECODER: type[SingleItemDecoder]

class Decoder(decoder.Decoder):
    """
    Create a BER decoder object.

    Parse BER/CER/DER octet-stream into one, possibly nested, ASN.1 object.
    """
    STREAMING_DECODER: type[StreamingDecoder]

decode: Decoder
