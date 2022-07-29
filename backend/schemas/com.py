from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime

#каждый класс отражает схему (данные, которые пользователь может ввести сам), по которой создаётся, обновляется, возвращается или удаляется комментарий

class ComBase(BaseModel):
    article : Optional[int] = None
    description : Optional[str] = None


class ComBase1(BaseModel):
    description : Optional[str] = None


class ComCreate(ComBase):
    article : int
    description : str = "add comment"


class ComUpdate(ComBase1):
    description : Optional[str] = None


class ShowCom(ComBase1): 
    description : Optional[str] = None
    id : int

    class Config():
        orm_mode = True
