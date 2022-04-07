from app.todo_interface import ITodo


class TodoManager:
    
    def __init__(self, Todo: ITodo):
        self.todo = Todo()
    
    def save(self, id, task, is_done):
        return self.todo.add_task(id=id, task=task, is_done=is_done)

    def get(self, id):
        return self.todo.get_task_by_id(id=id)

    def update(self, id):
        return self.todo.update_task_status(id=id)

    def delete(self, id):
        return self.todo.delete_task(id=id)
