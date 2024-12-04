from _typeshed import Incomplete
from collections.abc import ItemsView, Iterator

from .exceptions import ValidationError

def ignore_ref_siblings(schema) -> list[tuple[str, Incomplete]] | ItemsView[str, Incomplete]:
    """
    Ignore siblings of ``$ref`` if it is present.

    Otherwise, return all keywords.

    Suitable for use with `create`'s ``applicable_validators`` argument.
    """
    ...
def dependencies_draft3(validator, dependencies, instance, schema) -> None: ...
def dependencies_draft4_draft6_draft7(validator, dependencies, instance, schema) -> None:
    """
    Support for the ``dependencies`` keyword from pre-draft 2019-09.

    In later drafts, the keyword was split into separate
    ``dependentRequired`` and ``dependentSchemas`` validators.
    """
    ...
def disallow_draft3(validator, disallow, instance, schema) -> None: ...
def extends_draft3(validator, extends, instance, schema) -> None: ...
def items_draft3_draft4(validator, items, instance, schema) -> None: ...
def additionalItems(validator, aI, instance, schema) -> None: ...
def items_draft6_draft7_draft201909(validator, items, instance, schema) -> None: ...
def minimum_draft3_draft4(validator, minimum, instance, schema) -> None: ...
def maximum_draft3_draft4(validator, maximum, instance, schema) -> None: ...
def properties_draft3(validator, properties, instance, schema) -> None: ...
def type_draft3(validator, types, instance, schema) -> None: ...
def contains_draft6_draft7(validator, contains, instance, schema) -> None: ...
def recursiveRef(validator, recursiveRef, instance, schema) -> None: ...
def find_evaluated_item_indexes_by_schema(validator, instance, schema) -> list[int]:
    """
    Get all indexes of items that get evaluated under the current schema.

    Covers all keywords related to unevaluatedItems: items, prefixItems, if,
    then, else, contains, unevaluatedItems, allOf, oneOf, anyOf
    """
    ...
def unevaluatedItems_draft2019(validator, unevaluatedItems, instance, schema) -> Iterator[ValidationError]: ...
def find_evaluated_property_keys_by_schema(validator, instance, schema) -> list[Incomplete]: ...
def unevaluatedProperties_draft2019(validator, uP, instance, schema) -> Iterator[ValidationError]: ...
