import _typeshed
from collections import OrderedDict
from collections.abc import Iterator, Sequence
from functools import partial
from logging import Logger
from typing import Any, ClassVar, Generic, Literal, NoReturn, TypeVar, overload
from typing_extensions import TypeAlias, deprecated

from django.db.models import Field as DjangoField, Model, QuerySet
from django.utils.safestring import SafeString

from .declarative import DeclarativeMetaclass, ModelDeclarativeMetaclass
from .fields import Field
from .instance_loaders import BaseInstanceLoader
from .options import ResourceOptions
from .results import Error, Result, RowResult
from .widgets import ForeignKeyWidget, ManyToManyWidget, Widget

Dataset: TypeAlias = _typeshed.Incomplete  # tablib.Dataset
logger: Logger

def has_natural_foreign_key(model: Model) -> bool:
    """Determine if a model has natural foreign key functions"""
    ...

class Diff:
    left: list[str]
    right: list[str]
    new: bool
    def __init__(self, resource: Resource[_ModelT], instance: _ModelT, new: bool) -> None: ...
    def compare_with(self, resource: Resource[_ModelT], instance: _ModelT, dry_run: bool = False) -> None: ...
    def as_html(self) -> list[SafeString]: ...

_ModelT = TypeVar("_ModelT", bound=Model)

class Resource(Generic[_ModelT], metaclass=DeclarativeMetaclass):
    """
    Resource defines how objects are mapped to their import and export
    representations and handle importing and exporting data.
    """
    _meta: ResourceOptions[_ModelT]
    fields: OrderedDict[str, Field]
    create_instances: list[_ModelT]
    update_instances: list[_ModelT]
    delete_instances: list[_ModelT]
    def __init__(self, **kwargs: Any) -> None:
        """
        kwargs:
           An optional dict of kwargs.
           Subclasses can use kwargs to pass dynamic values to enhance import / exports.
        """
        ...
    @classmethod
    def get_result_class(self) -> type[Result]:
        """Returns the class used to store the result of an import."""
        ...
    @classmethod
    def get_row_result_class(self) -> type[RowResult]:
        """Returns the class used to store the result of a row import."""
        ...
    @classmethod
    def get_error_result_class(self) -> type[Error]:
        """Returns the class used to store an error resulting from an import."""
        ...
    @classmethod
    def get_diff_class(self) -> type[Diff]:
        """Returns the class used to display the diff for an imported instance."""
        ...
    @classmethod
    def get_db_connection_name(self) -> str: ...
    def get_use_transactions(self) -> bool: ...
    def get_chunk_size(self) -> int: ...
    @deprecated("The 'get_fields()' method is deprecated and will be removed in a future release.")
    def get_fields(self, **kwargs: Any) -> list[Field]:
        """
        Returns fields sorted according to
        :attr:`~import_export.resources.ResourceOptions.export_order`.
        """
        ...
    def get_field_name(self, field: Field) -> str:
        """Returns the field name for a given field."""
        ...
    def init_instance(self, row: dict[str, Any] | None = None) -> _ModelT:
        """
        Initializes an object. Implemented in
        :meth:`import_export.resources.ModelResource.init_instance`.
        """
        ...
    def get_instance(self, instance_loader: BaseInstanceLoader, row: dict[str, Any]) -> _ModelT | None:
        """
        If all 'import_id_fields' are present in the dataset, calls
        the :doc:`InstanceLoader <api_instance_loaders>`. Otherwise,
        returns `None`.
        """
        ...
    def get_or_init_instance(self, instance_loader: BaseInstanceLoader, row: dict[str, Any]) -> tuple[_ModelT | None, bool]:
        """Either fetches an already existing instance or initializes a new one."""
        ...
    def get_import_id_fields(self) -> Sequence[str]: ...
    def get_bulk_update_fields(self) -> list[str]:
        """
        Returns the fields to be included in calls to bulk_update().
        ``import_id_fields`` are removed because `id` fields cannot be supplied to
        bulk_update().
        """
        ...
    def bulk_create(
        self,
        using_transactions: bool,
        dry_run: bool,
        raise_errors: bool,
        batch_size: int | None = None,
        result: Result | None = None,
    ) -> None:
        """Creates objects by calling ``bulk_create``."""
        ...
    def bulk_update(
        self,
        using_transactions: bool,
        dry_run: bool,
        raise_errors: bool,
        batch_size: int | None = None,
        result: Result | None = None,
    ) -> None:
        """Updates objects by calling ``bulk_update``."""
        ...
    def bulk_delete(self, using_transactions: bool, dry_run: bool, raise_errors: bool, result: Result | None = None) -> None:
        """
        Deletes objects by filtering on a list of instances to be deleted,
        then calling ``delete()`` on the entire queryset.
        """
        ...
    def validate_instance(
        self, instance: _ModelT, import_validation_errors: dict[str, Any] | None = None, validate_unique: bool = True
    ) -> None:
        """
        Takes any validation errors that were raised by
        :meth:`~import_export.resources.Resource.import_obj`, and combines them
        with validation errors raised by the instance's ``full_clean()``
        method. The combined errors are then re-raised as single, multi-field
        ValidationError.

        If the ``clean_model_instances`` option is False, the instances's
        ``full_clean()`` method is not called, and only the errors raised by
        ``import_obj()`` are re-raised.
        """
        ...
    # For all the definitions below (from `save_instance()` to `import_row()`), `**kwargs` should contain:
    # dry_run: bool, use_transactions: bool, row_number: int, retain_instance_in_row_result: bool.
    # Users are free to pass extra arguments in `import_data()`so PEP 728 can probably be leveraged here.
    def save_instance(self, instance: _ModelT, is_create: bool, row: dict[str, Any], **kwargs: Any) -> None:
        """
        Takes care of saving the object to the database.

        Objects can be created in bulk if ``use_bulk`` is enabled.

        :param instance: The instance of the object to be persisted.
        :param is_create: A boolean flag to indicate whether this is a new object
                          to be created, or an existing object to be updated.
        :param using_transactions: A flag to indicate whether db transactions are used.
        :param dry_run: A flag to indicate dry-run mode.
        """
        ...
    def do_instance_save(self, instance: _ModelT) -> None: ...
    def before_save_instance(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def after_save_instance(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def delete_instance(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None:
        """
        Calls :meth:`instance.delete` as long as ``dry_run`` is not set.
        If ``use_bulk`` then instances are appended to a list for bulk import.
        """
        ...
    def before_delete_instance(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def after_delete_instance(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def import_field(self, field: Field, instance: _ModelT, row: dict[str, Any], is_m2m: bool = False, **kwargs: Any) -> None:
        """
        Calls :meth:`import_export.fields.Field.save` if ``Field.attribute``
        is specified, and ``Field.column_name`` is found in ``data``.
        """
        ...
    def get_import_fields(self) -> list[Field]: ...
    def import_instance(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None: ...
    def save_m2m(self, instance: _ModelT, row: dict[str, Any], **kwargs: Any) -> None:
        """
        Saves m2m fields.

        Model instance need to have a primary key value before
        a many-to-many relationship can be used.
        """
        ...
    def for_delete(self, row: dict[str, Any], instance: _ModelT) -> bool:
        """
        Returns ``True`` if ``row`` importing should delete instance.

        Default implementation returns ``False``.
        Override this method to handle deletion.
        """
        ...
    def skip_row(
        self, instance: _ModelT, original: _ModelT, row: dict[str, Any], import_validation_errors: dict[str, Any] | None = None
    ) -> bool:
        """
        Returns ``True`` if ``row`` importing should be skipped.

        Default implementation returns ``False`` unless skip_unchanged == True
        and skip_diff == False.

        If skip_diff is True, then no comparisons can be made because ``original``
        will be None.

        When left unspecified, skip_diff and skip_unchanged both default to ``False``,
        and rows are never skipped.

        By default, rows are not skipped if validation errors have been detected
        during import.  You can change this behavior and choose to ignore validation
        errors by overriding this method.

        Override this method to handle skipping rows meeting certain
        conditions.

        Use ``super`` if you want to preserve default handling while overriding
        ::

            class YourResource(ModelResource):
                def skip_row(self, instance, original,
                             row, import_validation_errors=None):
                    # Add code here
                    return super().skip_row(instance, original, row,
                                            import_validation_errors=import_validation_errors)
        """
        ...
    def get_diff_headers(self) -> list[str]:
        """Diff representation headers."""
        ...
    def before_import(self, dataset: Dataset, **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def after_import(self, dataset: Dataset, result: Result, **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def before_import_row(self, row: dict[str, Any], **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def after_import_row(self, row: dict[str, Any], row_result: RowResult, **kwargs: Any) -> None:
        """
        Override to add additional logic. Does nothing by default.

        :param row: A ``dict`` of the import row.

        :param row_result: A ``RowResult`` instance.
          References the persisted ``instance`` as an attribute.

        :param row_number: The row number from the dataset.
        """
        ...
    def after_init_instance(self, instance: _ModelT, new: bool, row: dict[str, Any], **kwargs: Any) -> None: ...
    @overload
    def handle_import_error(self, result: Result, error: Exception, raise_errors: Literal[True]) -> NoReturn: ...
    @overload
    def handle_import_error(self, result: Result, error: Exception, raise_errors: Literal[False] = ...) -> None: ...
    def import_row(self, row: dict[str, Any], instance_loader: BaseInstanceLoader, **kwargs: Any) -> RowResult:
        """
        Imports data from ``tablib.Dataset``. Refer to :doc:`import_workflow`
        for a more complete description of the whole import process.

        :param row: A ``dict`` of the row to import

        :param instance_loader: The instance loader to be used to load the row

        :param using_transactions: If ``using_transactions`` is set, a transaction
            is being used to wrap the import

        :param dry_run: If ``dry_run`` is set, or error occurs, transaction
            will be rolled back.
        """
        ...
    def import_data(
        self,
        dataset: Dataset,
        dry_run: bool = False,
        raise_errors: bool = False,
        use_transactions: bool | None = None,
        collect_failed_rows: bool = False,
        rollback_on_validation_errors: bool = False,
        **kwargs: Any,
    ) -> Result:
        """
        Imports data from ``tablib.Dataset``. Refer to :doc:`import_workflow`
        for a more complete description of the whole import process.

        :param dataset: A ``tablib.Dataset``

        :param raise_errors: Whether errors should be printed to the end user
                             or raised regularly.

        :param use_transactions: If ``True`` the import process will be processed
                                 inside a transaction.

        :param collect_failed_rows: If ``True`` the import process will collect
                                    failed rows.

        :param rollback_on_validation_errors: If both ``use_transactions`` and
                                              ``rollback_on_validation_errors``
                                              are set to ``True``, the import
                                              process will be rolled back in
                                              case of ValidationError.

        :param dry_run: If ``dry_run`` is set, or an error occurs, if a transaction
                        is being used, it will be rolled back.
        """
        ...
    def import_data_inner(
        self,
        dataset: Dataset,
        dry_run: bool,
        raise_errors: bool,
        using_transactions: bool,
        collect_failed_rows: bool,
        **kwargs: Any,
    ) -> Result: ...
    def get_import_order(self) -> tuple[str, ...]: ...
    def get_export_order(self) -> tuple[str, ...]: ...
    def before_export(self, queryset: QuerySet[_ModelT], **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def after_export(self, queryset: QuerySet[_ModelT], dataset: Dataset, **kwargs: Any) -> None:
        """Override to add additional logic. Does nothing by default."""
        ...
    def filter_export(self, queryset: QuerySet[_ModelT], **kwargs: Any) -> QuerySet[_ModelT]:
        """Override to filter an export queryset."""
        ...
    def export_field(self, field: Field, instance: _ModelT, **kwargs: Any) -> str: ...
    def get_export_fields(self, selected_fields: Sequence[str] | None = None) -> list[Field]: ...
    def export_resource(self, instance: _ModelT, selected_fields: Sequence[str] | None = None, **kwargs: Any) -> list[str]: ...
    def get_export_headers(self, selected_fields: Sequence[str] | None = None) -> list[str]: ...
    def get_user_visible_headers(self) -> list[str]: ...
    def get_user_visible_fields(self) -> list[str]: ...
    def iter_queryset(self, queryset: QuerySet[_ModelT]) -> Iterator[_ModelT]: ...
    def export(self, queryset: QuerySet[_ModelT] | None = None, **kwargs: Any) -> Dataset:
        """
        Exports a resource.
        :returns: Dataset object.
        """
        ...

class ModelResource(Resource[_ModelT], metaclass=ModelDeclarativeMetaclass):
    """ModelResource is Resource subclass for handling Django models."""
    DEFAULT_RESOURCE_FIELD: ClassVar[type[Field]] = ...
    WIDGETS_MAP: ClassVar[dict[str, type[Widget]]]
    @classmethod
    def get_m2m_widget(cls, field: DjangoField[Any, Any]) -> partial[ManyToManyWidget[Any]]:
        """Prepare widget for m2m field"""
        ...
    @classmethod
    def get_fk_widget(cls, field: DjangoField[Any, Any]) -> partial[ForeignKeyWidget[Any]]:
        """Prepare widget for fk and o2o fields"""
        ...
    @classmethod
    def widget_from_django_field(cls, f: DjangoField[Any, Any], default: type[Widget] = ...) -> type[Widget]:
        """
        Returns the widget that would likely be associated with each
        Django type.

        Includes mapping of Postgres Array field. In the case that
        psycopg2 is not installed, we consume the error and process the field
        regardless.
        """
        ...
    @classmethod
    def widget_kwargs_for_field(cls, field_name: str, django_field: DjangoField[Any, Any]) -> dict[str, Any]:
        """Returns widget kwargs for given field_name."""
        ...
    @classmethod
    def field_from_django_field(cls, field_name: str, django_field: DjangoField[Any, Any], readonly: bool) -> Field:
        """Returns a Resource Field instance for the given Django model field."""
        ...
    def get_queryset(self) -> QuerySet[_ModelT]:
        """
        Returns a queryset of all objects for this model. Override this if you
        want to limit the returned queryset.
        """
        ...
    def init_instance(self, row: dict[str, Any] | None = None) -> _ModelT:
        """Initializes a new Django model."""
        ...
    def after_import(self, dataset: Dataset, result: Result, **kwargs: Any) -> None:
        """Reset the SQL sequences after new objects are imported"""
        ...
    @classmethod
    def get_display_name(cls) -> str: ...

_ResourceT = TypeVar("_ResourceT", bound=Resource[Any])

# HK Type Vars could help type the first overload:
@overload
def modelresource_factory(model: Model, resource_class: type[_ResourceT]) -> _ResourceT:
    """Factory for creating ``ModelResource`` class for given Django model."""
    ...
@overload
def modelresource_factory(model: _ModelT) -> ModelResource[_ModelT]:
    """Factory for creating ``ModelResource`` class for given Django model."""
    ...
