# -*- coding: utf-8 -*-
import os
import subprocess
import sys


ROOT_DIR = os.path.dirname(__file__)


def _program(name, args):
    bin_dir = ROOT_DIR if os.name == 'nt' else os.path.join(ROOT_DIR, "bin")
    return subprocess.call([os.path.join(bin_dir, name)] + args, close_fds=False)


def call_node(*args):
    suffix = '.exe' if os.name == 'nt' else ''
    return _program('node' + suffix, list(args))


def node(args=None):
    """Call the node executable with the given arguments.
    
    Parameters
    ----------
    args : Optional[list[str]], default=None
        List of arguments to pass to the node executable.
        If None, the arguments are taken from sys.argv[1:].

    Returns
    -------
    int
        Return code of the node executable.
    """
    if args is None:
        args = sys.argv[1:]
    return call_node(*args)


def npm(args=None):
    """Call the npm executable with the given arguments.
    
    Parameters
    ----------
    args : Optional[list[str]], default=None
        List of arguments to pass to the npm executable.
        If None, the arguments are taken from sys.argv[1:].

    Returns
    -------
    int
        Return code of the npm executable.
    """
    if args is None:
        args = sys.argv[1:]
    return call_node(os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npm-cli.js"), *args)


def npx(args=None):
    """Call the npx executable with the given arguments.
    
    Parameters
    ----------
    args : Optional[list[str]], default=None
        List of arguments to pass to the npx executable.
        If None, the arguments are taken from sys.argv[1:].

    Returns
    -------
    int
        Return code of the npx executable.
    """
    if args is None:
        args = sys.argv[1:]
    return call_node(os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npx-cli.js"), *args)


def _node_entry_point():
    raise SystemExit(node())


def _npm_entry_point():
    raise SystemExit(npm())


def _npx_entry_point():
    raise SystemExit(npx())
