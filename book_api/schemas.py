from typing import Optional

from marshmallow import Schema, fields
from pydantic import BaseModel, Field, ValidationError, field_validator


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    isbn = fields.Str(required=True, validate=lambda x: len(x) == 13)


class Book(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str
    author: str
    isbn: str

    @field_validator("isbn")
    def validate_isbn(cls, v):
        if len(v) != 13:
            raise ValidationError("ISBN must be exactly 13 characters long")
        if not v.isdigit():
            raise ValidationError("ISBN must contain only digits")
        return v
