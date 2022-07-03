from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class EvaluationBase(BaseModel):
    article : Optional[int] = None
    evaluation : Optional[int] = None


class EvaluationBase1(BaseModel):
    evaluation : Optional[int] = None


class EvaluationCreate(EvaluationBase):
    article : int
    evaluation : int


class ShowEvaluation(EvaluationBase1): 
    evaluation : int

    class Config():
        orm_mode = True
