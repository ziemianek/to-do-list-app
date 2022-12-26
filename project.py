# Title: Todo-list app for CS50P final project
# Author: Michal Ziemianek

import sys
import json


tasks = []


def main():
    
    # Main loop
    while True:
        action = input("What would you like to do? (add, remove, complete, view, view completed, view not completed, save, load, exit) ")
        action = action.strip()
        if action == "add":
            description = input("Enter the task description: ")
            due_date = input("Enter the task due date: ")
            add_task(description, due_date)
        elif action == "remove":
            idx = int(input("Enter the task index: "))
            remove_task(idx)
        elif action == "complete":
            idx = int(input("Enter the task index: "))
            mark_task_as_completed(idx)
        elif action == "view":
            view_tasks()
        elif action == "view completed":
            view_tasks(completed=True)
        elif action == "view not completed":
            view_tasks(completed=False)
        elif action == "save":
            save_tasks("tasks.json")
        elif action == "load":
            load_tasks("tasks.json")
        elif action == "exit":
            sys.exit("\nSee you later!\n")


def add_task(description, due_date):
    """Add new task to the list of all tasks"""
    
    tasks.append({
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Info: Added new task")


def remove_task(index):
    """Remove task from the task list"""
    
    try:
        tasks.pop(index - 1)
        print("Info: Task removed")
        return True
    except IndexError:
        print("Error: invalid index")
        return False


def mark_task_as_completed(index):
    """Mark task as completed"""
    
    try:
        if index > 0:
            task = tasks[index - 1]
            task["completed"] = True
            print(f"{index}: {task['description']}, due on {task['due_date']}, completed: {task['completed']}")
        else:
            raise IndexError
        return True
    except IndexError:
        print("Error: invalid index")
        return False


def view_tasks(completed=None):
    """
    View tasks according to completion status:
    ``completed=None`` -> view all tasks
    ``completed=True`` -> view only tasks marked as completed
    ``completed=False`` -> view only tasks marked as uncompleted
    """
    
    if completed is None:
        for i, task in enumerate(tasks):
            print(f"{i + 1}: {task['description']}, due on {task['due_date']}, completed: {task['completed']}")
    else:
        for i, task in enumerate(tasks):
            if task["completed"] == completed:
                print(f"{i + 1}: {task['description']}, due on {task['due_date']}, completed: {task['completed']}")


def save_tasks(filename):
    """Save all tasks to json file"""
    
    global tasks
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)
        print("Info: Tasks file saved")


def load_tasks(filename):
    """Load task list from a json file"""
    
    global tasks
    try:
        with open(filename, "r") as f:
            tasks = json.loads(f.read())
            return True
    except FileNotFoundError:
        print("Error: tasks file not found")
        return False



if __name__ == "__main__":
    main()