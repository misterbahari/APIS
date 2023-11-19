from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException

app = FastAPI()


class UserIn(BaseModel):
    name: str
    age: int
    pss: str


class UserOut(BaseModel):
    name: str
    age: int


@app.post('/users', response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserIn):
    if user.name == 'admin':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="nemishe agha")
    return user
