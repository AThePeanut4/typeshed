from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Namespace(SystemBackendMixin):
    def create_namespace(self, path):
        """
        Create a namespace at the given path.

        Supported methods:
            POST: /sys/namespaces/{path}. Produces: 200 application/json

        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def list_namespaces(self):
        """
        Lists all the namespaces.

        Supported methods:
            LIST: /sys/namespaces. Produces: 200 application/json

        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def delete_namespace(self, path):
        """
        Delete a namespaces. You cannot delete a namespace with existing child namespaces.

        Supported methods:
            DELETE: /sys/namespaces. Produces: 204 (empty body)

        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
