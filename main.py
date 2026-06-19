clients = ["Pablo", "Ricardo"]


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print("Client already exists in the system")


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print("Client is not in the system")


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print("Client is not in the system")


def search_client(client_name):

    for client in clients:
        if client.lower() == client_name.lower():
            return True

    return False


def list_clients():
    for idx, client in enumerate(clients):
        print("{}: {}".format(idx, client))



def _print_welcome():
    print("Welcome to the client management system")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")
    print("[L]ist clients")


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
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is in the system")
        else:
            print("The client: {0} is not in the system".format(client_name))
    elif command == "U":
        client_name = _get_client_name()
        update_client_name = input("What is the new name of the client? ")
        update_client(client_name, update_client_name)
        list_clients()
    elif command == "L":
        list_clients()
    else:
        print("Invalid command")