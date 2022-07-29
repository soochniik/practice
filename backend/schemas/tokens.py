from pydantic import BaseModel

#каждый класс отражает схему (данные, которые пользователь может ввести сам), по которой генерируется персональный токен

class Token(BaseModel):
    access_token: str
    token_type: str