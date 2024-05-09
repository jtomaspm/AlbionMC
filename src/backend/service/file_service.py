import requests
import os

def download_raw_file(url: str, save_path: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print("File downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  
