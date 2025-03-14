from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator


class BookSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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
