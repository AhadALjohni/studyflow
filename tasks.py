class TaskManager:
    """Manage a collection of study tasks."""

    def __init__(self) -> None:
        self._tasks: list[str] = []

    def add_task(self, title: str) -> None:
        """Add a non-empty task."""
        cleaned_title = title.strip()

        if not cleaned_title:
            raise ValueError("Task title cannot be empty.")

        self._tasks.append(cleaned_title)

    def list_tasks(self) -> list[str]:
        """Return a copy of all tasks."""
        return self._tasks.copy()