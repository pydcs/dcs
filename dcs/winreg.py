"""Wrapper around the stdlib winreg that fails gracefully on non-Windows."""
import logging
import sys
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


def read_current_user_value(
    key: str, value: str, ctor: Callable[[Any], T] = lambda x: x
) -> Optional[T]:
    if sys.platform == "win32":
        import winreg

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key) as hkey:
                # QueryValueEx returns a tuple of (value, type ID).
                return ctor(winreg.QueryValueEx(hkey, value)[0])
        except FileNotFoundError:
            return None
    else:
        logging.getLogger("pydcs").error(
            "Cannot read registry keys on non-Windows OS, returning None"
        )
        return None
