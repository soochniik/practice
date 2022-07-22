from typing import Optional
from pydantic import BaseModel,EmailStr


class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str

class UserUpdate(BaseModel):
    is_active : bool = False
    is_moderator : bool = False
    is_superuser : bool = False
    is_writer : bool = False

class ShowUser(BaseModel):
    id : int
    username : str 
    email : EmailStr
    is_active : bool
    is_moderator : bool
    is_superuser : bool
    is_writer : bool

    class Config():
        orm_mode = True