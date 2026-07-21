from tasks import TaskManager


def main() -> None:
    """Run the StudyFlow command-line application."""
    manager = TaskManager()

    print("StudyFlow")
    print("A simple study task manager.")

    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            manager.add_task(title)
            print("Task added successfully.")

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks available.")
                continue

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()