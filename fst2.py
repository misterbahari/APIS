import pydantic
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Person(pydantic.BaseModel):
    name: str
    height: int
    email: str


@app.post('/create')
def create_person(person: Person):
    return person



