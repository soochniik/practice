from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.articles import Article
from schemas.articles import ArticleCreate,ShowArticle
from db.repository.articles import create_new_article,retreive_article,list_articles,update_article_by_id,delete_article_by_id
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-article/",response_model=ShowArticle)
def create_article(article: ArticleCreate,db: Session = Depends(get_db),current_user:User = Depends(get_current_user_from_token)):
    article = create_new_article(article=article,db=db,owner_id=current_user)
    return article


@router.get("/get/{id}",response_model=ShowArticle)
def read_article(id:int,db:Session = Depends(get_db)):
    article = retreive_article(id=id,db=db)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with this id {id} does not exist")
    return article


@router.get("/all",response_model=List[ShowArticle])
def read_articles(db:Session = Depends(get_db)):
    articles = list_articles(db=db)
    return articles


@router.put("/update/{id}")
def update_article(id: int,article: ArticleCreate,db: Session = Depends(get_db)):
    current_user = 1
    message = update_article_by_id(id=id,article=article,db=db,owner_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {id} not found")
    return {"msg":"Successfully updated data."}


@router.delete("/delete/{id}")
def delete_article(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    article = retreive_job(id =id,db=db)
    if not article:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with {id} does not exist")
    print(article.owner_id,current_user.id,current_user.is_superuser)
    if article.owner_id == current_user.id or current_user.is_superuser:
        delete_article_by_id(id=id,db=db,owner_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")