# Example Flask API

This repository demonstrates a well-structured Flask API implementation with proper separation of concerns. It includes:

- Database integration with SQLAlchemy
- Service/Repository pattern for business logic separation
- Schema validation with Marshmallow
- Unit tests with pytest
- Type checking with mypy
- Code linting with ruff

## Requirements

- Python 3.13+
- uv (Python package installer)

## Installation

Install the project and its dependencies using uv:

```bash
uv sync
```

## Available Commands

Run the application in debug mode:
```bash
make run
```

Run the tests:
```bash
make test
```

## Project Structure

- `book_api/` - Main application package
  - `app.py` - Flask application setup
  - `models.py` - SQLAlchemy database models
  - `schemas.py` - Marshmallow serialization schemas
  - `service.py` - Business logic layer
  - `repo.py` - Data access layer
  - `db.py` - Database configuration
  - `exceptions.py` - Custom exception definitions

- `tests/` - Test suite
  - `test_service.py` - Service layer tests