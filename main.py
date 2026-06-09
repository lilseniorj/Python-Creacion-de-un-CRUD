clients = "Pablo, Ricardo, "


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("Client already exists in the system")


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ", ", update_client_name + ", ")
    else:
        print("Client is not in the system")


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients += ", "


def _print_welcome():
    print("Welcome to the client management system")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input("What is the name of the client? ")

    return client_name


if __name__ == "__main__":
    _print_welcome()

    command = input()
    command = command.upper()

    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "D":
        pass
    elif command == "U":
        client_name = _get_client_name()
        update_client_name = input("What is the new name of the client? ")
        update_client(client_name, update_client_name)
        list_clients()
    else:
        print("Invalid command")

    create_client("Maria")

    list_clients()