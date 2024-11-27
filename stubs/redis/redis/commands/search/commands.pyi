from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any, Literal
from typing_extensions import TypeAlias

from .aggregation import AggregateRequest, AggregateResult, Cursor
from .query import Query
from .result import Result

_QueryParams: TypeAlias = Mapping[str, str | float]

NUMERIC: Literal["NUMERIC"]

CREATE_CMD: Literal["FT.CREATE"]
ALTER_CMD: Literal["FT.ALTER"]
SEARCH_CMD: Literal["FT.SEARCH"]
ADD_CMD: Literal["FT.ADD"]
ADDHASH_CMD: Literal["FT.ADDHASH"]
DROP_CMD: Literal["FT.DROP"]
EXPLAIN_CMD: Literal["FT.EXPLAIN"]
EXPLAINCLI_CMD: Literal["FT.EXPLAINCLI"]
DEL_CMD: Literal["FT.DEL"]
AGGREGATE_CMD: Literal["FT.AGGREGATE"]
PROFILE_CMD: Literal["FT.PROFILE"]
CURSOR_CMD: Literal["FT.CURSOR"]
SPELLCHECK_CMD: Literal["FT.SPELLCHECK"]
DICT_ADD_CMD: Literal["FT.DICTADD"]
DICT_DEL_CMD: Literal["FT.DICTDEL"]
DICT_DUMP_CMD: Literal["FT.DICTDUMP"]
GET_CMD: Literal["FT.GET"]
MGET_CMD: Literal["FT.MGET"]
CONFIG_CMD: Literal["FT.CONFIG"]
TAGVALS_CMD: Literal["FT.TAGVALS"]
ALIAS_ADD_CMD: Literal["FT.ALIASADD"]
ALIAS_UPDATE_CMD: Literal["FT.ALIASUPDATE"]
ALIAS_DEL_CMD: Literal["FT.ALIASDEL"]
INFO_CMD: Literal["FT.INFO"]
SUGADD_COMMAND: Literal["FT.SUGADD"]
SUGDEL_COMMAND: Literal["FT.SUGDEL"]
SUGLEN_COMMAND: Literal["FT.SUGLEN"]
SUGGET_COMMAND: Literal["FT.SUGGET"]
SYNUPDATE_CMD: Literal["FT.SYNUPDATE"]
SYNDUMP_CMD: Literal["FT.SYNDUMP"]

NOOFFSETS: Literal["NOOFFSETS"]
NOFIELDS: Literal["NOFIELDS"]
STOPWORDS: Literal["STOPWORDS"]
WITHSCORES: Literal["WITHSCORES"]
FUZZY: Literal["FUZZY"]
WITHPAYLOADS: Literal["WITHPAYLOADS"]

class SearchCommands:
    """Search commands."""
    def batch_indexer(self, chunk_size: int = 100):
        """Create a new batch indexer from the client with a given chunk size"""
        ...
    def create_index(
        self,
        fields,
        no_term_offsets: bool = False,
        no_field_flags: bool = False,
        stopwords: Incomplete | None = None,
        definition: Incomplete | None = None,
        max_text_fields: bool = False,  # added in 4.1.1
        temporary: Incomplete | None = None,  # added in 4.1.1
        no_highlight: bool = False,  # added in 4.1.1
        no_term_frequencies: bool = False,  # added in 4.1.1
        skip_initial_scan: bool = False,  # added in 4.1.1
    ):
        """
        Create the search index. The index must not already exist.

        ### Parameters:

        - **fields**: a list of TextField or NumericField objects
        - **no_term_offsets**: If true, we will not save term offsets in
        the index
        - **no_field_flags**: If true, we will not save field flags that
        allow searching in specific fields
        - **stopwords**: If not None, we create the index with this custom
        stopword list. The list can be empty
        - **max_text_fields**: If true, we will encode indexes as if there
        were more than 32 text fields which allows you to add additional
        fields (beyond 32).
        - **temporary**: Create a lightweight temporary index which will
        expire after the specified period of inactivity (in seconds). The
        internal idle timer is reset whenever the index is searched or added to.
        - **no_highlight**: If true, disabling highlighting support.
        Also implied by no_term_offsets.
        - **no_term_frequencies**: If true, we avoid saving the term frequencies
        in the index.
        - **skip_initial_scan**: If true, we do not scan and index.

        For more information see `FT.CREATE <https://redis.io/commands/ft.create>`_.
        """
        ...
    def alter_schema_add(self, fields):
        """
        Alter the existing search index by adding new fields. The index
        must already exist.

        ### Parameters:

        - **fields**: a list of Field objects to add for the index

        For more information see `FT.ALTER <https://redis.io/commands/ft.alter>`_.
        """
        ...
    def dropindex(self, delete_documents: bool = False):
        """
        Drop the index if it exists.
        Replaced `drop_index` in RediSearch 2.0.
        Default behavior was changed to not delete the indexed documents.

        ### Parameters:

        - **delete_documents**: If `True`, all documents will be deleted.

        For more information see `FT.DROPINDEX <https://redis.io/commands/ft.dropindex>`_.
        """
        ...
    def add_document(
        self,
        doc_id,
        nosave: bool = False,
        score: float = 1.0,
        payload: Incomplete | None = None,
        replace: bool = False,
        partial: bool = False,
        language: Incomplete | None = None,
        no_create: bool = False,
        **fields,
    ):
        """
        Add a single document to the index.

        ### Parameters

        - **doc_id**: the id of the saved document.
        - **nosave**: if set to true, we just index the document, and don't
                      save a copy of it. This means that searches will just
                      return ids.
        - **score**: the document ranking, between 0.0 and 1.0
        - **payload**: optional inner-index payload we can save for fast
        i              access in scoring functions
        - **replace**: if True, and the document already is in the index,
        we perform an update and reindex the document
        - **partial**: if True, the fields specified will be added to the
                       existing document.
                       This has the added benefit that any fields specified
                       with `no_index`
                       will not be reindexed again. Implies `replace`
        - **language**: Specify the language used for document tokenization.
        - **no_create**: if True, the document is only updated and reindexed
                         if it already exists.
                         If the document does not exist, an error will be
                         returned. Implies `replace`
        - **fields** kwargs dictionary of the document fields to be saved
                         and/or indexed.
                     NOTE: Geo points shoule be encoded as strings of "lon,lat"
        """
        ...
    def add_document_hash(self, doc_id, score: float = 1.0, language: Incomplete | None = None, replace: bool = False):
        """
        Add a hash document to the index.

        ### Parameters

        - **doc_id**: the document's id. This has to be an existing HASH key
                      in Redis that will hold the fields the index needs.
        - **score**:  the document ranking, between 0.0 and 1.0
        - **replace**: if True, and the document already is in the index, we
                      perform an update and reindex the document
        - **language**: Specify the language used for document tokenization.
        """
        ...
    def delete_document(self, doc_id, conn: Incomplete | None = None, delete_actual_document: bool = False):
        """
        Delete a document from index
        Returns 1 if the document was deleted, 0 if not

        ### Parameters

        - **delete_actual_document**: if set to True, RediSearch also delete
                                      the actual document if it is in the index
        """
        ...
    def load_document(self, id):
        """Load a single document by id"""
        ...
    def get(self, *ids):
        """
        Returns the full contents of multiple documents.

        ### Parameters

        - **ids**: the ids of the saved documents.
        """
        ...
    def info(self):
        """
        Get info an stats about the the current index, including the number of
        documents, memory consumption, etc

        For more information see `FT.INFO <https://redis.io/commands/ft.info>`_.
        """
        ...
    def get_params_args(self, query_params: _QueryParams) -> list[Any]: ...
    def search(self, query: str | Query, query_params: _QueryParams | None = None) -> Result:
        """
        Search the index for a given query, and return a result of documents

        ### Parameters

        - **query**: the search query. Either a text for simple queries with
                     default parameters, or a Query object for complex queries.
                     See RediSearch's documentation on query format

        For more information see `FT.SEARCH <https://redis.io/commands/ft.search>`_.
        """
        ...
    def explain(self, query: str | Query, query_params: _QueryParams | None = None):
        """
        Returns the execution plan for a complex query.

        For more information see `FT.EXPLAIN <https://redis.io/commands/ft.explain>`_.
        """
        ...
    def explain_cli(self, query): ...
    def aggregate(self, query: AggregateRequest | Cursor, query_params: _QueryParams | None = None) -> AggregateResult:
        """
        Issue an aggregation query.

        ### Parameters

        **query**: This can be either an `AggregateRequest`, or a `Cursor`

        An `AggregateResult` object is returned. You can access the rows from
        its `rows` property, which will always yield the rows of the result.

        For more information see `FT.AGGREGATE <https://redis.io/commands/ft.aggregate>`_.
        """
        ...
    def profile(
        self, query: str | Query | AggregateRequest, limited: bool = False, query_params: Mapping[str, str | float] | None = None
    ) -> tuple[Incomplete, Incomplete]:
        """
        Performs a search or aggregate command and collects performance
        information.

        ### Parameters

        **query**: This can be either an `AggregateRequest`, `Query` or string.
        **limited**: If set to True, removes details of reader iterator.
        **query_params**: Define one or more value parameters.
        Each parameter has a name and a value.
        """
        ...
    def spellcheck(
        self, query, distance: Incomplete | None = None, include: Incomplete | None = None, exclude: Incomplete | None = None
    ):
        """
        Issue a spellcheck query

        ### Parameters

        **query**: search query.
        **distance***: the maximal Levenshtein distance for spelling
                       suggestions (default: 1, max: 4).
        **include**: specifies an inclusion custom dictionary.
        **exclude**: specifies an exclusion custom dictionary.

        For more information see `FT.SPELLCHECK <https://redis.io/commands/ft.spellcheck>`_.
        """
        ...
    def dict_add(self, name, *terms):
        """
        Adds terms to a dictionary.

        ### Parameters

        - **name**: Dictionary name.
        - **terms**: List of items for adding to the dictionary.

        For more information see `FT.DICTADD <https://redis.io/commands/ft.dictadd>`_.
        """
        ...
    def dict_del(self, name, *terms):
        """
        Deletes terms from a dictionary.

        ### Parameters

        - **name**: Dictionary name.
        - **terms**: List of items for removing from the dictionary.

        For more information see `FT.DICTDEL <https://redis.io/commands/ft.dictdel>`_.
        """
        ...
    def dict_dump(self, name):
        """
        Dumps all terms in the given dictionary.

        ### Parameters

        - **name**: Dictionary name.

        For more information see `FT.DICTDUMP <https://redis.io/commands/ft.dictdump>`_.
        """
        ...
    def config_set(self, option: str, value: str) -> bool:
        """
        Set runtime configuration option.

        ### Parameters

        - **option**: the name of the configuration option.
        - **value**: a value for the configuration option.

        For more information see `FT.CONFIG SET <https://redis.io/commands/ft.config-set>`_.
        """
        ...
    def config_get(self, option: str) -> dict[str, str]:
        """
        Get runtime configuration option value.

        ### Parameters

        - **option**: the name of the configuration option.

        For more information see `FT.CONFIG GET <https://redis.io/commands/ft.config-get>`_.
        """
        ...
    def tagvals(self, tagfield):
        """
        Return a list of all possible tag values

        ### Parameters

        - **tagfield**: Tag field name

        For more information see `FT.TAGVALS <https://redis.io/commands/ft.tagvals>`_.
        """
        ...
    def aliasadd(self, alias):
        """
        Alias a search index - will fail if alias already exists

        ### Parameters

        - **alias**: Name of the alias to create

        For more information see `FT.ALIASADD <https://redis.io/commands/ft.aliasadd>`_.
        """
        ...
    def aliasupdate(self, alias):
        """
        Updates an alias - will fail if alias does not already exist

        ### Parameters

        - **alias**: Name of the alias to create

        For more information see `FT.ALIASUPDATE <https://redis.io/commands/ft.aliasupdate>`_.
        """
        ...
    def aliasdel(self, alias):
        """
        Removes an alias to a search index

        ### Parameters

        - **alias**: Name of the alias to delete

        For more information see `FT.ALIASDEL <https://redis.io/commands/ft.aliasdel>`_.
        """
        ...
    def sugadd(self, key, *suggestions, **kwargs):
        """
        Add suggestion terms to the AutoCompleter engine. Each suggestion has
        a score and string.
        If kwargs["increment"] is true and the terms are already in the
        server's dictionary, we increment their scores.

        For more information see `FT.SUGADD <https://redis.io/commands/ft.sugadd/>`_.
        """
        ...
    def suglen(self, key):
        """
        Return the number of entries in the AutoCompleter index.

        For more information see `FT.SUGLEN <https://redis.io/commands/ft.suglen>`_.
        """
        ...
    def sugdel(self, key, string):
        """
        Delete a string from the AutoCompleter index.
        Returns 1 if the string was found and deleted, 0 otherwise.

        For more information see `FT.SUGDEL <https://redis.io/commands/ft.sugdel>`_.
        """
        ...
    def sugget(self, key, prefix, fuzzy: bool = False, num: int = 10, with_scores: bool = False, with_payloads: bool = False):
        """
        Get a list of suggestions from the AutoCompleter, for a given prefix.

        Parameters:

        prefix : str
            The prefix we are searching. **Must be valid ascii or utf-8**
        fuzzy : bool
            If set to true, the prefix search is done in fuzzy mode.
            **NOTE**: Running fuzzy searches on short (<3 letters) prefixes
            can be very
            slow, and even scan the entire index.
        with_scores : bool
            If set to true, we also return the (refactored) score of
            each suggestion.
            This is normally not needed, and is NOT the original score
            inserted into the index.
        with_payloads : bool
            Return suggestion payloads
        num : int
            The maximum number of results we return. Note that we might
            return less. The algorithm trims irrelevant suggestions.

        Returns:

        list:
             A list of Suggestion objects. If with_scores was False, the
             score of all suggestions is 1.

        For more information see `FT.SUGGET <https://redis.io/commands/ft.sugget>`_.
        """
        ...
    def synupdate(self, groupid, skipinitial: bool = False, *terms):
        """
        Updates a synonym group.
        The command is used to create or update a synonym group with
        additional terms.
        Only documents which were indexed after the update will be affected.

        Parameters:

        groupid :
            Synonym group id.
        skipinitial : bool
            If set to true, we do not scan and index.
        terms :
            The terms.

        For more information see `FT.SYNUPDATE <https://redis.io/commands/ft.synupdate>`_.
        """
        ...
    def syndump(self):
        """
        Dumps the contents of a synonym group.

        The command is used to dump the synonyms data structure.
        Returns a list of synonym terms and their synonym group ids.

        For more information see `FT.SYNDUMP <https://redis.io/commands/ft.syndump>`_.
        """
        ...
