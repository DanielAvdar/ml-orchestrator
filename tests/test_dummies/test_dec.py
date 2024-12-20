from ml_orchestrator import ComponentParser
from ml_orchestrator.meta_comp import MetaComponentV2


def test_create_kfp_decorator(dummy_meta_classes_all):
    op_dec = ComponentParser()
    if issubclass(dummy_meta_classes_all, MetaComponentV2):
        ob_to_check = dummy_meta_classes_all
        env_ob = ob_to_check.env().__dict__
    else:
        ob_to_check = dummy_meta_classes_all()
        env_ob = ob_to_check.env.__dict__
    dec_str = op_dec.create_decorator(ob_to_check)

    assert "@component" in dec_str
    assert "base_image" in dec_str if env_ob["base_image"] is not None else True
    assert "install_kfp_package" in dec_str if env_ob["install_kfp_package"] is not None else True
    assert "packages_to_install" in dec_str if env_ob["packages_to_install"] is not None else True
    assert "pip_index_urls" in dec_str if env_ob["pip_index_urls"] is not None else True
    assert "target_image" in dec_str if env_ob["target_image"] is not None else True
    assert "kfp_package_path" in dec_str if env_ob["kfp_package_path"] is not None else True
    assert ":" not in dec_str
    assert "(" in dec_str
    assert ")" in dec_str
    assert "None" not in dec_str
