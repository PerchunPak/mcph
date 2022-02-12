from mc_plugin_helper.file_manager.local import LocalFileManager


class FileManagerFactory(object):
    """Fabric for File Managers."""

    @staticmethod
    def create_file_manager(protocol: str) -> LocalFileManager:
        """Create object with file manager.

        Args:
            protocol: Protocol for which create file manager.

        Raises:
            TypeError: Wrong protocol provided.

        Returns:
            Object of file manager.
        """
        if protocol.lower() == "local":
            return LocalFileManager()
        else:
            # because there are another protocols planning in future
            raise TypeError("Got wrong protocol")  # noqa: WPS503
