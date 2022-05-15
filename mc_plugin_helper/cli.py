"""Module for CLI commands."""

from pathlib import Path
from typing import List

from prettytable import PrettyTable
from typer import Argument, Typer, echo

from mc_plugin_helper.config import config
from mc_plugin_helper.models.plugin import Plugin
from mc_plugin_helper.plugin_manager import PluginManager

app = Typer(name="mc-plugin-helper")


class CLI:
    """Class for CLI interface. Do not forget add commands to __main__.py!"""

    @staticmethod
    @app.callback(help=None)
    def callback() -> None:
        """Stub for typer, so it is not transforming command to main CLI, only as subcommand.

        Remove this when there will be more than one command.
        """

    @staticmethod
    @app.command(help="Check updates for plugin or all plugins.")
    def check(
        plugin_name: str = Argument("all", help="Plugin name to check, or just `all`."),
        folder: Path = Argument(
            config.plugins_path,
            show_default="From Config",
            exists=True,
            file_okay=False,
            dir_okay=True,
            help="Folder with plugins. If passed something, try to find plugin with name of `plugin_name`.",
        ),
    ) -> None:
        """Check updates for plugin or all plugins.

        Args:
            plugin_name: Plugin name to check, or just `all`.
            folder: Folder with plugins.
                If nothing passing, use from config.
                If passed something, try to find plugin with name of ``plugin_name``.
        """
        plugin_manager = PluginManager(str(folder))
        plugins = plugin_manager.get_all_plugins()
        plugin = plugin_manager.get_specified_plugin(plugin_name, plugins)

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
        table.field_names = ["Num", "Name", "Current Version", "Last Version", "Update Available"]

        i = 1
        for plugin in plugins:
            table.add_row([i, plugin.name, plugin.version, plugin.last_version, plugin.update_available])
            i += 1

        echo(table)
