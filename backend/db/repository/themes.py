from sqlalchemy.orm import Session

from schemas.themes import ThemeCreate
from db.models.themes import Theme


def create_new_themes(theme: ThemeCreate,db: Session,user:int):
    theme_object = Theme(**theme.dict(),user=user)
    db.add(theme_object)
    db.commit()
    db.refresh(theme_object)
    return theme_object


def list_themes(db:Session):
    item = db.query(Theme).all()
    return item


def retreive_theme(id:int,db:Session):
    item = db.query(Theme).filter(Theme.id == id).first()
    return item


def delete_theme(id: int,db: Session,user):
    existing = db.query(Theme).filter(Theme.id == id)
    if not existing.first():
        return 0
    existing.delete(synchronize_session=False)
    db.commit()
    return 1
