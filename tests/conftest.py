"""Conftest file for pytest."""
from os import path, remove


def pytest_sessionfinish() -> None:
    """Clean up some trash from tests."""
    try:
        remove(path.join(path.expanduser("~"), ".TEST.mcph.yml.TEST."))
    except FileNotFoundError:
        pass
