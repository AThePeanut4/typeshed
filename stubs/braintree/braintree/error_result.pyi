from _typeshed import Incomplete
from typing import Literal

from braintree.credit_card_verification import CreditCardVerification
from braintree.errors import Errors
from braintree.plan import Plan
from braintree.subscription import Subscription
from braintree.transaction import Transaction

class ErrorResult:
    """
    An instance of this class is returned from most operations when there is a validation error.  Call :func:`errors` to get the collection of errors::

        error_result = Transaction.sale({})
        assert(error_result.is_success == False)
        assert(error_result.errors.for_object("transaction").on("amount")[0].code == ErrorCodes.Transaction.AmountIsRequired)

    Errors can be nested at different levels.  For example, creating a transaction with a credit card can have errors at the transaction level as well as the credit card level.  :func:`for_object` returns the :class:`ValidationErrorCollection <braintree.validation_error_collection.ValidationErrorCollection>` for the errors at that level.  For example::

        error_result = Transaction.sale({"credit_card": {"number": "invalid"}})
        assert(error_result.errors.for_object("transaction").for_object("credit_card").on("number")[0].code == ErrorCodes.CreditCard.NumberHasInvalidLength)
    """
    params: Incomplete
    errors: Errors
    message: Incomplete
    credit_card_verification: CreditCardVerification | None
    transaction: Transaction
    subscription: Subscription
    merchant_account: Plan
    def __init__(self, gateway, attributes: dict[str, Incomplete]) -> None: ...
    @property
    def is_success(self) -> Literal[False]:
        """Returns whether the result from the gateway is a successful response. """
        ...
