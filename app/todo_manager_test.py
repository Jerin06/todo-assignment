import unittest

from app.todo_manager import TodoManager


class TodoManagerTest(unittest.TestCase):
    def setUp(self):
        self.todo_manager = TodoManager()
        self.todo_manager.save("1234", "The second task in the list", False)
        self.todo_manager.save("1235", "The third task in the list", False)
        self.todo_manager.save("1236", "The third task in the list", False)

    def test_save(self):
        id = "1233"
        task = "The first task details everything"
        is_done = False
        result = self.todo_manager.save(id, task, is_done)
        todo_expected = {"id": id, "task": task, "is_done": is_done}
        self.assertEqual(todo_expected, result["data"])

    def test_get(self):       
        result = self.todo_manager.get("1234")
        task_expected = "The second task in the list"
        self.assertEqual(task_expected, result["task"])
        
    def test_get_item_not_exist(self):       
        result = self.todo_manager.get("1250")
        task_expected = None
        self.assertEqual(task_expected, result)
        
    def test_update(self):
        result = self.todo_manager.update("1235")
        status_expected = True
        self.assertEqual(status_expected, result["is_done"])
        
    def test_delete(self):
        result = self.todo_manager.delete("1236")
        self.assertEqual(True, result["ok"])
