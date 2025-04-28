"""Module for defining base artifact classes used in ML pipeline components.

This module provides base classes for representing and managing artifacts
with support for JSON serialization of metadata.
"""

import json
from typing import Any, Dict, Mapping, Optional


class JSONSerializableDict(dict):
    """Dictionary that ensures all values are JSON serializable.

    A specialized dictionary that validates all values to ensure they can be
    serialized to JSON format. This is useful for storing metadata that
    needs to be serialized for storage or transmission.
    """

    def __setitem__(self, key: Any, value: Any) -> None:
        """Set an item in the dictionary after ensuring it's JSON serializable.

        Args:
            key: The dictionary key
            value: The value to set, must be JSON serializable

        Raises:
            ValueError: If the value cannot be serialized to JSON

        """
        try:
            json.dumps(value)
            return super().__setitem__(key, value)

        except (TypeError, OverflowError, ValueError):
            pass
        raise ValueError(f"Value for key '{key}' is not JSON serializable: {value}")

    def update(self, m: Mapping = None, **kwargs: Any) -> None:  # type: ignore[override]
        """Update the dictionary with another mapping after ensuring values are JSON serializable.

        Args:
            m: A mapping to update from
            **kwargs: Additional key-value pairs to update with

        Raises:
            ValueError: If any values cannot be serialized to JSON

        """
        try:
            json.dumps(m)
            return super().update(m, **kwargs)

        except TypeError:
            pass
        raise ValueError(f"Aritfact metadata must be JSON serializable, got: {m}")

    def __or__(self, other: Mapping) -> "JSONSerializableDict":
        """Implement the | operator to combine two mappings.

        Args:
            other: Another mapping to combine with this one

        Returns:
            A new JSONSerializableDict containing items from both mappings

        """
        new_dict = JSONSerializableDict(self)
        new_dict.update(other)
        return new_dict


class Artifact:
    """Base class for all artifacts used in ML pipeline components.

    An artifact represents a file or directory that is an input to or output from
    a pipeline component, with associated metadata stored in a JSON-serializable format.

    Attributes:
        schema_title: The schema title for this artifact type
        schema_version: The schema version for this artifact type

    """

    schema_title = "system.Artifact"
    schema_version = "0.0.1"

    def __init__(self, name: Optional[str] = None, uri: Optional[str] = None, metadata: Optional[Dict] = None) -> None:
        """Initialize an artifact with a name, URI, and metadata.

        Args:
            name: The name of the artifact
            uri: The URI where the artifact is stored
            metadata: A dictionary of metadata to associate with the artifact

        """
        self.uri = uri or "./"
        self.name = name or "artifact"
        self._metadata = JSONSerializableDict(metadata or dict())

    @property
    def path(self) -> str:
        """Get the path where the artifact is stored.

        Returns:
            The URI of the artifact

        """
        return self.uri

    @property
    def metadata(self) -> "JSONSerializableDict":
        """Get the metadata associated with this artifact.

        Returns:
            A JSON-serializable dictionary of metadata

        """
        return self._metadata

    @metadata.setter
    def metadata(self, new_data: Mapping) -> None:
        """Set new metadata for this artifact.

        Args:
            new_data: A mapping containing the new metadata

        Raises:
            ValueError: If the new metadata cannot be serialized to JSON

        """
        try:
            json.dumps(new_data)
            self._metadata = JSONSerializableDict(new_data)
            return

        except TypeError:
            pass
        raise ValueError(f"Aritfact metadata is not JSON serializable: {new_data}")
