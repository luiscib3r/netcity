from pydantic import BaseModel, Field
from typing import Union


class RentHouse(BaseModel):
    id: Union[int, bool] = False
    x_name: str = Field(alias="name")
    x_description: str = Field(alias="description")
    x_coordinates: str = Field(alias="coordinates")
    x_address: str = Field(alias="address")

    class Config:
        allow_population_by_field_name = True
