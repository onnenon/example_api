from typing import List, Optional

from book_api.models import Book
from book_api.repo import AbstractBookRepository
from book_api.schemas import BookSchema


class BookService:
    def __init__(self, book_repository: AbstractBookRepository):
        self.book_repository = book_repository

    def get_all_books(self) -> List[BookSchema]:
        """
        Retrieve all books from the repository.

        Returns:
            list[BookSchema]: A list of all books.
        """
        return [
            BookSchema.model_validate(book) for book in self.book_repository.get_all()
        ]

    def create_book(self, book_data: BookSchema) -> BookSchema:
        """
        Creates a new book record in the repository.

        Args:
            book_data (BookSchema): The data of the book to be created.

        Returns:
            BookSchema: The created book data after being saved in the repository.

        Raises:
            DuplicateBookError: If a book with the same ISBN already exists.
        """
        book = Book.from_schema(book_data)
        saved_book = self.book_repository.save(book)
        return BookSchema.model_validate(saved_book)

    def get_book(self, book_id: int) -> Optional[BookSchema]:
        """
        Retrieve a book by its ID.

        Args:
            book_id (int): The unique identifier of the book to retrieve.

        Returns:
            BookSchema: The book corresponding to the given ID, or None if no
            book is found.
        """
        try:
            book = self.book_repository.get_by_id(book_id)
            return BookSchema.model_validate(book)
        except ValueError:
            return None

    def delete_book(self, book_id: int) -> bool:
        """
        Deletes a book from the repository.

        Args:
            book_id (int): The ID of the book to be deleted.

        Returns:
            bool: True if the book was successfully deleted, False otherwise.
        """
        try:
            self.book_repository.delete(book_id)
            return True
        except ValueError:
            return False

    def get_all_books_by_author(self, author: str) -> List[BookSchema]:
        """
        Retrieve all books by a specific author.

        Args:
            author (str): The name of the author.

        Returns:
            list[BookSchema]: A list of books written by the specified author.
        """
        return [book for book in self.get_all_books() if book.author == author]
