"""Main point to run script."""

from click import group

from mc_plugin_helper.cli import CLI


@group()
def cli() -> None:
    """Group for CLI commands."""


def run() -> None:
    """Entrypoint to script."""
    cli_class = CLI()
    cli.add_command(cli_class.check)
    cli()


if __name__ == "__main__":
    run()
