from pydantic import BaseModel

class Model(BaseModel):
    name: str
    model: str
    state: str = "manual"