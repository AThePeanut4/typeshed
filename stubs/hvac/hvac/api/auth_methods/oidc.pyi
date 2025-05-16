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
        bound_audiences=None,
        clock_skew_leeway=None,
        expiration_leeway=None,
        not_before_leeway=None,
        bound_subject=None,
        bound_claims=None,
        groups_claim=None,
        claim_mappings=None,
        oidc_scopes=None,
        bound_claims_type: str = "string",
        verbose_oidc_logging: bool = False,
        token_ttl=None,
        token_max_ttl=None,
        token_policies=None,
        token_bound_cidrs=None,
        token_explicit_max_ttl=None,
        token_no_default_policy=None,
        token_num_uses=None,
        token_period=None,
        token_type=None,
        path=None,
        user_claim_json_pointer=None,
    ) -> None: ...
