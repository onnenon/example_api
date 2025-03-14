from typing import Annotated, Any, Dict, List

from fastapi import Depends, FastAPI
from pydantic import ValidationError

from book_api.exceptions import DuplicateBookError
from book_api.schemas import BookSchema
from book_api.service import BookService

app = FastAPI()


async def get_book_service():
    from book_api.db import db_session
    from book_api.repo import BookRepository

    book_repository = BookRepository(db_session)
    return BookService(book_repository)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/books")
async def get_books(
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Dict[str, List[BookSchema]]:
    books = book_service.get_all_books()
    return {"books": books}


@app.get("/books/{book_id}")
async def get_book(
    book_id: int,
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Dict[str, str] | Dict[str, BookSchema]:
    book = book_service.get_book(book_id)
    if not book:
        return {"error": f"Book not found with ID {book_id}"}
    return {"book": book}


@app.delete("/books/{book_id}")
async def delete_book(
    book_id: int,
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Dict[str, Any]:
    deleted_book = book_service.delete_book(book_id)
    if deleted_book:
        return {
            "message": "Book deleted successfully",
            "id": book_id,
        }
    return {"error": f"Book not found with ID {book_id}"}


@app.post("/books")
async def create_book(
    book: BookSchema,
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Dict[str, BookSchema | str]:
    try:
        created_book = book_service.create_book(book)
        return {"book": created_book}
    except ValidationError as e:
        return {"error": str(e)}
    except DuplicateBookError as e:
        return {"error": str(e)}
