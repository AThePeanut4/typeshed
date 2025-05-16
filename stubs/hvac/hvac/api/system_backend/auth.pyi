from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Auth(SystemBackendMixin):
    def list_auth_methods(self):
        """
        List all enabled auth methods.

        Supported methods:
            GET: /sys/auth. Produces: 200 application/json

        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def enable_auth_method(
        self, method_type, description=None, config=None, plugin_name=None, local: bool = False, path=None, **kwargs
    ): ...
    def disable_auth_method(self, path): ...
    def read_auth_method_tuning(self, path): ...
    def tune_auth_method(
        self,
        path,
        default_lease_ttl=None,
        max_lease_ttl=None,
        description=None,
        audit_non_hmac_request_keys=None,
        audit_non_hmac_response_keys=None,
        listing_visibility=None,
        passthrough_request_headers=None,
        **kwargs,
    ):
        """
        Tune configuration parameters for a given auth path.

        This endpoint requires sudo capability on the final path, but the same functionality can be achieved without
        sudo via sys/mounts/auth/[auth-path]/tune.

        Supported methods:
            POST: /sys/auth/{path}/tune. Produces: 204 (empty body)

        :param path: The path the method was mounted on. If not provided, defaults to the value of the "method_type"
            argument.
        :type path: str | unicode
        :param default_lease_ttl: Specifies the default time-to-live. If set on a specific auth path, this overrides the
            global default.
        :type default_lease_ttl: int
        :param max_lease_ttl: The maximum time-to-live. If set on a specific auth path, this overrides the global
            default.
        :type max_lease_ttl: int
        :param description: Specifies the description of the mount. This overrides the current stored value, if any.
        :type description: str | unicode
        :param audit_non_hmac_request_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the
            request data object.
        :type audit_non_hmac_request_keys: array
        :param audit_non_hmac_response_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the
            response data object.
        :type audit_non_hmac_response_keys: list
        :param listing_visibility: Specifies whether to show this mount in the UI-specific listing endpoint. Valid
            values are "unauth" or "".
        :type listing_visibility: list
        :param passthrough_request_headers: List of headers to whitelist and pass from the request to the backend.
        :type passthrough_request_headers: list
        :param kwargs: All dicts are accepted and passed to vault. See your specific secret engine for details on which
            extra key-word arguments you might want to pass.
        :type kwargs: dict
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
