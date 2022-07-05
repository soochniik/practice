from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List,Optional
from datetime import date,datetime
from db.session import get_db
from db.models.articles import Article
from db.repository.articles import *
from schemas.articles import ShowArticle
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.get("/by-title")
def serch_by_title(term: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    articles = search_title(term, db=db)
    article_titles = []
    for article in articles:
        article_titles.append(article.title)
    return article_titles
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/by-description")
def serch_by_description(term: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    articles = search_description(term, db=db)
    article_descriptions = []
    for article in articles:
        article_descriptions.append(article.description)
    return article_descriptions
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/by-author")
def serch_by_author(term: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    articles = search_author(term, db=db)
    article_authors = []
    for article in articles:
        article_authors.append(article.author)
    return article_authors
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/by-date")
def serch_by_date(term: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    articles = search_date(term, db=db)
    article_dates = []
    for article in articles:
        article_dates.append(article.date_posted)
    return article_dates
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/by-eval")
def serch_by_evaluation(term: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    articles = search_eval(term, db=db)
    article_evals = []
    for article in articles:
        article_evals.append(article.eval)
    return article_evals
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/by-reader")
def serch_by_reader(term: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    articles = search_reader(term, db=db)
    article_readers = []
    for article in articles:
        article_readers.append(article.reader)
    return article_readers
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
