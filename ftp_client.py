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

    if message[0:8] == 'GET_FILE':
        tokens = shlex.split(message)
        command = tokens[0]
        source_file = tokens[1]
        destination_file = tokens[2]

        final_query = ' '.join([command, f"'{source_file}'"])
        client_socket.send(final_query.encode())
        file_transfer_receiver_side(destination_file,client_socket)
        
    elif message[0:9] == 'LOAD_FILE':
        tokens = shlex.split(message)
        command = tokens[0]
        source_file = tokens[1]
        destination_file = tokens[2]

        final_query = ' '.join([command, f"'{destination_file}'"])
        client_socket.send(final_query.encode())

        file_transfer_sender_side(source_file, client_socket)
    
    elif message[0:10]=='GET_FOLDER':
        tokens = shlex.split(message)
        command = tokens[0]
        source_folder = tokens[1]
        destination_folder = tokens[2]

        final_query = ' '.join([command, f"'{source_folder}'"])
        client_socket.send(final_query.encode())
        folder_transfer_receiver_side(destination_folder,client_socket)

    elif message[0:11]=='LOAD_FOLDER':
        tokens = shlex.split(message)
        command = tokens[0]
        source_folder = tokens[1]
        destination_folder = tokens[2]

        final_query = ' '.join([command, f"'{destination_folder}'"])
        client_socket.send(final_query.encode())
        
        folder_transfer_sender_side(source_folder,client_socket)

    elif message[0:5] == 'CLEAR':
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        client_socket.send(message.encode())
        data = client_socket.recv(8192).decode()
        print('SERVER RESPONSE: \n' + data)

    message = input(" -> ").strip()

client_socket.send('QUIT'.encode())
client_socket.close()
