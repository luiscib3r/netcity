from pydantic import BaseModel
from typing import List


class ModelField(BaseModel):
    id: int
    model_id: List
    name: str
    field_description: str = ""
    ttype: str
    state: str = "manual"
    required = False


class CreateModelField(BaseModel):
    model_id: int
    name: str
    field_description: str = ""
    ttype: str
    state: str = "manual"
    required = False
