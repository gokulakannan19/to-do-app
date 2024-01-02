FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the to-do items
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_local:
        todos_local = [todo.strip("\n") for todo in file_local.readlines()]
    return todos_local


def write_todos(todo_args, filepath=FILEPATH):
    """
    Write the to-do to a text file
    :param todo_args:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file_local:
        todo_args = [todo+"\n" for todo in todo_args]
        file_local.writelines(todo_args)

