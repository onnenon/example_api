run:
	uv run flask --app book_api/flask_app:create_app --debug run
run-fastapi:
	uv run fastapi dev book_api/fastapi_app.py
test:
	uv run pytest .
pretty:
	uv run ruff format .
	uv run ruff check --fix .
reset-db:
	rm -rf test.db
check:
	uv run mypy book_api tests
	uv run ruff format --check
	uv run ruff check