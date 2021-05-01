from pydantic import BaseModel
from typing import Union


class Attachment(BaseModel):
    id: Union[int, bool] = False
    name: str
    type: str = "binary"
    datas: Union[str, bool] = False
    url: Union[str, bool] = False
    mimetype: Union[str, bool] = False
