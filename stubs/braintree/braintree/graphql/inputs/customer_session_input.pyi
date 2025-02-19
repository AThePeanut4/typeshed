from _typeshed import Incomplete

from braintree.graphql.inputs.phone_input import PhoneInput

class CustomerSessionInput:
    def __init__(
        self,
        email: str | None = None,
        phone: PhoneInput | None = None,
        device_fingerprint_id: str | None = None,
        paypal_app_installed: bool | None = None,
        venmo_app_installed: bool | None = None,
        user_agent: str | None = None,
    ) -> None: ...
    def to_graphql_variables(self) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    def builder(): ...

    class Builder:
        def __init__(self) -> None: ...
        def email(self, email: str): ...
        def phone(self, phone: PhoneInput): ...
        def device_fingerprint_id(self, device_fingerprint_id: str): ...
        def paypal_app_installed(self, paypal_app_installed: bool): ...
        def venmo_app_installed(self, venmo_app_installed: bool): ...
        def user_agent(self, user_agent: str): ...
        def build(self): ...
