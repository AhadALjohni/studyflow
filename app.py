from tasks import TaskManager


def display_tasks(manager: TaskManager) -> bool:
    """
    Display all tasks.

    Returns:
        True if tasks exist.
        False if the task list is empty.
    """
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks available.")
        return False

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    return True


def main() -> None:
    """Run the StudyFlow command-line application."""
    manager = TaskManager()

    print("StudyFlow")
    print("A simple study task manager.")

    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()

            try:
                manager.add_task(title)
                print("Task added successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            display_tasks(manager)

        elif choice == "3":
            if not display_tasks(manager):
                continue

            try:
                number = int(input("Task number: ").strip())
                index = number - 1

                if manager.delete_task(index):
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()