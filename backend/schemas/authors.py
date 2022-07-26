from typing import Optional
from pydantic import BaseModel


class AuthorBase(BaseModel):
    article : Optional[int] = None
    author_id : Optional[int] = None


class AuthorCreate(AuthorBase):
    article : int
    author_id : int


class ShowAuthor(AuthorBase):
    article : int
    author_id : int

    class Config():
        orm_mode = True