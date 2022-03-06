from app.todo_table import TodoTable


class TodoManager:
    
    @staticmethod
    def save(id, task, is_done):
        return TodoTable().add_task(id=id, task=task, is_done=is_done)

    @staticmethod
    def get(id):
        return TodoTable().get_task_by_id(id=id)

    @staticmethod
    def update(id):
        return TodoTable().update_task_status(id=id)

    @staticmethod
    def delete(id):
        return TodoTable().delete_task(id=id)
