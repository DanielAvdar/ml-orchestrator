import importlib


def test_kfp_not_installed():
    # assert kfp not installed
    try:
        importlib.import_module("kfp")
    except ModuleNotFoundError:
        assert True
        return
    raise AssertionError()


def test_import_orchestrator():
    # assert orchestrator is installed
    from ml_orchestrator import (  # noqa
        ComponentParser,
        MetaComponent,
        EnvironmentParams,
        ProtocolCompSuite,
        FunctionParser,
    )

    assert True
