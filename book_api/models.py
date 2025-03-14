from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from book_api.db import Base


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(255), nullable=False)
    author = mapped_column(String(255), nullable=False)
    isbn = mapped_column(String(13), unique=True, nullable=False)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}, ISBN: {self.isbn}>"
