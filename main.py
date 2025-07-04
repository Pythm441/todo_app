import os

tasks = []
fileName = "tasks.txt"

def load_tasks(fileName):
    if not os.path.exists(fileName):
        return tasks
    with open(fileName, 'r') as file:
        for line in file:
            task = line.strip()
            if task:
                tasks.append(task)
    return tasks

def save_tasks(tasks, fileName):
    with open(fileName, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):

    task_name = input("Add a task:\n")
    tasks.append(task_name)


    return




def check_task(tasks):
    try:
        task_number = int(input("What is the number of task you want to check? "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Removed task {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")        
    return
def show_tasks(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("Add some tasks first")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("--------------\n")
def main():
    tasks = load_tasks(fileName)
    while True:
        
        print("Welcome to this To do app")

        show_tasks(tasks)

        print("Choose an option:\n 1. Add a task\n 2. Delete/check a task\n 3. Quit")

        try:
            option = int(input("Enter a the number of the option: "))
        except ValueError:
            print("please enter a valid option.")
            continue



        if option == 1:
            add_task(tasks)
        elif option == 2:
            check_task(tasks)
        elif option == 3:
            save_tasks(tasks, fileName)
            break
    return



if __name__ == "__main__":
    main()