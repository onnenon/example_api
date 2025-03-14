import pytest
from pydantic import ValidationError

from book_api.schemas import BookSchema


def test_create_book_with_isbn_not_13_characters_should_raise_validation_error():
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "invalid_isbn",
    }
    with pytest.raises(ValidationError):
        BookSchema.model_validate(book_data)


def test_create_book_with_isbn_not_digit_should_raise_validation_error():
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890abc",
    }
    with pytest.raises(ValidationError):
        BookSchema.model_validate(book_data)
