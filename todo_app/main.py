#Version 1.0 

import json 

#These functions will load and save tasks from the JSON file. 
def load_tasks (filename = "tasks.json"): 
    try: 
        with open (filename, "r") as f: 
            return json.load(f)
    except FileNotFoundError: 
        return []
def save_tasks(tasks, filename = "tasks.json"): 
    with open (filename, "w") as f: 
        json.dump(tasks, f, indent = 2)

#The following functions will add, view, and delete tasks 
def show_the_tasks (tasks):
    if not tasks: 
        print ("Hey! You do not have any tasks yet!")
    for i , task in enumerate (tasks): 
        print (f"{i+1}. {task}")

def add_task (tasks):
    task = input ("enter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task (tasks): 
    show_the_tasks(tasks)
    try:
        idx = int(input("Please enter the task number you want to delete: ")) - 1 
        removed = tasks.pop(idx)
        print(f"Successfully Removed Task: {removed}")
    except (IndexError, ValueError): 
        print ("Invalid Task Number.")
#Loop that interacts with the app, adding a main menu 

def main (): 
    tasks = load_tasks()
    while True: 
        print("\nT0-D0 List")
        print("1. Show Your Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Quit App")

        users_choice = input ("Choose an option: ")
        if users_choice == "1": 
            show_the_tasks(tasks)
        elif users_choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif users_choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif users_choice == "4":
            print("Goodbye")
            break
        else:
            print("The choice you entered is Invalid.")
if __name__ == "__main__": 
    main()




        