import pytest

from dummy_components.dummy_components import ComponentTestA, ComponentTestB


@pytest.mark.skip
def test_base_class():
    assert set(ComponentTestA.comp_fields()).issubset(set(ComponentTestB.comp_fields()))


@pytest.mark.skip
def test_base_instance():
    comp1 = ComponentTestA()
    comp2 = ComponentTestB()
    assert set(comp1.comp_vars().values()).issubset(set(comp2.comp_vars().values()))
