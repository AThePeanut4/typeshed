""""""

from _typeshed import ReadableBuffer

from pyasn1.type.base import Asn1Item

from ..protocol.rfc4511 import ExtendedRequest

def extended_operation(
    request_name, request_value: Asn1Item | ReadableBuffer | None = None, no_encode: bool | None = None
) -> ExtendedRequest: ...
def extended_request_to_dict(request): ...
def extended_response_to_dict(response): ...
def intermediate_response_to_dict(response): ...
def extended_response_to_dict_fast(response): ...
def intermediate_response_to_dict_fast(response): ...
