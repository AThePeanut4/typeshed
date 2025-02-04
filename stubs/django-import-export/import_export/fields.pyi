from collections.abc import Callable, Mapping
from typing import Any, ClassVar

from django.db.models import Model
from django.db.models.fields import NOT_PROVIDED

from .widgets import Widget

class Field:
    """
    Field represent mapping between `object` field and representation of
    this field.

    :param attribute: A string of either an instance attribute or callable off
        the object.

    :param column_name: Lets you provide a name for the column that represents
        this field in the export.

    :param widget: Defines a widget that will be used to represent this
        field's data in the export, or transform the value during import.

    :param readonly: A Boolean which defines if this field will be ignored
        during import.

    :param default: This value will be returned by
        :meth:`~import_export.fields.Field.clean` if this field's widget did
        not return an adequate value.

    :param saves_null_values: Controls whether null values are saved on the object
    :param dehydrate_method: Lets you choose your own method for dehydration rather
        than using `dehydrate_{field_name}` syntax.
    :param m2m_add: changes save of this field to add the values, if they do not exist,
        to a ManyToMany field instead of setting all values.  Only useful if field is
        a ManyToMany field.
    """
    empty_values: ClassVar[list[str | None]]
    attribute: str | None
    default: type[NOT_PROVIDED] | Callable[[], Any] | Any
    column_name: str | None
    widget: Widget
    readonly: bool
    saves_null_values: bool
    dehydrate_method: str
    m2m_add: bool
    def __init__(
        self,
        attribute: str | None = None,
        column_name: str | None = None,
        widget: Widget | None = None,
        default: type[NOT_PROVIDED] | Callable[[], Any] | Any = ...,
        readonly: bool = False,
        saves_null_values: bool = True,
        dehydrate_method: str | None = None,
        m2m_add: bool = False,
    ) -> None: ...
    def clean(self, row: Mapping[str, Any], **kwargs: Any) -> Any: ...
    def get_value(self, instance: Model) -> Any: ...
    def save(self, instance: Model, row: Mapping[str, Any], is_m2m: bool = False, **kwargs: Any) -> None: ...
    def export(self, instance: Model, **kwargs: Any) -> str: ...
    def get_dehydrate_method(self, field_name: str | None = None) -> str: ...
