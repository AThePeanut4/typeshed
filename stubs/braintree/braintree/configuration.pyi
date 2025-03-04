from _typeshed import Incomplete

class Configuration:
    """
    A class representing the configuration of your Braintree account.
    You must call configure before any other Braintree operations. ::

        braintree.Configuration.configure(
            braintree.Environment.Sandbox,
            "your_merchant_id",
            "your_public_key",
            "your_private_key"
        )
    """
    @staticmethod
    def configure(environment, merchant_id, public_key, private_key, **kwargs) -> None: ...
    @staticmethod
    def for_partner(environment, partner_id, public_key, private_key, **kwargs): ...
    @staticmethod
    def gateway(): ...
    @staticmethod
    def instantiate(): ...
    @staticmethod
    def api_version(): ...
    @staticmethod
    def graphql_api_version(): ...
    environment: Incomplete
    merchant_id: Incomplete
    public_key: Incomplete
    private_key: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    access_token: Incomplete
    timeout: Incomplete
    wrap_http_exceptions: Incomplete
    def __init__(
        self,
        environment: Incomplete | None = None,
        merchant_id: Incomplete | None = None,
        public_key: Incomplete | None = None,
        private_key: Incomplete | None = None,
        client_id: Incomplete | None = None,
        client_secret: Incomplete | None = None,
        access_token: Incomplete | None = None,
        *args,
        **kwargs,
    ) -> None: ...
    def base_merchant_path(self): ...
    def base_url(self): ...
    def graphql_base_url(self): ...
    def http(self): ...
    def graphql_client(self): ...
    def http_strategy(self): ...
    def has_client_credentials(self): ...
    def assert_has_client_credentials(self) -> None: ...
    def has_access_token(self): ...
