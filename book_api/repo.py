import logging
from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, scoped_session

from book_api.exceptions import DuplicateBookError
from book_api.models import Book

logger = logging.getLogger(__name__)


class AbstractBookRepository(ABC):
    """
    Abstract base class defining the interface for book repositories.

    This could be generic, but for simplicity, we are keeping it specific to the
    Book model. Subclasses should implement the methods to interact with the underlying
    data store.
    """

    @abstractmethod
    def get_all(self) -> List[Book]:
        """Retrieve all books."""
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Book:
        """Retrieve a book by its ID."""
        pass

    @abstractmethod
    def save(self, book: Book) -> Book:
        """Save a book to the repository."""
        pass

    @abstractmethod
    def delete(self, book_id: int) -> Book:
        """Delete a book from the repository."""
        pass


class BookRepository(AbstractBookRepository):
    """
    Implementation of the Book repository using SQLAlchemy and a DataBase
    as the data store.
    """

    def __init__(self, session: scoped_session[Session]) -> None:
        self.session = session

    def get_all(self) -> List[Book]:
        return self.session.query(Book).all()

    def get_by_id(self, book_id: int) -> Book:
        book = self.session.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise ValueError(f"Book with id {book_id} not found.")
        return book

    def delete(self, book_id: int) -> Book:
        book = self.get_by_id(book_id)
        self.session.delete(book)
        self.session.commit()
        return book

    def save(self, book: Book) -> Book:
        try:
            self.session.add(book)
            self.session.commit()
            return book
        except IntegrityError as e:
            logger.error(f"Error saving book with ISBN {book.isbn}")
            self.session.rollback()
            raise DuplicateBookError(
                f"Book with ISBN {book.isbn} already exists."
            ) from e
