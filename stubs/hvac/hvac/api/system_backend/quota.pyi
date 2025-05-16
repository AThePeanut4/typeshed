from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Quota(SystemBackendMixin):
    def read_quota(self, name):
        """
        Read quota. Only works when calling on the root namespace.

        Supported methods:
            GET: /sys/quotas/rate-limit/:name. Produces: 200 application/json

        :param name: the name of the quota to look up.
        :type name: str | unicode
        :return: JSON response from API request.
        :rtype: requests.Response
        """
        ...
    def list_quotas(self):
        """
        Retrieve a list of quotas by name. Only works when calling on the root namespace.

        Supported methods:
            LIST: /sys/quotas/rate-limit. Produces: 200 application/json

        :return: JSON response from API request.
        :rtype: requests.Response
        """
        ...
    def create_or_update_quota(
        self, name, rate, path=None, interval=None, block_interval=None, role=None, rate_limit_type=None, inheritable=None
    ): ...
    def delete_quota(self, name): ...
