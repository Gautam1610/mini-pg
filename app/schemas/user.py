from pydantic import BaseModel , EmailStr
from enum import Enum
from typing import Optional


class UserRole(str, Enum):
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"


class UserSignup(BaseModel):
    id : int
    fname : str
    lname : Optional[str]
    email : EmailStr
    password : str
    role : UserRole

class UserLogin(BaseModel):
    email : EmailStr
    password : str
