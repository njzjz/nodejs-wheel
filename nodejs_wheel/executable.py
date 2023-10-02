# -*- coding: utf-8 -*-
import os
import subprocess
import sys


ROOT_DIR = os.path.dirname(__file__)


def _program(name, args):
    return subprocess.call([os.path.join(ROOT_DIR, "bin", name)] + args, close_fds=False)


def node():
    suffix = '.exe' if os.name == 'nt' else ''
    raise SystemExit(_program('node' + suffix, sys.argv[1:]))

def npm():
    suffix = '.exe' if os.name == 'nt' else ''
    raise SystemExit(_program('npm' + suffix, sys.argv[1:]))

def npx():
    suffix = '.exe' if os.name == 'nt' else ''
    raise SystemExit(_program('npx' + suffix, sys.argv[1:]))
