from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):   #таблица User
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)
    is_moderator = Column(Boolean(),default=False)
    is_writer = Column(Boolean(),default=False)
    articles = relationship("Article",back_populates="owner")
    com = relationship("Comment",back_populates="us")
    evaluation = relationship("Evaluation",back_populates="us")
    reason = relationship("Reason",back_populates="us")
    theme = relationship("Theme",back_populates="us")
    auth = relationship("Author",back_populates="us")