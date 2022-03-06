from app.todo_table import TodoTable


class TodoManager:
    
    def __init__(self):
        self.todo_table = TodoTable()
    
    def save(self, id, task, is_done):
        return self.todo_table.add_task(id=id, task=task, is_done=is_done)

    def get(self, id):
        return self.todo_table.get_task_by_id(id=id)

    def update(self, id):
        return self.todo_table.update_task_status(id=id)

    def delete(self, id):
        return self.todo_table.delete_task(id=id)
