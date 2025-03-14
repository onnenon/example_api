from flask import Flask, request

from py_api.db import init_db, db_session
from py_api.models import Book

app = Flask(__name__)


@app.route("/health")
def health_check():
    return {"status": "healthy"}, 200


@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return {
        "books": [
            {"id": book.id, "title": book.title, "author": book.author}
            for book in books
        ]
    }, 200


@app.route("/books", methods=["POST"])
def create_book():
    book_data = request.get_json()
    print(book_data)
    new_book = Book(title=book_data["title"], author=book_data["author"])
    db_session.add(new_book)
    db_session.commit()

    return {"message": "Book created successfully"}, 201


def create_app():
    with app.app_context():
        init_db()
    return app
