FILEPATH = "todos.txt"

# reads textfile and assign it to the list


def read_text(filename=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filename, 'r') as file:
        listname = file.readlines()

    return listname


def write_text(todos_arg, filename=FILEPATH):
    """Write the todo items list in the text file"""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
