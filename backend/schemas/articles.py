from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class ArticleBase(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()

class ArticleBase1(BaseModel):
    title : Optional[str] = None
    status : Optional[str] = None
    description : Optional[str] = None
    id : Optional[int] = None
    date_posted : Optional[date] = datetime.now().date()  

class ArticleBase2(BaseModel):
    status : Optional[str] = None

class ArticleBase3(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None

class ArticleCreate(ArticleBase):
    title : str
    description : Optional[str] 

class ArticleUpdate1(ArticleBase3):
    title : str
    description : Optional[str]

class ArticleUpdate2(ArticleBase2):
    status : str = "publ"

class ArticleUpdate3(ArticleBase2):
    status : str

class ArticleUpdate4(ArticleBase2):
    status : str = "draft" 
       
class ShowArticle(ArticleBase1):
    title : str 
    status : str  
    description : str 
    id : int
    date_posted : date

    class Config():
        orm_mode = True