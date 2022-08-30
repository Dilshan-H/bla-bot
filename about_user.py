"""Show information about a specific user"""

from functools import lru_cache
import os
import csv

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "full_batch_data.csv")


@lru_cache
def user_info(query: str) -> str:
    """Get all users info and return the message body including requested info"""
    message_body: str = "<b>🔎 Here's what I have found:</b>\n\n"
    found_info: list = []
    with open(file=data_path, mode="r", encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            for item in row:
                if query.lower() in item.lower():
                    found_info.append(row)
                    break

        if not found_info:
            return (
                "😕 No matching data found!\nCan you try again with a different query?"
            )
        if len(found_info) > 1:
            return (
                f"😕 <b>'{query}' found in {len(found_info)} places!"
                "</b>\nCan you narrow your search query?"
            )
        for info in found_info:
            message_body += (
                "<b>👤 <u>About</u></b>"
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


def calculate_lucky_no(birthday: str) -> int:
    """Calculate the lucky number of a user based on his/her birthday"""
    lucky_no = sum(map(int, birthday.replace("-", "")))
    if lucky_no > 9:
        return calculate_lucky_no(str(lucky_no))
    return lucky_no
