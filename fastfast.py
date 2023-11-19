from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/{name}")
def root(name: str, num: Optional[int] = 1234):
    return {'hello': name, 'adad': num}
