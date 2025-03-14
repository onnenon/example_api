from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Date


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(255), nullable=False)
    author = mapped_column(String(255), nullable=False)
    published_date = mapped_column(Date, nullable=True)
    isbn = mapped_column(String(13), unique=True, nullable=False)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
