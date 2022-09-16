"""Module for CLI commands."""
from typing import List

from prettytable import PrettyTable
from typer import echo

from mcph.models.plugin import Plugin


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
