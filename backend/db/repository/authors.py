from sqlalchemy.orm import Session
from schemas.authors import AuthorCreate
from db.models.authors import Author
from db.models.articles import Article


def add_new_author(author: AuthorCreate, db: Session, auth:str):   #функция для добавления в бд нового автора статьи 
    author_object = Author(**author.dict())
    art_id = author_object.article
    db.add(author_object)
    db.commit()
    db.refresh(author_object)
    item = db.query(Article).filter(Article.id == art_id).first()
    item.author+=(", " + auth)
    db.commit()
    return author_object

