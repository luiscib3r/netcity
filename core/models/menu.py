from pydantic import BaseModel
from typing import List, Union


class Menu(BaseModel):
    id: Union[int, bool] = False
    name: str
    parent_id: Union[int, List, bool] = False
    sequence: int = 10
    action: str
    web_icon_data: Union[str, bool] = False
