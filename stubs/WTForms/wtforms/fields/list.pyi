from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any, Generic, TypeVar

from wtforms.fields.core import Field, UnboundField, _FormT, _Validator, _Widget
from wtforms.form import BaseForm
from wtforms.meta import DefaultMeta, _SupportsGettextAndNgettext

__all__ = ("FieldList",)

_BoundFieldT = TypeVar("_BoundFieldT", bound=Field)

class FieldList(Field, Generic[_BoundFieldT]):
    """
    Encapsulate an ordered list of multiple instances of the same field type,
    keeping data as a list.

    >>> authors = FieldList(StringField('Name', [validators.DataRequired()]))

    :param unbound_field:
        A partially-instantiated field definition, just like that would be
        defined on a form directly.
    :param min_entries:
        if provided, always have at least this many entries on the field,
        creating blank ones if the provided input does not specify a sufficient
        amount.
    :param max_entries:
        accept no more than this many entries as input, even if more exist in
        formdata.
    :param separator:
        A string which will be suffixed to this field's name to create the
        prefix to enclosed list entries. The default is fine for most uses.
    """
    unbound_field: UnboundField[_BoundFieldT]
    min_entries: int
    max_entries: int | None
    last_index: int
    entries: list[_BoundFieldT]
    object_data: Iterable[Any]
    # NOTE: This depends on the shape of errors of the bound field, which usually should
    #       be a `Sequence[Sequence[str]]`, but can be `Sequence[_FormErrors]` for `FormField`
    #       we could model this with a fake descriptor with overloads for `FieldList[FormField]`
    #       but it might not be worth the hassle, for now we'll just leave it lax
    errors: Sequence[Any]
    def __init__(
        self: FieldList[_BoundFieldT],  # pyright: ignore[reportInvalidTypeVarUse]  #11780
        # because of our workaround we need to accept Field as well
        unbound_field: UnboundField[_BoundFieldT] | _BoundFieldT,
        label: str | None = None,
        validators: tuple[_Validator[_FormT, _BoundFieldT], ...] | list[Any] | None = None,
        min_entries: int = 0,
        max_entries: int | None = None,
        separator: str = "-",
        default: Iterable[Any] | Callable[[], Iterable[Any]] = (),
        *,
        description: str = "",
        id: str | None = None,
        widget: _Widget[FieldList[Any]] | None = None,
        render_kw: dict[str, Any] | None = None,
        name: str | None = None,
        _form: BaseForm | None = None,
        _prefix: str = "",
        _translations: _SupportsGettextAndNgettext | None = None,
        _meta: DefaultMeta | None = None,
    ) -> None: ...
    def append_entry(self, data: Any = ...) -> _BoundFieldT:
        """
        Create a new entry with optional default data.

        Entries added in this way will *not* receive formdata however, and can
        only receive object data.
        """
        ...
    def pop_entry(self) -> _BoundFieldT:
        """Removes the last entry from the list and returns it."""
        ...
    def __iter__(self) -> Iterator[_BoundFieldT]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> _BoundFieldT: ...
    @property
    def data(self) -> list[Any]: ...
