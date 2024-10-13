venv:
  uv venv
run:
  uv run -- uvicorn --reload fastapi_timezone.main:app

get:
  sqlite3 -header -box database.db 'select * from message;'

tables:
  sqlite3 -header -box database.db "SELECT * from sqlite_master;"
