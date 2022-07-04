from typing import Optional
from pydantic import BaseModel


class ThemeBase(BaseModel):
    theme : Optional[str] = None


class ThemeCreate(ThemeBase):
    theme : str = "theme"


class ShowTheme(ThemeBase): 
    theme : Optional[str] 
    id : int

    class Config():
        orm_mode = True
