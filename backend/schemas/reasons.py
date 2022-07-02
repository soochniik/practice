from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class ReasonBase(BaseModel):
    article : Optional[int] = None
    description : Optional[str] = None


class ReasonBase1(BaseModel):
    description : Optional[str] = None


class ReasonCreate(ReasonBase):
    article : int
    description : str = "reason"


class ShowReason(ReasonBase1): 
    description : Optional[str] 

    class Config():
        orm_mode = True
