# Pokemon Team Picker — Backend

FastAPI backend.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker

```bash
docker build -t pokemon-team-picker-backend .
docker run -p 8000:8000 pokemon-team-picker-backend
```

API available at http://localhost:8000, health check at `/health`.
