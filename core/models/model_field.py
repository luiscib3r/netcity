from pydantic import BaseModel
from typing import List, Union


class ModelField(BaseModel):
    id: Union[int, bool] = False
    model_id: Union[List, int]
    name: str
    field_description: str = ""
    ttype: str
    state: str = "manual"
    required = False
    relation: Union[str, bool] = False
    readonly: bool = False
    index: bool = False
