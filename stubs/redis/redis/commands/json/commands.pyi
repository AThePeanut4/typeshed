from _typeshed import Incomplete

class JSONCommands:
    """json commands."""
    def arrappend(self, name: str, path: str | None = ".", *args) -> list[int | None]:
        """
        Append the objects ``args`` to the array under the
        ``path` in key ``name``.

        For more information see `JSON.ARRAPPEND <https://redis.io/commands/json.arrappend>`_..
        """
        ...
    def arrindex(
        self, name: str, path: str, scalar: int, start: int | None = None, stop: int | None = None
    ) -> list[int | None]:
        """
        Return the index of ``scalar`` in the JSON array under ``path`` at key
        ``name``.

        The search can be limited using the optional inclusive ``start``
        and exclusive ``stop`` indices.

        For more information see `JSON.ARRINDEX <https://redis.io/commands/json.arrindex>`_.
        """
        ...
    def arrinsert(self, name: str, path: str, index: int, *args) -> list[int | None]:
        """
        Insert the objects ``args`` to the array at index ``index``
        under the ``path` in key ``name``.

        For more information see `JSON.ARRINSERT <https://redis.io/commands/json.arrinsert>`_.
        """
        ...
    def arrlen(self, name: str, path: str | None = ".") -> list[int | None]:
        """
        Return the length of the array JSON value under ``path``
        at key``name``.

        For more information see `JSON.ARRLEN <https://redis.io/commands/json.arrlen>`_.
        """
        ...
    def arrpop(self, name: str, path: str | None = ".", index: int | None = -1) -> list[str | None]:
        """
        Pop the element at ``index`` in the array JSON value under
        ``path`` at key ``name``.

        For more information see `JSON.ARRPOP <https://redis.io/commands/json.arrpop>`_.
        """
        ...
    def arrtrim(self, name: str, path: str, start: int, stop: int) -> list[int | None]:
        """
        Trim the array JSON value under ``path`` at key ``name`` to the
        inclusive range given by ``start`` and ``stop``.

        For more information see `JSON.ARRTRIM <https://redis.io/commands/json.arrtrim>`_.
        """
        ...
    def type(self, name: str, path: str | None = ".") -> list[str]:
        """
        Get the type of the JSON value under ``path`` from key ``name``.

        For more information see `JSON.TYPE <https://redis.io/commands/json.type>`_.
        """
        ...
    def resp(self, name: str, path: str | None = ".") -> list[Incomplete]:
        """
        Return the JSON value under ``path`` at key ``name``.

        For more information see `JSON.RESP <https://redis.io/commands/json.resp>`_.
        """
        ...
    def objkeys(self, name, path="."):
        """
        Return the key names in the dictionary JSON value under ``path`` at
        key ``name``.

        For more information see `JSON.OBJKEYS <https://redis.io/commands/json.objkeys>`_.
        """
        ...
    def objlen(self, name, path="."):
        """
        Return the length of the dictionary JSON value under ``path`` at key
        ``name``.

        For more information see `JSON.OBJLEN <https://redis.io/commands/json.objlen>`_.
        """
        ...
    def numincrby(self, name, path, number):
        """
        Increment the numeric (integer or floating point) JSON value under
        ``path`` at key ``name`` by the provided ``number``.

        For more information see `JSON.NUMINCRBY <https://redis.io/commands/json.numincrby>`_.
        """
        ...
    def nummultby(self, name, path, number):
        """
        Multiply the numeric (integer or floating point) JSON value under
        ``path`` at key ``name`` with the provided ``number``.

        For more information see `JSON.NUMMULTBY <https://redis.io/commands/json.nummultby>`_.
        """
        ...
    def clear(self, name, path="."):
        """
        Empty arrays and objects (to have zero slots/keys without deleting the
        array/object).

        Return the count of cleared paths (ignoring non-array and non-objects
        paths).

        For more information see `JSON.CLEAR <https://redis.io/commands/json.clear>`_.
        """
        ...
    def delete(self, key, path="."):
        """
        Delete the JSON value stored at key ``key`` under ``path``.

        For more information see `JSON.DEL <https://redis.io/commands/json.del>`_.
        """
        ...
    forget = delete
    def get(self, name, *args, no_escape: bool = False):
        """
        Get the object stored as a JSON value at key ``name``.

        ``args`` is zero or more paths, and defaults to root path
        ```no_escape`` is a boolean flag to add no_escape option to get
        non-ascii characters

        For more information see `JSON.GET <https://redis.io/commands/json.get>`_.
        """
        ...
    def mget(self, keys, path):
        """
        Get the objects stored as a JSON values under ``path``. ``keys``
        is a list of one or more keys.

        For more information see `JSON.MGET <https://redis.io/commands/json.mget>`_.
        """
        ...
    def set(self, name, path, obj, nx: bool = False, xx: bool = False, decode_keys: bool = False):
        """
        Set the JSON value at key ``name`` under the ``path`` to ``obj``.

        ``nx`` if set to True, set ``value`` only if it does not exist.
        ``xx`` if set to True, set ``value`` only if it exists.
        ``decode_keys`` If set to True, the keys of ``obj`` will be decoded
        with utf-8.

        For the purpose of using this within a pipeline, this command is also
        aliased to JSON.SET.

        For more information see `JSON.SET <https://redis.io/commands/json.set>`_.
        """
        ...
    def set_file(self, name, path, file_name, nx: bool = False, xx: bool = False, decode_keys: bool = False):
        """
        Set the JSON value at key ``name`` under the ``path`` to the content
        of the json file ``file_name``.

        ``nx`` if set to True, set ``value`` only if it does not exist.
        ``xx`` if set to True, set ``value`` only if it exists.
        ``decode_keys`` If set to True, the keys of ``obj`` will be decoded
        with utf-8.
        """
        ...
    def set_path(self, json_path, root_folder, nx: bool = False, xx: bool = False, decode_keys: bool = False):
        """
        Iterate over ``root_folder`` and set each JSON file to a value
        under ``json_path`` with the file name as the key.

        ``nx`` if set to True, set ``value`` only if it does not exist.
        ``xx`` if set to True, set ``value`` only if it exists.
        ``decode_keys`` If set to True, the keys of ``obj`` will be decoded
        with utf-8.
        """
        ...
    def strlen(self, name, path: Incomplete | None = None):
        """
        Return the length of the string JSON value under ``path`` at key
        ``name``.

        For more information see `JSON.STRLEN <https://redis.io/commands/json.strlen>`_.
        """
        ...
    def toggle(self, name, path="."):
        """
        Toggle boolean value under ``path`` at key ``name``.
        returning the new value.

        For more information see `JSON.TOGGLE <https://redis.io/commands/json.toggle>`_.
        """
        ...
    def strappend(self, name, value, path="."):
        """
        Append to the string JSON value. If two options are specified after
        the key name, the path is determined to be the first. If a single
        option is passed, then the root_path (i.e Path.root_path()) is used.

        For more information see `JSON.STRAPPEND <https://redis.io/commands/json.strappend>`_.
        """
        ...
    def debug(self, subcommand, key: Incomplete | None = None, path="."):
        """
        Return the memory usage in bytes of a value under ``path`` from
        key ``name``.

        For more information see `JSON.DEBUG <https://redis.io/commands/json.debug>`_.
        """
        ...
    def jsonget(self, *args, **kwargs): ...
    def jsonmget(self, *args, **kwargs): ...
    def jsonset(self, *args, **kwargs): ...
