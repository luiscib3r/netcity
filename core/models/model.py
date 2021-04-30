from pydantic import BaseModel

class Model(BaseModel):
    id: int
    name: str
    model: str
    state: str = "manual"

class CreateModel(BaseModel):
    name: str
    model: str
    state: str = "manual"