from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from typing import List
from models import User,Roles,Gender,UserUpdateRequest

app = FastAPI()

db: List[User] =[
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="kervin",
        gender=Gender.male,
        roles=[Roles.student],
        middle_name="null"
    ),
    User(
        id=uuid4(),
        first_name="zhang",
        last_name="xin",
        gender=Gender.female,
        roles=[Roles.student],
        middle_name="null"

    )
]
@app.get("/")
def root():
    return {"Hello":"world"}

@app.get("/api/v1/users")
async def fetch_user():
    return db

@app.post("/api/v1/users")
async def add_user(user:User):
    db.append(user)
    return {"id":user.id}

@app.put("/api/v1/users")
async def update_user(user_update:UserUpdateRequest,id:UUID):
    for user in db:
        if user.id ==id:
            if user_update.first_name  is not None:
                user.first_name = user_update.first_name
            if user_update.last_name  is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name  is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles  is not None:
                user.roles = user_update.roles
            return
        
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {id} does not exists"
    )

@app.delete("/api/v1/users/{user_id}")
async def delete_user(id:UUID):
    for user in db:
        if user.id ==id:
            db.remove(user)
            return 
    raise HTTPException (
            status_code =404, 
            detail =f"{id} not found"
        )

