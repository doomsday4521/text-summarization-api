from fastapi.testclient import TestClient
from app.main import app
from tests.fakes import FakeRedis
from app.services.rate_limiter import RateLimiter

client = TestClient(app)

def test_rate_limiting_blocks_excess_requests():
    fake_redis = FakeRedis()

    app.state.rate_limiter = RateLimiter(
        redis_client=fake_redis,
        limit=2,
        window=60
    )

    payload = {
        "text": "FastAPI is a modern Python framework designed for APIs."
    }

    assert client.post("/summarize", json=payload).status_code == 200
    assert client.post("/summarize", json=payload).status_code == 200
    assert client.post("/summarize", json=payload).status_code == 429
