from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Theme(Base):      #таблица Theme
    id = Column(Integer,primary_key = True, index=True)
    theme = Column(String,nullable= False)
    user = Column(Integer,ForeignKey("user.id"))
    us = relationship("User",back_populates="theme")
