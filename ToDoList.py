import os

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_id = 1

    def add_task(self, description):
        self.tasks[self.task_id] = {"description": description, "completed": False}
        print(f"Task added with ID {self.task_id}")
        self.task_id += 1

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for task_id, task in self.tasks.items():
            status = "Done" if task["completed"] else "X"
            print(f"{task_id}. {task['description']} [{status}]")
        print("------------------\n")

    def update_task(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id]["description"] = new_description
            print(f"Task {task_id} updated.")
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted.")
        else:
            print("Invalid task ID.")

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed.")
        else:
            print("Invalid task ID.")

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark a task as completed")
        print("6. Clear the screen")
        print("7. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            description = input("Enter task description: ").strip()
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: ").strip())
                new_description = input("Enter new task description: ").strip()
                todo_list.update_task(task_id, new_description)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                todo_list.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to mark as completed: ").strip())
                todo_list.mark_task_completed(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "6":
            todo_list.clear_screen()
        elif choice == "7":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
