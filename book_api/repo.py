import logging

from sqlalchemy.exc import IntegrityError

from book_api.exceptions import DuplicateBookError
from book_api.models import Book

logger = logging.getLogger(__name__)


class BookRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Book).all()

    def get_by_id(self, book_id):
        book = self.session.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise ValueError(f"Book with id {book_id} not found.")
        return book

    def delete(self, book_id):
        book = self.get_by_id(book_id)
        self.session.delete(book)
        self.session.commit()
        return book

    def save(self, book):
        try:
            self.session.add(book)
            self.session.commit()
            return book
        except IntegrityError as e:
            logger.exception(str(e))
            self.session.rollback()
            raise DuplicateBookError(
                f"Book with ISBN {book.isbn} already exists."
            ) from e
