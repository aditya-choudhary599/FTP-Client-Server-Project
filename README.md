# FTP Client-Server Project

## Overview

This project is an implementation of a basic FTP (File Transfer Protocol) client-server system in Python. The system facilitates efficient file and folder operations between a client and a server, providing a command-line interface for users to interact with the FTP server.

## Features

### FTP Client (`ftp_client.py`)

1. **Connection Handling:**
   - Establishes a socket connection to the FTP server.
   - Uses TCP/IP sockets for communication.

2. **Command Interpretation:**
   - Interprets various commands entered by the user, including `GET_FILE`, `LOAD_FILE`, `GET_FOLDER`, `LOAD_FOLDER`, `CD`, `MKDIR`, `RMDIR`, `MKFILE`, `RMFILE`, `PWD`, and `LIST`.

3. **File and Folder Transfer:**
   - Implements file transfer functionalities using the `GET_FILE` and `LOAD_FILE` commands.
   - Supports folder transfers through the `GET_FOLDER` and `LOAD_FOLDER` commands.
   - Utilizes the `tqdm` library for progress bars during file and folder transfers.

4. **User Interface:**
   - Provides a simple command-line interface for users to interact with the FTP server.
   - Displays server responses and prompts for user input.

### FTP Server (`ftp_server.py`)

1. **Connection Management:**
   - Listens for incoming client connections on a specified IP address and port.
   - Accepts client connections and establishes communication.

2. **Command Execution:**
   - Executes various commands received from the client, such as `QUIT`, `PWD`, `LIST`, `CD`, `MKDIR`, `RMDIR`, `MKFILE`, `RMFILE`, `GET_FILE`, `LOAD_FILE`, `GET_FOLDER`, and `LOAD_FOLDER`.

3. **File and Folder Operations:**
   - Handles file and folder transfers with the client using sockets.
   - Supports basic file and folder operations like listing directory contents, changing directories, creating folders, and deleting files and folders.

4. **User Interface:**
   - Provides server responses to client requests.
   - Displays information about successful connections and command executions.

### Utilities (`utils.py`)

1. **File Transfer Functions:**
   - Implements functions for sending and receiving files between the client and server.
   - Progress bars provided for visualizing file transfer progress.

2. **Folder Transfer Functions:**
   - Supports compression and decompression of folders for efficient transfer.
   - Utilizes the `tqdm` library for progress bars during folder transfers.

3. **Query Parameter Extraction:**
   - Extracts parameters from user queries for processing.

## Usage

1. Run the FTP server: `python ftp_server.py`.
2. Run the FTP client: `python ftp_client.py`.
3. Enter commands in the client to interact with the server.

## File and Folder Transfer

- File transfers use `GET_FILE` and `LOAD_FILE` commands.
- Folder transfers use `GET_FOLDER` and `LOAD_FOLDER` commands.
- Files and folders are transferred using sockets, and folders are compressed and decompressed for efficient transfer.
- Progress bars indicate the status of file and folder transfers.

## Additional Notes

- The project utilizes Python's `socket` library for network communication.
- Basic error handling is implemented for socket connections and file operations.
- Commands are parsed using the `shlex` module.
- Progress bars are provided during file and folder transfers using the `tqdm` library.