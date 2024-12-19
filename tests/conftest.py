import shutil
from pathlib import Path

import pytest

import dummy_components.dummy_components as dcomps
import dummy_components.invalid_protocol_components as ipcomps
import dummy_components.protocol_components as pcomps
from ml_orchestrator import ComponentParser
from ml_orchestrator.comp_protocol.func_parser import FunctionParser


@pytest.fixture(params=[True, False])
def op(request):
    return ComponentParser(only_function=request.param)


@pytest.fixture
def fp(request):
    return FunctionParser()


@pytest.fixture(
    params=[
        dcomps.ComponentTestB,
        dcomps.ComponentTestA,
        dcomps.ComponentTestC,
        dcomps.ComponentTestC2,
        dcomps.ComponentTestC3,
        dcomps.ComponentTestD,
        dcomps.ComponentTestD2,
        pcomps.ComponentTestB,
        pcomps.ComponentTestA,
        pcomps.ComponentTestC,
        pcomps.ComponentTestC2,
        pcomps.ComponentTestC3,
    ]
)
def dummy_component_class(request):
    return request.param


@pytest.fixture(params=[ipcomps.ComponentTestB, ipcomps.ComponentTestA])
def dummy_invalid_component_class(request):
    return request.param


@pytest.fixture
def dummy_component(dummy_component_class):
    return dummy_component_class()


@pytest.fixture(scope="session")
def test_directory() -> Path:
    folder_path = Path(__file__).parent
    assert folder_path.exists()
    return folder_path


@pytest.fixture(scope="session")
def tmp_files_folder(test_directory) -> Path:
    folder_path = test_directory / "tmp_folder_for_tests"
    if folder_path.exists():
        shutil.rmtree(folder_path)
    folder_path.mkdir()
    return folder_path
