# -*- coding: utf-8 -*-
import os
import subprocess
import sys


ROOT_DIR = os.path.dirname(__file__)


def _program(name, args):
    return subprocess.call([os.path.join(ROOT_DIR, "bin", name)] + args, close_fds=False)


def call_node(*args):
    suffix = '.exe' if os.name == 'nt' else ''
    raise SystemExit(_program('node' + suffix, list(args)))


def node():
    call_node(*sys.argv[1:])


def npm():
    call_node(os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npm-cli.js"), *sys.argv[1:])


def npx():
    call_node(os.path.join(ROOT_DIR, "lib", "node_modules", "npm", "bin", "npx-cli.js"), *sys.argv[1:])
