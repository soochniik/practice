from typing import Optional
from pydantic import BaseModel

#каждый класс отражает схему (данные, которые пользователь может ввести сам), по которой создаётся, возвращается или удаляется тематика статьи

class ThemeBase(BaseModel):
    theme : Optional[str] = None


class ThemeCreate(ThemeBase):
    theme : str = "theme"


class ShowTheme(ThemeBase): 
    theme : Optional[str] 
    id : int

    class Config():
        orm_mode = True
