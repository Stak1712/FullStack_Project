# ИИ-платформа для прохождения технических собеседований с виртуальным интервьюером.

## Быстрый запуск (локальный)

```bash и PowerShell
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate или .\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -e .
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/v1/health/live
- http://127.0.0.1:8000/docs

## Docker
```bash
docker compose up --build
```

## Макет проекта
```
app/
  core/
  api/v1/endpoints/
  schemas/
  services/
  models/
tests/
```
