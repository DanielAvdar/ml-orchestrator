from pathlib import Path


def test_write_to_file_base(fp, dummy_component_class, write_dummies_files_folder):
    name = dummy_component_class.__name__
    comp_func_name = fp.comp_func_name(dummy_component_class)
    assert name.lower() == comp_func_name.replace("_", "")
    content = fp.create_kfp_file_str(components=[dummy_component_class])
    file_name = f"base_{comp_func_name}.py"
    file_path = write_dummies_files_folder / Path(file_name)
    fp._write_to_file(file_path, content)
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
