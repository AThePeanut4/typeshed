from _typeshed import Incomplete

CODE_VERIFIER_PATTERN: Incomplete
CODE_CHALLENGE_PATTERN: Incomplete

def create_s256_code_challenge(code_verifier):
    """Create S256 code_challenge with the given code_verifier."""
    ...
def compare_plain_code_challenge(code_verifier, code_challenge): ...
def compare_s256_code_challenge(code_verifier, code_challenge): ...

class CodeChallenge:
    """
    CodeChallenge extension to Authorization Code Grant. It is used to
    improve the security of Authorization Code flow for public clients by
    sending extra "code_challenge" and "code_verifier" to the authorization
    server.

    The AuthorizationCodeGrant SHOULD save the ``code_challenge`` and
    ``code_challenge_method`` into database when ``save_authorization_code``.
    Then register this extension via::

        server.register_grant(AuthorizationCodeGrant, [CodeChallenge(required=True)])
    """
    DEFAULT_CODE_CHALLENGE_METHOD: str
    SUPPORTED_CODE_CHALLENGE_METHOD: Incomplete
    CODE_CHALLENGE_METHODS: Incomplete
    required: Incomplete
    def __init__(self, required: bool = True) -> None: ...
    def __call__(self, grant) -> None: ...
    def validate_code_challenge(self, grant) -> None: ...
    def validate_code_verifier(self, grant) -> None: ...
    def get_authorization_code_challenge(self, authorization_code):
        """
        Get "code_challenge" associated with this authorization code.
        Developers MAY re-implement it in subclass, the default logic::

            def get_authorization_code_challenge(self, authorization_code):
                return authorization_code.code_challenge

        :param authorization_code: the instance of authorization_code
        """
        ...
    def get_authorization_code_challenge_method(self, authorization_code):
        """
        Get "code_challenge_method" associated with this authorization code.
        Developers MAY re-implement it in subclass, the default logic::

            def get_authorization_code_challenge_method(self, authorization_code):
                return authorization_code.code_challenge_method

        :param authorization_code: the instance of authorization_code
        """
        ...
