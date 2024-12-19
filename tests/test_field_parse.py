import dataclasses
from dataclasses import field

import pytest

from ml_orchestrator import FunctionParser


@pytest.mark.parametrize(
    "field, expected_default",
    [
        (field(default=42), 42),
        (field(default_factory=lambda: "test"), "test"),
        (field(), dataclasses.MISSING),
        (field(default=None), None),
        (field(default_factory=lambda: None), None),
        (field(default_factory=lambda: 42), 42),
        (field(default=0), 0),
        (field(default_factory=lambda: 0), 0),
        (field(default_factory=lambda: [1, 2, 3]), [1, 2, 3]),
        (field(default_factory=list), []),
        (field(default_factory=lambda: []), []),
        (field(default_factory=dict), {}),
        (field(default_factory=lambda: {}), {}),
        (field(default_factory=lambda: {"a": 1}), {"a": 1}),
    ],
)
def test_parse_field(field, expected_default):
    result = FunctionParser.parse_field_default(field)
    assert result == expected_default
