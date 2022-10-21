"""
Encrypt the data using a key.
IMPORTANT:
    - The key will be saved in the current folder with name 'key.txt'
    - Do not share the key with anyone!
    - Make sure to delete the original data files after encryption.
"""

from typing import List
from datetime import datetime
from cryptography.fernet import Fernet

FILES: List[str] = [
    "full_batch_data.csv",
    "results.csv",
    "resources.csv",
    "staff_info.txt",
]

key = Fernet.generate_key()
filename: str = (
    "KEY_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(":", "_") + ".txt"
)
# Save the key in the current folder
with open(filename, "wb") as key_file:
    key_file.write(key)
print(f"Key saved in {filename}")

for file in FILES:
    try:
        with open(file, "rb") as file_to_encrypt:
            data = file_to_encrypt.read()
            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)
    except FileNotFoundError:
        print(f"File '{file}' not found! -- Resuming...")
        continue

    try:
        with open(file + ".crypt", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
    except Exception as e:
        print(f"Error occurred while saving encrypted file: '{file}' -- Resuming...")
        print(e)
        continue

    print(f"==== {file} Encrypted. =====")

print("Encryption completed!")
