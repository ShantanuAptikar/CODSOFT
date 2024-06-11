class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Removed task: '{removed_task['task']}'")
        else:
            print("Invalid task number!")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            print(f"Updated task number {task_index + 1} to: '{new_task}'")
        else:
            print("Invalid task number!")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Marked task number {task_index + 1} as completed.")
        else:
            print("Invalid task number!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{idx}. {task['task']} [{status}]")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Update a task")
    print("4. Complete a task")
    print("5. List all tasks")
    print("6. Exit")

def main():
    todo_list = ToDoList()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
