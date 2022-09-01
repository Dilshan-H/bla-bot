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

FILES: List[str] = ["full_batch_data.csv", "results.csv", "staff_info.txt"]

key = Fernet.generate_key()
filename: str = (
    "KEY_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(":", "_") + ".txt"
)
# Save the key in the current folder
with open(filename, "wb") as key_file:
    key_file.write(key)


for file in FILES:
    with open(file, "rb") as file_to_encrypt:
        data = file_to_encrypt.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

    with open(file + ".crypt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"{file} encrypted.")

print("Encryption complete.")
