print("Alvan's First Python Project")

import json
import os

FILE_NAME = 'tasks.json'


# to check if the file 'tasks.json is exist
# return empty list if not exist
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# save the tasks in file after running program this time
# will create tasks.json if not exist
# will overwrite tasks.json if file is created
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# show tasks starting from 1 instead of default 0 (auto assign starting from 1 to total tasks added)
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nTasks")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['task']} [{status}]")

# add task into dictionaries with status:incomplete
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})

# mark task as complete
# (num -1) because default is starting fromo 0
# ensure input is correct 
def mark_complete(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to mark as complete: "))
    if 0 < num <= len(tasks):
        tasks[num - 1]["completed"] = True
    else:
        print("\nInvalid input!")

# delete task and ensure correct input
def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
    else:
        print("\nInvalid input!")

def main():
    tasks = load_tasks()
    while True:
        print("\n------------------")
        print("--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit and Save")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")


# runs main() only if the script is executed directly, not imported
if __name__ == "__main__":
    main()
