"""Kubernetes methods module."""

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Kubernetes(VaultApiBase):
    """
    Kubernetes Auth Method (API).

    Reference: https://www.vaultproject.io/api/auth/kubernetes/index.html
    """
    def configure(
        self,
        kubernetes_host,
        kubernetes_ca_cert=None,
        token_reviewer_jwt=None,
        pem_keys=None,
        issuer=None,
        mount_point="kubernetes",
        disable_local_ca_jwt: bool = False,
    ):
        """
        Configure the connection parameters for Kubernetes.

        This path honors the distinction between the create and update capabilities inside ACL policies.

        Supported methods:
            POST: /auth/{mount_point}/config. Produces: 204 (empty body)

        :param kubernetes_host: Host must be a host string, a host:port pair, or a URL to the base of the
            Kubernetes API server. Example: https://k8s.example.com:443
        :type kubernetes_host: str | unicode
        :param kubernetes_ca_cert: PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
            NOTE: Every line must end with a newline: 

        :type kubernetes_ca_cert: str | unicode
        :param token_reviewer_jwt: A service account JWT used to access the TokenReview API to validate other
            JWTs during login. If not set the JWT used for login will be used to access the API.
        :type token_reviewer_jwt: str | unicode
        :param pem_keys: Optional list of PEM-formatted public keys or certificates used to verify the signatures of
            Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every
            installation of Kubernetes exposes these keys.
        :type pem_keys: list
        :param issuer: Optional JWT issuer.
        :type token_reviewer_jwt: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :param disable_local_ca_jwt: Disable defaulting to the local CA cert and service account JWT
        :type disable_local_ca_jwt: bool
        :return: The response of the configure_method request.
        :rtype: requests.Response
        """
        ...
    def read_config(self, mount_point="kubernetes"):
        """
        Return the previously configured config, including credentials.

        Supported methods:
            GET: /auth/{mount_point}/config. Produces: 200 application/json

        :param mount_point: The "path" the kubernetes auth method was mounted on.
        :type mount_point: str | unicode
        :return: The data key from the JSON response of the request.
        :rtype: dict
        """
        ...
    def create_role(
        self,
        name,
        bound_service_account_names,
        bound_service_account_namespaces,
        ttl=None,
        max_ttl=None,
        period=None,
        policies=None,
        token_type: str = "",
        mount_point="kubernetes",
        alias_name_source=None,
        audience: str | None = None,
    ): ...
    def read_role(self, name, mount_point="kubernetes"): ...
    def list_roles(self, mount_point="kubernetes"): ...
    def delete_role(self, name, mount_point="kubernetes"): ...
    def login(self, role, jwt, use_token: bool = True, mount_point="kubernetes"): ...
