from _typeshed import Incomplete
from typing import Final

from braintree.resource import Resource

class DocumentUpload(Resource):
    """
    A class representing a DocumentUpload.

    An example of creating a document upload with all available fields:

        result = braintree.DocumentUpload.create(
            {
                "kind": braintree.DocumentUpload.Kind.EvidenceDocument,
                "file": open("path/to/file", "rb"),
            }
        )

    For more information on DocumentUploads, see https://developer.paypal.com/braintree/docs/reference/request/document-upload/create
    """
    class Kind:
        EvidenceDocument: Final = "evidence_document"

    @staticmethod
    def create(params: Incomplete | None = None):
        """
        Create a DocumentUpload

        File and Kind are required:

            result = braintree.DocumentUpload.create(
                {
                    "kind": braintree.DocumentUpload.Kind.EvidenceDocument,
                    "file": open("path/to/file", "rb"),
                }
            )
        """
        ...
    @staticmethod
    def create_signature(): ...
    def __init__(self, gateway, attributes) -> None: ...
