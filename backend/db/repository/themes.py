from sqlalchemy.orm import Session

from schemas.themes import ThemeCreate
from db.models.themes import Theme


def create_new_theme(theme: ThemeCreate,db: Session,user:int):  #функция для создания новой тематики
    theme_object = Theme(**theme.dict(),user=user)
    db.add(theme_object)
    db.commit()
    db.refresh(theme_object)
    return theme_object


def list_themes(db:Session):    #функция для возвращения всех тематик
    item = db.query(Theme).all()
    return item


def retreive_theme(id:int,db:Session):  #функция для возвращения конкретной тематики (указав id)
    item = db.query(Theme).filter(Theme.id == id).first()
    return item


def delete_theme(id: int,db: Session,user):     #функция для удаления конкретной тематики (указав id)
    existing = db.query(Theme).filter(Theme.id == id)
    if not existing.first():
        return 0
    existing.delete(synchronize_session=False)
    db.commit()
    return 1
