import datetime

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Please enter a valid value.")
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def add_task(tasks):
    task = get_user_input("Enter a new task: ")
    priority = get_user_input("Enter the task priority (low, medium, high): ")
    due_date = get_date("Enter the due date (YYYY-MM-DD): ")
    tasks.append((datetime.datetime.now(), task, priority, due_date, False))
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, (time, task, priority, due_date, completed) in enumerate(tasks):
            status = "Completed" if completed else "Pending"
            print(f"{i+1}. {task} ({priority}) - Due: {due_date} ({status})")

def mark_task_complete(tasks):
    index = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index] = (tasks[index][0], tasks[index][1], tasks[index][2], tasks[index][3], True)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted.")
    else:
        print("Invalid task number.")

def get_date(prompt):
    while True:
        try:
            user_input = get_user_input(prompt)
            date_object = datetime.datetime.strptime(user_input, "%Y-%m-%d")
            return date_object.date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    tasks = []

    while True:
        print("\nTask Scheduler")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = get_user_input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()