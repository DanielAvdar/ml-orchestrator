from pathlib import Path

from dummy_components.dummy_components import ComponentTestA, ComponentTestB

import pytest


def test_write_to_file_base(fp, dummy_component_class, tmp_files_folder):
    name = dummy_component_class.__name__
    comp_func_name = name.lower()
    content = fp.create_kfp_file_str(components=[dummy_component_class])
    file_name_base = f"base_{comp_func_name}"
    file_name = f"{file_name_base}.py"
    file_path = tmp_files_folder / Path(file_name)
    fp.write_to_file(file_path, content)
    with open(file_path, "r") as f:
        file_content = f.read()
    assert content in file_content
    assert "from kfp.dsl import *" in file_content
    assert f"{comp_func_name}(" in file_content
    assert f"{name}(" in file_content
    return_type = dummy_component_class.execute.__annotations__["return"]
    if return_type is not None:
        assert "return comp.execute()" in file_content
        assert f"-> {return_type.__name__}:" in file_content


@pytest.mark.parametrize("comp", [ComponentTestB(), ComponentTestA()])
def test_write_to_file(op, comp, tmp_files_folder):
    content = op.create_kfp_file_str(components=[comp])
    file_name = f"{str(op.only_function).lower()}-t_file.py"
    file_path = tmp_files_folder / Path(file_name)
    op.write_to_file(file_path, content)
    file_content = open(file_path, "r").read()
    assert content in file_content
    assert "from kfp.dsl import *" in file_content


def test_list_of_comp_write_to_file(op, tmp_files_folder):
    comp_list = [ComponentTestB(), ComponentTestA()]
    file_name = f"{str(op.only_function).lower()}-t_comps2.py"
    file_path = tmp_files_folder / Path(file_name)

    op.parse_components_to_file(comp_list, file_path.as_posix())
    file_content = open(file_path, "r").read()
    assert "from dummy_components.dummy_components import ComponentTestB" in file_content
    assert "from dummy_components.dummy_components import ComponentTestA" in file_content
    assert "ComponentTestB(" in file_content
    assert "ComponentTestA(" in file_content


def test_list_of_comp_write_to_file_with_add_imports(op, tmp_files_folder):
    add_imports = ["from ml_orchestrator import MetaComponent"]
    op.add_imports = add_imports
    comp_list = [ComponentTestB(), ComponentTestA()]
    file_name = f"{str(op.only_function).lower()}-t_comps2.py"
    file_path = tmp_files_folder / Path(file_name)
    op.parse_components_to_file(comp_list, file_path.as_posix())
    assert "from ml_orchestrator import MetaComponent" in op.add_imports
    file_content = open(file_path, "r").read()
    assert "from ml_orchestrator import MetaComponent" in file_content
    assert "ComponentTestB(" in file_content
    assert "ComponentTestA(" in file_content
