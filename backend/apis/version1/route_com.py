from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.com import Comment
from schemas.com import ComCreate,ShowCom
from db.repository.com import create_new_com,update_com,delete_com,list_com,retreive_com
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-comment/",response_model=ShowCom)
def create_comment(com: ComCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    com = create_new_com(com=com,db=db,user=current_user.id)
    return com
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/get-comments",response_model=List[ShowCom])
def read_comments(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    com = list_com(db=db)
    return com
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.put("/update-comment/{id}")
def update_comment(id: int,com: ComCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    current_user = 1
    message = update_com(id=id, com=com, db=db, user=current_user)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment with id {id} not found"
        )
    return {"msg": "Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.delete("/delete/{id}")
def delete_article(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    com = retreive_com(id =id,db=db)
    if not com:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Comment with id {id} does not exist")
    print(com.user,current_user.id,current_user.is_superuser)
    if com.user == current_user.id or current_user.is_superuser:
        delete_com(id=id,db=db,user=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")