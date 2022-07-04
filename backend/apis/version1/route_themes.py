from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List
from db.session import get_db
from db.models.themes import Theme
from schemas.themes import ThemeCreate,ShowTheme
from db.repository.themes import *
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create-theme/",response_model=ShowTheme)
def create_theme(theme: ThemeCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_superuser or current_user.is_moderator:
        theme = create_new_themes(theme=theme,db=db,user=current_user.id)
        return theme
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.get("/all",response_model=List[ShowTheme])
def list_all_themes(db:Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):  
    themes = list_themes(db=db)
    return themes
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")


@router.delete("/delete/{id}")
def delete_theme_by_id(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    theme = retreive_theme(id =id,db=db)
    if not theme:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Theme with id {id} does not exist")
    print(theme.user,current_user.id,current_user.is_superuser)
    if current_user.is_superuser or current_user.is_moderator:
        delete_theme(id=id,db=db,user=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
