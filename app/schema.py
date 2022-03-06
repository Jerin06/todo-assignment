from pydantic import BaseModel


class TodoBase(BaseModel):
    id: str


class TodoCreate(TodoBase):
    task: str
    status: bool = False
    