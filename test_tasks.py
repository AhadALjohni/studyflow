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

    def test_delete_task(self) -> None:
        manager = TaskManager()

        manager.add_task("Git")
        manager.add_task("Python")

        deleted = manager.delete_task(0)

        self.assertTrue(deleted)
        self.assertEqual(manager.list_tasks(), ["Python"])

    def test_delete_task_with_invalid_index(self) -> None:
        manager = TaskManager()

        manager.add_task("Git")

        deleted = manager.delete_task(5)

        self.assertFalse(deleted)
        self.assertEqual(manager.list_tasks(), ["Git"])

    def test_delete_task_with_negative_index(self) -> None:
        manager = TaskManager()

        manager.add_task("Git")

        deleted = manager.delete_task(-1)

        self.assertFalse(deleted)
        self.assertEqual(manager.list_tasks(), ["Git"])


if __name__ == "__main__":
    unittest.main()