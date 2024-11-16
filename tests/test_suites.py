from ml_orchestrator.comp_protocol.t_suites import ProtocolCompSuite

import pytest


class TestProtocolCompSuite(ProtocolCompSuite):
    @pytest.fixture
    def comp_fixture(self, dummy_component_class):
        return dummy_component_class


@pytest.mark.xfail(raises=(AssertionError, TypeError), strict=True)
class TestInvalidProtocolCompSuite(ProtocolCompSuite):
    @pytest.fixture
    def comp_fixture(self, dummy_invalid_component_class):
        return dummy_invalid_component_class
