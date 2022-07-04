from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.com import Comment
from schemas.com import ComCreate,ShowCom,ComUpdate
from db.repository.com import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-comment/",response_model=ShowCom)
def create_comment(com: ComCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    com = create_new_com(com=com,db=db,user=current_user.id)
    return com
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-comments/{article}",response_model=List[ShowCom])
def read_comments(article:int, db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    com = list_com(article=article, db=db)
    return com
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-comment/{id}")
def update_comment(id: int,com: ComUpdate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if Comment.user == current_user.id or current_user.is_superuser:
        current_user = 1
        message = update_com(id=id, com=com, db=db, user=Comment.user)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment with id {id} not found"
            )
        return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!") 


@router.delete("/delete/{id}")
def delete_comment(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    com = retreive_com(id =id,db=db)
    if not com:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Comment with id {id} does not exist")
    print(com.user,current_user.id,current_user.is_superuser)
    if com.user == current_user.id or current_user.is_superuser or current_user.is_moderator:
        delete_com(id=id,db=db,user=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")