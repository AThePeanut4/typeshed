"""
authlib.jose.rfc7518.
~~~~~~~~~~~~~~~~~~~~

Cryptographic Algorithms for Cryptographic Algorithms for Content
Encryption per `Section 5`_.

.. _`Section 5`: https://tools.ietf.org/html/rfc7518#section-5
"""

from _typeshed import Incomplete
from typing import Final

from authlib.jose.rfc7516 import JWEEncAlgorithm

class CBCHS2EncAlgorithm(JWEEncAlgorithm):
    IV_SIZE: int
    name: str
    description: str
    key_size: int
    key_len: int
    CEK_SIZE: int
    hash_alg: Incomplete
    def __init__(self, key_size: int, hash_type: int | str) -> None: ...
    def encrypt(self, msg, aad, iv, key) -> tuple[bytes, bytes]:
        """
        Key Encryption with AES_CBC_HMAC_SHA2.

        :param msg: text to be encrypt in bytes
        :param aad: additional authenticated data in bytes
        :param iv: initialization vector in bytes
        :param key: encrypted key in bytes
        :return: (ciphertext, iv, tag)
        """
        ...
    def decrypt(self, ciphertext, aad, iv, tag, key) -> bytes:
        """
        Key Decryption with AES AES_CBC_HMAC_SHA2.

        :param ciphertext: ciphertext in bytes
        :param aad: additional authenticated data in bytes
        :param iv: initialization vector in bytes
        :param tag: authentication tag in bytes
        :param key: encrypted key in bytes
        :return: message
        """
        ...

class GCMEncAlgorithm(JWEEncAlgorithm):
    IV_SIZE: int
    name: str
    description: str
    key_size: int
    CEK_SIZE: int
    def __init__(self, key_size: int) -> None: ...
    def encrypt(self, msg, aad, iv, key) -> tuple[bytes, bytes]:
        """
        Key Encryption with AES GCM.

        :param msg: text to be encrypt in bytes
        :param aad: additional authenticated data in bytes
        :param iv: initialization vector in bytes
        :param key: encrypted key in bytes
        :return: (ciphertext, iv, tag)
        """
        ...
    def decrypt(self, ciphertext, aad, iv, tag, key) -> bytes:
        """
        Key Decryption with AES GCM.

        :param ciphertext: ciphertext in bytes
        :param aad: additional authenticated data in bytes
        :param iv: initialization vector in bytes
        :param tag: authentication tag in bytes
        :param key: encrypted key in bytes
        :return: message
        """
        ...

JWE_ENC_ALGORITHMS: Final[list[CBCHS2EncAlgorithm | GCMEncAlgorithm]]
