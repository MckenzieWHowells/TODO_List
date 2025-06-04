"""
A simple to-do application that allows users to add tasks to a to-do list.
"""

def convey_instructions():
    """
    Print instructions for the user
    """
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("="*50)

def add_task(listo:list[str]):
    """
    Add task to-do list

    Args:
        listo (list[str]): The user's to-do list
    """
    tsk = input("Enter task: ")
    listo.append(tsk)
    print("-"*50)

def view_task(listo:list[str]):
    """
    View tasks in to-do list

    Args:
        listo (list[str]): The user's to-do list
    """
    print("Tasks:")
    for i, t in enumerate(listo):
        print(f"{i+1}. {t}")
    print("-"*50)

def mark_as_done(listo:list[str]):
    """
    Mark tasks as done in to do list (takes them out of list)

    Args:
        listo (list[str]): The user's to-do list
    """
    usr_input = input("Enter task number to mark as done: ")
    if 0 <=  int(usr_input) - 1 < len(listo):
        listo.pop(int(usr_input) - 1)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def print_exit_message():
    """
    Print exit message
    """
    print("Exiting.")
    print("-"*50)

def main():
    """
    Runs the main menu for the to do list program
    """
    listo:list[str] = []
    while True:

        convey_instructions()

        x = input("Enter your choice: ")

        if x == '1':
            add_task(listo)
        elif x == '2':
            view_task(listo)
        elif x == '3':
            mark_as_done(listo)
        elif x == '4':
            print_exit_message()
            break
        else:
            print("Invalid choice.")
            print("-"*50)
            kgk

main()
 