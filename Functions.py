FILEPATH = 'todos.txt'
from datetime import datetime

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        file_local = file.readlines()
        return file_local


def write_todos(passed_todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(passed_todos)


def done_todos(completed, filepath = "completed_todos.txt"):
    timestamp = datetime.now().strftime("%m-%d-%Y %H:%M")
    entry = f"{completed.strip()} - Completed on {timestamp}\n"
    with open(filepath, 'a') as file:
        file.writelines(entry)

if __name__ == "__main__":
    write_todos('test')
    print("It works!")