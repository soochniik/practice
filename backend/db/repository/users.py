from sqlalchemy.orm import Session

from schemas.users import UserCreate, UserUpdate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user:UserCreate,db:Session):
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


def list_users(db:Session):
    item = db.query(User).all()
    return item

def upd_for_admin(id:int, user: UserUpdate,db: Session):
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
    user.__dict__.update()
    existing_user.update(user.__dict__)
    db.commit()
    return 1
