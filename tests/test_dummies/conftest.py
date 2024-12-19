import pytest

from dummy_components import invalid_protocol_components as ipcomps, protocol_components as pcomps
from tests.conftest import valid_classes


@pytest.fixture(params=valid_classes)
def dummy_component_class_(request):
    return request.param


@pytest.fixture(
    params=valid_classes
    + [
        pcomps.ComponentWithMandatoryParam,
        pcomps.ComponentWithMandatoryParamB,
    ]
)
def dummy_component_class(request):
    return request.param


@pytest.fixture(params=[ipcomps.ComponentTestB, ipcomps.ComponentTestA])
def dummy_invalid_component_class(request):
    return request.param


@pytest.fixture
def dummy_component(dummy_component_class_):
    return dummy_component_class_()
