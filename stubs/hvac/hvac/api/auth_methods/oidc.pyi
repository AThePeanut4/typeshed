"""JWT/OIDC methods module."""

from _typeshed import Incomplete

from hvac.api.auth_methods.jwt import JWT

class OIDC(JWT):
    """
    OIDC auth method which can be used to authenticate with Vault using OIDC.

    The OIDC method allows authentication via a configured OIDC provider using the user's web browser.
    This method may be initiated from the Vault UI or the command line. Alternatively, a JWT can be provided directly.
    The JWT is cryptographically verified using locally-provided keys, or, if configured, an OIDC Discovery service can
    be used to fetch the appropriate keys. The choice of method is configured per role.

    Note: this class is duplicative of the JWT class (as both JWT and OIDC share the same family of Vault API routes).

    Reference: https://www.vaultproject.io/api/auth/jwt
    """
    DEFAULT_PATH: str
    def create_role(
        self,
        name,
        user_claim,
        allowed_redirect_uris,
        role_type: str = "oidc",
        bound_audiences: Incomplete | None = None,
        clock_skew_leeway: Incomplete | None = None,
        expiration_leeway: Incomplete | None = None,
        not_before_leeway: Incomplete | None = None,
        bound_subject: Incomplete | None = None,
        bound_claims: Incomplete | None = None,
        groups_claim: Incomplete | None = None,
        claim_mappings: Incomplete | None = None,
        oidc_scopes: Incomplete | None = None,
        bound_claims_type: str = "string",
        verbose_oidc_logging: bool = False,
        token_ttl: Incomplete | None = None,
        token_max_ttl: Incomplete | None = None,
        token_policies: Incomplete | None = None,
        token_bound_cidrs: Incomplete | None = None,
        token_explicit_max_ttl: Incomplete | None = None,
        token_no_default_policy: Incomplete | None = None,
        token_num_uses: Incomplete | None = None,
        token_period: Incomplete | None = None,
        token_type: Incomplete | None = None,
        path: Incomplete | None = None,
        user_claim_json_pointer: Incomplete | None = None,
    ) -> None:
        """
        Register a role in the OIDC method.

        Role types have specific entities that can perform login operations against this endpoint. Constraints
        specific to the role type must be set on the role. These are applied to the authenticated entities
        attempting to login. At least one of the bound values must be set.

        Supported methods:
            POST: /auth/{path}/role/:name.

        :param name: Name of the role.
        :type name: str | unicode
        :param role_type: Type of role, either "oidc" or "jwt" (default).
        :type role_type: str | unicode
        :param bound_audiences: List of aud claims to match against. Any match is sufficient.
            Required for "jwt" roles, optional for "oidc" roles.
        :type bound_audiences: list
        :param user_claim: The claim to use to uniquely identify the user; this will be used as the name for the
            Identity entity alias created due to a successful login. The interpretation of the user claim
            is configured with ``user_claim_json_pointer``. If set to ``True``, ``user_claim`` supports JSON pointer syntax
            for referencing a claim. The claim value must be a string.
        :type user_claim: str | unicode
        :param clock_skew_leeway: Only applicable with "jwt" roles.
        :type clock_skew_leeway: int
        :param expiration_leeway: Only applicable with "jwt" roles.
        :type expiration_leeway: int
        :param not_before_leeway: Only applicable with "jwt" roles.
        :type not_before_leeway: int
        :param bound_subject:  If set, requires that the sub claim matches this value.
        :type bound_subject: str | unicode
        :param bound_claims: If set, a dict of claims (keys) to match against respective claim values (values).
            The expected value may be a single string or a list of strings. The interpretation of the bound claim
            values is configured with bound_claims_type. Keys support JSON pointer syntax for referencing claims.
        :type bound_claims: dict
        :param groups_claim: The claim to use to uniquely identify the set of groups to which the user belongs; this
            will be used as the names for the Identity group aliases created due to a successful login. The claim value
            must be a list of strings. Supports JSON pointer syntax for referencing claims.
        :type groups_claim: str | unicode
        :param claim_mappings: If set, a map of claims (keys) to be copied to specified metadata fields (values). Keys
            support JSON pointer syntax for referencing claims.
        :type claim_mappings: map
        :param oidc_scopes: If set, a list of OIDC scopes to be used with an OIDC role.
            The standard scope "openid" is automatically included and need not be specified.
        :type oidc_scopes: list
        :param allowed_redirect_uris: The list of allowed values for redirect_uri
            during OIDC logins.
        :type allowed_redirect_uris: list
        :param bound_claims_type: Configures the interpretation of the bound_claims values. If "string" (the default),
            the values will treated as string literals and must match exactly. If set to "glob", the values will be
            interpreted as globs, with * matching any number of characters.
        :type bound_claims_type: str | unicode
        :param verbose_oidc_logging: Log received OIDC tokens and claims when debug-level
            logging is active. Not recommended in production since sensitive information may be present
            in OIDC responses.
        :type verbose_oidc_logging: bool
        :param token_ttl: The incremental lifetime for generated tokens. This current value of this will be referenced
            at renewal time.
        :type token_ttl: int | str
        :param token_max_ttl: The maximum lifetime for generated tokens. This current value of this will be referenced
            at renewal time.
        :type token_max_ttl: int | str
        :param token_policies: List of policies to encode onto generated tokens. Depending on the auth method, this
            list may be supplemented by user/group/other values.
        :type token_policies: list[str]
        :param token_bound_cidrs:  List of CIDR blocks; if set, specifies blocks of IP addresses which can authenticate
            successfully, and ties the resulting token to these blocks as well.
        :type token_bound_cidrs: list[str]
        :param token_explicit_max_ttl:  If set, will encode an explicit max TTL onto the token. This is a hard cap
            even if token_ttl and token_max_ttl would otherwise allow a renewal.
        :type token_explicit_max_ttl: int | str
        :param token_no_default_policy: If set, the default policy will not be set on generated tokens; otherwise it
            will be added to the policies set in token_policies.
        :type token_no_default_policy: bool
        :param token_num_uses: The maximum number of times a generated token may be used (within its lifetime); 0 means
            unlimited. If you require the token to have the ability to create child tokens, you will need to set this
            value to 0.
        :type token_num_uses: str | unicode
        :param token_period: The period, if any, to set on the token.
        :type token_period: int | str
        :param token_type: The type of token that should be generated. Can be service, batch, or default.
        :type token_type: str
        :param path: The "path" the method/backend was mounted on.
        :type path: str | unicode
        :param user_claim_json_pointer: Specifies if the ``user_claim`` value uses JSON pointer syntax for referencing claims.
            By default, the ``user_claim`` value will not use JSON pointer.
        :type user_claim_json_pointer: bool
        :return: The response of the create_role request.
        :rtype: dict
        """
        ...
