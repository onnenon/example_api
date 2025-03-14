from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from book_api.db import Base


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(255), nullable=False)
    author = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

    @classmethod
    def get_all(cls):
        """Fetch all books from the database."""
        return cls.session.query(Book).all()

    @classmethod
    def get_by_id(cls, book_id):
        """Fetch a book by its ID."""
        book = cls.session.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise ValueError(f"Book with id {book_id} not found.")
        return book

    def save(self):
        """Save the book instance to the database."""
        self.session.add(self)
        self.session.commit()
