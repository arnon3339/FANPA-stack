from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str
    email: str
    nick_name: Union[str, None] = None
    # class Config:
    #     orm_mode = True
