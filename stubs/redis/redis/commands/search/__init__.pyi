from _typeshed import Incomplete

from .commands import SearchCommands

class Search(SearchCommands):
    """
    Create a client for talking to search.
    It abstracts the API of the module and lets you just use the engine.
    """
    class BatchIndexer:
        """
        A batch indexer allows you to automatically batch
        document indexing in pipelines, flushing it every N documents.
        """
        def __init__(self, client, chunk_size: int = 1000) -> None: ...
        def add_document(
            self,
            doc_id,
            nosave: bool = False,
            score: float = 1.0,
            payload: Incomplete | None = None,
            replace: bool = False,
            partial: bool = False,
            no_create: bool = False,
            **fields,
        ):
            """Add a document to the batch query"""
            ...
        def add_document_hash(self, doc_id, score: float = 1.0, replace: bool = False):
            """Add a hash to the batch query"""
            ...
        def commit(self):
            """Manually commit and flush the batch indexing query"""
            ...

    def __init__(self, client, index_name: str = "idx") -> None:
        """
        Create a new Client for the given index_name.
        The default name is `idx`

        If conn is not None, we employ an already existing redis connection
        """
        ...
