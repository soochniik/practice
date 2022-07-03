from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.eval import Evaluation
from schemas.eval import EvaluationCreate,ShowEvaluation
from db.repository.eval import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/leave-evaluation/",response_model=ShowEvaluation)
def leave_evaluation(evaluation: EvaluationCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    evaluation = leave_evaluation(evaluation=evaluation,db=db,user=current_user.id)
    return evaluation
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-evaluation/{article}",response_model=List[ShowEvaluation])
def show_evaluations(article:int, db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    evaluations = list_evaluations(article=article, db=db)
    return evaluations
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
