def get_well_known_url(issuer: str, external: bool = False, suffix: str = "oauth-authorization-server") -> str:
    """
    Get well-known URI with issuer via `Section 3.1`_.

    .. _`Section 3.1`: https://tools.ietf.org/html/rfc8414#section-3.1

    :param issuer: URL of the issuer
    :param external: return full external url or not
    :param suffix: well-known URI suffix for RFC8414
    :return: URL
    """
    ...
