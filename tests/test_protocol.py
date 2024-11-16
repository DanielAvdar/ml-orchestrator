from ml_orchestrator.comp_protocol.comp_protocol import ComponentProtocol


def test_protocol_meta_component(dummy_component):
    assert isinstance(dummy_component, ComponentProtocol)
