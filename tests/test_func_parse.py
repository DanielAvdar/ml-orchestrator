import dataclasses
from dataclasses import field

import pytest

from ml_orchestrator import FunctionParser
from ml_orchestrator.comp_protocol.func_parser import _FunctionParser


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
        (field(default=42), 42),
        (field(default_factory=lambda: "test"), "test"),
        (field(), dataclasses.MISSING),
    ],
)
def test_parse_field(field, expected_default):
    result = FunctionParser.parse_field_default(field)
    assert result == expected_default


@dataclasses.dataclass
class MockComponent:
    param1: int = 42
    param2: str = "default"

    def execute(self) -> str:
        return "Execution Result"


@pytest.mark.parametrize(
    "component, expected_class",
    [
        (MockComponent, MockComponent),
        (MockComponent(), MockComponent),
    ],
)
def test_get_class_def(component, expected_class):
    result = _FunctionParser.get_class_def(component)
    assert result == expected_class


@pytest.mark.parametrize(
    "name, expected_name",
    [
        ("MockComponent", "mock_component"),
        ("MOckComponent", "m_ock_component"),
        ("Mockcomponent", "mockcomponent"),
        ("mockcomponent", "mockcomponent"),
        ("mockComponenT", "mock_componen_t"),
        ("MockComponent123", "mock_component123"),
        ("MockComponent_123", "mock_component_123"),
        ("MockComponent_123_456", "mock_component_123_456"),
    ],
)
def test_comp_func_name(name, expected_name):
    result = _FunctionParser._comp_func_name(name)
    assert result == expected_name
