from fastapi import FastAPI, HTTPException

from app.schema import TodoBase, TodoCreate
from app.todo_table import TodoTable
from app.todo_manager import TodoManager


app = FastAPI()
todo_manager = TodoManager(TodoTable)

@app.post("/todo/create")
def create_todo(todo: TodoCreate):
    task = todo_manager.get(id=todo.id)
    if task:
        raise HTTPException(status_code=400, detail="Task already exists")
    return todo_manager.save(id=todo.id, task=todo.task, is_done=todo.status)


@app.post("/todo/get")
def get_todo(todo: TodoBase):
    todo = todo_manager.get(id=todo.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task doesn't exist")
    return todo
    

@app.post("/todo/update")
def update_todo(todo: TodoBase):
    task = todo_manager.get(id=todo.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task doesn't exist")    
    return todo_manager.update(id=todo.id)


@app.post("/todo/delete")
def delete_todo(todo: TodoBase):
    task = todo_manager.get(id=todo.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task doesn't exist")
    return todo_manager.delete(id=todo.id)
