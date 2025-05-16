from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Init(SystemBackendMixin):
    def read_init_status(self):
        """
        Read the initialization status of Vault.

        Supported methods:
            GET: /sys/init. Produces: 200 application/json

        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def is_initialized(self):
        """
        Determine is Vault is initialized or not.

        :return: True if Vault is initialized, False otherwise.
        :rtype: bool
        """
        ...
    def initialize(
        self,
        secret_shares=None,
        secret_threshold=None,
        pgp_keys=None,
        root_token_pgp_key=None,
        stored_shares=None,
        recovery_shares=None,
        recovery_threshold=None,
        recovery_pgp_keys=None,
    ): ...
