"""Spigot library manager."""
from mc_plugin_helper.library_manager.abstract import AbstractLibraryManager


class SpigotLibraryManager(AbstractLibraryManager):
    """Library manager for ``spigotmc.org``."""

    def get_latest_version(self, plugin: str) -> str:
        """Getter for latest plugin version.

        Args:
            plugin: Plugin name to check.

        Returns:
            String with the latest plugin version.
        """
