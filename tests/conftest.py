"""Conftest file for pytest."""
from os import path, remove


def pytest_sessionfinish() -> None:
    """Clean up some trash from tests."""
    try:
        remove(path.join(path.expanduser("~"), ".TEST.mc-plugin-helper.ini.TEST."))
    except FileNotFoundError:
        pass
