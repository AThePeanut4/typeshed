"""Identity secret engine module."""

from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

logger: Incomplete

class Identity(VaultApiBase):
    """
    Identity Secrets Engine (API).

    Reference: https://www.vaultproject.io/api/secret/identity/entity.html
    """
    def create_or_update_entity(
        self, name, entity_id=None, metadata=None, policies=None, disabled=None, mount_point: str = "identity"
    ): ...
    def create_or_update_entity_by_name(
        self, name, metadata=None, policies=None, disabled=None, mount_point: str = "identity"
    ): ...
    def read_entity(self, entity_id, mount_point: str = "identity"): ...
    def read_entity_by_name(self, name, mount_point: str = "identity"): ...
    def update_entity(self, entity_id, name=None, metadata=None, policies=None, disabled=None, mount_point: str = "identity"): ...
    def delete_entity(self, entity_id, mount_point: str = "identity"): ...
    def delete_entity_by_name(self, name, mount_point: str = "identity"): ...
    def list_entities(self, method: str = "LIST", mount_point: str = "identity"): ...
    def list_entities_by_name(self, method: str = "LIST", mount_point: str = "identity"): ...
    def merge_entities(
        self, from_entity_ids, to_entity_id, force=None, mount_point: str = "identity", conflicting_alias_ids_to_keep=None
    ): ...
    def create_or_update_entity_alias(self, name, canonical_id, mount_accessor, alias_id=None, mount_point: str = "identity"): ...
    def read_entity_alias(self, alias_id, mount_point: str = "identity"): ...
    def update_entity_alias(self, alias_id, name, canonical_id, mount_accessor, mount_point: str = "identity"): ...
    def list_entity_aliases(self, method: str = "LIST", mount_point: str = "identity"): ...
    def delete_entity_alias(self, alias_id, mount_point: str = "identity"): ...
    @staticmethod
    def validate_member_id_params_for_group_type(group_type, params, member_group_ids, member_entity_ids):
        """
        Determine whether member ID parameters can be sent with a group create / update request.

        These parameters are only allowed for the internal group type. If they're set for an external group type, Vault
        returns a "error" response.

        :param group_type: Type of the group, internal or external
        :type group_type: str | unicode
        :param params: Params dict to conditionally add the member entity/group ID's to.
        :type params: dict
        :param member_group_ids:  Group IDs to be assigned as group members.
        :type member_group_ids: str | unicode
        :param member_entity_ids: Entity IDs to be assigned as  group members.
        :type member_entity_ids: str | unicode
        :return: Params dict with conditionally added member entity/group ID's.
        :rtype: dict
        """
        ...
    def create_or_update_group(
        self,
        name,
        group_id=None,
        group_type: str = "internal",
        metadata=None,
        policies=None,
        member_group_ids=None,
        member_entity_ids=None,
        mount_point: str = "identity",
    ):
        """
        Create or update a Group.

        Supported methods:
            POST: /{mount_point}/group. Produces: 200 application/json

        :param name: Name of the group.
        :type name: str | unicode
        :param group_id: ID of the group. If set, updates the corresponding existing group.
        :type group_id: str | unicode
        :param group_type: Type of the group, internal or external. Defaults to internal.
        :type group_type: str | unicode
        :param metadata: Metadata to be associated with the group.
        :type metadata: dict
        :param policies: Policies to be tied to the group.
        :type policies: str | unicode
        :param member_group_ids:  Group IDs to be assigned as group members.
        :type member_group_ids: str | unicode
        :param member_entity_ids: Entity IDs to be assigned as  group members.
        :type member_entity_ids: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response where available, otherwise the generic response object, of the request.
        :rtype: dict | requests.Response
        """
        ...
    def read_group(self, group_id, mount_point: str = "identity"):
        """
        Query the group by its identifier.

        Supported methods:
            GET: /{mount_point}/group/id/{id}. Produces: 200 application/json

        :param group_id: Identifier of the group.
        :type group_id: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: requests.Response
        """
        ...
    def update_group(
        self,
        group_id,
        name,
        group_type: str = "internal",
        metadata=None,
        policies=None,
        member_group_ids=None,
        member_entity_ids=None,
        mount_point: str = "identity",
    ):
        """
        Update an existing group.

        Supported methods:
            POST: /{mount_point}/group/id/{id}. Produces: 200 application/json

        :param group_id: Identifier of the entity.
        :type group_id: str | unicode
        :param name: Name of the group.
        :type name: str | unicode
        :param group_type: Type of the group, internal or external. Defaults to internal.
        :type group_type: str | unicode
        :param metadata: Metadata to be associated with the group.
        :type metadata: dict
        :param policies: Policies to be tied to the group.
        :type policies: str | unicode
        :param member_group_ids:  Group IDs to be assigned as group members.
        :type member_group_ids: str | unicode
        :param member_entity_ids: Entity IDs to be assigned as group members.
        :type member_entity_ids: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response where available, otherwise the generic response object, of the request.
        :rtype: dict | requests.Response
        """
        ...
    def delete_group(self, group_id, mount_point: str = "identity"):
        """
        Delete a group.

        Supported methods:
            DELETE: /{mount_point}/group/id/{id}. Produces: 204 (empty body)

        :param group_id: Identifier of the entity.
        :type group_id: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def list_groups(self, method: str = "LIST", mount_point: str = "identity"):
        """
        List available groups by their identifiers.

        :param method: Supported methods:
            LIST: /{mount_point}/group/id. Produces: 200 application/json
            GET: /{mount_point}/group/id?list=true. Produces: 200 application/json
        :type method: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def list_groups_by_name(self, method: str = "LIST", mount_point: str = "identity"):
        """
        List available groups by their names.

        :param method: Supported methods:
            LIST: /{mount_point}/group/name. Produces: 200 application/json
            GET: /{mount_point}/group/name?list=true. Produces: 200 application/json
        :type method: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def create_or_update_group_by_name(
        self,
        name,
        group_type: str = "internal",
        metadata=None,
        policies=None,
        member_group_ids=None,
        member_entity_ids=None,
        mount_point: str = "identity",
    ):
        """
        Create or update a group by its name.

        Supported methods:
            POST: /{mount_point}/group/name/{name}. Produces: 200 application/json

        :param name: Name of the group.
        :type name: str | unicode
        :param group_type: Type of the group, internal or external. Defaults to internal.
        :type group_type: str | unicode
        :param metadata: Metadata to be associated with the group.
        :type metadata: dict
        :param policies: Policies to be tied to the group.
        :type policies: str | unicode
        :param member_group_ids: Group IDs to be assigned as group members.
        :type member_group_ids: str | unicode
        :param member_entity_ids: Entity IDs to be assigned as group members.
        :type member_entity_ids: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def read_group_by_name(self, name, mount_point: str = "identity"):
        """
        Query a group by its name.

        Supported methods:
            GET: /{mount_point}/group/name/{name}. Produces: 200 application/json

        :param name: Name of the group.
        :type name: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def delete_group_by_name(self, name, mount_point: str = "identity"):
        """
        Delete a group, given its name.

        Supported methods:
            DELETE: /{mount_point}/group/name/{name}. Produces: 204 (empty body)

        :param name: Name of the group.
        :type name: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the request.
        :rtype: requests.Response
        """
        ...
    def create_or_update_group_alias(
        self, name, alias_id=None, mount_accessor=None, canonical_id=None, mount_point: str = "identity"
    ): ...
    def update_group_alias(self, entity_id, name, mount_accessor=None, canonical_id=None, mount_point="identity"): ...
    def read_group_alias(self, alias_id, mount_point: str = "identity"): ...
    def delete_group_alias(self, entity_id, mount_point: str = "identity"): ...
    def list_group_aliases(self, method: str = "LIST", mount_point: str = "identity"): ...
    def lookup_entity(
        self, name=None, entity_id=None, alias_id=None, alias_name=None, alias_mount_accessor=None, mount_point: str = "identity"
    ): ...
    def lookup_group(
        self, name=None, group_id=None, alias_id=None, alias_name=None, alias_mount_accessor=None, mount_point: str = "identity"
    ): ...
    def configure_tokens_backend(self, issuer=None, mount_point: str = "identity"): ...
    def read_tokens_backend_configuration(self, mount_point: str = "identity"): ...
    def create_named_key(
        self,
        name,
        rotation_period: str = "24h",
        verification_ttl: str = "24h",
        allowed_client_ids=None,
        algorithm: str = "RS256",
        mount_point: str = "identity",
    ):
        """
        Create or update a named key which is used by a role to sign tokens.

        Supported methods:
            POST: {mount_point}/oidc/key/:name.

        :param name: Name of the named key.
        :type name: str | unicode
        :param rotation_period: How often to generate a new signing key. Can be specified as a number of seconds or as
            a time string like "30m" or "6h".
        :type rotation_period: str | unicode
        :param verification_ttl: Controls how long the public portion of a signing key will be available for
            verification after being rotated.
        :type verification_ttl: str | unicode
        :param allowed_client_ids: List of role client ids allowed to use this key for signing.
            If empty, no roles are allowed. If "*", all roles are allowed.
        :type allowed_client_ids: list
        :param algorithm: Signing algorithm to use. Allowed values are: RS256 (default), RS384, RS512, ES256, ES384,
            ES512, EdDSA.
        :type algorithm: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the create_a_named_key request.
        :rtype: dict
        """
        ...
    def read_named_key(self, name, mount_point: str = "identity"):
        """
        Query a named key and returns its configurations.

        Supported methods:
            GET: {mount_point}/oidc/key/:name.

        :param name: Name of the key.
        :type name: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the read_a_named_key request.
        :rtype: dict
        """
        ...
    def delete_named_key(self, name, mount_point: str = "identity"):
        """
        Delete a named key.

        Supported methods:
            DELETE: {mount_point}/oidc/key/:name.

        :param name: Name of the key.
        :type name: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the delete_a_named_key request.
        :rtype: dict
        """
        ...
    def list_named_keys(self, mount_point: str = "identity"):
        """
        List all named keys.

        Supported methods:
            LIST: {mount_point}/oidc/key.

        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the list_named_keys request.
        :rtype: dict
        """
        ...
    def rotate_named_key(self, name, verification_ttl, mount_point: str = "identity"):
        """
        Rotate a named key.

        Supported methods:
            POST: {mount_point}/oidc/key/:name/rotate.

        :param name: Name of the key to be rotated.
        :type name: str | unicode
        :param verification_ttl: Controls how long the public portion of the key will be available for verification after being rotated.
            Setting verification_ttl here will override the verification_ttl set on the key.
        :type verification_ttl: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The response of the rotate_a_named_key request.
        :rtype: dict
        """
        ...
    def create_or_update_role(
        self, name, key, template=None, client_id=None, ttl: str = "24h", mount_point: str = "identity"
    ): ...
    def read_role(self, name, mount_point: str = "identity"): ...
    def delete_role(self, name, mount_point: str = "identity"): ...
    def list_roles(self, mount_point: str = "identity"): ...
    def generate_signed_id_token(self, name, mount_point: str = "identity"): ...
    def introspect_signed_id_token(self, token, client_id=None, mount_point: str = "identity"): ...
    def read_well_known_configurations(self, mount_point: str = "identity"): ...
    def read_active_public_keys(self, mount_point: str = "identity"): ...
