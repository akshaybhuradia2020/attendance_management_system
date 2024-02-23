from pydantic import BaseModel


class Login(BaseModel):
    username: str
    passwd: str


class Check_User_Status(Login):
    active: bool