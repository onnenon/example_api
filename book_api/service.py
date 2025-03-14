from typing import List, Optional

from book_api.models import Book
from book_api.repo import AbstractBookRepository


class BookService:
    def __init__(self, book_repository: AbstractBookRepository):
        self.book_repository = book_repository

    def get_all_books(self) -> List[Book]:
        """
        Retrieve all books from the repository.

        Returns:
            list: A list of all books.
        """
        return self.book_repository.get_all()

    def create_book(self, title: str, author: str, isbn: str) -> Book:
        """
        Creates a new book with the given title, author, and ISBN, and saves
        it to the repository.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.

        Returns:
            Book: The saved book instance.

        Raises:
            DuplicateBookError: If a book with the same ISBN already exists
            in the repository.
        """
        book = Book(title=title, author=author, isbn=isbn)
        return self.book_repository.save(book)

    def get_book(self, book_id: int) -> Optional[Book]:
        """
        Retrieve a book by its ID.

        Args:
            book_id (int): The unique identifier of the book to retrieve.

        Returns:
            Book: The book corresponding to the given ID, or None if no book is found.
        """
        try:
            book = self.book_repository.get_by_id(book_id)
            return book
        except ValueError:
            return None

    def delete_book(self, book_id):
        return self.book_repository.delete(book_id)
