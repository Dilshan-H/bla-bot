"""
Provide information about various resources based on the user's query

Functions:
    get_resources(query: str) -> str

Author: @dilshan-h (https://github.com/dilshan-h)
"""

import os
import csv
from functools import lru_cache
from cryptography.fernet import Fernet
from thefuzz import fuzz

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "resources.csv.crypt")
fernet = Fernet(os.environ["SECRET_KEY"])


@lru_cache(maxsize=4)
def get_resources(query: str) -> str:
    """Construct info and return message body text"""
    found_info: list = []
    message_body: str = "<b>🔎 Here's what I have found:</b>\n\n"

    with open(file=data_path, mode="rb") as data_file:
        stream = data_file.read()
        decrypted_data = fernet.decrypt(stream).decode().strip().split("\n")
        reader = csv.reader(decrypted_data)
        for row in reader:
            try:
                for keyword in row[0].split(","):
                    if fuzz.partial_ratio(query.lower(), keyword.lower()) > 70:
                        found_info.append(row)
                        break
            except ValueError:
                continue

    if not found_info:
        return "😕 No matching data found!\nCan you try again with a different query?"
    if len(found_info) > 5:
        return (
            f"😕 <b>'{query}' found in {len(found_info)} places!"
            "</b>\nCan you narrow your search query?"
        )
    for info in found_info:
        message_body += f"<b>{info[1]}</b>\n"
        for link in info[2].split(","):
            if link:
                message_body += f"🔹 {link}\n"
        message_body += "\n"
    return message_body
