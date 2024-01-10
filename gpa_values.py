# pylint: disable=line-too-long import-error

"""
Get GPA values from results.csv for all users and filter according to the request

Functions:
    get_gpa(user_id: str, step: int) -> List[str]
    calculate_gpa(user_nic: str) -> str
    academic_status(cgpa: float) -> str


Author: @dilshan-h (https://github.com/dilshan-h)
"""

import os
from typing import List
import csv
from random import choice
from functools import lru_cache
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "results.csv.crypt")
fernet = Fernet(os.environ["SECRET_KEY"])


@lru_cache(maxsize=16)
def get_gpa(user_id: str, step: int) -> List[str]:
    """Get GPA data from results.csv for a specific user"""
    with open(file=data_path, mode="rb") as data_file:
        stream = data_file.read()
        decrypted_data = fernet.decrypt(stream).decode().strip().split("\n")
        reader = csv.reader(decrypted_data)
        for row in reader:
            if step == 1:
                if row[0].lower() == user_id.lower():
                    return row
            elif step == 2:
                if row[1].lower() == user_id.lower():
                    return row

    return []


@lru_cache(maxsize=16)
def calculate_gpa(user_nic: str, admin: bool = False) -> str:
    """Construct and return reply-message body with GPA values"""
    if admin:
        results = get_gpa(user_nic, 1)
    else:
        results = get_gpa(user_nic, 2)
    message_body: str = ""
    warnings: str = ""

    if results == []:
        return "Invalid NIC detected! - Sorry, You are not authorized to continue..."

    if results[11] == "ERROR":
        return (
            "I can't validate your NIC because it's not registered in database.\n"
            "Please mention/ping admin to update your NIC"
        )
    if results[11] == "HOLD":
        warnings += "🔵 Your final results are on hold. Partially calculated GPA values are shown.\n\n"
    elif results[11] == "NEW":
        warnings += (
            "🔵 Since calculated GPA values are based on your current results within this batch;"
            "OGPA, CGPA and Academic Status will not represent accurate information.\n\n"
        )

    # Semester GPAs
    count: int = 1
    message_body += "<b><u>Semester GPA</u></b>\n\n"
    for item in results[3:11]:
        if item in ["", "\n"]:
            count += 1
            continue
        sgpa: float = round(float(item), 2)
        if sgpa < 1.50:
            warnings += (
                f"🔴 Semester {count} GPA: <b>{sgpa}</b> - <b>Academic Probation</b>\n"
            )
        elif sgpa < 2.00:
            warnings += (
                f"🔴 Semester {count} GPA: <b>{sgpa}</b> - <b>Academic Warning</b>\n"
            )
        message_body += f"🔹Semester {count} GPA: <b>{sgpa}</b>\n"
        count += 1
    message_body += "\n"

    # Level GPAs
    count = 1
    message_body += "<b><u>Level GPA</u></b>\n\n"
    for item in results[12:16]:
        if item in ["", "\n"]:
            count += 1
            continue
        message_body += f"🔹Level {count} GPA: <b>{round(float(item), 2)}</b>\n"
        count += 1
    message_body += "\n"

    # Current GPA
    cgpa: float = round(float(results[16]), 2)
    message_body += f"🔹Your Cumulative GPA is <b>{cgpa}</b>\n\n"

    # Academic Status
    message_body += academic_status(cgpa)

    # Add academic Warnings
    if warnings != "":
        message_body += "\n\n<b><u>Warnings</u></b>\n\n" + warnings
    else:
        message_body += (
            "\n\n<b><u>Warnings</u></b>\n\nCool! 👍 No Academic Warnings for you"
        )

    # Add disclaimer info
    message_body += "\n\n<i>🔹Please note that these data might not reflect the finalized GPA values in case of the usage of weighted average GPA.</i>\n\n"
    return message_body


def get_leaderboard() -> str:
    """Construct and return reply-message body with leaderboard"""
    with open(file=data_path, mode="rb") as data_file:
        stream = data_file.read()
        decrypted_data = fernet.decrypt(stream).decode().strip().split("\n")
        reader = csv.reader(decrypted_data)
        data: List[List[str]] = []
        for row in reader:
            data.append(row)

    # Sort data by CGPA
    # print(data)
    # data[1:].sort(key=lambda x: float(x[16]), reverse=True)
    sorted_data = sorted(data[1:], key=lambda x: float(x[16]), reverse=True)

    # Construct message body
    message_body: str = "<b><u>Leaderboard [Cumulative GPA]</u></b>\n\n"
    count: int = 1
    for row in sorted_data[:10]:
        if row[16] == "":
            continue
        message_body += f"{count}. <b>{row[2]}</b> 🔸 {row[16]}\n\n"
        count += 1

    return message_body


def academic_status(cgpa: float) -> str:
    """Construct the academic status message based on cgpa value"""
    status_msg: str = ""
    greetings: List[str] = [
        "Cheers!",
        "Yay!",
        "Cool!",
        "Awesome!",
    ]
    greeting: str = choice(greetings)
    # spoiler: str = "<span class='tg-spoiler'>"

    if cgpa >= 3.70:
        status_msg += (
            f"{greeting} 🎉✨ You currently have a <b>First Class</b> 🔥🔥\nKeep it up!"
        )
    elif cgpa >= 3.30:
        status_msg += f"{greeting} 🎉✨ You currently have a <b>Second Class Upper</b> 🔥🔥\nKeep it up!"
    elif cgpa >= 3.00:
        status_msg += f"{greeting} 🎉✨ You currently have a <b>Second Class Lower</b> 🔥🔥\nKeep it up!"
    elif cgpa >= 2.00:
        status_msg += (
            f"{greeting} 🎉✨ You have a "
            f"<b>pass</b>... \nKeep it up! ✨ - You can achieve a class!"
        )
    else:
        status_msg += "GPA is less than 2.0 😢 - or did I make any mistake?"

    return status_msg
