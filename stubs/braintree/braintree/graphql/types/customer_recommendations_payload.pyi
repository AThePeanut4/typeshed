from typing import Any

from braintree.graphql.unions.customer_recommendations import CustomerRecommendations

class CustomerRecommendationsPayload:
    """Represents the customer recommendations information associated with a PayPal customer session."""
    is_in_paypal_network: bool | None
    recommendations: CustomerRecommendations | None
    def __init__(
        self,
        is_in_paypal_network: bool | None = None,
        recommendations: CustomerRecommendations | None = None,
        response: dict[str, Any] | None = None,
    ): ...
