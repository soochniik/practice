from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime

#каждый класс отражает схему (данные, которые пользователь может ввести сам), по которой создаётся, обновляется, возвращается или удаляется статья

class ArticleBase(BaseModel):
    title : Optional[str] = None
    theme : Optional[str] = None
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()

class ArticleBase1(BaseModel):
    title : Optional[str] = None
    theme : Optional[str] = None
    status : Optional[str] = None
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()
    id : Optional[int] = None

class ArticleBase2(BaseModel):
    status : Optional[str] = None

class ArticleBase3(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None

class ArticleBase4(BaseModel):
    evaluation : Optional[int]

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

class ArticleEval(ArticleBase4):
    evaluation : int
       
class ShowArticle(ArticleBase1):
    title : str 
    theme : str
    status : str  
    description : str 
    id : int
    date_posted : date

    class Config():
        orm_mode = True