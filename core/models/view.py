from pydantic import BaseModel
from typing import Union


class View(BaseModel):
    id: Union[int, bool] = False
    name: str
    type: str
    model: str
    arch_base: str
    priority: int = 16
    mode: str = "primary"
