import os
import json
import subprocess
from beautifultable import BeautifulTable, BTRowCollection
import sys
import validators

memhost_filepath = os.path.expanduser("~") + "/memhost"


def data_get():
    default_data = {"servers": {}}
    try:
        with open(memhost_filepath, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except:
        return data_upd(default_data)


def data_upd(data):
    if os.path.exists(memhost_filepath):
        os.remove(memhost_filepath)

    with open(memhost_filepath, 'w') as f:
        f.write(json.dumps(data))
        subprocess.run(["attrib", "+H", memhost_filepath], check=True)
    return data


def connect(server):
    subprocess.run(['ssh', f'{server["username"]}@{server["host"]}'])


def show_all_servers(servers):
    table = BeautifulTable()
    table_collection = BTRowCollection(table)
    table_data = ["", "", ""]
    if servers:

        for name in servers:
            table_data[0] += f'\n{name}'
            table_data[1] += f'\n{data["servers"][name]["username"]}@{data["servers"][name]["host"]}'
            table_data[2] += f'\n{data["servers"][name]["description"]}'
        table_data[0] = table_data[0][1:]
        table_data[1] = table_data[1][1:]
        table_data[2] = table_data[2][1:]
        table_collection.append(table_data)
        print(table)
    else:
        print("There's no servers")


data = data_get()
if len(sys.argv) > 1:
    if sys.argv[1] in data["servers"]:
        connect(data["servers"][sys.argv[1]])
show_all_servers(data["servers"])


def InputWithoutInterrup(text, retry=False):
    if not retry:
        try: return input(text)
        except KeyboardInterrupt:
            print()
            return None

    while True:
        try: return input(text)
        except KeyboardInterrupt:
            print()


def ssh_copy_id(server):
    subprocess.run(['bash', '-l', 'ssh-copy-id', f'{server["username"]}@{server["host"]}'])


while True:
    com = InputWithoutInterrup(">> ", retry=True)
    if com == "add":
        name = InputWithoutInterrup("Name: ")
        if not name: continue

        username = InputWithoutInterrup("Username (leave empty for root): ")
        if username is None: continue
        if username == '': username = 'root'

        host = InputWithoutInterrup("Host: ")
        if host is None: continue
        if not validators.ipv4(host) and not validators.domain(host):
            print("Invalid host")
            continue

        description = InputWithoutInterrup("Description: ")
        if description is None: continue

        data["servers"][name] = {"username": username,
                                 "host": host,
                                 "description": description}
        server = data["servers"][name]
        ssh_copy_id(server)
        data_upd(data)
        connect(server)
        continue

    if com == "del":
        name = InputWithoutInterrup("Name: ")
        if name is None: continue
        if name in data["servers"]:
            print("Deleted.")
            del data["servers"][name]
            data_upd(data)
        else: print("Server not found.")
        continue

    if com == "ls":
        show_all_servers(data["servers"])
        continue

    if com == "copyid":
        name = InputWithoutInterrup("Name: ")
        if name is None: continue
        if name in data["servers"]: ssh_copy_id(data["servers"][name])
        else: print("Server not found.")
        continue

    if com == "help":
        print("add - add server\ndel - delete server\nls - list of all your servers\ncopyid - throw ssh-copy-id to server\nexit - stop program")
        continue

    if com == "exit":
        sys.exit()

    if com in data["servers"]:
        connect(data["servers"][com])
