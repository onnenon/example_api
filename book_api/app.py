import logging

import werkzeug.exceptions
from flask import Flask, request
from marshmallow import ValidationError

from book_api.db import db_session, init_db
from book_api.repo import BookRepository
from book_api.schemas import BookSchema
from book_api.service import BookService

app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return {"error": str(e)}, 400


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(e):
    return {"error": "not found"}, 404


@app.route("/health")
def health_check():
    logger.debug("Health check endpoint called")
    return {"status": "healthy"}, 200


@app.route("/books", methods=["GET"])
def get_books():
    books = app.book_service.get_all_books()
    return {"books": [BookSchema().dump(book) for book in books]}, 200


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        book = app.book_service.get_book(book_id)
        return {"book": BookSchema().dump(book)}, 200
    except ValueError as e:
        return {"error": str(e)}, 404


@app.route("/books", methods=["POST"])
def create_book():
    try:
        book_data = BookSchema().load(request.json)
        new_book = app.book_service.create_book(**book_data)
        return {"message": "Book created successfully", "id": new_book.id}, 201
    except ValidationError as e:
        logger.error(f"Validation error: {e.messages}")
        return {"error": e.messages}, 400
    except werkzeug.exceptions.BadRequest:
        return {
            "error": "Invalid JSON format or missing Content-Type: application/json header"
        }, 400


def create_app():
    app.logger.setLevel(logging.DEBUG)
    app.book_repository = BookRepository(db_session)
    app.book_service = BookService(app.book_repository)

    with app.app_context():
        init_db()
    return app
