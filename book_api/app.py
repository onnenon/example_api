import logging

import werkzeug.exceptions
from flask import Flask

from book_api.db import db_session, init_db
from book_api.repo import BookRepository
from book_api.service import BookService

logger = logging.getLogger(__name__)


class AppDefinition:
    def __init__(self):
        self.api = Flask(__name__)
        self.book_repository = BookRepository(db_session)
        self.book_service = BookService(self.book_repository)


app = AppDefinition()


@app.api.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return {"error": str(e)}, 400


@app.api.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(e):
    return {"error": "not found"}, 404


def create_app():
    app.api.logger.setLevel(logging.DEBUG)

    with app.api.app_context():
        init_db()
    return app.api
