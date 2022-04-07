from pydantic import BaseModel


class TodoCreate(BaseModel):
    id: str
    task: str
    status: bool = False
    