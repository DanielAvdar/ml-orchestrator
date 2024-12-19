from ml_orchestrator.comp_protocol.func_parser import IMPORT_COMPOUND, FunctionParser


def test_get_class(dummy_component_class):
    fp = FunctionParser()

    assert fp.get_class_def(dummy_component_class) == dummy_component_class


def test_get_class_cons(dummy_component_class_):
    fp = FunctionParser()
    inst = dummy_component_class_()
    assert fp.get_class_def(inst) == dummy_component_class_


def test_class(dummy_component_class):
    fp = FunctionParser()
    comp_function = fp.create_function(dummy_component_class)
    comp_function_with_imports = IMPORT_COMPOUND + "\n" + comp_function
    exec(comp_function_with_imports)


def test_instances(dummy_component):
    fp = FunctionParser()
    comp_function = fp.create_function(dummy_component)
    comp_function_with_imports = IMPORT_COMPOUND + "\n" + comp_function
    exec(comp_function_with_imports)
