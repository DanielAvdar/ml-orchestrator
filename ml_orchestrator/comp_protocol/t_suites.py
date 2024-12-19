import abc
from typing import Any

import pytest

from .comp_protocol import ComponentProtocol
from .func_parser import FunctionParser


class ProtocolCompSuite(abc.ABC):
    @pytest.fixture
    @abc.abstractmethod
    def comp_fixture(self, *args: Any, **kwargs: Any) -> ComponentProtocol: ...

    def test_flows_protocol(self, comp_fixture: ComponentProtocol) -> None:
        assert isinstance(comp_fixture, ComponentProtocol)

    def test_comp_protocol_attrs(self, comp_fixture: ComponentProtocol) -> None:
        fp = FunctionParser()
        comp_vars = fp.comp_vars(comp_fixture)  # type: ignore
        assert comp_vars
        assert fp.get_func_params(comp_vars)

    def test_comp_protocol_e2e(self, comp_fixture: ComponentProtocol) -> None:
        fp = FunctionParser()
        fp.create_function(comp_fixture)
