"""Support for "Auth"-related System Backend Methods."""

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
    ):
        """
        Enable a new auth method.

        After enabling, the auth method can be accessed and configured via the auth path specified as part of the URL.
        This auth path will be nested under the auth prefix.

        Supported methods:
            POST: /sys/auth/{path}. Produces: 204 (empty body)

        :param method_type: The name of the authentication method type, such as "github" or "token".
        :type method_type: str | unicode
        :param description: A human-friendly description of the auth method.
        :type description: str | unicode
        :param config: Configuration options for this auth method. These are the possible values:

            * **default_lease_ttl**: The default lease duration, specified as a string duration like "5s" or "30m".
            * **max_lease_ttl**: The maximum lease duration, specified as a string duration like "5s" or "30m".
            * **audit_non_hmac_request_keys**: Comma-separated list of keys that will not be HMAC'd by audit devices in
              the request data object.
            * **audit_non_hmac_response_keys**: Comma-separated list of keys that will not be HMAC'd by audit devices in
              the response data object.
            * **listing_visibility**: Specifies whether to show this mount in the UI-specific listing endpoint.
            * **passthrough_request_headers**: Comma-separated list of headers to whitelist and pass from the request to
              the backend.
        :type config: dict
        :param plugin_name: The name of the auth plugin to use based from the name in the plugin catalog. Applies only
            to plugin methods.
        :type plugin_name: str | unicode
        :param local: <Vault enterprise only> Specifies if the auth method is a local only. Local auth methods are not
            replicated nor (if a secondary) removed by replication.
        :type local: bool
        :param path: The path to mount the method on. If not provided, defaults to the value of the "method_type"
            argument.
        :type path: str | unicode
        :param kwargs: All dicts are accepted and passed to vault. See your specific secret engine for details on which
            extra key-word arguments you might want to pass.
        :type kwargs: dict
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def disable_auth_method(self, path):
        """
        Disable the auth method at the given auth path.

        Supported methods:
            DELETE: /sys/auth/{path}. Produces: 204 (empty body)

        :param path: The path the method was mounted on. If not provided, defaults to the value of the "method_type"
            argument.
        :type path: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def read_auth_method_tuning(self, path):
        """
        Read the given auth path's configuration.

        This endpoint requires sudo capability on the final path, but the same functionality can be achieved without
        sudo via sys/mounts/auth/[auth-path]/tune.

        Supported methods:
            GET: /sys/auth/{path}/tune. Produces: 200 application/json

        :param path: The path the method was mounted on. If not provided, defaults to the value of the "method_type"
            argument.
        :type path: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
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
