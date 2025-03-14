from book_api.models import Book


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

    def save(self, book):
        self.session.add(book)
        self.session.commit()
        return book
