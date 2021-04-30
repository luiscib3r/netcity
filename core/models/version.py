from pydantic import BaseModel
from typing import List


class Version(BaseModel):
    server_version: str
    server_version_info: List
    server_serie: str
    protocol_version: str
