from _typeshed import Incomplete

from braintree.graphql.enums import RecommendedPaymentOption

class PaymentOptions:
    """Represents the payment method and priority associated with a PayPal customer session."""
    payment_option: Incomplete
    recommended_priority: Incomplete
    def __init__(self, payment_option: RecommendedPaymentOption, recommended_priority: int) -> None: ...
