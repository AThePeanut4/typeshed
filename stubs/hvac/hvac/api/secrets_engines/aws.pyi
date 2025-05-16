from hvac.api.vault_api_base import VaultApiBase

class Aws(VaultApiBase):
    """
    AWS Secrets Engine (API).

    Reference: https://www.vaultproject.io/api/secret/aws/index.html
    """
    def configure_root_iam_credentials(
        self, access_key, secret_key, region=None, iam_endpoint=None, sts_endpoint=None, max_retries=None, mount_point="aws"
    ): ...
    def rotate_root_iam_credentials(self, mount_point="aws"): ...
    def configure_lease(self, lease, lease_max, mount_point="aws"): ...
    def read_lease_config(self, mount_point="aws"): ...
    def create_or_update_role(
        self,
        name,
        credential_type,
        policy_document=None,
        default_sts_ttl=None,
        max_sts_ttl=None,
        role_arns=None,
        policy_arns=None,
        legacy_params: bool = False,
        iam_tags=None,
        mount_point="aws",
    ):
        """
        Create or update the role with the given name.

        If a role with the name does not exist, it will be created. If the role exists, it will be updated with the new
        attributes.

        Supported methods:
            POST: /{mount_point}/roles/{name}. Produces: 204 (empty body)

        :param name: Specifies the name of the role to create. This is part of the request URL.
        :type name: str | unicode
        :param credential_type: Specifies the type of credential to be used when retrieving credentials from the role.
            Must be one of iam_user, assumed_role, or federation_token.
        :type credential_type: str | unicode
        :param policy_document: The IAM policy document for the role. The behavior depends on the credential type. With
            iam_user, the policy document will be attached to the IAM user generated and augment the permissions the IAM
            user has. With assumed_role and federation_token, the policy document will act as a filter on what the
            credentials can do.
        :type policy_document: dict | str | unicode
        :param default_sts_ttl: The default TTL for STS credentials. When a TTL is not specified when STS credentials
            are requested, and a default TTL is specified on the role, then this default TTL will be used. Valid only
            when credential_type is one of assumed_role or federation_token.
        :type default_sts_ttl: str | unicode
        :param max_sts_ttl: The max allowed TTL for STS credentials (credentials TTL are capped to max_sts_ttl). Valid
            only when credential_type is one of assumed_role or federation_token.
        :type max_sts_ttl: str | unicode
        :param role_arns: Specifies the ARNs of the AWS roles this Vault role is allowed to assume. Required when
            credential_type is assumed_role and prohibited otherwise. This is a comma-separated string or JSON array.
            String types supported for Vault legacy parameters.
        :type role_arns: list | str | unicode
        :param policy_arns: Specifies the ARNs of the AWS managed policies to be attached to IAM users when they are
            requested. Valid only when credential_type is iam_user. When credential_type is iam_user, at least one of
            policy_arns or policy_document must be specified. This is a comma-separated string or JSON array.
        :type policy_arns: list
        :param legacy_params: Flag to send legacy (Vault versions < 0.11.0) parameters in the request. When this is set
            to True, policy_document and policy_arns are the only parameters used from this method.
        :type legacy_params: bool
        :param iam_tags: A list of strings representing a key/value pair to be used for any IAM user that is created by
            this role. Format is a key and value separated by an =.
        :type iam_tags: list
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def read_role(self, name, mount_point="aws"):
        """
        Query an existing role by the given name.

        If the role does not exist, a 404 is returned.

        Supported methods:
            GET: /{mount_point}/roles/{name}. Produces: 200 application/json

        :param name: Specifies the name of the role to read. This is part of the request URL.
        :type name: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def list_roles(self, mount_point="aws"):
        """
        List all existing roles in the secrets engine.

        Supported methods:
            LIST: /{mount_point}/roles. Produces: 200 application/json

        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def delete_role(self, name, mount_point="aws"):
        """
        Delete an existing role by the given name.

        If the role does not exist, a 404 is returned.

        Supported methods:
            DELETE: /{mount_point}/roles/{name}. Produces: 204 (empty body)

        :param name: the name of the role to delete. This
            is part of the request URL.
        :type name: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def generate_credentials(
        self, name, role_arn=None, ttl=None, endpoint: str = "creds", mount_point="aws", role_session_name=None
    ): ...
