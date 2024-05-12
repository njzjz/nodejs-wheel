from __future__ import annotations

import os
import subprocess
import sys
from typing import Any

ROOT_DIR = os.path.dirname(__file__)


def _program(name: str, args: list[str], **kwargs: Any) -> int:
    bin_dir = ROOT_DIR if os.name == "nt" else os.path.join(ROOT_DIR, "bin")
    return subprocess.call([os.path.join(bin_dir, name), *args], **kwargs)


def call_node(*args: str, **kwargs: Any) -> int:
    suffix = ".exe" if os.name == "nt" else ""
    return _program("node" + suffix, list(args), **kwargs)


def node(args: list[str] | None = None, **kwargs: Any) -> int:
    """Call the node executable with the given arguments.

    Parameters
    ----------
    args : Optional[list[str]], default=None
        List of arguments to pass to the node executable.
        If None, the arguments are taken from sys.argv[1:].
    **kwargs : dict[str, Any]
        Other arguments passed to subprocess.call

    Returns
    -------
    int
        Return code of the node executable.
    """
    if args is None:
        args = sys.argv[1:]
    return call_node(*args, **kwargs)


def npm(args: list[str] | None = None, **kwargs: Any) -> int:
    """Call the npm executable with the given arguments.

    Parameters
    ----------
    args : Optional[list[str]], default=None
        List of arguments to pass to the npm executable.
        If None, the arguments are taken from sys.argv[1:].
    **kwargs : dict[str, Any]
        Other arguments passed to subprocess.call

    Returns
    -------
    int
        Return code of the npm executable.
    """
    if args is None:
        args = sys.argv[1:]
    return call_node(
        os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npm-cli.js"),
        *args,
        **kwargs,
    )


def npx(args: list[str] | None = None, **kwargs: Any) -> int:
    """Call the npx executable with the given arguments.

    Parameters
    ----------
    args : Optional[list[str]], default=None
        List of arguments to pass to the npx executable.
        If None, the arguments are taken from sys.argv[1:].
    **kwargs : dict[str, Any]
        Other arguments passed to subprocess.call

    Returns
    -------
    int
        Return code of the npx executable.
    """
    if args is None:
        args = sys.argv[1:]
    return call_node(
        os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npx-cli.js"),
        *args,
        **kwargs,
    )


def _node_entry_point() -> None:
    raise SystemExit(node(close_fds=False))


def _npm_entry_point() -> None:
    raise SystemExit(npm(close_fds=False))


def _npx_entry_point() -> None:
    raise SystemExit(npx(close_fds=False))
