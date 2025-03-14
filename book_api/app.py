import logging

import werkzeug.exceptions
from flask import Flask, request
from marshmallow import ValidationError

from book_api.db import db_session, init_db
from book_api.exceptions import DuplicateBookError
from book_api.repo import BookRepository
from book_api.schemas import BookSchema
from book_api.service import BookService


class AppDefinition:
    def __init__(self):
        self.api = Flask(__name__)
        self.book_repository = BookRepository(db_session)
        self.book_service = BookService(self.book_repository)


app = AppDefinition()

logger = logging.getLogger(__name__)


@app.api.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return {"error": str(e)}, 400


@app.api.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(e):
    return {"error": "not found"}, 404


@app.api.route("/health")
def health_check():
    logger.debug("Health check endpoint called")
    return {"status": "healthy"}, 200


@app.api.route("/books", methods=["GET"])
def get_books():
    books = app.book_service.get_all_books()
    return {"books": [BookSchema().dump(book) for book in books]}, 200


@app.api.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = app.book_service.get_book(book_id)
    if not book:
        return {"error": f"Book not found with ID {book_id}"}, 404
    return {"book": BookSchema().dump(book)}, 200


@app.api.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        deleted_book = app.book_service.delete_book(book_id)
        return {
            "message": "Book deleted successfully",
            "book": BookSchema().dump(deleted_book),
        }, 200
    except ValueError as e:
        return {"error": str(e)}, 404
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": "An unexpected error occurred"}, 500


@app.api.route("/books", methods=["POST"])
def create_book():
    try:
        book_data = BookSchema().load(request.json)
        new_book = app.book_service.create_book(**book_data)
        return {"message": "Book created successfully", "id": new_book.id}, 201
    except ValidationError as e:
        logger.error(f"Validation error: {e.messages}")
        return {"error": e.messages}, 400
    except DuplicateBookError as e:
        logger.error(f"Duplicate book error: {str(e)}")
        return {"error": str(e)}, 409


def create_app():
    app.api.logger.setLevel(logging.DEBUG)

    with app.api.app_context():
        init_db()
    return app.api
