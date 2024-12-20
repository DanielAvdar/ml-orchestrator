import shutil
from pathlib import Path

import pytest

from ml_orchestrator import ComponentParser
from ml_orchestrator.comp_protocol.func_parser import FunctionParser


@pytest.fixture(params=[True, False])
def op(request):
    return ComponentParser(only_function=request.param)


@pytest.fixture
def fp(request):
    return FunctionParser()


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
