from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.eval import Evaluation
from schemas.eval import EvaluationCreate,ShowEvaluation,EvaluationUpdate
from db.repository.eval import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/leave-evaluation/",response_model=ShowEvaluation)
def leave_evaluation(evaluation: EvaluationCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    evaluation = create_evaluation(evaluation=evaluation,db=db,user=current_user.id)
    return evaluation
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-evaluation/{article}",response_model=List[ShowEvaluation])
def show_evaluations(article:int, db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    evaluations = list_evaluations(article=article, db=db)
    return evaluations
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-evaluation/{id}")
def update_evaluation(id: int,evaluation: EvaluationUpdate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if Evaluation.user == current_user.id or current_user.is_superuser:
        current_user = 1
        message = update_eval(id=id, evaluation=evaluation, db=db, user=Evaluation.user)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Evaluation with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.delete("/delete/{id}")
def delete_evaluation(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    evaluation = retreive_evaluation(id =id,db=db)
    if not evaluation:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Evaluation with id {id} does not exist")
    print(evaluation.user,current_user.id,current_user.is_superuser)
    if evaluation.user == current_user.id or current_user.is_superuser:
        delete_eval(id=id,db=db,user=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")