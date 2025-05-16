from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Transit(VaultApiBase):
    """
    Transit Secrets Engine (API).

    Reference: https://www.vaultproject.io/api/secret/transit/index.html
    """
    def create_key(
        self,
        name,
        convergent_encryption=None,
        derived=None,
        exportable=None,
        allow_plaintext_backup=None,
        key_type=None,
        mount_point="transit",
        auto_rotate_period=None,
    ): ...
    def read_key(self, name, mount_point="transit"): ...
    def list_keys(self, mount_point="transit"): ...
    def delete_key(self, name, mount_point="transit"): ...
    def update_key_configuration(
        self,
        name,
        min_decryption_version=None,
        min_encryption_version=None,
        deletion_allowed=None,
        exportable=None,
        allow_plaintext_backup=None,
        mount_point="transit",
        auto_rotate_period=None,
    ): ...
    def rotate_key(self, name, mount_point="transit"): ...
    def export_key(self, name, key_type, version=None, mount_point="transit"): ...
    def encrypt_data(
        self,
        name,
        plaintext=None,
        context=None,
        key_version=None,
        nonce=None,
        batch_input=None,
        type=None,
        convergent_encryption=None,
        mount_point: str = "transit",
        associated_data: str | None = None,
    ):
        """
        Encrypt the provided plaintext using the named key.

        This path supports the create and update policy capabilities as follows: if the user has the create capability
        for this endpoint in their policies, and the key does not exist, it will be upserted with default values
        (whether the key requires derivation depends on whether the context parameter is empty or not). If the user only
        has update capability and the key does not exist, an error will be returned.

        Supported methods:
            POST: /{mount_point}/encrypt/{name}. Produces: 200 application/json

        :param name: Specifies the name of the encryption key to encrypt against. This is specified as part of the URL.
        :type name: str | unicode
        :param plaintext: Specifies base64 encoded plaintext to be encoded. Ignored if ``batch_input`` is set, otherwise required.
        :type plaintext: str | unicode
        :param context: Specifies the base64 encoded context for key derivation. This is required if key derivation is
            enabled for this key.
        :type context: str | unicode
        :param associated_data: Specifies base64 encoded associated data (also known as additional data or AAD) to also be authenticated
            with AEAD ciphers (aes128-gcm96, aes256-gcm, and chacha20-poly1305)
        :type associated_data: str | unicode
        :param key_version: Specifies the version of the key to use for encryption. If not set, uses the latest version.
            Must be greater than or equal to the key's min_encryption_version, if set.
        :type key_version: int
        :param nonce: Specifies the base64 encoded nonce value. This must be provided if convergent encryption is
            enabled for this key and the key was generated with Vault 0.6.1. Not required for keys created in 0.6.2+.
            The value must be exactly 96 bits (12 bytes) long and the user must ensure that for any given context (and
            thus, any given encryption key) this nonce value is never reused.
        :type nonce: str | unicode
        :param batch_input: Specifies a list of items to be encrypted in a single batch. When this parameter is set, if
            the parameters 'plaintext', 'context' and 'nonce' are also set, they will be ignored. The format for the
            input is: [dict(context="b64_context", plaintext="b64_plaintext"), ...]
        :type batch_input: List[dict]
        :param type: This parameter is required when encryption key is expected to be created. When performing an
            upsert operation, the type of key to create.
        :type type: str | unicode
        :param convergent_encryption: This parameter will only be used when a key is expected to be created. Whether to
            support convergent encryption. This is only supported when using a key with key derivation enabled and will
            require all requests to carry both a context and 96-bit (12-byte) nonce. The given nonce will be used in
            place of a randomly generated nonce. As a result, when the same context and nonce are supplied, the same
            ciphertext is generated. It is very important when using this mode that you ensure that all nonces are
            unique for a given context. Failing to do so will severely impact the ciphertext's security.
        :type convergent_encryption: str | unicode
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def decrypt_data(
        self,
        name,
        ciphertext=None,
        context=None,
        nonce=None,
        batch_input=None,
        mount_point: str = "transit",
        associated_data: str | None = None,
    ):
        """
        Decrypt the provided ciphertext using the named key.

        Supported methods:
            POST: /{mount_point}/decrypt/{name}. Produces: 200 application/json

        :param name: Specifies the name of the encryption key to decrypt against. This is specified as part of the URL.
        :type name: str | unicode
        :param ciphertext: The ciphertext to decrypt. Ignored if ``batch_input`` is set, otherwise required.
        :type ciphertext: str | unicode
        :param context: Specifies the base64 encoded context for key derivation. This is required if key derivation is
            enabled.
        :type context: str | unicode
        :param associated_data: Specifies base64 encoded associated data (also known as additional data or AAD) to also
            be authenticated with AEAD ciphers (aes128-gcm96, aes256-gcm, and chacha20-poly1305)
        :type associated_data: str | unicode
        :param nonce: Specifies a base64 encoded nonce value used during encryption. Must be provided if convergent
            encryption is enabled for this key and the key was generated with Vault 0.6.1. Not required for keys created
            in 0.6.2+.
        :type nonce: str | unicode
        :param batch_input: Specifies a list of items to be decrypted in a single batch. When this parameter is set, if
            the parameters 'ciphertext', 'context' and 'nonce' are also set, they will be ignored. Format for the input
            goes like this: [dict(context="b64_context", ciphertext="b64_plaintext"), ...]
        :type batch_input: List[dict]
        :param mount_point: The "path" the method/backend was mounted on.
        :type mount_point: str | unicode
        :return: The JSON response of the request.
        :rtype: dict
        """
        ...
    def rewrap_data(
        self, name, ciphertext, context=None, key_version=None, nonce=None, batch_input=None, mount_point="transit"
    ): ...
    def generate_data_key(self, name, key_type, context=None, nonce=None, bits=None, mount_point="transit"): ...
    def generate_random_bytes(self, n_bytes=None, output_format=None, mount_point="transit"): ...
    def hash_data(self, hash_input, algorithm=None, output_format=None, mount_point="transit"): ...
    def generate_hmac(self, name, hash_input, key_version=None, algorithm=None, mount_point="transit"): ...
    def sign_data(
        self,
        name,
        hash_input=None,
        key_version=None,
        hash_algorithm=None,
        context=None,
        prehashed=None,
        signature_algorithm=None,
        marshaling_algorithm=None,
        salt_length=None,
        mount_point="transit",
        batch_input=None,
    ): ...
    def verify_signed_data(
        self,
        name,
        hash_input,
        signature=None,
        hmac=None,
        hash_algorithm=None,
        context=None,
        prehashed=None,
        signature_algorithm=None,
        salt_length=None,
        marshaling_algorithm=None,
        mount_point="transit",
    ): ...
    def backup_key(self, name, mount_point="transit"): ...
    def restore_key(self, backup, name=None, force=None, mount_point="transit"): ...
    def trim_key(self, name, min_version, mount_point="transit"): ...
