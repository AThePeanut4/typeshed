from _typeshed import Incomplete, SupportsGetItem
from logging import Logger
from typing import Any, Generic, TypeVar
from typing_extensions import TypeAlias

from django.db.models import Model, QuerySet
from django.forms import BaseForm, Form
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic.edit import FormView

from .formats.base_formats import Format
from .resources import Resource

Dataset: TypeAlias = Incomplete  # tablib.Dataset

logger: Logger

_ModelT = TypeVar("_ModelT", bound=Model)

class BaseImportExportMixin(Generic[_ModelT]):
    """
    Base mixin for functionality related to importing and exporting via the Admin
    interface.
    """
    resource_class: type[Resource[_ModelT]]
    resource_classes: SupportsGetItem[int, type[Resource[_ModelT]]]
    @property
    def formats(self) -> list[type[Format]]: ...
    @property
    def export_formats(self) -> list[type[Format]]: ...
    @property
    def import_formats(self) -> list[type[Format]]: ...
    def check_resource_classes(self, resource_classes: SupportsGetItem[int, type[Resource[_ModelT]]]) -> None: ...
    def get_resource_classes(self) -> list[type[Resource[_ModelT]]]:
        """Return subscriptable type (list, tuple, ...) containing resource classes"""
        ...
    def get_resource_kwargs(self, request: HttpRequest, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """
        Return the kwargs which are to be passed to the Resource constructor.
        Can be overridden to provide additional kwarg params.

        :param request: The request object.
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :returns: The Resource kwargs (by default, is the kwargs passed).
        """
        ...
    def get_resource_index(self, form: Form) -> int:
        """
        Return the index of the resource class defined in the form.

        :param form: The form object.
        :returns: The index of the resource as an int.
        """
        ...

class BaseImportMixin(BaseImportExportMixin[_ModelT]):
    def get_import_resource_classes(self) -> list[type[Resource[_ModelT]]]:
        """Returns ResourceClass subscriptable (list, tuple, ...) to use for import."""
        ...
    def get_import_formats(self) -> list[Format]:
        """Returns available import formats."""
        ...
    def get_import_resource_kwargs(self, request: HttpRequest, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def choose_import_resource_class(self, form: Form) -> type[Resource[_ModelT]]: ...

class BaseExportMixin(BaseImportExportMixin[_ModelT]):
    model: Model
    escape_exported_data: bool
    escape_html: bool
    escape_formulae: bool
    @property
    def should_escape_html(self) -> bool: ...
    @property
    def should_escape_formulae(self) -> bool: ...
    def get_export_formats(self) -> list[Format]:
        """Returns available export formats."""
        ...
    def get_export_resource_classes(self) -> list[Resource[_ModelT]]:
        """Returns ResourceClass subscriptable (list, tuple, ...) to use for export."""
        ...
    def choose_export_resource_class(self, form: Form) -> Resource[_ModelT]: ...
    def get_export_resource_kwargs(self, request: HttpRequest, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def get_data_for_export(self, request: HttpRequest, queryset: QuerySet[_ModelT], *args: Any, **kwargs: Any) -> Dataset: ...
    def get_export_filename(self, file_format: Format) -> str: ...

class ExportViewMixin(BaseExportMixin[_ModelT]):
    form_class: type[BaseForm] = ...
    def get_export_data(self, file_format: Format, queryset: QuerySet[_ModelT], *args: Any, **kwargs: Any) -> str | bytes:
        """Returns file_format representation for given queryset."""
        ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...

_FormT = TypeVar("_FormT", bound=BaseForm)

class ExportViewFormMixin(ExportViewMixin[_ModelT], FormView[_FormT]):  # type: ignore[misc]
    def form_valid(self, form: _FormT) -> HttpResponse: ...