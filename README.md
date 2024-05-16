# Unoffical Node.js wheels

[![Pypi version](https://img.shields.io/pypi/v/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dm/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dw/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dd/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)

`nodejs-wheel` is an unofficial repository to distribute Node.js prebuilt wheels through PyPI using

```sh
pip install nodejs-wheel
```

*New in v20.13.0*: If you don't need command line interface (CLI), install only `nodejs-wheel-binaries`, which is a direct dependency of `nodejs-wheel`.

```sh
pip install nodejs-wheel-binaries
```

The package requires Python 3.7 and above.

The project is powered by [scikit-build-core](https://github.com/scikit-build/scikit-build-core) and [cibuildwheel](https://github.com/pypa/cibuildwheel).

## Available Builds

| OS      | Arch    | Bit | Conditions     | New in      |
| ------- | ------- | --- | -------------- | ----------- |
| Linux   | x86_64  | 64  | glibc >= 2.17  | v18.18.0    |
| Linux   | x86_64  | 64  | musl >= 1.2    | v20.14.0    |
| Linux   | aarch64 | 64  | glibc >= 2.17  | v20.13.0    |
| macOS   | x86_64  | 64  | >= macOS-10.15 | v18.18.0    |
| macOS   | arm64   | 64  | >= macOS-11    | v20.11.1    |
| Windows | amd64   | 64  |                | v18.18.0    |

## Usage

### Command line

Only available in the `nodejs-wheel` package.

```sh
node -h
npm -h
npx -h
```

### Run library module as a script

*New in v20.13.0*.

Only support `node`.

```sh
python -m nodejs_wheel --version
```

### Python API

*New in v20.13.0*.

```py
from nodejs_wheel import (
    node,
    npm,
    npx,
)

return_code0 = node(["--version"])
return_code1 = npm(["--version"])
return_code2 = npx(["--version"])
```

*New in v20.13.1*: pass `return_completed_process=True` to get `subprocess.CompletedProcess` instead of `int`.

```py
completed_process0 = node(["--version"], return_completed_process=True)
completed_process1 = npm(["--version"], return_completed_process=True)
completed_process2 = npx(["--version"], return_completed_process=True)
```

## License

`nodejs-wheel` distributed under the same MIT [license](LICENSE) as [Node.js](https://github.com/nodejs/node).

## Other projects

The project is inspired by many other similiar projects:

- [samwillis/nodejs-pypi](https://github.com/samwillis/nodejs-pypi): The package redistribute the official Node.js binaraies to PyPI. However, the offical binary for Nodejs 18 requires GLIBC 2.28, making it unsupported in [manylinux2014](https://github.com/pypa/manylinux) images. Besides, the wheel tag is wrong.
- [sbwml/node-latest-centos](https://github.com/sbwml/node-latest-centos): Use GitHub Actions to build Node.js in CentOS 7, but is not related to Python or PyPI.
- [scikit-build/cmake-python-distributions](https://github.com/scikit-build/cmake-python-distributions): Use cibuildwheel and scikit-build to build CMake and distribute CMake in PyPI.
