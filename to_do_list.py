# Function to display the menu
def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

# Function to add a task to the list
def add_task(tasks):
    task_description = input("Enter the task description: ")
    tasks.append({"description": task_description, "completed": False})
    print("Task added successfully!")

# Function to display all tasks
def display_tasks(tasks):
    print("\n===== To-Do List =====")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['description']} - {'Completed' if task['completed'] else 'Pending'}")

# Function to mark a task as completed
def mark_completed(tasks):
    if tasks:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number. Please enter a valid task number.")
    else:
        print("No tasks to mark as completed.")

# Main function
def main():
    tasks = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            display_tasks(tasks)
        elif choice == 3:
            mark_completed(tasks)
        elif choice == 4:
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the program
if __name__ == "__main__":
    main()
