import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks added!")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number: ") )
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
    except (ValueError, IndexError):
        print("Invalid choice.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number: "))
        tasks.pop(task_num -1)
        save_tasks(tasks)
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid Choice!")

def main():
    tasks = load_tasks()

    while True:
        print("\n - - - TO-DO-LIST-APP - - -")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        if choice == "2":
            view_tasks(tasks)
        if choice == "3":
            complete_task(tasks)
        if choice == "4":
            delete_task(tasks)
        if choice == "5":
            print("Goodbye!")
            break

    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    main()