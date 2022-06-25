from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class ArticleBase(BaseModel):
    title : Optional[str] = None
    status : Optional[str] = None
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()
    

class ArticleCreate(ArticleBase):
    title : str
    status : str 
    description : str 

class ShowArticle(ArticleBase):
    title : str 
    status : str  
    date_posted : date
    description : Optional[str]

    class Config():
        orm_mode = True