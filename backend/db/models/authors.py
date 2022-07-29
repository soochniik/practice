from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Author(Base):     #таблица Author
    id = Column(Integer,primary_key = True, index=True)
    article = Column(Integer,ForeignKey("article.id"))
    author_id = Column(Integer,ForeignKey("user.id"))
    artic = relationship("Article",back_populates="auth")
    us = relationship("User",back_populates="auth")
