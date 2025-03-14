from flask import Flask, request

from py_api.db import init_db
from py_api.models import Book
from py_api.schemas import BookSchema

app = Flask(__name__)


@app.route("/health")
def health_check():
    return {"status": "healthy"}, 200


@app.route("/books", methods=["GET"])
def get_books():
    books = Book.get_all()
    return {
        "books": [
            {"id": book.id, "title": book.title, "author": book.author}
            for book in books
        ]
    }, 200


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        book = Book.get_by_id(book_id)
        return {"id": book.id, "title": book.title, "author": book.author}, 200
    except ValueError as e:
        return {"error": str(e)}, 404


@app.route("/books", methods=["POST"])
def create_book():
    try:
        book_data = BookSchema().load(request.get_json())
        new_book = Book(title=book_data["title"], author=book_data["author"])
        new_book.save()  # Save the book to the database
        return {"message": "Book created successfully", "id": new_book.id}, 201
    except Exception as e:
        print(e)
        return {"error": "Failed to create book"}, 400


def create_app():
    with app.app_context():
        init_db()
    return app
