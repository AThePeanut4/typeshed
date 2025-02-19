from _typeshed import Incomplete

from braintree.graphql.inputs.customer_session_input import CustomerSessionInput

class UpdateCustomerSessionInput:
    """Represents the input to request an update to a PayPal customer session."""
    def __init__(
        self, session_id: str, merchant_account_id: str | None = None, customer: CustomerSessionInput | None = None
    ) -> None: ...
    def to_graphql_variables(self) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    def builder(session_id: str):
        """
        Creates a builder instance for fluent construction of UpdateCustomerSessionInput objects.

        Args:
            session_id (str): ID of the customer session to be updated.
        """
        ...

    class Builder:
        def __init__(self, session_id: str) -> None: ...
        def merchant_account_id(self, merchant_account_id):
            """Sets the merchant account ID."""
            ...
        def customer(self, customer):
            """Sets the input object representing customer information relevant to the customer session."""
            ...
        def build(self): ...
