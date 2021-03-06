
class TodoTable:
    """A hashmap to perform CRUD operations for todo tasks"""

    def __init__(self):
        self.todo = dict() # in memory storage using dict

    def add_task(self, id, task, is_done):
        if id not in self.todo:
            self.todo[id] = {"task": task, "is_done": is_done}
            return {"ok": True, "data": self.get(id)}
        return None

    def get_task_by_id(self, id):
        if id in self.todo:
            return self.get(id)
        return None 

    def update_task_status(self, id):
        if id in self.todo:
            self.todo[id]["is_done"] = not self.todo[id]["is_done"]
            return self.get(id)
        return None

    def delete_task(self, id):
        if id in self.todo:
            del self.todo[id]
            return {"ok": True}
        return None

    def get(self, id):
        return {
            "id": id,
            "task": self.todo[id]["task"],
            "is_done": self.todo[id]["is_done"]
        }
