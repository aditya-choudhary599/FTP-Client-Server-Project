import socket
import subprocess
from utils import *


class FTP_Server:
    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server_socket(self) -> None:
        self.server_socket.bind((self.ip_address, self.port))
        self.server_socket.listen()
        print(
            f'Server is listening on the {self.ip_address}:{self.port}', end='\n')
        self.run_server_socket()
        return

    def run_server_socket(self) -> None:
        client_socket, client_address = self.server_socket.accept()
        print(f"Connected with {client_address}", end='\n')
        client_socket.send(
            "Successfully connected with the ftp server!".encode())

        while True:
            query = client_socket.recv(8192).decode().strip()
            command = query.split(' ')[0].upper()

            if command == 'QUIT':
                client_socket.send("Closing the connection ....".encode())
                time.sleep(5)
                client_socket.close()
                self.server_socket.close()

            elif command == 'PWD':
                helper = os.getcwd()
                client_socket.send(f"{helper}".encode())

            elif command == 'LIST':
                arguments = get_params_from_query(query)
                ls_command = f"ls '{arguments}' -lha --color"
                result = subprocess.run(
                    ls_command, shell=True, stdout=subprocess.PIPE, text=True).stdout
                client_socket.send(result.encode())

            elif command == 'CD':
                arguments = get_params_from_query(query)
                os.chdir(arguments)
                response = f"Now you are in {os.getcwd()}"
                client_socket.send(response.encode())

            elif command == 'MKDIR':
                arguments = get_params_from_query(query)
                os.mkdir(arguments)
                response = f"Folder {arguments} created"
                client_socket.send(response.encode())

            elif command == 'RMDIR':
                arguments = get_params_from_query(query)
                rm_command = f"rm -r '{arguments}'"
                subprocess.run(rm_command, shell=True,
                               stdout=subprocess.PIPE, text=True)
                response = f"Folder {arguments} deleted"
                client_socket.send(response.encode())

            elif command == 'MKFILE':
                arguments = get_params_from_query(query)
                subprocess.run(['touch', f'{arguments}'], check=True)
                response = f"File {arguments} created"
                client_socket.send(response.encode())

            elif command == 'RMFILE':
                arguments = get_params_from_query(query)
                subprocess.run(['rm', f'{arguments}'], check=True)
                response = f"File {arguments} deleted"
                client_socket.send(response.encode())

            elif command == 'GET_FILE':
                arguments = get_params_from_query(query)
                file_transfer_sender_side(arguments, client_socket)

            elif command == 'LOAD_FILE':
                arguments = get_params_from_query(query)
                file_transfer_receiver_side(arguments, client_socket)

            elif command=='GET_FOLDER':
                arguments = get_params_from_query(query)
                folder_transfer_sender_side(arguments,client_socket)

            elif command=='LOAD_FOLDER':
                arguments = get_params_from_query(query)
                folder_transfer_receiver_side(arguments,client_socket)

server = FTP_Server('0.0.0.0', 44000)
server.start_server_socket()
