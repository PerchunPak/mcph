"""Module for some plugin-manager methods."""

from os.path import join
from typing import Dict, List

from yaml import safe_load as parse_yaml

from mc_plugin_helper.config import config
from mc_plugin_helper.file_manager.factory import FileManagerFactory


class Plugin:
    """Create object for plugin."""

    def __init__(self, name, version, file_path) -> None:
        """__init__ method."""
        self.name = name
        self.version = version
        self.file_path = file_path


class PluginManager:
    """Make some stuff with plugin management."""

    def __init__(self, folder: str) -> None:
        """__init__ method.

        Args:
            folder: Folder with plugins.
        """
        self.file_manager = FileManagerFactory.create_file_manager(config["config"]["protocol"])  # type: ignore[arg-type]
        self.plugins_location = folder

    def get_all_plugins(self) -> List[Plugin]:
        """Getter for list with all plugins.

        Returns:
            List with all plugins.
        """
        plugins = []
        for file in self.file_manager.get_all_files(self.plugins_location):
            if not file.endswith(".jar"):
                continue
            parsed_data = self.process_plugin(join(self.plugins_location, file))
            plugins.append(
                Plugin(
                    name=parsed_data["name"],
                    version=parsed_data["version"],
                    file_path=join(self.plugins_location, file),
                ),
            )
        return plugins

    # TODO move to async function
    def process_plugin(self, jar_file) -> Dict[str, str]:
        """Opens plugin.jar and then parsing plugin.yml inside .jar.

        Args:
            jar_file: File object, which points to plugin.

        Returns:
            Parsed yaml in dict.
        """
        plugin_yml = self.file_manager.open_jar(jar_file)
        return parse_yaml(plugin_yml)  # type: ignore[no-any-return]
