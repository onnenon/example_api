import pytest

from book_api.flask_app import create_app
from book_api.models import Book
from book_api.service import BookService
from tests.stub_repo import StubBookRepository


@pytest.fixture
def book_service():
    return BookService(StubBookRepository())


@pytest.fixture()
def seeded_book_service():
    """Fixture to seed the book service with initial data."""
    books = {
        "1234567890123": Book(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            id=1,
        ),
        "1234567890122": Book(
            title="Test Book 2",
            author="Test Author 2",
            isbn="1234567890122",
            id=2,
        ),
    }
    bs = StubBookRepository(books)
    return BookService(bs)


@pytest.fixture()
def flask_app():
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture()
def flask_client(flask_app):
    return flask_app.test_client()
