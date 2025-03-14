import pytest

from book_api.exceptions import DuplicateBookError


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


def create_duplicate_book_should_raise_duplicate_book_error(book_service):
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890123",
    }
    book_service.create_book(**book_data)
    with pytest.raises(DuplicateBookError):
        book_service.create_book(**book_data)


def test_get_all_books_should_return_all_books(seeded_book_service):
    books = seeded_book_service.get_all_books()
    assert len(books) == 2
    assert books[0].title == "Test Book"
    assert books[1].title == "Test Book 2"


def test_get_all_books_should_return_empty_list_when_no_books(book_service):
    books = book_service.get_all_books()
    assert len(books) == 0


def test_get_book_should_return_book_by_id(seeded_book_service):
    book = seeded_book_service.get_book(1)
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.isbn == "1234567890123"


def test_get_book_should_return_none_when_book_not_found(book_service):
    book = book_service.get_book(999)
    assert book is None


def test_delete_book_should_delete_book_successfully(seeded_book_service):
    assert seeded_book_service.delete_book(1) is True
    assert seeded_book_service.get_book(1) is None


def test_delete_book_should_return_false_if_it_does_not_exist(book_service):
    assert book_service.delete_book(999) is False


def test_get_all_books_by_author_should_return_books_by_author(seeded_book_service):
    books = seeded_book_service.get_all_books_by_author("Test Author")
    assert len(books) == 1
    assert books[0].title == "Test Book"


def test_get_all_books_by_author_should_return_empty_list_if_no_books_by_author(
    seeded_book_service,
):
    books = seeded_book_service.get_all_books_by_author("Nonexistent Author")
    assert len(books) == 0
