import logging

from hvac.api.vault_api_base import VaultApiBase

logger: logging.Logger

class Kv(VaultApiBase):
    allowed_kv_versions: list[str]
    def __init__(self, adapter, default_kv_version: str = "2") -> None: ...
    @property
    def v1(self):
        """
        Accessor for kv version 1 class / method. Provided via the :py:class:`hvac.api.secrets_engines.kv_v1.KvV1` class.

        :return: This Kv instance's associated KvV1 instance.
        :rtype: hvac.api.secrets_engines.kv_v1.KvV1
        """
        ...
    @property
    def v2(self):
        """
        Accessor for kv version 2 class / method. Provided via the :py:class:`hvac.api.secrets_engines.kv_v2.KvV2` class.

        :return: This Kv instance's associated KvV2 instance.
        :rtype: hvac.api.secrets_engines.kv_v2.KvV2
        """
        ...
    @property
    def default_kv_version(self): ...
    @default_kv_version.setter
    def default_kv_version(self, default_kv_version) -> None: ...
    def __getattr__(self, item):
        """
        Overridden magic method used to direct method calls to the appropriate KV version's hvac class.

        :param item: Name of the attribute/method being accessed
        :type item: str | unicode
        :return: The selected secrets_engines class corresponding to this instance's default_kv_version setting
        :rtype: hvac.api.vault_api_base.VaultApiBase
        """
        ...
