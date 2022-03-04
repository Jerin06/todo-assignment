import unittest

from app.todo_manager import TodoManager


class TodoManagerTest(unittest.TestCase):
    def test_add_task(self):
        todo_manager = TodoManager()
        todo_manager.add_task("568", "The first task details everything")
        task = todo_manager.get_task_by_id("568")
        self.assertEqual("The first task details everything", task)
