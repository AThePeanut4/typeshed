from collections.abc import Mapping
from datetime import datetime
from typing import Any, ClassVar, Generic, TypeVar

from django.db.models import Model, QuerySet

def format_datetime(value: datetime, datetime_format: str) -> str: ...

class Widget:
    """
    A Widget takes care of converting between import and export representations.

    This is achieved by the two methods,
    :meth:`~import_export.widgets.Widget.clean` and
    :meth:`~import_export.widgets.Widget.render`.
    """
    def clean(self, value: Any, row: Mapping[str, Any] | None = None, **kwargs: Any) -> Any:
        """
        Returns an appropriate Python object for an imported value.

        For example, if you import a value from a spreadsheet,
        :meth:`~import_export.widgets.Widget.clean` handles conversion
        of this value into the corresponding Python object.

        Numbers or dates can be *cleaned* to their respective data types and
        don't have to be imported as Strings.
        """
        ...
    def render(self, value: Any, obj: Model | None = None) -> Any:
        """
        Returns an export representation of a Python value.

        For example, if you have an object you want to export,
        :meth:`~import_export.widgets.Widget.render` takes care of converting
        the object's field to a value that can be written to a spreadsheet.
        """
        ...

class NumberWidget(Widget):
    """
    Widget for converting numeric fields.

    :param coerce_to_string: If True, render will return a string representation
        of the value (None is returned as ""), otherwise the value is returned.
    """
    coerce_to_string: bool
    def __init__(self, coerce_to_string: bool = False) -> None: ...
    def is_empty(self, value: Any) -> bool: ...
    def render(self, value: Any, obj: Model | None = None) -> Any: ...

class FloatWidget(NumberWidget):
    """Widget for converting float fields."""
    ...
class IntegerWidget(NumberWidget):
    """Widget for converting integer fields."""
    ...
class DecimalWidget(NumberWidget):
    """Widget for converting decimal fields."""
    ...

class CharWidget(Widget):
    """
    Widget for converting text fields.

    :param coerce_to_string: If True, the value returned by clean() is cast to a
      string.
    :param allow_blank:  If True, and if coerce_to_string is True, then clean() will
      return null values as empty strings, otherwise as null.
    """
    coerce_to_string: bool
    allow_blank: bool
    def __init__(self, coerce_to_string: bool = False, allow_blank: bool = False) -> None: ...

class BooleanWidget(Widget):
    """
    Widget for converting boolean fields.

    The widget assumes that ``True``, ``False``, and ``None`` are all valid
    values, as to match Django's `BooleanField
    <https://docs.djangoproject.com/en/dev/ref/models/fields/#booleanfield>`_.
    That said, whether the database/Django will actually accept NULL values
    will depend on if you have set ``null=True`` on that Django field.

    While the BooleanWidget is set up to accept as input common variations of
    "True" and "False" (and "None"), you may need to munge less common values
    to ``True``/``False``/``None``. Probably the easiest way to do this is to
    override the :func:`~import_export.resources.Resource.before_import_row`
    function of your Resource class. A short example::

        from import_export import fields, resources, widgets

        class BooleanExample(resources.ModelResource):
            warn = fields.Field(widget=widgets.BooleanWidget())

            def before_import_row(self, row, row_number=None, **kwargs):
                if "warn" in row.keys():
                    # munge "warn" to "True"
                    if row["warn"] in ["warn", "WARN"]:
                        row["warn"] = True

                return super().before_import_row(row, row_number, **kwargs)
    """
    TRUE_VALUES: ClassVar[list[str | int | bool]]
    FALSE_VALUES: ClassVar[list[str | int | bool]]
    NULL_VALUES: ClassVar[list[str | None]]

class DateWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter. If none is set, either
    ``settings.DATE_INPUT_FORMATS`` or ``"%Y-%m-%d"`` is used.
    """
    formats: tuple[str, ...]
    def __init__(self, format: str | None = None) -> None: ...

class DateTimeWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter. If none is set, either
    ``settings.DATETIME_INPUT_FORMATS`` or ``"%Y-%m-%d %H:%M:%S"`` is used.
    """
    formats: tuple[str, ...]
    def __init__(self, format: str | None = None) -> None: ...

class TimeWidget(Widget):
    """
    Widget for converting time fields.

    Takes optional ``format`` parameter. If none is set, either
    ``settings.DATETIME_INPUT_FORMATS`` or ``"%H:%M:%S"`` is used.
    """
    formats: tuple[str, ...]
    def __init__(self, format: str | None = None) -> None: ...

class DurationWidget(Widget):
    """Widget for converting time duration fields."""
    ...

class SimpleArrayWidget(Widget):
    """
    Widget for an Array field. Can be used for Postgres' Array field.

    :param separator: Defaults to ``','``
    """
    separator: str
    def __init__(self, separator: str | None = None) -> None: ...

class JSONWidget(Widget):
    """
    Widget for a JSON object
    (especially required for jsonb fields in PostgreSQL database.)

    :param value: Defaults to JSON format.
    The widget covers two cases: Proper JSON string with double quotes, else it
    tries to use single quotes and then convert it to proper JSON.
    """
    ...

_ModelT = TypeVar("_ModelT", bound=Model)

class ForeignKeyWidget(Widget, Generic[_ModelT]):
    """
    Widget for a ``ForeignKey`` field which looks up a related model using
    either the PK or a user specified field that uniquely identifies the
    instance in both export and import.

    The lookup field defaults to using the primary key (``pk``) as lookup
    criterion but can be customized to use any field on the related model.

    Unlike specifying a related field in your resource like so…

    ::

        class Meta:
            fields = ('author__name',)

    …using a :class:`~import_export.widgets.ForeignKeyWidget` has the
    advantage that it can not only be used for exporting, but also importing
    data with foreign key relationships.

    Here's an example on how to use
    :class:`~import_export.widgets.ForeignKeyWidget` to lookup related objects
    using ``Author.name`` instead of ``Author.pk``::

        from import_export import fields, resources
        from import_export.widgets import ForeignKeyWidget

        class BookResource(resources.ModelResource):
            author = fields.Field(
                column_name='author',
                attribute='author',
                widget=ForeignKeyWidget(Author, 'name'))

            class Meta:
                fields = ('author',)

    :param model: The Model the ForeignKey refers to (required).
    :param field: A field on the related model used for looking up a particular
        object.
    :param use_natural_foreign_keys: Use natural key functions to identify
        related object, default to False
    """
    model: _ModelT
    field: str
    use_natural_foreign_keys: bool
    def __init__(self, model: _ModelT, field: str = "pk", use_natural_foreign_keys: bool = False, **kwargs: Any) -> None: ...
    def get_queryset(self, value: Any, row: Mapping[str, Any], *args: Any, **kwargs: Any) -> QuerySet[_ModelT]:
        """
        Returns a queryset of all objects for this Model.

        Overwrite this method if you want to limit the pool of objects from
        which the related object is retrieved.

        :param value: The field's value in the datasource.
        :param row: The datasource's current row.

        As an example; if you'd like to have ForeignKeyWidget look up a Person
        by their pre- **and** lastname column, you could subclass the widget
        like so::

            class FullNameForeignKeyWidget(ForeignKeyWidget):
                def get_queryset(self, value, row, *args, **kwargs):
                    return self.model.objects.filter(
                        first_name__iexact=row["first_name"],
                        last_name__iexact=row["last_name"]
                    )
        """
        ...

class ManyToManyWidget(Widget, Generic[_ModelT]):
    """
    Widget that converts between representations of a ManyToMany relationships
    as a list and an actual ManyToMany field.

    :param model: The model the ManyToMany field refers to (required).
    :param separator: Defaults to ``','``.
    :param field: A field on the related model. Default is ``pk``.
    """
    model: _ModelT
    separator: str
    field: str
    def __init__(self, model: _ModelT, separator: str | None = None, field: str | None = None, **kwargs: Any) -> None: ...
