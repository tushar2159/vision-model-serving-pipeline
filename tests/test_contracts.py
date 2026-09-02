import pytest
from fastapi.testclient import TestClient

from vision_serving.api import app
from vision_serving.predict import build_demo_router


def test_router_contract():
    r = build_demo_router()
    assert r.predict("classification", [1.0])["task"] == "classification"


def test_unknown_task():
    with pytest.raises(ValueError):
        build_demo_router().predict("unknown", [])


def test_health_and_readiness_contracts():
    client = TestClient(app)
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/ready").json()["tasks"] == ["classification", "detection", "segmentation"]


def test_predict_validates_and_routes_request():
    client = TestClient(app)
    response = client.post("/predict", json={"task": "classification", "values": [1.0]})
    assert response.status_code == 200
    assert response.json()["task"] == "classification"
    assert client.post("/predict", json={"task": "unknown", "values": []}).status_code == 422
