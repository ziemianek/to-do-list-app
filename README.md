# TO-DO LIST APP
### Video Demo:  https://www.youtube.com/watch?v=AQmZTv1IoSs


### Description

The to-do list app is a command-line application that allows users to manage their tasks by adding, removing, and marking tasks as completed, as well as viewing their list of tasks. The app also has the ability to save and load tasks from a file, so that users can access their tasks across multiple sessions.

### Data model

The app uses a data model based on a list of dictionaries, with a dictionary representing individual tasks and a python list object representing the overall to-do list. Each task has three attributes: description, which stores the task description as a string; due_date, which stores the task due date as a string; and completed, which stores a boolean value indicating whether the task has been completed or not. 

The app has a simple command-line interface, which prompts the user to enter an action and then performs the corresponding action. The available actions are:

- **add**: adds a new task to the to-do list
- **remove**: removes a task from the to-do list
- **complete**: marks a task as completed
- **view**: displays a list of all tasks
- **view completed**: displays a list of all tasks marked as completed
- **view not completed**: displays a list of all tasks marked as not completed
- **save**: saves the current tasks to a file
- **load**: loads the tasks from a file into the app
- **exit**: exits the app

### How to use the App

You can use this program by executing it with python:

```
python project.py
```

But first make sure that you have `json` and `sys` modules installed. They come by default with have Python installation on your computer but you can try to install it using pip:

```
pip install json
pip install sys
```

To use the app, run the script from the command line. You will be prompted to enter an action. Follow the prompts to perform the desired action.

For example, to add a new task, enter `add` when prompted for an action. You will then be prompted to enter the task description and due date.

To remove a task, enter `remove` when prompted for an action. You will then be prompted to enter the index of the task to remove.

To mark a task as completed, enter `complete` when prompted for an action. You will then be prompted to enter the index of the task to mark as completed.

To view the list of tasks, enter `view` when prompted for an action. You can also enter `view completed` or `view not completed` to view only the completed or not completed tasks, respectively.

To save the tasks to a file, enter `save` when prompted for an action. You will then be prompted to enter the filename to save the tasks to.

To load the tasks file to the program, enter `load` when prompted for an action. File will be automaticaly loaded and saved task list will be ready to work with.

### Functionality

The app's functionality is implemented using simple functions:

- `add_task(description, due_date)`: adds a new task to the list with the specified description and due date
- `remove_task(index)`: removes the task at the specified index from the list
- `mark_task_as_completed(index)`: marks the task at the specified index as completed
- `view_tasks(completed=None)`: displays the list of tasks. An optional parameter allows you to filter the tasks by completion status (True for completed tasks, False for not completed tasks, or None for all tasks)
- `save_tasks(filename)`: saves the tasks to the specified file
- `load_tasks(filename)`: loads the tasks from the specified file

#### Adding a task

To add a task to the to-do list, the user enters the add action and provides the task description and due date. The app then creates a new task and adds it to the tasks list using the `add_task` function.

```python
def add_task(description, due_date):
    """Add new task to the list of all tasks"""
    
    tasks.append({
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Info: Added new task")
```

#### Removing a task

To remove a task from the to-do list, the user enters the remove action and specifies the index of the task to be removed. The app removes the task from the tasks list using the `remove_task` function, which uses the pop method to remove the task at the specified index. 

```python
def remove_task(index):
    """Remove task from the task list"""
    
    try:
        tasks.pop(index - 1)
        print("Info: Task removed")
        return True
    except IndexError:
        print("Error: invalid index")
        return False
```

The `remove_task` function includes a try-except block to catch an `IndexError` exception, which will be raised if the user attempts to remove a task with an index that is out of range for the tasks list. If an `IndexError` is caught, the app prints an error message and continues running otherwise it prints a message to inform that task has been removed succesfully. For testing, the function returns `True` if succeeded or `False` if there was an `IndexError`.

#### Marking a task as completed

To mark a task as completed, the user enters the complete action and specifies the index of the task to be marked. The app marks the task as completed using the `mark_task_as_completed` function, which sets the `completed` attribute of the task with correct index.

```python
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
```

The `mark_task_as_completed` function includes a try-except block to catch an `IndexError` exception, which will be raised if the user attempts to remove a task with an index that is out of range for the tasks list. If an `IndexError` is caught, the app prints an error message and continues running otherwise it prints chosen task to show that completion status is now changed to `True`. For testing, the function returns `True` if succeeded or `False` if there was an `IndexError`.

#### View tasks
To view task list, the user enters the view action. The app prints all tasks currently existing in the program using `view_tasks`. User can also specity the `completed` parameter which is set to None by default. If `completed=True` the program will display only tasks that have their `completed` parameter set to `True`. Otherwise if `completed=False` the program will display only tasks with `completed` attribute set to `False`.

```python
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
```

#### Save task list to a file
To save the task list to a file, the user enters the save action. The app uses `json` module and the `save_tasks` function to save task list to a .json file named according to `filename` parameter. Program writes all tasks to a file otherwise if file does not exist, the app creates the file and then writes to it.

```python
def save_tasks(filename):
    """Save all tasks to json file"""
    
    global tasks
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)
        print("Info: Tasks file saved")
```

#### Load task list from a file
To load the task list from the file, the user enters the load action. The program then loads tasks from a json file to the app using `load_tasks` function.

```python
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
```
The `load_tasks` function includes a try-except block to catch a `FileNotFoundError` exception, which will be raised if the user attempts to load a file that does not exist. If a `FileNotFoundError` is caught, the app prints an error message and continues running otherwise it loads the task list.

### Testing

All the tests created with `pytest` module are located in `test_project.py` file. You can run it using `pytest` but first make sure you have `pytest` installed on your computer.

```
pip install pytest
```
Then try running the tests:

```
pytest test_project.py
```
