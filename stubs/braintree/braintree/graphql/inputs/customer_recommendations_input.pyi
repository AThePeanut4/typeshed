from _typeshed import Incomplete

from braintree.graphql.enums.recommendations import Recommendations
from braintree.graphql.inputs.customer_session_input import CustomerSessionInput

class CustomerRecommendationsInput:
    """Represents the input to request PayPal customer session recommendations."""
    def __init__(
        self,
        session_id: str,
        recommendations: list[Recommendations],
        merchant_account_id: str | None = None,
        customer: CustomerSessionInput | None = None,
    ) -> None: ...
    def to_graphql_variables(self) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    def builder(session_id: str, recommendations: list[Recommendations]):
        """
        Creates a builder instance for fluent construction of CustomerRecommendationsInput objects.

        Args:
            session_id (str): ID of the customer session for getting recommendations.
            recommendations (List[Recommendations]): List of recommendations to retrieve for the customer session.
        """
        ...

    class Builder:
        def __init__(self, session_id: str, recommendations: list[Recommendations]) -> None: ...
        def merchant_account_id(self, merchant_account_id: str):
            """Sets the merchant account ID."""
            ...
        def customer(self, customer: CustomerSessionInput):
            """Sets the input object representing customer information relevant to the customer session."""
            ...
        def build(self): ...
