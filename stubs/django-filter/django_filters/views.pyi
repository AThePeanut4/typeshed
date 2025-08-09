from _typeshed import Unused
from typing import Any

from django.db.models import Model, QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin, MultipleObjectTemplateResponseMixin

from .constants import ALL_FIELDS
from .filterset import FilterSet

class FilterMixin:
    """A mixin that provides a way to show and handle a FilterSet in a request."""
    filterset_class: type[FilterSet] | None
    filterset_fields = ALL_FIELDS
    strict: bool
    def get_filterset_class(self) -> type[FilterSet] | None:
        """Returns the filterset class to use in this view"""
        ...
    def get_filterset(self, filterset_class: type[FilterSet]) -> FilterSet:
        """Returns an instance of the filterset to be used in this view."""
        ...
    def get_filterset_kwargs(self, filterset_class: type[FilterSet]) -> dict[str, Any]:
        """Returns the keyword arguments for instantiating the filterset."""
        ...
    def get_strict(self) -> bool: ...

class BaseFilterView(FilterMixin, MultipleObjectMixin[Any], View):  # Generic model type
    filterset: FilterSet
    object_list: QuerySet[Any]  # Filtered objects of any model type

    def get(self, request: HttpRequest, *args: Unused, **kwargs: Unused) -> HttpResponse: ...

class FilterView(MultipleObjectTemplateResponseMixin, BaseFilterView):
    """
    Render some list of objects with filter, set by `self.model` or
    `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    """
    template_name_suffix: str

def object_filter(
    request: HttpRequest,
    model: type[Model] | None = None,
    queryset: QuerySet[Any] | None = None,  # Base queryset for any model
    template_name: str | None = None,
    extra_context: dict[str, Any] | None = None,  # Template context values vary
    context_processors: list[Any] | None = None,  # Context processors vary by implementation
    filter_class: type[FilterSet] | None = None,
) -> HttpResponse: ...
