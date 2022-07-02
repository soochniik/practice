from sqlalchemy.orm import Session

from schemas.com import ComCreate, ComUpdate
from db.models.com import Comment


def create_new_com(com: ComCreate,db: Session,user:int):
    com_object = Comment(**com.dict(),user=user)
    db.add(com_object)
    db.commit()
    db.refresh(com_object)
    return com_object


def retreive_com(id:int,db:Session):
    item = db.query(Comment).filter(Comment.id == id).first()
    return item


def list_com(db:Session):
    item = db.query(Comment).all()
    return item


def update_com(id:int, com: ComUpdate,db: Session,user):
    existing = db.query(Comment).filter(Comment.id == id)
    if not existing.first():
        return 0
    com.__dict__.update(user=user)
    existing.update(com.__dict__)
    db.commit()
    return 1


def delete_com(id: int,db: Session,user):
    existing = db.query(Comment).filter(Comment.id == id)
    if not existing.first():
        return 0
    existing.delete(synchronize_session=False)
    db.commit()
    return 1