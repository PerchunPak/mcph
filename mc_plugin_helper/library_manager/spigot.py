"""Spigot library manager."""
from mc_plugin_helper.library_manager.abstract import AbstractLibraryManager
from mc_plugin_helper.models.plugin import Plugin


class SpigotLibraryManager(AbstractLibraryManager):
    """Library manager for ``spigotmc.org``."""

    def get_latest_version(self, plugin: Plugin) -> str:
        """Getter for latest plugin version.

        Args:
            plugin: Plugin object to check.

        Returns:
            String with the latest plugin version.
        """
