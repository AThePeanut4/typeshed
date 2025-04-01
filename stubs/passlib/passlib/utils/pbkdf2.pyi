"""
passlib.pbkdf2 - PBKDF2 support

this module is getting increasingly poorly named.
maybe rename to "kdf" since it's getting more key derivation functions added.
"""

from _typeshed import Incomplete

from passlib.crypto.digest import norm_hash_name as norm_hash_name

def get_prf(name): ...
def pbkdf1(secret, salt, rounds, keylen: Incomplete | None = None, hash: str = "sha1"): ...
def pbkdf2(secret, salt, rounds, keylen: Incomplete | None = None, prf: str = "hmac-sha1"): ...

__all__ = [
    # hash utils
    "norm_hash_name",
    # prf utils
    "get_prf",
    # kdfs
    "pbkdf1",
    "pbkdf2",
]
