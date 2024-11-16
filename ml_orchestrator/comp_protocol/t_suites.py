from .comp_protocol import ComponentProtocol
from .func_parser import FunctionParser

import pytest


class ProtocolCompSuite:
    @pytest.fixture
    def comp_fixture(self, *args, **kwargs):
        pass

    def test_flows_protocol(self, comp_fixture):
        # if isinstance(comp_fixture, type):
        #     comp_fixture()
        assert isinstance(comp_fixture, ComponentProtocol)

    def test_comp_protocol_attrs(self, comp_fixture):
        fp = FunctionParser()
        assert fp.comp_vars(comp_fixture)
        assert fp.get_func_params(fp.comp_vars(comp_fixture))

    def test_comp_protocol_e2e(self, comp_fixture):
        fp = FunctionParser()
        fp.create_function(comp_fixture)
