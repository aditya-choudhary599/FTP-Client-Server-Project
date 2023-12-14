import socket
from utils import *

server_address = '0.0.0.0'
server_port = 44000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_address, server_port))

data = client_socket.recv(8192).decode()
print(data, end='\n')

message = input(" -> ").strip()
while message != 'EXIT':
    if 'GET_FILES' in message:
        command, source_files, destination_files = get_source_and_destination_items(
            message)

        for i in range(len(source_files)):
            source_file = source_files[i]
            destination_file = destination_files[i]

            final_query = ' '.join([command, f"'{source_file}'"])
            client_socket.send(final_query.encode())
            file_transfer_receiver_side(destination_file, client_socket)

    elif 'GET_FILE' in message:
        tokens = shlex.split(message)
        command = tokens[0]
        source_file = tokens[1]
        destination_file = tokens[2]

        final_query = ' '.join([command, f"'{source_file}'"])
        client_socket.send(final_query.encode())
        file_transfer_receiver_side(destination_file, client_socket)

    elif 'LOAD_FILES' in message:
        command, source_files, destination_files = get_source_and_destination_items(
            message)

        for i in range(len(source_files)):
            source_file = source_files[i]
            destination_file = destination_files[i]

            final_query = ' '.join([command, f"'{destination_file}'"])
            client_socket.send(final_query.encode())
            file_transfer_sender_side(source_file, client_socket)

    elif 'LOAD_FILE' in message:
        tokens = shlex.split(message)
        command = tokens[0]
        source_file = tokens[1]
        destination_file = tokens[2]

        final_query = ' '.join([command, f"'{destination_file}'"])
        client_socket.send(final_query.encode())
        file_transfer_sender_side(source_file, client_socket)

    elif 'GET_FOLDERS' in message:
        command, source_folders, destination_folders = get_source_and_destination_items(
            message)

        for i in range(len(source_folders)):
            source_folder = source_folders[i]
            destination_folder = destination_folders[i]

            final_query = ' '.join([command, f"'{source_folder}'"])
            client_socket.send(final_query.encode())
            folder_transfer_receiver_side(destination_folder, client_socket)

    elif 'GET_FOLDER' in message:
        tokens = shlex.split(message)
        command = tokens[0]
        source_folder = tokens[1]
        destination_folder = tokens[2]

        final_query = ' '.join([command, f"'{source_folder}'"])
        client_socket.send(final_query.encode())
        folder_transfer_receiver_side(destination_folder, client_socket)

    elif 'LOAD_FOLDERS' in message:
        command, source_folders, destination_folders = get_source_and_destination_items(
            message)

        for i in range(len(source_folders)):
            source_folder = source_folders[i]
            destination_folder = destination_folders[i]

            final_query = ' '.join([command, f"'{destination_folder}'"])
            client_socket.send(final_query.encode())
            folder_transfer_sender_side(source_folder, client_socket)

    elif 'LOAD_FOLDER' in message:
        tokens = shlex.split(message)
        command = tokens[0]
        source_folder = tokens[1]
        destination_folder = tokens[2]

        final_query = ' '.join([command, f"'{destination_folder}'"])
        client_socket.send(final_query.encode())
        folder_transfer_sender_side(source_folder, client_socket)

    elif message[0:5] == 'CLEAR':
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        client_socket.send(message.encode())
        data = client_socket.recv(8192).decode()
        print('SERVER RESPONSE: \n' + data)

    message = input(" -> ").strip()

client_socket.send('QUIT'.encode())
client_socket.close()
