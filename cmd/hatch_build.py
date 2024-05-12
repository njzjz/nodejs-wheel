from __future__ import annotations

from typing import Any

from hatchling.metadata.plugin.interface import MetadataHookInterface
from hatchling.plugin import hookimpl


class DependenciesMetadataHook(MetadataHookInterface):
    PLUGIN_NAME = "dependencies"

    def update(self, metadata: dict[str, Any]) -> None:
        metadata["dependencies"] = [f"nodejs-wheel-binaries=={metadata['version']}"]


@hookimpl
def hatch_register_metadata_hook() -> type[DependenciesMetadataHook]:
    return DependenciesMetadataHook
