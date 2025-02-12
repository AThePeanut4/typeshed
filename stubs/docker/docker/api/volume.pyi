from typing import Any

class VolumeApiMixin:
    def volumes(self, filters: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        List volumes currently registered by the docker daemon. Similar to the
        ``docker volume ls`` command.

        Args:
            filters (dict): Server-side list filtering options.

        Returns:
            (dict): Dictionary with list of volume objects as value of the
            ``Volumes`` key.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> client.api.volumes()
            {u'Volumes': [{u'Driver': u'local',
               u'Mountpoint': u'/var/lib/docker/volumes/foobar/_data',
               u'Name': u'foobar'},
              {u'Driver': u'local',
               u'Mountpoint': u'/var/lib/docker/volumes/baz/_data',
               u'Name': u'baz'}]}
        """
        ...
    def create_volume(
        self,
        name: str | None = None,
        driver: str | None = None,
        driver_opts: dict[str, Any] | None = None,
        labels: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create and register a named volume

        Args:
            name (str): Name of the volume
            driver (str): Name of the driver used to create the volume
            driver_opts (dict): Driver options as a key-value dictionary
            labels (dict): Labels to set on the volume

        Returns:
            (dict): The created volume reference object

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> volume = client.api.create_volume(
            ...     name='foobar',
            ...     driver='local',
            ...     driver_opts={'foo': 'bar', 'baz': 'false'},
            ...     labels={"key": "value"},
            ... )
            ... print(volume)
            {u'Driver': u'local',
            u'Labels': {u'key': u'value'},
            u'Mountpoint': u'/var/lib/docker/volumes/foobar/_data',
            u'Name': u'foobar',
            u'Scope': u'local'}
        """
        ...
    def inspect_volume(self, name: str) -> dict[str, Any]:
        """
        Retrieve volume info by name.

        Args:
            name (str): volume name

        Returns:
            (dict): Volume information dictionary

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.

        Example:

            >>> client.api.inspect_volume('foobar')
            {u'Driver': u'local',
             u'Mountpoint': u'/var/lib/docker/volumes/foobar/_data',
             u'Name': u'foobar'}
        """
        ...
    def prune_volumes(self, filters: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Delete unused volumes

        Args:
            filters (dict): Filters to process on the prune list.

        Returns:
            (dict): A dict containing a list of deleted volume names and
                the amount of disk space reclaimed in bytes.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    def remove_volume(self, name, force: bool = False) -> None:
        """
        Remove a volume. Similar to the ``docker volume rm`` command.

        Args:
            name (str): The volume's name
            force (bool): Force removal of volumes that were already removed
                out of band by the volume driver plugin.

        Raises:
            :py:class:`docker.errors.APIError`
                If volume failed to remove.
        """
        ...
