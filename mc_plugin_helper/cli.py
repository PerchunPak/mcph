from click import Path, command, echo, option
from mc_plugin_helper.config import Config
from mc_plugin_helper.plugin_manager import Plugin, PluginManager


class CLI(object):
    """Класс для CLI интерфейса."""

    def __init__(self) -> None:
        """__init__ method."""
        self.config = Config.init().config
        self._echo = NiceEcho

    @command()
    @option(
        "--folder",
        "-f",
        type=Path(exists=True),
        help="Folder to search .jar files.\nDefault - get value from config.",
    )
    @option(
        "--plugin_name",
        "-p",
        type=str,
        default="all",
        help="Plugin name to check.\nDefault - all.",
    )
    def check(self, folder: str, plugin_name: str):
        """Check updates for plugin or all plugins.

        Args:
            folder: Folder with plugins.
                If nothing passing, check in config.
                If passed something, check all .jar files in folder.
            plugin_name: Plugin name to check, or just "all".
        """
        if folder is None:
            folder = self.config["plugins-path"]

        plugin_manager = PluginManager(folder)
        plugins = plugin_manager.get_all_plugins()

        if plugin_name == "all":
            self._echo.nice_echo_all_plugins(plugins)
        elif Plugin(plugin_name) not in plugins:
            echo("Plugin not installed!")
        else:
            self._echo.nice_echo_plugin(plugin_name)


# TODO Build a normal class
class NiceEcho(object):
    """Class for Nice Echo some info, to console."""

    @staticmethod
    def nice_echo_plugin(plugin) -> None:
        """Nice echo one plugin."""
        echo("Plugin: {0}".format(plugin.name))

    @staticmethod
    def nice_echo_all_plugins(plugins) -> None:
        """Nice echo all plugins, from a list."""
        for plugin in plugins:
            echo("Plugin: {0}".format(plugin.name))
