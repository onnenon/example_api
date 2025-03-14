# Example API Project

This repository demonstrates well-structured API implementations using both Flask and FastAPI with proper separation of concerns. It includes:

- Database integration with SQLAlchemy
- Service/Repository pattern for business logic separation
- Schema validation with Pydantic
- Unit tests with pytest
- Type checking with mypy
- Code linting with ruff
- Dual implementations showcasing Flask and FastAPI approaches

## Requirements

- Python 3.13+
- uv (Python package installer)

## Installation

Install the project and its dependencies using uv:

```bash
uv sync
```

## Available Commands

Run the Flask application in debug mode:
```bash
make run
```

Run the FastAPI application:
```bash
make run-fastapi
```

Run the tests:
```bash
make test
```

Format and lint the code:
```bash
make pretty
```
This command will:
- Format the code using ruff formatter
- Run the ruff linter and apply auto-fixes where possible

Check code quality:
```bash
make check
```
This command will:
- Run type checking with mypy
- Verify code formatting with ruff
- Run the ruff linter without applying fixes

## Project Structure

- `book_api/` - Main application package
  - `flask_app.py` - Flask application implementation
  - `fastapi_app.py` - FastAPI application implementation
  - `models.py` - SQLAlchemy database models
  - `schemas.py` - Pydantic schemas for validation
  - `service.py` - Business logic layer
  - `repo.py` - Data access layer
  - `db.py` - Database configuration
  - `exceptions.py` - Custom exception definitions

- `tests/` - Test suite
  - `test_flask_app.py` - Flask application tests
  - `test_fastapi_app.py` - FastAPI application tests
  - `test_service.py` - Service layer tests

## API Testing with Bruno
This project includes collections of API requests that can be imported into Bruno, a modern API client.

### Setting up Bruno
1. Install Bruno from https://www.usebruno.com/
2. Open Bruno
3. Click "Open Collection" or use the keyboard shortcut
4. Navigate to the `requests_collection` folder in this repository
5. Select the folder to import all the available API requests

### Available Requests
The collection includes the following requests for both Flask and FastAPI implementations:
- Health Check - Test the API's health endpoint
- Create Book - Create a new book
- Get Books - List all books (supports optional author filter)
- Get Book - Retrieve a specific book
- Delete Book - Remove a book

Each request is pre-configured with the appropriate HTTP method, headers, and body structure for testing the API endpoints. The FastAPI requests can be found in the `FastApi` subfolder within the request collection.