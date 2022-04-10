"""Module for library managers factory, use it as entry-point to library managers."""
from typing import Literal

from mc_plugin_helper.library_manager.spigot import SpigotLibraryManager


class LibraryManagerFactory:
    """Fabric for Library Managers."""

    @staticmethod
    def create_file_manager(protocol: Literal["spigot"]) -> SpigotLibraryManager:
        """Create object with library manager.

        Args:
            protocol: Protocol for which create file manager.

        Raises:
            TypeError: Wrong protocol provided.

        Returns:
            Object of file manager.
        """
        if protocol.lower() == "spigot":
            return SpigotLibraryManager()
        else:
            # because there are another protocols, planning do it in future
            raise TypeError("Got wrong protocol")
