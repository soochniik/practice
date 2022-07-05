from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.reasons import Reason
from schemas.reasons import ReasonCreate,ShowReason
from db.repository.reasons import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-reason/",response_model=ShowReason)
def create_reason(reason: ReasonCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_superuser or current_user.is_moderator:
        reason = create_new_reason(reason=reason,db=db,user=current_user.id)
        return reason
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-reason/{article}",response_model=List[ShowReason])
def read_reason(article:int, db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    if current_user.is_superuser or current_user.is_moderator or current_user.is_writer:
        reasons = list_reason(article=article, db=db)
        return reasons
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
