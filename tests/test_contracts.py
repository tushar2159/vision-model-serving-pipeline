import pytest
from vision_serving.predict import build_demo_router
def test_router_contract():
    r=build_demo_router()
    assert r.predict("classification",[1.0])["task"]=="classification"
def test_unknown_task():
    with pytest.raises(ValueError):
        build_demo_router().predict("unknown",[])
