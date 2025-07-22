def show_menu():
    print("\n To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({'title': title, 'completed': False})
    print("✅ Task added!")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]['completed'] = True
            print("🎉 Task marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            deleted = tasks.pop(choice - 1)
            print(f"🗑️ Task '{deleted['title']}' deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Have a productive day!")
            break
        else:
            print("❌ Invalid option. Please choose from 1 to 5.")

# Run the app
main()
