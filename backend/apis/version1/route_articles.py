from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.articles import Article
from schemas.articles import ArticleCreate,ShowArticle, ArticleUpdate
from db.repository.articles import create_new_article,update_article_by_id,delete_article_by_id,retreive_article
from db.repository.articles import list_publ_articles,list_ok_articles,list_draft_articles,list_no_articles
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-article/",response_model=ShowArticle)
def create_article(article: ArticleCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_writer or current_user.is_superuser:
        article = create_new_article(article=article,db=db,owner_id=current_user.id)
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


@router.get("/get-no",response_model=List[ShowArticle])
def read_no_articles(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    if current_user.is_moderator or current_user.is_writer or current_user.is_superuser:
        article = list_no_articles(db=db)
        return article
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-writer/{id}")
def update_article(id: int,article: ArticleCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_writer or current_user.is_superuser:
        current_user = 1
        message = update_article_by_id(id=id, article=article, db=db, owner_id=current_user)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-moderator/{id}")
def update_status(id: int,article: ArticleUpdate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_moderator or current_user.is_superuser:
        current_user = 1
        message = update_article_by_id(id=id, article=article, db=db, owner_id=current_user)
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