import unittest

from app.todo_manager import TodoManager


class TodoManagerTest(unittest.TestCase):
    
    def setUp(self):
        self.todo_manager = TodoManager()
    
    def test_save(self):
        id = "568"
        task = "The first task details everything"
        is_done = False
        result = self.todo_manager.save(id, task, is_done)
        todo_expected = {"id": id, "task": task, "is_done": is_done}
        self.assertEqual(todo_expected, result["data"])
