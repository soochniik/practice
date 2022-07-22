from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from db.models.users import User
from typing import List 
from apis.version1.route_login import get_current_user_from_token
from schemas.users import UserUpdate,ShowUser
from db.session import get_db
from db.repository.users import upd_for_admin,list_users

router = APIRouter()


@router.get("/show-users",response_model=List[ShowUser])
def show_users(db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_superuser:
        users = list_users(db=db)
        return users
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-user/{id}")
def update_user(id:int, user : UserUpdate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_superuser:
        mes = upd_for_admin(id=id, user=user,db=db)
        if not mes:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
