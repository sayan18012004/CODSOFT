import os

def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(task, filename="todo.txt"):
    with open(filename, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully!")

def view_tasks(filename="todo.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\n===== To-Do List =====")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("\nNo tasks found.")
    else:
        print("\nNo tasks found.")

def mark_completed(index, filename="todo.txt"):
    tasks = read_tasks(filename)
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        with open(filename, "w") as file:
            file.writelines(tasks)
        print(f"Task '{completed_task.strip()}' marked as completed!")
    else:
        print("Invalid task index.")

def delete_task(index, filename="todo.txt"):
    tasks = read_tasks(filename)
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        with open(filename, "w") as file:
            file.writelines(tasks)
        print(f"Task '{deleted_task.strip()}' deleted successfully!")
    else:
        print("Invalid task index.")

def read_tasks(filename="todo.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.readlines()
    else:
        return []

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter the index of the completed task: "))
            mark_completed(index)
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            delete_task(index)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

