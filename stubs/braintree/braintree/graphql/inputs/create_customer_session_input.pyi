from _typeshed import Incomplete

from braintree.graphql.inputs.customer_session_input import CustomerSessionInput

class CreateCustomerSessionInput:
    """Represents the input to request the creation of a PayPal customer session."""
    def __init__(
        self,
        merchant_account_id: str | None = None,
        session_id: str | None = None,
        customer: CustomerSessionInput | None = None,
        domain: str | None = None,
    ) -> None: ...
    def to_graphql_variables(self) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    def builder():
        """Creates a builder instance for fluent construction of CreateCustomerSessionInput objects."""
        ...

    class Builder:
        def __init__(self) -> None: ...
        def merchant_account_id(self, merchant_account_id: str):
            """Sets the merchant account ID."""
            ...
        def session_id(self, session_id: str):
            """Sets the customer session ID."""
            ...
        def customer(self, customer: str):
            """Sets the input object representing customer information relevant to the customer session."""
            ...
        def domain(self, domain: str):
            """Sets the customer domain."""
            ...
        def build(self): ...
