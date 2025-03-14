import pytest

from book_api.exceptions import DuplicateBookError
from book_api.models import Book
from book_api.service import BookService


class MockBookRepository:
    def __init__(self, books=None):
        if books:
            print(books)
            self.books = books
        else:
            self.books = {}

    def get_all(self):
        return list(self.books.values())

    def get_by_id(self, book_id):
        return list(filter(lambda b: b.id == book_id, self.books.values()))[0]

    def save(self, book):
        if self.books.get(book.isbn) is not None:
            raise DuplicateBookError("Book already exists.")
        book = Book(
            id=len(self.books.keys()) + 1,
            title=book.title,
            author=book.author,
            isbn=book.isbn,
        )
        self.books[book.isbn] = book
        return book


@pytest.fixture
def book_service():
    return BookService(MockBookRepository())


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
    bs = MockBookRepository(books)
    return BookService(bs)


def test_create_book_should_create_book_successfully(book_service):
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890123",
    }
    book = book_service.create_book(**book_data)
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.isbn == "1234567890123"


def test_get_all_books_should_return_all_books(seeded_book_service):
    books = seeded_book_service.get_all_books()
    assert len(books) == 2
    assert books[0].title == "Test Book"
    assert books[1].title == "Test Book 2"


def test_get_book_should_return_book_by_id(seeded_book_service):
    book = seeded_book_service.get_book(1)
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.isbn == "1234567890123"
