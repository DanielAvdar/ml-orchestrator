import pytest

from dummy_components.dummy_components import ComponentTestB
from ml_orchestrator.comp_parser import ComponentParser
from ml_orchestrator.env_params import EnvironmentParams

params = dict(
    base_image="base_image",
    target_image="target_image",
    packages_to_install=["packages_to_install", ""],
    pip_index_urls=["pip_index_urls"],
    install_kfp_package=True,
    kfp_package_path="kfp_package_path",
)


@pytest.mark.parametrize("only_function", [True, False])
def test_fun_op(only_function):
    component1 = ComponentTestB()
    op = ComponentParser(only_function=only_function)
    str_func = op.create_function(component=component1)
    assert str(component1.param_1) in str_func
    assert str(component1.param_2) in str_func
    assert "param_1" in str_func and "param_1=param_1" in str_func
    assert "param_2" in str_func and "param_2=param_2" in str_func
    assert component1.kfp_func_name() in str_func
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
    assert "ComponentTestB(" in str_func

    if only_function:
        assert str_func == op.create_kfp_str(component=component1)
    else:
        assert str_func != op.create_kfp_str(component=component1)


def test_dec_op():
    str_func = ComponentParser.create_decorator(EnvironmentParams())

    assert "None" not in str_func
    assert "@component" in str_func
    assert "(\n\t\n)" in str_func

    str_func = ComponentParser.create_decorator(EnvironmentParams(**params))

    assert "(\n\t\n)" not in str_func and "()" not in str_func
    assert "None" not in str_func
    for k, v in params.items():
        parsed = ComponentParser.convert_to_format_str(str(v))
        assert parsed in str_func
        assert k in str_func
    assert ":" not in str_func
