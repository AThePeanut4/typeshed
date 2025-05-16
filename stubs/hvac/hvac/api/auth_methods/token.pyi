from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Token(VaultApiBase):
    """
    Token Auth Method (API).

    Reference: http://localhost:3000/api-docs/auth/token
    """
    def create(
        self,
        id=None,
        role_name=None,
        policies=None,
        meta=None,
        no_parent: bool = False,
        no_default_policy: bool = False,
        renewable: bool = True,
        ttl=None,
        type=None,
        explicit_max_ttl=None,
        display_name: str = "token",
        num_uses: int = 0,
        period=None,
        entity_alias=None,
        wrap_ttl=None,
        mount_point="token",
    ):
        """
        Create a new token.

        Certain options are only available when called by a root token. If used
        via the /auth/token/create-orphan endpoint, a root token is not required
        to create an orphan token (otherwise set with the no_parent option). If
        used with a role name in the path, the token will be created against the
        specified role name; this may override options set during this call.


        :param id: The ID of the client token. Can only be specified by a root token.
            The ID provided may not contain a `.` character. Otherwise, the
            token ID is a randomly generated value.
        :type id: str
        :param role_name: The name of the token role.
        :type role_name: str
        :param policies: A list of policies for the token. This must be a
            subset of the policies belonging to the token making the request, unless root.
            If not specified, defaults to all the policies of the calling token.
        :type policies: list
        :param meta: A map of string to string valued metadata. This is
            passed through to the audit devices.
        :type meta: map
        :param no_parent: This argument only has effect if used by a root or sudo caller.
            When set to `True`, the token created will not have a parent.
        :type no_parent: bool
        :param no_default_policy: If `True` the default policy will not be contained in this token's policy set.
        :type no_default_policy: bool
        :param renewable:  Set to false to disable the ability of the token to be renewed past its initial TTL.
            Setting the value to true will allow the token to be renewable up to the system/mount maximum TTL.
        :type renewable: bool
        :param ttl: The TTL period of the token, provided as "1h", where hour is the largest suffix. If not provided,
            the token is valid for the default lease TTL, or indefinitely if the root policy is used.
        :type ttl: str
        :param type: The token type. Can be "batch" or "service". Defaults to the type
            specified by the role configuration named by role_name.
        :type type: str
        :param explicit_max_ttl: If set, the token will have an explicit max TTL set upon it.
            This maximum token TTL cannot be changed later, and unlike with normal tokens, updates to the system/mount
            max TTL value will have no effect at renewal time -- the token will never be able to be renewed or used past
            the value set at issue time.
        :type explicit_max_ttl: str
        :param display_name: The display name of the token.
        :type display_name: str
        :param num_uses: The maximum uses for the given token. This can be
            used to create a one-time-token or limited use token. The value of 0 has no
            limit to the number of uses.
        :type num_uses: int
        :param period: If specified, the token will be periodic; it will have
            no maximum TTL (unless an "explicit-max-ttl" is also set) but every renewal
            will use the given period. Requires a root token or one with the sudo capability.
        :type period: str
        :param entity_alias: Name of the entity alias to associate with during token creation.
            Only works in combination with role_name argument and used entity alias must be listed in
            `allowed_entity_aliases`. If this has been specified, the entity will not be inherited from the parent.
        :type entity_alias: str
        :param wrap_ttl: Specifies response wrapping token creation with duration. IE: '15s', '20m', '25h'.
        :type wrap_ttl: str
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str
        :return: The response of the create request.
        :rtype: requests.Response
        """
        ...
    def create_orphan(
        self,
        id=None,
        role_name=None,
        policies=None,
        meta=None,
        no_default_policy: bool = False,
        renewable: bool = True,
        ttl=None,
        type=None,
        explicit_max_ttl=None,
        display_name: str = "token",
        num_uses: int = 0,
        period=None,
        entity_alias=None,
        wrap_ttl=None,
        mount_point="token",
    ): ...
    def list_accessors(self, mount_point="token"): ...
    def lookup(self, token, mount_point="token"): ...
    def lookup_self(self, mount_point="token"): ...
    def lookup_accessor(self, accessor, mount_point="token"): ...
    def renew(self, token, increment=None, wrap_ttl=None, mount_point="token"): ...
    def renew_self(self, increment=None, wrap_ttl=None, mount_point="token"): ...
    def renew_accessor(self, accessor, increment=None, wrap_ttl=None, mount_point="token"): ...
    def revoke(self, token, mount_point="token"): ...
    def revoke_self(self, mount_point="token"): ...
    def revoke_accessor(self, accessor, mount_point="token"): ...
    def revoke_and_orphan_children(self, token, mount_point="token"): ...
    def read_role(self, role_name, mount_point="token"): ...
    def list_roles(self, mount_point="token"): ...
    def create_or_update_role(
        self,
        role_name,
        allowed_policies=None,
        disallowed_policies=None,
        orphan: bool = False,
        renewable: bool = True,
        path_suffix=None,
        allowed_entity_aliases=None,
        mount_point="token",
        token_period=None,
        token_explicit_max_ttl=None,
    ): ...
    def delete_role(self, role_name, mount_point="token"): ...
    def tidy(self, mount_point="token"): ...
