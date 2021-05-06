from pydantic import BaseModel, Field
from typing import Union, List


class AppRelease(BaseModel):
    id: Union[int, bool] = False
    x_name: str = Field(alias="name")
    x_description: str = Field(alias="description")
    x_version: str = Field(alias="version")
    x_apps: List[int] = Field(alias="apps")

    class Config:
        allow_population_by_field_name = True
