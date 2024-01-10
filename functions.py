FILEPATH = "todos.txt"  # varijable koje sadržavaju konstante tako da ako ako se promijeni naziv datoteke, ne moramo mijenjati nazive u kodu // pišemo ih velikim slovima

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Read the to do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":          # when you run cli.py and it runs functions, its name is functions, but when you run it in functions.py its name is "__main__"
    print("Hello from functions")      #kad je kod pušten direktno je "__main__", kad je pušteno kroz drugi file ima drugo ime
    print(get_todos())

