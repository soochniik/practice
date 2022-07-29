from sqlalchemy.orm import Session

from schemas.com import ComCreate, ComUpdate
from db.models.com import Comment


def create_new_com(com: ComCreate,db: Session,user:int):    #функция для создания комментария (введённый пользователем словарь добавляется в бд новой строкой)
    com_object = Comment(**com.dict(),user=user)
    db.add(com_object)
    db.commit()
    db.refresh(com_object)
    return com_object


def retreive_com(id:int,db:Session):    #функция для возвращения конкретного комментария из бд (указав id)
    item = db.query(Comment).filter(Comment.id == id).first()
    return item


def list_com(article:int, db:Session):  #функция для возвращения всех комментариев указанной пользователем статьи
    item = list(db.query(Comment).filter(Comment.article == article))
    return item


def update_com(id:int, com: ComUpdate,db: Session,user):    #функция для обновления комментария (указав id)
    existing = db.query(Comment).filter(Comment.id == id)
    if not existing.first():
        return 0
    com.__dict__.update(user=user)
    existing.update(com.__dict__)
    db.commit()
    return 1


def delete_com(id: int,db: Session,user):   #функция для удаления комментария (указав id)
    existing = db.query(Comment).filter(Comment.id == id)
    if not existing.first():
        return 0
    existing.delete(synchronize_session=False)
    db.commit()
    return 1