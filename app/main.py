from fastapi import FastAPI, HTTPException

from app.schema import TodoCreate
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


@app.get("/todo/get/{todo_id}")
def get_todo(todo_id: str):
    todo = todo_manager.get(id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task doesn't exist")
    return todo
    

@app.put("/todo/update/{todo_id}")
def update_todo(todo_id: str):
    task = todo_manager.get(id=todo_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task doesn't exist")    
    return todo_manager.update(id=todo_id)


@app.delete("/todo/delete/{todo_id}")
def delete_todo(todo_id: str):
    task = todo_manager.get(id=todo_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task doesn't exist")
    return todo_manager.delete(id=todo_id)
