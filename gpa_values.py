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
from functools import lru_cache

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "results.csv")


@lru_cache()
def get_gpa(user_id: str, step: int) -> List[str]:
    """Get GPA data from results.csv for a specific user"""
    with open(file=data_path, mode="r", encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if step == 1:
                if row[0].lower() == user_id.lower():
                    return row
            elif step == 2:
                if row[1].lower() == user_id.lower():
                    return row

    return []


@lru_cache()
def calculate_gpa(user_nic: str) -> str:
    """Construct and return reply-message body with GPA values"""
    results = get_gpa(user_nic, 2)
    message_body: str = ""
    warnings: str = ""

    if results == []:
        return "Invalid NIC detected! - Sorry, You are not authorized to continue..."
    if results[10]:
        return (
            "I can't validate your NIC because it's not registered in database.\n"
            "Please mention admin to update your NIC"
        )

    # Semester GPAs
    count: int = 1
    message_body += "<b><u>Semester GPA</u></b>\n\n"
    for item in results[2:10]:
        if item in ["", "\n"]:
            count += 1
            continue
        sgpa: float = round(float(item), 2)
        if sgpa < 1.50:
            warnings += (
                f"🔴 Semester {count} GPA: <b>{sgpa}</b> - <b>Academic Probation</b>\n"
            )
        if sgpa < 2.00:
            warnings += (
                f"🔴 Semester {count} GPA: <b>{sgpa}</b> - <b>Academic Warning</b>\n"
            )
        message_body += f"🔹Semester {count} GPA: <b>{sgpa}</b>\n"
        count += 1
    message_body += "\n"

    # Level GPAs
    count = 1
    message_body += "<b><u>Level GPA</u></b>\n\n"
    for item in results[11:15]:
        if item in ["", "\n"]:
            count += 1
            continue
        message_body += f"🔹Level {count} GPA: <b>{round(float(item), 2)}</b>\n"
        count += 1
    message_body += "\n"

    # Current GPA
    cgpa: float = round(float(results[15]), 2)
    message_body += f"🔹Your Current GPA is <b>{cgpa}</b>\n\n"

    # Academic Status
    message_body += academic_status(cgpa)

    # Add academic Warnings
    if warnings != "":
        message_body += "\n\n<b><u>Warnings</u></b>\n\n" + warnings
    else:
        message_body += (
            "\n\n<b><u>Warnings</u></b>\n\nCool! 👍 No Academic Warnings for you"
        )

    return message_body


@lru_cache()
def academic_status(cgpa: float) -> str:
    """Construct the academic status message based on cgpa value"""
    status_msg: str = ""
    if cgpa >= 3.70:
        status_msg += "Congrats! 🎉✨🚀 You currently have a First Class 🔥🔥🔥 - Keep it up!"
    elif cgpa >= 3.30:
        status_msg += (
            "Congrats! 🎉✨ You currently have a Second Class Upper 🔥🔥 - Keep it up!"
        )
    elif cgpa >= 3.30:
        status_msg += (
            "Congrats! 🎉✨ You currently have a Second Class Lower 🔥🔥 - Keep it up!"
        )
    elif cgpa >= 2.00:
        status_msg += "Pass! ✨ - Keep it up! - You can achieve a class! 🔥"
    else:
        status_msg += "GPA is less than 2.0 😢 - or did I make any mistake?"

    return status_msg
