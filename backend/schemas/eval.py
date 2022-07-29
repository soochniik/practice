from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime

#каждый класс отражает схему (данные, которые пользователь может ввести сам), по которой создаётся, обновляется, возвращается или удаляется оценка статьи

class EvaluationBase(BaseModel):
    article : Optional[int] = None
    evaluation : Optional[int] = None


class EvaluationBase1(BaseModel):
    evaluation : Optional[int] = None


class EvaluationCreate(EvaluationBase):
    article : int
    evaluation : int


class EvaluationUpdate(EvaluationBase1):
    evaluation : int


class ShowEvaluation(EvaluationBase1): 
    evaluation : int
    id : int

    class Config():
        orm_mode = True
