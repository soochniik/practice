from sqlalchemy.orm import Session

from schemas.users import UserCreate, UserUpdate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user:UserCreate,db:Session):    #функция для создания нового пользователя
    user = User(username=user.username,
        email = user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
        is_moderator=False,
        is_writer=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db:Session):     #функция для возвращения информации о всех пользователях
    item = db.query(User).all()
    return item


def upd_for_admin(id:int, user: UserUpdate,db: Session):    #функция для обновления информации о конкретном пользователе (указав id)
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
    user.__dict__.update()
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def retreive_user(id:int,db:Session):   #функция для возвращения информации о конкретном пользователе (указав id)
    item = db.query(User).filter(User.id == id).first()
    return item


def delete_user_by_id(id: int,db: Session):     #функция для удаления пользователя (указав id)
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1
