def display_menu():
    menu = """
Welcome to the To-Do List App!
Menu:
1. Add task(s)
2. View tasks
3. Mark a task as complete
4. Delete task(s)
5. Reorder tasks
6. Quit
"""
    print(menu)

def get_user_choice():
    while True:
        try:
            user_input = int(input("Please enter your choice (1-6): "))
            if 1 <= user_input <= 6:
                return user_input
            else:
                print("Invalid choice. Please enter a number from 1-6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_tasks(tasks):
    while True:
        task = input("Add a new task to your list: ")
        tasks.append({"task": task, "status": "Incomplete"})
        print(f'Task "{task}" added to list!')
        
        if input("Would you like to add another task? (y/n): ").lower() != 'y':
            break

def view_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {task['status']}")
    else:
        print("Task list empty.")

def mark_task_complete(tasks):
    if not tasks:
        print("No tasks to complete.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task you want to complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            print(f'Task "{tasks[task_number - 1]["task"]}" marked as complete!')
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

def delete_tasks(tasks):
    while tasks:
        view_tasks(tasks)
        try:
            delete_task = int(input("Enter the number of the task you want to delete: "))
            if 1 <= delete_task <= len(tasks):
                removed_task = tasks.pop(delete_task - 1)
                print(f'Task "{removed_task["task"]}" has been deleted!')
                
                if not tasks:
                    print("No more tasks to delete.")
                    break
                
                if input("Would you like to delete another task? (y/n): ").lower() != 'y':
                    break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")

def reorder_tasks(tasks):
    if not tasks:
        print("No tasks to reorder.")
        return

    view_tasks(tasks)
    try:
        old_pos = int(input("Enter the number of the task you want to move: ")) - 1
        new_pos = int(input("Enter the new position for this task: ")) - 1

        if 0 <= old_pos < len(tasks) and 0 <= new_pos < len(tasks):
            task = tasks.pop(old_pos)
            tasks.insert(new_pos, task)
            print("Task reordered successfully!")
            view_tasks(tasks)
        else:
            print("Invalid task number or position. Please try again.")
    except ValueError:
        print("Please enter valid numbers.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_task_complete(tasks)
        elif choice == 4:
            delete_tasks(tasks)
        elif choice == 5:
            reorder_tasks(tasks)
        elif choice == 6:
            print("Goodbye!")
            break

        input("\nPress Enter to continue...")

main()