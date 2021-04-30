from pydantic import BaseModel

class ModelAccess(BaseModel):
    model_id: int
    name: str
    group_id: int = 1
    perm_read: bool = True
    perm_write: bool = True
    perm_create: bool = True
    perm_unlink: bool = True