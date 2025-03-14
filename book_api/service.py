from book_api.models import Book


class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def get_all_books(self):
        return self.book_repository.get_all()

    def create_book(self, title, author):
        book = Book(title=title, author=author)
        return self.book_repository.save(book)

    def get_book(self, book_id):
        return self.book_repository.get_by_id(book_id)
