from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import pickle
import os


def loadList():
    with open("tasklist", "rb") as fp:   
        return pickle.load(fp)

def saveList(listname):
    with open("tasklist", "wb") as fp:   
        pickle.dump(listname, fp)

try:
    tasks = loadList()
except:
    tasks = [Choice(value=False, name="Add New Task"),
         "Task1",
         "Task2",
         "Task3"]

while True:
    action = inquirer.select(
        message="Select an action:",
        choices= tasks,
        default=None,
    ).execute() 
    
    if not(action):
        newTask = input("Name of task:")
        tasks.append(newTask)
    else: 
        tasks.remove(action)

    os.system('cls' if os.name == 'nt' else 'clear')
    saveList(tasks)