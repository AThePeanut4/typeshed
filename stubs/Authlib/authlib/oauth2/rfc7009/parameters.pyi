from _typeshed import Incomplete

def prepare_revoke_token_request(
    token, token_type_hint: Incomplete | None = None, body: Incomplete | None = None, headers: Incomplete | None = None
):
    """
    Construct request body and headers for revocation endpoint.

    :param token: access_token or refresh_token string.
    :param token_type_hint: Optional, `access_token` or `refresh_token`.
    :param body: current request body.
    :param headers: current request headers.
    :return: tuple of (body, headers)

    https://tools.ietf.org/html/rfc7009#section-2.1
    """
    ...
