# Unoffical Node.js wheels

[![Pypi version](https://img.shields.io/pypi/v/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dm/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dw/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)
[![Pypi downloads](https://img.shields.io/pypi/dd/nodejs-wheel)](https://pypi.org/project/nodejs-wheel/)

`nodejs-wheel` is an unofficial repository to distribute Node.js prebuilt wheels through PyPI using 

```sh
pip install nodejs-wheel
```

The package requires Python 3.7 and above.

The project is powered by [scikit-build-core](https://github.com/scikit-build/scikit-build-core) and [cibuildwheel](https://github.com/pypa/cibuildwheel).

## Available Builds

| OS      | Arch    | Bit | Conditions     |
| ------- | ------- | --- | -------------- |
| Linux   | x86_64  | 64  | glibc >= 2.17  |
| macOS   | x86_64  | 64  | >= macOS-10.9  |
| macOS   | arm64   | 64  | >= macOS-11    |
| Windows | amd64   | 64  |                |

## Usage

```sh
node -h
npm -h
npx -h
```

## License

`nodejs-wheel` distributed under the same MIT [license](LICENSE) as [Node.js](https://github.com/nodejs/node).

## Other projects

The project is inspired by many other similiar projects:

- [samwillis/nodejs-pypi](https://github.com/samwillis/nodejs-pypi): The package redistribute the official Node.js binaraies to PyPI. However, the offical binary for Nodejs 18 requires GLIBC 2.28, making it unsupported in [manylinux2014](https://github.com/pypa/manylinux) images. Besides, the wheel tag is wrong.
- [sbwml/node-latest-centos](https://github.com/sbwml/node-latest-centos): Use GitHub Actions to build Node.js in CentOS 7, but is not related to Python or PyPI.
- [scikit-build/cmake-python-distributions](https://github.com/scikit-build/cmake-python-distributions): Use cibuildwheel and scikit-build to build CMake and distribute CMake in PyPI.
