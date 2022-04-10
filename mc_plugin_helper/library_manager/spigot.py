"""Spigot library manager."""
from typing import Any, Dict, Optional

import requests
from requests.models import Response

from mc_plugin_helper.library_manager.abstract import AbstractLibraryManager


class SpigotLibraryManager(AbstractLibraryManager):
    """Library manager for ``spigotmc.org``."""

    def get_latest_version(self, plugin_name: str) -> str:
        """Getter for latest plugin version.

        Args:
            plugin_name: Plugin name to check.

        Returns:
            String with the latest plugin version or "Not Found" if we can't find plugin.
        """
        plugin_data = self.get_plugin_data(plugin_name)
        if plugin_data is None:
            return "Not Found"

        plugin_id = plugin_data["id"]
        latest_version: str = self._api_request(f"resources/{plugin_id}/versions/latest").json()["name"]
        return latest_version

    def get_plugin_data(self, plugin_name: str) -> Optional[Dict[str, Any]]:
        """Getter for plugin data.

        Args:
            plugin_name: Name of plugin to check.

        Returns:
            Parsed JSON answer or None if no plugins found.
        """
        try:
            to_return: Dict[str, Any] = self._api_request(
                f"search/resources/{plugin_name}?field=name&sort=-downloads"
            ).json()[0]
            return to_return
        except IndexError:
            return None

    def _api_request(self, url: str) -> Response:
        """Perform API request to Spiget.

        Args:
            url: URL to request.

        Returns:
            Raw answer.
        """
        headers = {"User-Agent": "mc-plugin-helper"}
        return requests.get("https://api.spiget.org/v2/" + url, headers=headers)
