from pathlib import Path

import pytest

from dummy_components.dummy_components import ComponentTestA, ComponentTestB


@pytest.mark.parametrize("comp", [ComponentTestB(), ComponentTestA()])
def test_write_to_file(op, comp, write_files_folder):
    content = op.create_kfp_file_str(components=[comp])
    prefix = "only_function" if op.only_function else "with_decorator"
    file_name = f"{prefix}_t_comps1.py"
    file_path = write_files_folder / Path(file_name)
    op.write_to_file(file_path, content)
    file_content = open(file_path, "r").read()
    assert content in file_content
    assert "from kfp.dsl import *" in file_content


def test_list_of_comp_write_to_file(op, write_files_folder):
    comp_list = [ComponentTestB(), ComponentTestA()]
    prefix = "only_function" if op.only_function else "with_decorator"

    file_name = f"{prefix}_t_comps2.py"
    file_path = write_files_folder / Path(file_name)

    op.parse_components_to_file(comp_list, file_path.as_posix())
    file_content = open(file_path, "r").read()
    assert "from dummy_components.dummy_components import ComponentTestB" in file_content
    assert "from dummy_components.dummy_components import ComponentTestA" in file_content
    assert "ComponentTestB(" in file_content
    assert "ComponentTestA(" in file_content


def test_list_of_comp_write_to_file_with_add_imports(op, write_files_folder):
    add_imports = ["from ml_orchestrator import MetaComponent # noqa"]
    op.add_imports = add_imports
    comp_list = [ComponentTestB(), ComponentTestA()]
    prefix = "only_function" if op.only_function else "with_decorator"

    file_name = f"{prefix}_t_comps3.py"
    file_path = write_files_folder / Path(file_name)
    op.parse_components_to_file(comp_list, file_path.as_posix())
    assert "from ml_orchestrator import MetaComponent # noqa" in op.add_imports
    file_content = open(file_path, "r").read()
    assert "from ml_orchestrator import MetaComponent # noqa" in file_content
    assert "ComponentTestB(" in file_content
    assert "ComponentTestA(" in file_content
