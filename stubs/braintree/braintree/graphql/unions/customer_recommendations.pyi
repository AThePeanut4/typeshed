from _typeshed import Incomplete

from braintree.graphql.types.payment_options import PaymentOptions

class CustomerRecommendations:
    """A union of all possible customer recommendations associated with a PayPal customer session."""
    payment_options: Incomplete
    def __init__(self, payment_options: list[PaymentOptions]) -> None: ...
