import re
import os
import subprocess

filename = "db_task.txt"

def createFile(dbFile, task):
    with open(dbFile, "w") as file:
        file.write(task + "\n")  # Ensure a newline is added

def addNewTask(dbFile, task):
    index = readALastFile(dbFile)
    indexModified = int(index) + 1 if index else 1  # Ensure correct indexing
    with open(dbFile, "a") as file:
        file.write(f"[{indexModified}] {task}\n")  # Ensure newline
    print(f"Task [{indexModified}] added.")

def readALastFile(dbFile):
    with open(dbFile, "r") as file:
        index_list = re.findall(r"\[(\d+)\]", file.read())  # Extract only task numbers
        return index_list[-1] if index_list else None  # Return the last task number

def readAllRow(dbFile):
    with open(dbFile, "r") as file:
        tasks = [extract_task(task) for task in file.readlines() if extract_task(task)]
        for task in tasks:
            print(task)
        return tasks

def extract_task(text):
    match = re.match(r"\[(\d+)\]\s*(.+)", text.strip())  
    return f"{match.group(1)}: {match.group(2)}" if match else None  

def clear_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

def menuBar():
    print("\n\n")
    print("-----------------------------")
    print("------1. Add new task--------")
    print("------2. View Task   --------")
    print("------3. Delete the last task")
    print("-----------------------------")

while True:
    menuBar()
    userInput = input("Enter option...\n").strip()

    if userInput == "1":
        taskInput = input("Enter the task: ").strip()
        
        if not os.path.exists(filename):
            createFile(filename, f"[1] {taskInput}")
            print("File created successfully.")
        else:
            addNewTask(filename, taskInput)
        clear_terminal()
    
    elif userInput == "2":
        print("\nSHOW DATA:\n")
        readAllRow(filename)
    
    elif userInput == "3":
        print("\nFeature not implemented yet.")
