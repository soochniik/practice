from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from datetime import date,datetime
from db.session import get_db
from db.models.articles import Article
from schemas.articles import *
from db.repository.articles import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-article/",response_model=ShowArticle)
def create_article(article: ArticleCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_writer or current_user.is_superuser:
        article = create_new_article(article=article,db=db,owner_id=current_user.id,author=current_user.username)
        return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-draft",response_model=List[ShowArticle])
def read_draft_articles(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    if current_user.is_writer or current_user.is_superuser:
        article = list_draft_articles(db=db)
        return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-publ",response_model=List[ShowArticle])
def read_publ_articles(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    if current_user.is_moderator or current_user.is_superuser:
        article = list_publ_articles(db=db)
        return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-ok",response_model=List[ShowArticle])
def read_ok_articles(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    article = list_ok_articles(db=db)
    return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-by-id/{id}",response_model=ShowArticle)
def read_article(id:int, db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    article = retreive_article(id=id,db=db)
    return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-by-theme/{theme}",response_model=List[ShowArticle])
def read_articles_by_theme(theme:str, db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    articles = retreive_articles(theme=theme,db=db)
    return articles
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-no",response_model=List[ShowArticle])
def read_no_articles(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    if current_user.is_moderator or current_user.is_writer or current_user.is_superuser:
        article = list_no_articles(db=db)
        return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail=f"You are not permitted!!!!")


@router.get("/get-new-ok",response_model=List[ShowArticle])
def read_new_ok_articles(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    article = new_ok_articles(db=db)
    return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-draft/{id}")
def update_article(id: int,article: ArticleUpdate1,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_writer or current_user.is_superuser or article.owner_id == current_user.id:
        current_user = 1
        message = update_article_by_id(id=id, article=article, db=db, owner_id=Article.owner_id)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-for-writer/{id}")
def update_status(id: int,article: ArticleUpdate2,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_writer or current_user.is_superuser:
        current_user = 1
        message = update_for_draft(id=id, article=article, db=db, owner_id=Article.owner_id)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-for-moderator/{id}")
def update_status(id: int,article: ArticleUpdate3,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_moderator or current_user.is_superuser:
        current_user = 1
        message = update_article_by_id(id=id, article=article, db=db, owner_id=Article.owner_id)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-ok/{id}")
def update_status(id: int,article: ArticleUpdate4,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_writer or current_user.is_superuser:
        current_user = 1
        message = update_for_ok(id=id, article=article, db=db, owner_id=Article.owner_id)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.delete("/delete/{id}")
def delete_article(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    article = retreive_article(id =id,db=db)
    if not article:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with {id} does not exist")
    print(article.owner_id,current_user.id,current_user.is_superuser)
    if article.owner_id == current_user.id or current_user.is_superuser:
        delete_article_by_id(id=id,db=db,owner_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
