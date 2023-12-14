# FTP Client-Server Project

## Overview

The FTP Client-Server Project is a simple and versatile file transfer application built in Python. It consists of two main components: `ftp_server.py` and `ftp_client.py`. The system utilizes sockets for communication and supports various file and folder operations, including upload, download, listing, navigation, and more.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Server](#server)
  - [Client](#client)
- [Features](#features)
- [File Transfer](#file-transfer)
  - [Uploading Files](#uploading-files)
  - [Downloading Files](#downloading-files)
  - [Transferring Folders](#transferring-folders)
- [Commands](#commands)
- [Handling Multiple Files and Folders](#handling-multiple-files-and-folders)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- tqdm library (`pip install tqdm`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aditya-choudhary599/FTP-Client-Server-Project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 'FTP Client-Server Project'
   ```

3. Run the server:

   ```bash
   python3 ftp_server.py
   ```

4. Run the client:

   ```bash
   python3 ftp_client.py
   ```

## Usage

### Server

- The server runs on the specified IP address and port (default: `0.0.0.0:44000`).
- It accepts incoming connections from clients and handles various file and folder operations.

### Client

- The client connects to the server and provides a command-line interface for interacting with the file transfer system.
- Users can issue commands to navigate directories, list files, upload/download files, and transfer entire folders.

## Features

- **File Transfer:** Secure and efficient file transfer between the server and client.
- **Folder Operations:** Upload and download entire folders with automatic compression and decompression.
- **Command-Line Interface:** Simple and intuitive command-line interface for users.
- **Cross-Platform:** Compatible with Windows, Linux, and macOS.

## File Transfer

### Uploading a Single File

To upload a file from the client to the server, use the `LOAD_FILE` command:

```bash
LOAD_FILE 'source_file' 'destination_file'
```

### Downloading a Single File

To download a file from the server to the client, use the `GET_FILE` command:

```bash
GET_FILE 'source_file' 'destination_file'
```

### Transferring a Single Folder

To upload an entire folder, use the `LOAD_FOLDER` command:

```bash
LOAD_FOLDER 'source_folder' 'destination_folder'
```

To download an entire folder, use the `GET_FOLDER` command:

```bash
GET_FOLDER 'source_folder' 'destination_folder'
```

## Commands

- `PWD`: Print the current working directory.
- `LIST [directory]`: List files and directories in the specified directory.
- `CD [directory]`: Change the current working directory.
- `MKDIR [directory]`: Create a new directory.
- `RMDIR [directory]`: Remove a directory.
- `MKFILE [file]`: Create a new empty file.
- `RMFILE [file]`: Remove a file.
- `QUIT`: Disconnect from the server.

## Handling Multiple Files and Folders

- For commands involving files or folders (e.g., `LOAD_FILES`, `GET_FILES`, `LOAD_FOLDERS`, `GET_FOLDERS`), you can specify multiple items by providing additional pairs of paths. Each pair consists of a source and destination path.

  Example:

  ```bash
  LOAD_FILES 'local_file1-remote_file1' 'local_file2-remote_file2'
  ```

  ```bash
  GET_FILES 'remote_file1-local_file1' 'remote_file2-local_file2'
  ```

  ```bash
  LOAD_FOLDERS 'local_folder1-remote_folder1' 'local_folder2-remote_folder2'
  ```

  ```bash
  GET_FOLDERS 'remote_folder1-local_folder1' 'remote_folder2-local_folder2'
  ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
