"""Module for CLI commands."""

from typing import List, Optional, Union

from click import Path, argument, command, echo
from prettytable import PrettyTable

from mc_plugin_helper.config import config
from mc_plugin_helper.models.plugin import Plugin
from mc_plugin_helper.plugin_manager import PluginManager


def _find_plugin_in_list(plugin_name: str, plugins: List[Plugin]) -> Optional[Plugin]:
    """Found plugin in list, by its name.

    Args:
        plugin_name: Plugin name of plugin which we try to find.
        plugins: List of plugins, where we need to find.

    Returns:
        Plugin object, or None if we didn't find anything.
    """
    for plugin in plugins:
        if plugin_name == plugin.name:
            return plugin
    return None


class CLI:
    """Class for CLI interface. Do not forget add commands to __main__.py!"""

    @staticmethod
    @command()
    @argument("plugin_name", type=str, default="all")
    @argument("folder", type=Path(exists=True), required=False)
    def check(plugin_name: str, folder: Union[str, None]) -> None:
        """Check updates for plugin or all plugins.

        Args:
            folder: Folder with plugins.
                If nothing passing, check in config.
                If passed something, check all .jar files in folder.
            plugin_name: Plugin name to check, or just "all".
        """
        if folder is None:
            folder = config["config"]["plugins-path"]

        plugin_manager = PluginManager(folder)
        plugins = plugin_manager.get_all_plugins()
        plugin = _find_plugin_in_list(plugin_name, plugins)

        if plugin_name == "all":
            NiceEcho.nice_echo_plugins(plugins)
        elif plugin is None:
            echo("Plugin not installed!")
        else:
            NiceEcho.nice_echo_plugins([plugin])


class NiceEcho:
    """Class for Nice Echo some info, to console."""

    @staticmethod
    def style_table(table: PrettyTable) -> None:
        """Add some style options to table argument.

        Args:
            table: Table which we need change.
        """
        table.vertical_char = "│"
        table.horizontal_char = "─"
        table.top_junction_char = "─"
        table.bottom_junction_char = "─"
        table.top_right_junction_char = "┐"
        table.top_left_junction_char = "┌"
        table.bottom_left_junction_char = "└"
        table.bottom_right_junction_char = "┘"

    @staticmethod
    def nice_echo_plugins(plugins: List[Plugin]) -> None:
        """Nice echo all plugins from a list.

        Args:
            plugins: List with plugins objects with information about it.
        """
        if len(plugins) == 0:
            echo("No plugins found!")
            return

        table = PrettyTable()
        NiceEcho.style_table(table)
        table.field_names = ["Num", "Name", "Version", "Last Version"]

        i = 1
        for plugin in plugins:
            table.add_row([i, plugin.name, plugin.version, plugin.last_version])
            i += 1

        echo(table)
