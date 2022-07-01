from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Comment(Base):
    id = Column(Integer,primary_key = True, index=True)
    description = Column(String,nullable=False)
    article = Column(Integer,ForeignKey("article.id"))
    user = Column(Integer,ForeignKey("user.id"))
    artic = relationship("Article",back_populates="com")
    us = relationship("User",back_populates="com")