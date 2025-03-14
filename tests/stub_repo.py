from book_api.exceptions import DuplicateBookError
from book_api.models import Book
from book_api.repo import AbstractBookRepository


class StubBookRepository(AbstractBookRepository):
    def __init__(self, books=None):
        if books:
            print(books)
            self.books = books
        else:
            self.books = {}

    def get_all(self):
        return list(self.books.values())

    def get_by_id(self, book_id):
        books = list(filter(lambda b: b.id == book_id, self.books.values()))
        if not books:
            raise ValueError(f"Book with id {book_id} not found.")
        return books[0]

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

    def delete(self, book_id):
        book = self.get_by_id(book_id)
        del self.books[book.isbn]
        return book
