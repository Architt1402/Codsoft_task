# COMMAND LINE APPLICATION: TO-DO LIST

# Author : Archit Tanwar
# Description:
# This command-line application helps track your tasks.
# You can add, delete, update, and view tasks through the given menu.

# Initialize an empty list to hold tasks
task_list = []

# Function to display the main menu and handle user inputs
def menu():
    print("\n\n\t\t\tby @Archit Tanwar")
    print("________________________________________")
    print("\n\t\t\t***TO-DO LIST APPLICATION***\n")
    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Update Task")
        print("5. Exit")
        
        # Get the user's choice
        try:
            choice = int(input("\nSelect an option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.\n")
            continue
        
        # Process user's choice
        if choice == 1:
            add_task()
        elif choice == 2:
            delete_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            update_task()
        elif choice == 5:
            print("Exiting... Your tasks are saved!\n")
            break
        else:
            print("Please enter a valid choice (1-5).\n")


# Function to add a task
def add_task():
    task = input("Enter the task to add: ")
    task_list.append(task)
    print(f"Task '{task}' added successfully!\n")
    print("________________________________________")


# Function to delete a task
def delete_task():
    if len(task_list) == 0:
        print("No tasks available to delete.\n")
        return

    print("\nYour Current Tasks:")
    for index, task in enumerate(task_list, 1):
        print(f"{index}. {task}")

    try:
        task_index = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_index <= len(task_list):
            removed_task = task_list.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid task number.\n")

    print("________________________________________")


# Function to view all tasks
def view_tasks():
    if len(task_list) == 0:
        print("No tasks to display.\n")
    else:
        print("\nYour Current Tasks:")
        for index, task in enumerate(task_list, 1):
            print(f"{index}. {task}")
        print("\nTasks displayed successfully!\n")
    print("________________________________________")


# Function to update an existing task
def update_task():
    if len(task_list) == 0:
        print("No tasks available to update.\n")
        return

    print("\nYour Current Tasks:")
    for index, task in enumerate(task_list, 1):
        print(f"{index}. {task}")

    try:
        task_index = int(input("\nEnter the number of the task to update: "))
        if 1 <= task_index <= len(task_list):
            new_task = input("Enter the updated task: ")
            task_list[task_index - 1] = new_task
            print(f"Task updated to: '{new_task}'\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid task number.\n")

    print("________________________________________")


# Main function to execute the application
if __name__ == "__main__":
    menu()
