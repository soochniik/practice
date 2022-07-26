from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.authors import Author
from db.models.articles import Article
from schemas.authors import AuthorCreate, ShowAuthor
from db.repository.authors import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/add-author/{author_name}",response_model=ShowAuthor)
def add_author(author: AuthorCreate, author_name:str, db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_moderator or current_user.is_superuser:
        author = add_new_author(author=author,db=db,auth=author_name)
        return author
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
