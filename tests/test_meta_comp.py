from tests.dummy_components import ComponentTestA, ComponentTestB


def test_base_class():
    assert set(ComponentTestA.comp_fields()).issubset(set(ComponentTestB.comp_fields()))


def test_base_instance():
    comp1 = ComponentTestA()
    comp2 = ComponentTestB()
    assert set(comp1.comp_vars().values()).issubset(set(comp2.comp_vars().values()))
