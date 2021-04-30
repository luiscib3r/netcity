from pydantic import BaseModel


class ActionWindow(BaseModel):
    name: str
    res_model: str
    view_mode: str = "tree,form"
    context = "{}"