# Text Summarization API (FastAPI + Redis)

A production-style text summarization API built with FastAPI.  
The service serves a pretrained NLP model and uses Redis to cache inference
results, reducing latency and repeated computation.

This project focuses on **backend engineering, ML model serving, and
infrastructure-aware design**, not on training machine learning models.

---

## Features

- REST API for text summarization
- Pretrained transformer-based model loaded once at startup
- Redis-backed caching for deterministic inputs
- Graceful fallback when Redis is unavailable
- Input validation with clear request/response contracts
- Fully Dockerized setup (API + Redis)

---

## Architecture

The system is intentionally layered to keep responsibilities isolated.

- **FastAPI**  
  Handles HTTP routing, request validation, and application lifecycle.

- **Summarization Service**  
  Encapsulates ML inference logic. The model is loaded once at startup and
  reused across requests.

- **Redis Cache**  
  Used strictly as an ephemeral cache (not a database). Cached results are
  keyed using deterministic hashing of input text.

- **Docker Compose**  
  Orchestrates the API service and Redis service with a private container
  network.

### Request Flow

1. Client sends text to `/summarize`
2. Input text is hashed to generate a cache key
3. Redis is checked for a cached summary
4. If cache hit → summary is returned immediately
5. If cache miss → model runs inference and result is cached with TTL

---

## API

### POST `/summarize`

Summarizes the provided text.

**Request**
```json
{
  "text": "Long input text to summarize"
}
Response

json
Copy code
{
  "summary": "Generated summary"
}
Input validation:

Minimum and maximum text length enforced

Invalid input returns a 422 validation error

GET /health
Health check endpoint.

Response

json
Copy code
{
  "status": "ok"
}
Running the Project (Docker)
Prerequisites
Docker

Docker Compose

Run
bash
Copy code
docker compose up --build
The API will be available at:

http://localhost:8000

Swagger UI: http://localhost:8000/docs

Notes & Design Decisions
Redis is used only as a cache; cached data is ephemeral by design

Cache data is cleared on restarts or redeploys

First request may be slow due to model warm-up and cold cache

Subsequent identical requests are served from Redis

The system remains functional even if Redis is unavailable

Tech Stack
Python

FastAPI

HuggingFace Transformers

PyTorch

Redis

Docker & Docker Compose

yaml
Copy code

---

### What this README does **right**
- No beginner language
- No “learning project” nonsense
- Explains **why** decisions exist
- Matches how real backend + ML services are described
- Clean enough for recruiters, reviewers, and interviews

### What you should do next
1. Paste this into `README.md`
2. Commit it:
```bash
git add README.md
git commit -m "docs: add final project README"
