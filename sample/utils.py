from typing import Optional

import idaapi

from . import NAME


def log(
    message: str, plugin_name: str = NAME, scope: Optional[str] = None
) -> None:
    if scope is None:
        idaapi.msg(f"[{plugin_name}] {message}\n")

    else:
        idaapi.msg(f"[{plugin_name}][{scope}] {message}\n")


def info(message: str) -> None:
    log(message, scope="INFO")


def debug(message: str) -> None:
    log(message, scope="DEBUG")


def warning(message: str) -> None:
    log(message, scope="WARNING")


def error(message: str) -> None:
    log(message, scope="ERROR")
