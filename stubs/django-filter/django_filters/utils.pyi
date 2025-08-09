from collections.abc import Callable
from datetime import datetime
from typing import Any

from django.db import models
from django.db.models import Model

def deprecate(msg: str, level_modifier: int = 0) -> None: ...

class MigrationNotice(DeprecationWarning):
    url: str
    def __init__(self, message: str) -> None: ...

class RenameAttributesBase(type):
    """
    Handles the deprecation paths when renaming an attribute.

    It does the following:
    - Defines accessors that redirect to the renamed attributes.
    - Complain whenever an old attribute is accessed.

    This is conceptually based on `django.utils.deprecation.RenameMethodsBase`.
    """
    renamed_attributes: tuple[tuple[str, str, DeprecationWarning], ...] = ()

    # Class attrs vary by definition
    def __new__(metacls, name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> RenameAttributesBase: ...
    def get_name(metacls, name: str) -> str:
        """
        Get the real attribute name. If the attribute has been renamed,
        the new name will be returned and a deprecation warning issued.
        """
        ...
    def __getattr__(metacls, name: str) -> Any: ...  # Attribute values vary by name and class
    def __setattr__(metacls, name: str, value: Any) -> None: ...  # Attribute values can be any type

def try_dbfield(
    fn: Callable[[models.Field[Any, Any]], Any], field_class: type[models.Field[Any, Any]]
) -> Any:
    """
    Try ``fn`` with the DB ``field_class`` by walking its
    MRO until a result is found.

    ex::
        _try_dbfield(field_dict.get, models.CharField)
    """
    ...
def get_all_model_fields(model: type[Model]) -> dict[str, models.Field[Any, Any]]: ...  # Fields vary by model definition
def get_model_field(model: type[Model], field_name: str) -> models.Field[Any, Any]:
    """
    Get a ``model`` field, traversing relationships
    in the ``field_name``.

    ex::

        f = get_model_field(Book, 'author__first_name')
    """
    ...
def get_field_parts(model: type[Model], field_name: str) -> list[models.Field[Any, Any]]:
    """
    Get the field parts that represent the traversable relationships from the
    base ``model`` to the final field, described by ``field_name``.

    ex::

        >>> parts = get_field_parts(Book, 'author__first_name')
        >>> [p.verbose_name for p in parts]
        ['author', 'first name']
    """
    ...
def resolve_field(
    model_field: models.Field[Any, Any], lookup_expr: str
) -> tuple[models.Field[Any, Any], str]:
    """
    Resolves a ``lookup_expr`` into its final output field, given
    the initial ``model_field``. The lookup expression should only contain
    transforms and lookups, not intermediary model field parts.

    Note:
    This method is based on django.db.models.sql.query.Query.build_lookup

    For more info on the lookup API:
    https://docs.djangoproject.com/en/stable/ref/models/lookups/
    """
    ...
def handle_timezone(value: datetime, is_dst: bool | None = None) -> datetime: ...
def verbose_field_name(model: type[Model], field_name: str) -> str:
    """
    Get the verbose name for a given ``field_name``. The ``field_name``
    will be traversed across relationships. Returns '[invalid name]' for
    any field name that cannot be traversed.

    ex::

        >>> verbose_field_name(Article, 'author__name')
        'author name'
    """
    ...
def verbose_lookup_expr(lookup_expr: str) -> str:
    """
    Get a verbose, more humanized expression for a given ``lookup_expr``.
    Each part in the expression is looked up in the ``FILTERS_VERBOSE_LOOKUPS``
    dictionary. Missing keys will simply default to itself.

    ex::

        >>> verbose_lookup_expr('year__lt')
        'year is less than'

        # with `FILTERS_VERBOSE_LOOKUPS = {}`
        >>> verbose_lookup_expr('year__lt')
        'year lt'
    """
    ...
def label_for_filter(model: type[Model], field_name: str, lookup_expr: str, exclude: bool = False) -> str:
    """
    Create a generic label suitable for a filter.

    ex::

        >>> label_for_filter(Article, 'author__name', 'in')
        'auther name is in'
    """
    ...
def translate_validation(error_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Translate a Django ErrorDict into its DRF ValidationError."""
    ...
