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
        num_init_params = len(comp_fixture.__init__.__code__.co_varnames) - 1  # type: ignore
        func_params = fp.get_func_params(comp_vars)

        assert comp_vars if num_init_params > 0 else not comp_vars
        assert len(comp_vars) == num_init_params
        assert len(func_params) == num_init_params

    def test_comp_protocol_e2e(self, comp_fixture: ComponentProtocol) -> None:
        fp = FunctionParser()
        fp.create_function(comp_fixture)
