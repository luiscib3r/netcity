from pydantic import BaseModel
from typing import Union

class Model(BaseModel):
    id: Union[int, bool] = False
    name: str
    model: str
    state: str = "manual"