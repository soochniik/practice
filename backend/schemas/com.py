from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class ComBase(BaseModel):
    article : Optional[int] = None
    description : Optional[str] = None


class ComBase1(BaseModel):
    description : Optional[str] = None


class ComBase2(BaseModel):
    article : Optional[int] = None
    description : Optional[str] = None
    id : Optional[int] = None


class ComCreate(ComBase):
    article : int
    description : str = "add comment"


class ComUpdate(ComBase1):
    description : Optional[str] = None


class ShowCom(ComBase2): 
    id : Optional[int]
    article : Optional[int]
    description : Optional[str] 

    class Config():
        orm_mode = True
