from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.base_class import Base


class Article(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    theme = Column(String,nullable= False)
    author = Column(String,nullable= False)
    status = Column(String,nullable=False,default="draft")
    description = Column(String,nullable=False)
    date_posted = Column(Date)
    eval = Column(Float,nullable=False,default=0)
    reader = Column(Integer,nullable=False,default=0)
    owner_id = Column(Integer,ForeignKey("user.id"))
    owner = relationship("User",back_populates="articles")
    com = relationship("Comment",back_populates="artic")
    evaluation = relationship("Evaluation",back_populates="artic") 
    reason = relationship("Reason",back_populates="artic")
    auth = relationship("Author",back_populates="artic")
