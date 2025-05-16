"""AWS auth method module """

from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

logger: Incomplete

class Aws(VaultApiBase):
    """
    AWS Auth Method (API).

    Reference: https://www.vaultproject.io/api/auth/aws/index.html
    """
    def configure(
        self,
        max_retries=None,
        access_key=None,
        secret_key=None,
        endpoint=None,
        iam_endpoint=None,
        sts_endpoint=None,
        iam_server_id_header_value=None,
        mount_point: str = "aws",
        sts_region: str | None = None,
    ):
        """
        Configure the credentials required to perform API calls to AWS as well as custom endpoints to talk to AWS API.

        The instance identity document fetched from the PKCS#7 signature will provide the EC2 instance ID.
        The credentials configured using this endpoint will be used to query the status of the instances via
        DescribeInstances API. If static credentials are not provided using this endpoint, then the credentials will be
        retrieved from the environment variables AWS_ACCESS_KEY, AWS_SECRET_KEY and AWS_REGION respectively.
        If the credentials are still not found and if the method is configured on an EC2 instance with metadata querying
        capabilities, the credentials are fetched automatically

        Supported methods:
            POST: /auth/{mount_point}/config Produces: 204 (empty body)

        :param max_retries: Number of max retries the client should use for recoverable errors.
            The default (-1) falls back to the AWS SDK's default behavior
        :type max_retries: int
        :param access_key: AWS Access key with permissions to query AWS APIs. The permissions required depend on the
            specific configurations. If using the iam auth method without inferencing, then no credentials are
            necessary. If using the ec2 auth method or using the iam auth method with inferencing, then these
            credentials need access to ec2:DescribeInstances. If additionally a bound_iam_role is specified, then
            these credentials also need access to iam:GetInstanceProfile. If, however, an alternate sts configuration
            is set for the target account, then the credentials must be permissioned to call sts:AssumeRole on the
            configured role, and that role must have the permissions described here
        :type access_key: str | unicode
        :param secret_key: AWS Secret key with permissions to query AWS APIs
        :type secret_key: str | unicode
        :param endpoint: URL to override the default generated endpoint for making AWS EC2 API calls
        :type endpoint: str | unicode
        :param iam_endpoint: URL to override the default generated endpoint for making AWS IAM API calls
        :type iam_endpoint: str | unicode
        :param sts_endpoint: URL to override the default generated endpoint for making AWS STS API calls
        :type sts_endpoint: str | unicode
        :param iam_server_id_header_value: The value to require in the X-Vault-AWS-IAM-Server-ID header as part of
            GetCallerIdentity requests that are used in the iam auth method. If not set, then no value is required or
            validated. If set, clients must include an X-Vault-AWS-IAM-Server-ID header in the headers of login
            requests, and further this header must be among the signed headers validated by AWS. This is to protect
            against different types of replay attacks, for example a signed request sent to a dev server being resent
            to a production server
        :type iam_server_id_header_value: str | unicode
        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str | unicode
        :param sts_region: Region to override the default region for making AWS STS API calls. Should only be set if
            sts_endpoint is set. If so, should be set to the region in which the custom sts_endpoint resides
        :type sts_region: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def read_config(self, mount_point: str = "aws"):
        """
        Read previously configured AWS access credentials.

        Supported methods:
            GET: /auth/{mount_point}/config. Produces: 200 application/json

        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str | unicode
        :return: The data key from the JSON response of the request.
        :rtype: dict
        """
        ...
    def delete_config(self, mount_point: str = "aws"):
        """
        Delete previously configured AWS access credentials,

        Supported methods:
            DELETE: /auth/{mount_point}/config Produces: 204 (empty body)

        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def configure_identity_integration(
        self,
        iam_alias=None,
        ec2_alias=None,
        mount_point: str = "aws",
        iam_metadata: str | list[str] | None = None,
        ec2_metadata: str | list[str] | None = None,
    ): ...
    def read_identity_integration(self, mount_point: str = "aws"): ...
    def create_certificate_configuration(self, cert_name, aws_public_cert, document_type=None, mount_point: str = "aws"): ...
    def read_certificate_configuration(self, cert_name, mount_point: str = "aws"): ...
    def delete_certificate_configuration(self, cert_name, mount_point: str = "aws"): ...
    def list_certificate_configurations(self, mount_point: str = "aws"): ...
    def create_sts_role(self, account_id, sts_role, mount_point: str = "aws"): ...
    def read_sts_role(self, account_id, mount_point: str = "aws"): ...
    def list_sts_roles(self, mount_point: str = "aws"): ...
    def delete_sts_role(self, account_id, mount_point: str = "aws"): ...
    def configure_identity_whitelist_tidy(self, safety_buffer=None, disable_periodic_tidy=None, mount_point: str = "aws"): ...
    def read_identity_whitelist_tidy(self, mount_point: str = "aws"): ...
    def delete_identity_whitelist_tidy(self, mount_point: str = "aws"): ...
    def configure_role_tag_blacklist_tidy(self, safety_buffer=None, disable_periodic_tidy=None, mount_point: str = "aws"): ...
    def read_role_tag_blacklist_tidy(self, mount_point: str = "aws"): ...
    def delete_role_tag_blacklist_tidy(self, mount_point: str = "aws"): ...
    def create_role(
        self,
        role,
        auth_type=None,
        bound_ami_id=None,
        bound_account_id=None,
        bound_region=None,
        bound_vpc_id=None,
        bound_subnet_id=None,
        bound_iam_role_arn=None,
        bound_iam_instance_profile_arn=None,
        bound_ec2_instance_id=None,
        role_tag=None,
        bound_iam_principal_arn=None,
        inferred_entity_type=None,
        inferred_aws_region=None,
        resolve_aws_unique_ids=None,
        ttl=None,
        max_ttl=None,
        period=None,
        policies=None,
        allow_instance_migration=None,
        disallow_reauthentication=None,
        mount_point: str = "aws",
    ):
        """
        Register a role in the method.

        :param role:
        :param auth_type:
        :param bound_ami_id:
        :param bound_account_id:
        :param bound_region:
        :param bound_vpc_id:
        :param bound_subnet_id:
        :param bound_iam_role_arn:
        :param bound_iam_instance_profile_arn:
        :param bound_ec2_instance_id:
        :param role_tag:
        :param bound_iam_principal_arn:
        :param inferred_entity_type:
        :param inferred_aws_region:
        :param resolve_aws_unique_ids:
        :param ttl:
        :param max_ttl:
        :param period:
        :param policies:
        :param allow_instance_migration:
        :param disallow_reauthentication:
        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def read_role(self, role, mount_point: str = "aws"):
        """
        Returns the previously registered role configuration

        :param role:
        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def list_roles(self, mount_point: str = "aws"):
        """
        Lists all the roles that are registered with the method

        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def delete_role(self, role, mount_point: str = "aws"):
        """
        Deletes the previously registered role

        :param role:
        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def create_role_tags(
        self,
        role,
        policies=None,
        max_ttl=None,
        instance_id=None,
        allow_instance_migration=None,
        disallow_reauthentication=None,
        mount_point: str = "aws",
    ):
        """
        Create a role tag on the role, which helps in restricting the capabilities that are set on the role.

        Role tags are not tied to any specific ec2 instance unless specified explicitly using the
        instance_id parameter. By default, role tags are designed to be used across all instances that
        satisfies the constraints on the role. Regardless of which instances have role tags on them, capabilities
        defined in a role tag must be a strict subset of the given role's capabilities. Note that, since adding
        and removing a tag is often a widely distributed privilege, care needs to be taken to ensure that the
        instances are attached with correct tags to not let them gain more privileges than what were intended.
        If a role tag is changed, the capabilities inherited by the instance will be those defined on the new role
        tag. Since those must be a subset of the role capabilities, the role should never provide more capabilities
        than any given instance can be allowed to gain in a worst-case scenario

        :param role: Name of the role.
        :type role: str
        :param policies: Policies to be associated with the tag. If set, must be a subset of the role's policies. If
            set, but set to an empty value, only the 'default' policy will be given to issued tokens.
        :type policies: list
        :param max_ttl: The maximum allowed lifetime of tokens issued using this role.
        :type max_ttl: str
        :param instance_id: Instance ID for which this tag is intended for. If set, the created tag can only be used by
            the instance with the given ID.
        :type instance_id: str
        :param disallow_reauthentication: If set, only allows a single token to be granted per instance ID. This can be
            cleared with the auth/aws/identity-whitelist endpoint. Defaults to 'false'. Mutually exclusive with
            allow_instance_migration.
        :type disallow_reauthentication: bool
        :param allow_instance_migration: If set, allows migration of the underlying instance where the client resides.
            This keys off of pendingTime in the metadata document, so essentially, this disables the client nonce check
            whenever the instance is migrated to a new host and pendingTime is newer than the previously-remembered
            time. Use with caution. Defaults to 'false'. Mutually exclusive with disallow_reauthentication.
        :type allow_instance_migration: bool
        :param mount_point: The path the AWS auth method was mounted on.
        :type mount_point: str
        :return: The create role tag response.
        :rtype: dict
        """
        ...
    def iam_login(
        self,
        access_key,
        secret_key,
        session_token=None,
        header_value=None,
        role=None,
        use_token: bool = True,
        region: str = "us-east-1",
        mount_point: str = "aws",
    ): ...
    def ec2_login(self, pkcs7, nonce=None, role=None, use_token: bool = True, mount_point: str = "aws"): ...
    def place_role_tags_in_blacklist(self, role_tag, mount_point: str = "aws"): ...
    def read_role_tag_blacklist(self, role_tag, mount_point: str = "aws"): ...
    def list_blacklist_tags(self, mount_point: str = "aws"): ...
    def delete_blacklist_tags(self, role_tag, mount_point: str = "aws"): ...
    def tidy_blacklist_tags(self, safety_buffer: str = "72h", mount_point: str = "aws"): ...
    def read_identity_whitelist(self, instance_id, mount_point: str = "aws"): ...
    def list_identity_whitelist(self, mount_point: str = "aws"): ...
    def delete_identity_whitelist_entries(self, instance_id, mount_point: str = "aws"): ...
    def tidy_identity_whitelist_entries(self, safety_buffer: str = "72h", mount_point: str = "aws"): ...
