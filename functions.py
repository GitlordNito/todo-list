FILEPATH = "files/todos.txt"


def get_todos(filepath: str = FILEPATH) -> list:
    """ Read text file a return list of to-do's"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg: list, filepath: str = FILEPATH):
    """ Write the to-do items list in text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

