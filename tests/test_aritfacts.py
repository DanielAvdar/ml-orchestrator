import ml_orchestrator.artifacts as moa

import kfp.dsl as dsl
import pytest


@pytest.mark.parametrize(
    "artifact",
    [
        "Dataset",
        "Metrics",
        "Model",
        "Artifact",
        "Markdown",
    ],
)
def test_artifact_with_kfp(artifact):
    moa_ = getattr(moa, artifact)
    dsl_ = getattr(dsl, artifact)
    assert moa_.schema_title == dsl_.schema_title
    moa_i = moa_(
        uri="uri",
        name="name",
    )
    dsl_i = dsl_(
        uri="uri",
        name="name",
    )
    moa_i.metadata = dict(some_meta="some_meta")
    dsl_i.metadata = dict(some_meta="some_meta")
    assert moa_i.name == dsl_i.name
    assert moa_i.path == dsl_i.path
    assert moa_i.metadata == dsl_i.metadata


def test_html_with_kfp():
    moa_ = moa.HTML
    dsl_ = dsl.HTML
    assert moa_.schema_title == dsl_.schema_title
    moa_i = moa_(
        uri="uri",
        name="name",
    )
    dsl_i = dsl_(
        uri="uri",
        name="name",
    )
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
    )
    for k, v in metrics.items():
        moa_.log_metric(k, v)
        dsl_.log_metric(k, v)
    assert moa_.metadata == dsl_.metadata
