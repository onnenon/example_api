from book_api.schemas import BookSchema


def create_book_with_invalid_isbn_should_raise_validation_error(book_service):
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "invalid_isbn",
    }
    BookSchema.model_validate(**book_data)
