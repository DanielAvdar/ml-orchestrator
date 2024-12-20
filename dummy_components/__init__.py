from dummy_components import (
    dummy_components as dcomps,
    dummy_components_v2 as dv2comps,
    invalid_protocol_components as ipcomps,
    protocol_components as pcomps,
)

valid_classes_meta = [
    dcomps.ComponentTestB,
    dcomps.ComponentTestA,
    dcomps.ComponentTestC,
    dcomps.ComponentTestC2,
    dcomps.ComponentTestC3,
    dcomps.ComponentTestD,
    dcomps.ComponentTestD2,
]
valid_classes_meta_v2 = [
    dv2comps.ComponentTestB,
    dv2comps.ComponentTestA,
    dv2comps.ComponentTestC,
    dv2comps.ComponentTestC2,
    dv2comps.ComponentTestC3,
    dv2comps.ComponentTestD,
    dv2comps.ComponentTestD2V2,
]
valid_classes_protocol = [
    pcomps.ComponentTestB,
    pcomps.ComponentTestA,
    pcomps.ComponentTestC,
    pcomps.ComponentTestC2,
    pcomps.ComponentTestC3,
]
invalid_classes_protocols = [
    ipcomps.ComponentTestB,
    ipcomps.ComponentTestA,
]


valid_classes = valid_classes_meta + valid_classes_meta_v2 + valid_classes_protocol + valid_classes_meta_v2
