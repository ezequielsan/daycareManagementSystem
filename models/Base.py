from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: int

    class Config:
        orm_mode = True
