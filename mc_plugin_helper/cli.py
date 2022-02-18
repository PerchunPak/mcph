"""Module for CLI commands."""

from typing import List, Union
from click import Path, argument, command, echo
from mc_plugin_helper.config import Config
from mc_plugin_helper.plugin_manager import Plugin, PluginManager


def _find_plugin_in_list(
    plugin_name: str, plugins: List[Plugin],
) -> Union[Plugin, None]:
    """Found plugin in list, by its name.

    Args:
        plugin_name: Plugin name of plugin which we try to find.
        plugins: List of plugins, where we need to find.

    Returns:
        Plugin object, or None if we didn't find anything.
    """
    found_plugin = None
    for plugin in plugins:
        if plugin_name == plugin.name:
            found_plugin = plugin
            break
    return found_plugin


class CLI(object):
    """Class for CLI interface."""

    def __init__(self) -> None:
        """__init__ method."""
        self.config = Config.init().config
        self._echo = NiceEcho

    @command()
    @argument(
        "plugin_name",
        type=str,
        default="all",
    )
    @argument(
        "folder",
        type=Path(exists=True),
    )
    def check(self, plugin_name: str, folder: Union[str, None]) -> None:
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
        elif _find_plugin_in_list(plugin_name, plugins) is not None:
            echo("Plugin not installed!")
        else:
            self._echo.nice_echo_plugin(
                _find_plugin_in_list(  # type: ignore[arg-type]
                    plugin_name, plugins,
                ),
            )


# TODO Build a normal class
class NiceEcho(object):
    """Class for Nice Echo some info, to console."""

    @staticmethod
    def nice_echo_plugin(plugin: Plugin) -> None:
        """Nice echo one plugin.

        Args:
            plugin: Plugin object with information about it.
        """
        echo("Plugin: {0}".format(plugin.name))

    @staticmethod
    def nice_echo_all_plugins(plugins: List[Plugin]) -> None:
        """Nice echo all plugins, from a list.

        Args:
            plugins: List with plugins objects with information about it.
        """
        for plugin in plugins:
            echo("Plugin: {0}".format(plugin.name))
