from pydantic import BaseModel

class ModelField(BaseModel):
    model_id: int
    name: str
    ttype: str
    state: str = "manual"