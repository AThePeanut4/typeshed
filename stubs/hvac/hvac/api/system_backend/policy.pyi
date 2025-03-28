from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Policy(SystemBackendMixin):
    def list_policies(self):
        """
        List all configured policies.

        Supported methods:
            GET: /sys/policy. Produces: 200 application/json

        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def read_policy(self, name):
        """
        Retrieve the policy body for the named policy.

        Supported methods:
            GET: /sys/policy/{name}. Produces: 200 application/json

        :param name: The name of the policy to retrieve.
        :type name: str | unicode
        :return: The response of the request
        :rtype: dict
        """
        ...
    def create_or_update_policy(self, name, policy, pretty_print: bool = True):
        """
        Add a new or update an existing policy.

        Once a policy is updated, it takes effect immediately to all associated users.

        Supported methods:
            PUT: /sys/policy/{name}. Produces: 204 (empty body)

        :param name: Specifies the name of the policy to create.
        :type name: str | unicode
        :param policy: Specifies the policy document.
        :type policy: str | unicode | dict
        :param pretty_print: If True, and provided a dict for the policy argument, send the policy JSON to Vault with
            "pretty" formatting.
        :type pretty_print: bool
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def delete_policy(self, name):
        """
        Delete the policy with the given name.

        This will immediately affect all users associated with this policy.

        Supported methods:
            DELETE: /sys/policy/{name}. Produces: 204 (empty body)

        :param name: Specifies the name of the policy to delete.
        :type name: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
