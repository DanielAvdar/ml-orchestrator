from ml_orchestrator.comp_parser import ComponentParser
from ml_orchestrator.env_params import EnvironmentParams
from tests.dummy_components import ComponentTestA, ComponentTestB

params = dict(
    base_image="base_image",
    target_image="target_image",
    packages_to_install=["packages_to_install", ""],
    pip_index_urls=["pip_index_urls"],
    output_component_file="output_component_file",
    install_kfp_package=True,
    kfp_package_path="kfp_package_path",
)


def test_fun_op():
    component1 = ComponentTestB()
    op = ComponentParser()
    str_func = op.create_function(component=component1)
    assert str(component1.param_1) in str_func
    assert str(component1.param_2) in str_func
    assert "param_1" in str_func and "param_1=param_1" in str_func
    assert "param_2" in str_func and "param_2=param_2" in str_func
    assert component1.kfp_func_name in str_func
    assert "def " in str_func
    assert "execute" in str_func
    assert "comp" in str_func
    assert ">" not in str_func and "<" not in str_func
    assert "import" in str_func
    assert "," in str_func
    assert "(" in str_func and ")" in str_func
    assert "\t" in str_func
    assert " " in str_func
    assert "[Dataset]" in str_func
    assert "Input" in str_func
    assert "Output" in str_func


def test_dec_op():
    str_func = ComponentParser.create_decorator(EnvironmentParams())

    assert "None" not in str_func
    assert "@component" in str_func
    assert "(\n\t\n)" in str_func

    str_func = ComponentParser.create_decorator(EnvironmentParams(**params))

    assert "(\n\t\n)" not in str_func and "()" not in str_func
    assert "None" not in str_func
    for k, v in params.items():
        assert str(v).replace(", '", ", f'").replace("['", "[f'") in str_func
        assert k in str_func


def test_write_to_file():
    op = ComponentParser()
    content = op.create_kfp_str(component=ComponentTestB())
    op.write_to_file("t_file.py", content)


def test_list_of_comp_write_to_file():
    op = ComponentParser()
    comp_list = [ComponentTestB(), ComponentTestA()]
    op.parse_components_to_file(comp_list, "t_comps.py")
