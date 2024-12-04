from _typeshed import Incomplete

INDEX_NAME: str
INDEX_URL: Incomplete
TOKEN_USERNAME: str
log: Incomplete

def resolve_repository_name(repo_name): ...
def resolve_index_name(index_name): ...
def get_config_header(client, registry): ...
def split_repo_name(repo_name): ...
def get_credential_store(authconfig, registry): ...

class AuthConfig(dict[str, Incomplete]):
    def __init__(self, dct, credstore_env: Incomplete | None = None) -> None: ...
    @classmethod
    def parse_auth(cls, entries, raise_on_error: bool = False):
        """
        Parses authentication entries

        Args:
          entries:        Dict of authentication entries.
          raise_on_error: If set to true, an invalid format will raise
                          InvalidConfigFile

        Returns:
          Authentication registry.
        """
        ...
    @classmethod
    def load_config(cls, config_path, config_dict, credstore_env: Incomplete | None = None):
        """
        Loads authentication data from a Docker configuration file in the given
        root directory or if config_path is passed use given path.
        Lookup priority:
            explicit config_path parameter > DOCKER_CONFIG environment
            variable > ~/.docker/config.json > ~/.dockercfg
        """
        ...
    @property
    def auths(self): ...
    @property
    def creds_store(self): ...
    @property
    def cred_helpers(self): ...
    @property
    def is_empty(self): ...
    def resolve_authconfig(self, registry: Incomplete | None = None):
        """
        Returns the authentication data from the given auth configuration for a
        specific registry. As with the Docker client, legacy entries in the
        config with full URLs are stripped down to hostnames before checking
        for a match. Returns None if no match was found.
        """
        ...
    def get_credential_store(self, registry): ...
    def get_all_credentials(self): ...
    def add_auth(self, reg, data) -> None: ...

def resolve_authconfig(authconfig, registry: Incomplete | None = None, credstore_env: Incomplete | None = None): ...
def convert_to_hostname(url): ...
def decode_auth(auth): ...
def encode_header(auth): ...
def parse_auth(entries, raise_on_error: bool = False):
    """
    Parses authentication entries

    Args:
      entries:        Dict of authentication entries.
      raise_on_error: If set to true, an invalid format will raise
                      InvalidConfigFile

    Returns:
      Authentication registry.
    """
    ...
def load_config(
    config_path: Incomplete | None = None, config_dict: Incomplete | None = None, credstore_env: Incomplete | None = None
): ...
