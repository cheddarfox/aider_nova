import os

def safe_read_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path) and os.access(file_path, os.R_OK):
            with open(file_path, 'r', encoding='utf-8') as file:
                yield file_path, file.read()
        else:
            print(f"Impossible d'accéder au fichier : {file_path}")
