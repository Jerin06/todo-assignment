class TodoManager:
    def __init__(self):
        self.todo = dict()

    def add_task(self, id, task):
        self.todo["id"] = id
        self.todo["task"] = task
        return self.todo

    def get_task_by_id(self, id):
        pass
