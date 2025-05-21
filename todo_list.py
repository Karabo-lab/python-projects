
def show_tasks(tasks):
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def main():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
