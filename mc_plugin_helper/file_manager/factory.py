"""Module for file managers factory, use it as entry-point to file managers."""

from mc_plugin_helper.config import Protocol
from mc_plugin_helper.file_manager.local import LocalFileManager


class FileManagerFactory:
    """Fabric for File Managers."""

    @staticmethod
    def create_file_manager(protocol: Protocol) -> LocalFileManager:
        """Create object with file manager.

        Args:
            protocol: Protocol for which create file manager.

        Raises:
            TypeError: Wrong protocol provided.

        Returns:
            Object of file manager.
        """
        if protocol == Protocol.LOCAL:
            return LocalFileManager()
        else:
            # because there are another protocols, planning do it in future
            raise TypeError("Got wrong protocol")
