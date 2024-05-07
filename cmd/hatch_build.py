from typing import Type

from hatchling.metadata.plugin.interface import MetadataHookInterface
from hatchling.plugin import hookimpl


class DependenciesMetadataHook(MetadataHookInterface):
    PLUGIN_NAME = "dependencies"

    def update(self, metadata: dict) -> None:
        metadata["dependencies"] = [f"nodejs-wheel-binaries=={metadata['version']}"]


@hookimpl
def hatch_register_metadata_hook() -> Type[DependenciesMetadataHook]:
    return DependenciesMetadataHook
