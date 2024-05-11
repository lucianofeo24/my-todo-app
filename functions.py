FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        # 'todos_local' è una lista
        todos_local = file_local.readlines()
    return todos_local

# la funzione non ritorna nulla perchè serve a scrivere su un file di testo e non deve restituire nulla al codice

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())