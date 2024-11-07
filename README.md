
# To-Do List Application

A command-line application to manage a simple to-do list. This app allows users to add tasks, delete tasks, and view all tasks in a list. It also includes error handling to ensure smooth user interaction.

## Table of Contents
1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [Future Improvements](#future-improvements)
6. [Contributing](#contributing)
7. [License](#license)

---

### Features
- **Add Tasks**: Users can add a new task to the list.
- **Delete Tasks**: Users can remove a task from the list.
- **View Tasks**: Displays the list of tasks in a formatted way.
- **Error Handling**: Prevents users from entering invalid options, empty tasks, or tasks that don't exist.

---

### Getting Started

#### Prerequisites
- Python 3.x

#### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git

2. Navigate to the project directory:
   ```bash
   cd YourRepoName
   ```
3. Run the program:
   ```bash
   python3 your_program.py
   ```

---

### Usage

1. Run the program using Python.
2. Follow the on-screen prompts:
   - Type `1` to add a task.
   - Type `2` to delete a task.
   - Type `3` to view all tasks.
   - Type `4` to quit the program.

#### Example Usage

```
Welcome to To-Do List

Menu
1. Add Task
2. Delete Task
3. View Tasks
4. Quit Application

Select a Menu Option (e.g 1, 2, 3, 4): 
```

---

### Code Structure

- `tasks = []`: A list that holds all to-do tasks.
- **Functions**:
  - `add_task()`: Prompts the user to add a new task and validates the input.
  - `delete_task()`: Allows the user to delete a specified task from the list, ensuring the task exists.
  - `view_tasks()`: Displays all tasks in the list, formatted as a numbered list.
  - `user_input()`: Handles the menu selection process, ensuring valid input.
  - `continue_use()`: Asks the user if they want to perform another action or quit.

Each function has its own purpose, making the code modular and organized.

---

### Future Improvements

Considering adding these features to make the program more robust and user-friendly (not anytime soon maybe, IDK though):

- **Save and Load Tasks**: Store tasks in a file so they persist between program runs.
- **Task Completion**: Allow users to mark tasks as complete.
- **Prioritization**: Add a priority level to tasks.
- **UI Enhancements**: Use a graphical interface for a more intuitive experience.

---

### Contributing

Feel free to submit issues or pull requests for new features or bug fixes.

### License

None

---
