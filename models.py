from typing import List, Optional
from uuid import UUID,uuid4
from enum import Enum
from pydantic import BaseModel

class Gender(str,Enum):
    male = "male"
    female = "female"

class Roles(str,Enum):
    admin = "admin"
    user = "user"
    student = "student"



class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender:Gender
    roles:List[Roles]


class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Roles]]