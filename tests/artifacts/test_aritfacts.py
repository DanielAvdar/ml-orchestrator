import kfp.dsl as dsl
import pytest

import ml_orchestrator.artifacts as moa
from ml_orchestrator.artifacts.artifact import JSONSerializableDict


@pytest.fixture(params=["Dataset", "Metrics", "Model", "Artifact", "Markdown"])
def artifact_instances(request):
    artifact = request.param
    moa_ = getattr(moa, artifact)
    dsl_ = getattr(dsl, artifact)
    moa_i = moa_(
        uri="uri",
        name="name",
    )
    dsl_i = dsl_(
        uri="uri",
        name="name",
    )
    return moa_, dsl_, moa_i, dsl_i


def test_artifact_schema_title(artifact_instances):
    moa_, dsl_, _, _ = artifact_instances
    assert moa_.schema_title == dsl_.schema_title


def test_artifact_metadata_invalid(artifact_instances):
    _, _, moa_i, _ = artifact_instances
    with pytest.raises(ValueError):
        moa_i.metadata["invalid"] = object


def test_artifact_metadata_set_and_compare(artifact_instances):
    _, _, moa_i, dsl_i = artifact_instances
    moa_i.metadata = dict(some_meta="some_meta")
    dsl_i.metadata = dict(some_meta="some_meta")
    moa_i.metadata["str"] = "str"
    dsl_i.metadata["str"] = "str"
    moa_i.metadata["int"] = 1
    dsl_i.metadata["int"] = 1
    moa_i.metadata["float"] = 1.0
    dsl_i.metadata["float"] = 1.0
    moa_i.metadata["bool"] = True
    dsl_i.metadata["bool"] = True
    moa_i.metadata["list"] = [1, 2, 3]
    dsl_i.metadata["list"] = [1, 2, 3]
    moa_i.metadata["dict"] = dict(a=1, b="2", c=3.0, d=True)
    dsl_i.metadata["dict"] = dict(a=1, b="2", c=3.0, d=True)
    assert moa_i.metadata == dsl_i.metadata
    assert isinstance(moa_i.metadata, JSONSerializableDict)


def test_artifact_name_and_path(artifact_instances):
    _, _, moa_i, dsl_i = artifact_instances
    assert moa_i.name == dsl_i.name
    assert moa_i.path == dsl_i.path


def test_artifact_metadata_assignment_invalid(artifact_instances):
    _, _, moa_i, _ = artifact_instances
    with pytest.raises(ValueError):
        moa_i.metadata = dict(a=1, b="2", c=3.0, d=True, obj=object())
    with pytest.raises(ValueError):
        moa_i.metadata.update(dict(a=1, b="2", c=3.0, d=True, obj=object()))
    with pytest.raises(ValueError):
        moa_i.metadata | dict(a=1, b="2", c=3.0, d=True, obj=object())
    valid_mapping = moa_i.metadata | dict(
        a=1,
        b="2",
        c=3.0,
        d=True,
    )
    assert isinstance(valid_mapping, JSONSerializableDict)


def test_html_with_kfp():
    moa_ = moa.HTML
    dsl_ = dsl.HTML
    moa_i = moa_(
        uri="uri",
        name="name",
    )
    dsl_i = dsl_(
        uri="uri",
        name="name",
    )
    assert moa_.schema_title == dsl_.schema_title
    moa_i.metadata = dict(some_meta="some_meta")
    dsl_i.metadata = dict(some_meta="some_meta")
    assert moa_i.name == dsl_i.name
    assert moa_i.path == dsl_i.path + ".html"
    assert moa_i.metadata == dsl_i.metadata
    assert moa_i.uri == dsl_i.uri + ".html"


def test_log_metrics():
    moa_ = moa.Metrics(
        uri="uri",
        name="name",
    )
    dsl_ = dsl.Metrics(
        uri="uri",
        name="name",
    )
    metrics = dict(
        int_metric=1,
        float_metric=1.0,
        bool_metric=True,
        str_metric="str",
        list_metric=[1, 2, 3],
        dict_metric=dict(a=1, b="2", c=3.0, d=True),
    )
    for k, v in metrics.items():
        moa_.log_metric(k, v)
        dsl_.log_metric(k, v)
    with pytest.raises(ValueError):
        moa_.log_metric("invalid", object())

    assert moa_.metadata == dsl_.metadata
