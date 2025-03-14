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

Format and lint the code:
```bash
make pretty
```
This command will:
- Format the code using ruff formatter
- Run the ruff linter and apply auto-fixes where possible

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

## API Testing with Bruno
This project includes a collection of API requests that can be imported into Bruno, a modern API client.

### Setting up Bruno
1. Install Bruno from https://www.usebruno.com/
2. Open Bruno
3. Click "Open Collection" or use the keyboard shortcut
4. Navigate to the `requests_collection` folder in this repository
5. Select the folder to import all the available API requests

### Available Requests
The collection includes the following requests:
- Health Check - Test the API's health endpoint
- Create Book - Create a new book
- Get Books - List all books
- Get Book - Retrieve a specific book
- Delete Book - Remove a book

Each request is pre-configured with the appropriate HTTP method, headers, and body structure for testing the API endpoints.