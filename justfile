venv:
  uv venv
run:
  uv run -- uvicorn --reload fastapi_timezone.main:app
