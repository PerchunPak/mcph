from yaml import safe_load as parse_yaml
from typing import List, Dict
from mc_plugin_helper.config import Config
from mc_plugin_helper.file_manager.factory import FileManagerFactory


class Plugin(object):
    """Create object for plugin."""

    def __init__(self, name, version, file_path, url) -> None:
        """__init__ method."""
        self.name = name
        self.version = version
        self.file_path = file_path
        self.url = url


class PluginManager(object):
    """Make some stuff with plugin management."""

    def __init__(self, folder) -> None:
        """__init__ method.

        Args:
            folder: Folder with plugins.
        """
        self.config = Config.init().config
        self.file_manager = FileManagerFactory.create_file_manager(
            self.config["protocol"],
        )
        self.plugins_location = folder

    def get_all_plugins(self) -> List[Plugin]:
        """Getter for list with all plugins.

        Returns:
            List with all plugins.
        """
        plugins = []
        for file in self.file_manager.get_all_files(self.plugins_location):  # noqa: WPS110,E501
            if not file.name.endswith(".jar"):
                continue
            parsed_data = self.process_plugin(file)
            plugins.append(Plugin(parsed_data))
        return plugins

    # TODO move to async function
    def process_plugin(self, jar_file) -> Dict[str: str]:
        """Opens plugin.jar and then parsing plugin.yml inside .jar.

        Args:
            jar_file: File object, which points to plugin.

        Returns:
            Parsed yaml in dict.
        """
        plugin_yml = self.file_manager.open_jar(jar_file)
        return parse_yaml(plugin_yml)
