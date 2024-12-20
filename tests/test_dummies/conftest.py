import pytest

from dummy_components import (
    invalid_classes_protocols,
    protocol_components as pcomps,
    valid_classes,
    valid_classes_meta,
    valid_classes_meta_v2,
)


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


@pytest.fixture(params=invalid_classes_protocols)
def dummy_invalid_component_class(request):
    return request.param


@pytest.fixture
def dummy_component(dummy_component_class_):
    return dummy_component_class_()


# @pytest.fixture(params=valid_classes_meta)
# def dummy_meta_classes_v1(request):
#     return request.param
#
#
# @pytest.fixture(params=valid_classes_meta_v2)
# def dummy_meta_classes_v2(request):
#     return request.param


@pytest.fixture(params=valid_classes_meta + valid_classes_meta_v2)
def dummy_meta_classes_all(request):
    return request.param
