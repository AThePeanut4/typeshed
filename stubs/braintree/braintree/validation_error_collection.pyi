from _typeshed import Incomplete

class ValidationErrorCollection:
    """
    A class representing a collection of validation errors.

    For more information on ValidationErrors, see https://developer.paypal.com/braintree/docs/reference/general/validation-errors/overview/python
    """
    data: dict[str, Incomplete]
    def __init__(self, data: Incomplete | None = None) -> None: ...
    @property
    def deep_errors(self):
        """Return all :class:`ValidationErrors <braintree.validation_error.ValidationError>`, including nested errors."""
        ...
    def for_index(self, index): ...
    def for_object(self, nested_key):
        """
        Returns a :class:`ValidationErrorCollection <braintree.validation_error_collection.ValidationErrorCollection>`

        It represents the errors at the nested level:::

            error_result = Transaction.sale({"credit_card": {"number": "invalid"}})
            print error_result.errors.for_object("transaction").for_object("credit_card").on("number")[0].code
        """
        ...
    def on(self, attribute):
        """
        Returns the list of errors

        Restricted to a given attribute::

            error_result = Transaction.sale({"credit_card": {"number": "invalid"}})
            print [ error.code for error in error_result.errors.for_object("transaction").for_object("credit_card").on("number") ]
        """
        ...
    @property
    def deep_size(self):
        """Returns the number of errors on this object and any nested objects."""
        ...
    @property
    def errors(self):
        """Returns a list of :class:`ValidationError <braintree.validation_error.ValidationError>` objects."""
        ...
    @property
    def size(self):
        """Returns the number of errors on this object, without counting nested errors."""
        ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
