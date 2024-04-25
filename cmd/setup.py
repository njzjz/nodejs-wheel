from setuptools import setup
from setuptools_scm import Configuration, _get_version

config = Configuration.from_file("pyproject.toml")
version = _get_version(config)
assert version is not None

setup(
    install_requires=[
        f"nodejs-wheel=={version}",
    ],
)