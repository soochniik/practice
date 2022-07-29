from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Evaluation(Base):     #таблица Evaluation
    id = Column(Integer,primary_key = True, index=True)
    evaluation = Column(Integer,nullable=False,default=0)
    article = Column(Integer,ForeignKey("article.id"))
    user = Column(Integer,ForeignKey("user.id"))
    artic = relationship("Article",back_populates="evaluation")
    us = relationship("User",back_populates="evaluation")
