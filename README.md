# ML Text Summarization API

A FastAPI-based backend service that provides text summarization via a REST API.
The project focuses on backend engineering fundamentals such as validation,
caching, rate limiting, configuration management, and automated testing.

This is a backend-oriented project, not a research or model-training repository.

---

## Features

- Text summarization using a pretrained transformer model
- Input validation with strict length constraints
- Redis-backed caching to avoid repeated inference
- Redis-backed rate limiting to prevent abuse
- Clean configuration using Pydantic v2
- Fully automated tests with pytest

---

## Architecture Overview

Request flow:

Client  
→ FastAPI  
→ Request Validation (Pydantic)  
→ Rate Limiting  
→ Cache Lookup (Redis)  
→ Model Inference (on cache miss)  
→ Response

Key components:
- **FastAPI** for routing and request handling
- **Transformer model** for summarization
- **Redis** for caching and rate limiting
- **pytest** for automated testing

---

## API Endpoints

### Health Check

```http
GET /health

Response:
{
  "status": "ok"
}
Summarize Text
POST /summarize
Request body:
{
  "text": "Long input text to summarize..."
}
Constraints:

Minimum length: 20 characters

Maximum length: 4000 characters

{
  "summary": "Generated summary text"
}
Caching

Summaries are cached in Redis using a hash of the input text as the key

Identical requests reuse cached results

Cache TTL is configurable via environment variables

Caching behavior is covered by automated tests to ensure inference is skipped
when cached data is available.

Rate Limiting

Fixed-window rate limiting using Redis

Limits requests per client IP

Returns HTTP 429 Too Many Requests when the limit is exceeded

Designed to fail open if Redis is unavailable

Testing

The project includes automated tests using pytest and FastAPI’s TestClient.

Test coverage includes:

Application startup and health check

Successful summarization requests

Validation failures

Cache behavior

Rate limiting behavior

Run tests:
pytest -v

All tests run locally without requiring Docker or a running Redis instance.

Configuration

Configuration is managed with Pydantic Settings (v2).

Examples of configurable values:

Model name

Redis connection URL

Cache TTL

Debug mode

Environment variables can be provided via a .env file.

Limitations

Inference is synchronous and CPU-bound

Not optimized for high-throughput workloads

No authentication or user-level authorization

Intended for low-to-moderate traffic scenarios

These trade-offs are intentional to keep the system simple and focused.