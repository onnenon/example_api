run:
	uv run flask --app book_api/app:create_app --debug run
test:
	uv run pytest .
pretty:
	uv run ruff format .
	uv run ruff check --fix .
reset-db:
	rm -rf test.db