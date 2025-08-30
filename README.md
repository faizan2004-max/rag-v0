# RAG v0

A minimal Retrieval-Augmented Generation (RAG) system.

## Features
- FastAPI service with `/health` endpoint.
- Dockerized app (Python 3.10-slim).
- CI/CD with GitHub Actions (pytest).
- Unit test for health check.

## Quickstart
```bash
# Run locally
uvicorn src.main:app --reload

# Run in Docker
docker build -t rag-v0 .
docker run -p 8000:8000 rag-v0
