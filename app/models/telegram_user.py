from pydantic import BaseModel, Field
from typing import Union


class TelegramUser(BaseModel):
    x_user_id: str = Field(alias="id")
    x_name: str = Field(alias="first_name")
    x_last_name: Union[str, bool] = Field(False, alias="last_name")
    x_username: Union[str, bool] = Field(False, alias="username")
    x_language_code: Union[str, bool] = Field(False, alias="language_code")

    class Config:
        allow_population_by_field_name = True
