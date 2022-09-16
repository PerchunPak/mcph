"""Main point to run script."""

from pathlib import Path

from typer import Argument, Typer, echo

from mcph.config import config
from mcph.nice_echo import NiceEcho
from mcph.plugin_manager import PluginManager

app = Typer(name="mcph")


class CLI:
    """Class for CLI interface."""

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
            config.default_plugins_path,
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


if __name__ == "__main__":
    app()
