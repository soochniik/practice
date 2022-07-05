from sqlalchemy.orm import Session
from datetime import date,datetime
from schemas.articles import ArticleCreate, ArticleUpdate1, ArticleUpdate2, ArticleUpdate3, ArticleUpdate4, ArticleEval
from db.models.articles import Article


def create_new_article(article: ArticleCreate,db: Session,owner_id:int,author:str):
    article_object = Article(**article.dict(),owner_id=owner_id,author=author)
    db.add(article_object)
    db.commit()
    db.refresh(article_object)
    return article_object


def retreive_article(id:int,db:Session):
    item = db.query(Article).filter(Article.id == id).first()
    item.reader+=1
    db.commit()
    return item


def retreive_articles(theme:str,db:Session):
    item = db.query(Article).filter(Article.theme == theme, Article.status == 'ok')
    return list(item)


def new_ok_articles(db:Session):
    item = list(db.query(Article).filter(Article.date_posted == datetime.now().date(), Article.status == 'ok'))
    return item


def list_draft_articles(db:Session):
    item = list(db.query(Article).filter(Article.status == 'draft'))
    return item


def list_publ_articles(db:Session):
    item = list(db.query(Article).filter(Article.status == 'publ'))
    return item


def list_ok_articles(db:Session):
    item = list(db.query(Article).filter(Article.status == 'ok'))
    return item


def list_no_articles(db:Session):
    item = list(db.query(Article).filter(Article.status == 'no'))
    return item


def update_article_by_id(id:int, article: ArticleUpdate1,db: Session,owner_id):
    existing_article = db.query(Article).filter(Article.id == id, Article.status != 'ok')
    if not existing_article.first():
        return 0
    article.__dict__.update(owner_id=owner_id, date_posted=datetime.now().date())
    existing_article.update(article.__dict__)
    db.commit()
    return 1


def update_for_draft(id:int, article: ArticleUpdate2,db: Session,owner_id):
    existing_article = db.query(Article).filter(Article.id == id, Article.status == "draft")
    if not existing_article.first():
        return 0
    article.__dict__.update(owner_id=owner_id)
    existing_article.update(article.__dict__)
    db.commit()
    return 1


def update_for_ok(id:int, article: ArticleUpdate4,db: Session,owner_id):
    existing_article = db.query(Article).filter(Article.id == id, Article.status == "ok")
    if not existing_article.first():
        return 0
    article.__dict__.update(owner_id=owner_id)
    existing_article.update(article.__dict__)
    db.commit()
    return 1


def delete_article_by_id(id: int,db: Session,owner_id):
    existing_article = db.query(Article).filter(Article.id == id)
    if not existing_article.first():
        return 0
    existing_article.delete(synchronize_session=False)
    db.commit()
    return 1


def search_title(query: str, db: Session):
    articles = db.query(Article).filter(Article.title.contains(query), Article.status == 'ok')
    return articles


def search_description(query: str, db: Session):
    articles = db.query(Article).filter(Article.description.contains(query), Article.status == 'ok')
    return articles


def search_date(query: str, db: Session):
    articles = db.query(Article).filter(Article.date_posted.contains(query), Article.status == 'ok')
    return articles


def search_author(query: str, db: Session):
    articles = db.query(Article).filter(Article.author.contains(query), Article.status == 'ok')
    return articles


def search_reader(query: str, db: Session):
    articles = db.query(Article).filter(Article.reader.contains(query), Article.status == 'ok')
    return articles


def search_eval(query: str, db: Session):
    articles = db.query(Article).filter(Article.eval.contains(query), Article.status == 'ok')
    return articles
