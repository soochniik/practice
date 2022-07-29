from sqlalchemy.orm import Session

from db.models.users import User 


def get_user(username:str,db: Session):     #функция для возвращения конкретного пользователя с указанным email
    user = db.query(User).filter(User.email == username).first()
    return user