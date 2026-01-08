from fastapi.testclient import TestClient
from app.main import app

from tests.fakes import FakeCache, SpyModel
client = TestClient(app)

def test_summarize_success():
    payload = {
        "text": "FastAPI is a modern Python web framework for building APIs."
    }

    response = client.post("/summarize", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 0

def test_summarize_empty_text():
    response = client.post("/summarize", json={"text": ""})

    assert response.status_code == 422


def test_summarize_uses_cache():
    fake_cache = FakeCache()
    spy_model = SpyModel()

    app.state.cache = fake_cache
    app.state.model = spy_model

    payload = {
        "text": "FastAPI is a modern Python web framework designed for APIs."
    }

    # First request → cache miss → model called
    response1 = client.post("/summarize", json=payload)
    assert response1.status_code == 200
    assert spy_model.call_count == 1

    # Second request → cache hit → model NOT called again
    response2 = client.post("/summarize", json=payload)
    assert response2.status_code == 200
    assert spy_model.call_count == 1