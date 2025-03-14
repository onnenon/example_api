from book_api.models import Book


class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def get_all_books(self):
        return self.book_repository.get_all()

    def create_book(self, title, author, isbn):
        """
        Creates a new book with the given title, author, and ISBN, and saves it to the repository.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.

        Returns:
            Book: The saved book instance.
        Raises:
            DuplicateBookError: If a book with the same ISBN already exists in the repository.
        """
        book = Book(title=title, author=author, isbn=isbn)
        return self.book_repository.save(book)

    def get_book(self, book_id):
        return self.book_repository.get_by_id(book_id)
