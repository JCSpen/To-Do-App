FilePath = "Data.txt"


def get_todos(filepath=FilePath):  # Fetches from list
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FilePath):   # Writes to file
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
