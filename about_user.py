# pylint: disable=import-error

"""
Show information about a specific user based on the user's query

Functions:
    user_info(query: str) -> str
    calculate_lucky_no(birthday: str) -> str

Author: @dilshan-h (https://github.com/dilshan-h)
"""

from functools import lru_cache
import os
import csv
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from thefuzz import fuzz

load_dotenv()

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "full_batch_data.csv.crypt")
fernet = Fernet(os.environ["SECRET_KEY"])


@lru_cache(maxsize=16)
def user_info(query: str, admin: bool = False) -> str:
    """Get all users info and return the message body including requested info"""
    message_body: str = "<b>🔎 Here's what I have found:</b>\n\n"
    found_info: list = []
    with open(file=data_path, mode="rb") as data_file:
        stream = data_file.read()
        decrypted_data = fernet.decrypt(stream).decode().strip().split("\n")
        reader = csv.reader(decrypted_data)
        for row in reader:
            for item in row:
                if fuzz.ratio(query.lower(), item.lower()) > 80:
                    found_info.append(row)
                    break

        if not found_info:
            return (
                "😕 No matching data found!\nCan you try again with a different query?"
            )
        if len(found_info) > 1:
            if admin:
                items: str = ""
                for item in found_info:
                    items += item[9] + " | "
                return (
                    f"😕 <b>'{query}' found in {len(found_info)} places!"
                    f"</b>\nFound: {items}"
                )
            else:
                return (
                    f"😕 <b>'{query}' found in {len(found_info)} places!"
                    "</b>\nCan you narrow your search query?"
                )
        for info in found_info:
            message_body += (
                f"<b>👤 <u>About {info[9]}</u></b>"
                "\n\n"
                f"🔹<b>ID:</b> {info[0]}\n"
                f"🔹<b>Name:</b> {info[1]}\n"
                f"🔹<b>From:</b> {info[6]}\n"
                f"🔹<b>Birthday:</b> {info[2]}\n"
                f"🔹<b>Lucky No:</b> {calculate_lucky_no(info[2])}"
                "\n\n"
                "<b>📞 <u>Contact Info</u></b>"
                "\n\n"
                f"🔹<b>Phone:</b> +94{info[7]}\n"
                f"🔹<b>Emails:</b> {info[3]} {info[4]}\n"
                f"🔹<b>Address:</b> {info[5]}"
            )
            if info[8]:
                message_body += (
                    "\n\n<b><u>⛔ Database Errors</u></b>\n\n"
                    "NIC isn't registered in database.\n"
                    "Please mention/ping admin to update your NIC\n"
                )

    return message_body


def calculate_lucky_no(birthday: str) -> str:
    """Calculate the lucky number of a user based on his/her birthday"""
    lucky_no = sum(map(int, birthday.replace("-", "")))
    if lucky_no > 9:
        return calculate_lucky_no(str(lucky_no))
    return str(lucky_no)
