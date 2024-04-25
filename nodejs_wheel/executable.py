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
    raise SystemExit(_program('node' + suffix, list(args)))


def node(args=None):
    if args is None:
        args = sys.argv[1:]
    call_node(*args)


def npm(args=None):
    if args is None:
        args = sys.argv[1:]
    call_node(os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npm-cli.js"), *args)


def npx(args=None):
    if args is None:
        args = sys.argv[1:]
    call_node(os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npx-cli.js"), *args)
