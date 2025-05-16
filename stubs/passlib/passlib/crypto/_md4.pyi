class md4:
    """
    pep-247 compatible implementation of MD4 hash algorithm

    .. attribute:: digest_size

        size of md4 digest in bytes (16 bytes)

    .. method:: update

        update digest by appending additional content

    .. method:: copy

        create clone of digest object, including current state

    .. method:: digest

        return bytes representing md4 digest of current content

    .. method:: hexdigest

        return hexadecimal version of digest
    """
    name: str
    digest_size: int
    digestsize: int
    block_size: int
    def __init__(self, content=None) -> None: ...
    def update(self, content) -> None: ...
    def copy(self): ...
    def digest(self): ...
    def hexdigest(self): ...

__all__ = ["md4"]
