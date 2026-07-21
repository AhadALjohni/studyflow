import unittest

from tasks import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_task(self) -> None:
        manager = TaskManager()

        manager.add_task("Study Git")

        self.assertEqual(manager.list_tasks(), ["Study Git"])

    def test_empty_task_is_rejected(self) -> None:
        manager = TaskManager()

        with self.assertRaises(ValueError):
            manager.add_task("   ")


if __name__ == "__main__":
    unittest.main()