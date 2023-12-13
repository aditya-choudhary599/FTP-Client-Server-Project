import os
import time
import shlex
import zipfile
from tqdm import tqdm


def get_params_from_query(query) -> str:
    query = query.strip()
    tokens = shlex.split(query)
    arguments = ' '.join(tokens[1:])

    if '~' in arguments:
        arguments = os.path.expanduser(arguments)

    if not arguments:
        arguments = '.'

    return arguments


def file_transfer_receiver_side(save_path, conn):
    file_size = int(conn.recv(8192).decode())
    received_size = 0
    time.sleep(5)

    with tqdm(total=file_size, desc=f"Receiving {os.path.basename(save_path)}", unit='B', unit_scale=True) as pbar:
        with open(save_path, "wb") as file:
            while received_size < file_size:
                data = conn.recv(8192)
                if not data:
                    break
                file.write(data)
                received_size += len(data)
                pbar.update(len(data))

    print(f"{save_path} received successfully.")


def file_transfer_sender_side(file_path, conn):
    file_size = os.path.getsize(file_path)
    conn.sendall(str(file_size).encode())
    time.sleep(10)

    with tqdm(total=file_size, desc=f"Sending {os.path.basename(file_path)}", unit='B', unit_scale=True) as pbar:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(8192)
                if not data:
                    break
                conn.sendall(data)
                pbar.update(len(data))

    print(f"{file_path} sent successfully.")


def zip_folder(source_folder, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_folder)
                zip_file.write(file_path, arcname=arcname)


def unzip_folder(zip_path, destination_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(destination_folder)


def folder_transfer_receiver_side(save_path, conn):
    zip_path = f"{save_path}.zip"
    zip_size = int(conn.recv(8192).decode())
    time.sleep(5)

    with tqdm(total=zip_size, desc=f"Receiving {os.path.basename(save_path)}", unit='B', unit_scale=True) as pbar:
        with open(zip_path, 'wb') as zip_file:
            received_size = 0
            while received_size < zip_size:
                data = conn.recv(8192)
                if not data:
                    break
                zip_file.write(data)
                received_size += len(data)
                pbar.update(len(data))

    unzip_folder(zip_path, save_path)
    os.remove(zip_path)
    print(f"{save_path} received successfully.")


def folder_transfer_sender_side(save_path, conn):
    zip_path = f"{save_path}.zip"
    zip_folder(save_path, zip_path)
    zip_size = os.path.getsize(zip_path)

    conn.sendall(str(zip_size).encode())
    time.sleep(10)

    with tqdm(total=zip_size, desc=f"Sending {os.path.basename(save_path)}", unit='B', unit_scale=True) as pbar:
        with open(zip_path, 'rb') as zip_file:
            while True:
                data = zip_file.read(8192)
                if not data:
                    break
                conn.sendall(data)
                pbar.update(len(data))

    os.remove(zip_path)
    print(f"{save_path} sent successfully.")
