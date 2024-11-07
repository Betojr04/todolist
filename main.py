tasks = []


def add_task():
    """adds new task to task list []

    Args:
        item (string): new task input by user
    """
    item = input("enter new task: ")

    while not item.strip():
        print("Cannot add an empty task.")
        item = input("enter new task: ")
    tasks.append(item)
    print("Task added successfully!")


def delete_task():
    """deletes entered task from the task list []

    Args:
        item (string): entered task from user
    """

    item = input("enter task to remove: ")
    if not item.strip():
        print("Entry cannot be empty.")
        item = input("enter task to remove: ")
    elif item not in tasks:
        print("Cannot delete a task that does not exist.")
    else:
        tasks.remove(item)
        print(f"{item} successfully removed!")


def view_tasks():
    """prints the task list [] in a formatted way

    Args:
        task list [] (list): entered task from user
    """
    if not tasks:
        print("Cannot print an empty list")
    else:
        counter = 0
        for item in tasks:
            counter += 1
            print(f"{counter}.) {item}")


def user_input():
    """prompts user for their menu input

    Returns:
        _type_: _description_
    """
    options = [1, 2, 3, 4]
    user_input = None
    while user_input not in options:
        try:
            user_input = int(input("Select a Menu Option (e.g 1, 2 , 3, 4): "))
        except ValueError:
            print(f"Please choose an option from the menu")
    return user_input


def continue_use():
    """checks if the user wishes to continue using the program or not

    Returns:
        boolean: returns True or False depending user enters yes or no
    """
    again = input("would you like to do something else? (yes/no): ")
    if not again.strip():
        print("cannot be empty, enter `yes` or `no`.")
    elif again.lower() == "no":
        return False
    elif again.lower() == "yes":
        return True


# while loop to loop the program and preform multiple actions before quitting if necessary.
while True:
    """loop to take user through the program and offer multiple actions before exiting"""

    print("Welcome to To-Do List\n")

    print("Menu")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Quit Application")

    user_choice = user_input()

    if user_choice == 1:
        add_task()
        if continue_use() == False:
            print("Thank you for using the program. Goobye!")
            break
    elif user_choice == 2:
        delete_task()
        if continue_use() == False:
            print("Thank you for using the program. Goobye!")
            break
    elif user_choice == 3:
        view_tasks()
        if continue_use() == False:
            print("Thank you for using the program. Goobye!")
            break
    elif user_choice == 4:
        print("Thank you for using the program. Goobye!")
        break
