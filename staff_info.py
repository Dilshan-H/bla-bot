"""Provide information about an specific employee"""

import os
from functools import lru_cache

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "staff_info.txt")


@lru_cache
def employee_info(query: str) -> str:
    """Construct info and return message body text"""
    found_info: list = []
    message_body: str = "<b>🔎 Here's what I have found:</b>\n\n"

    with open(file=data_path, mode="r", encoding="utf-8") as data_file:
        employees: list = data_file.read().split("\n\n")
        for employee in employees:
            if query.lower() in employee.lower():
                found_info.append(employee)

    if not found_info:
        return "😕 No matching data found!\nCan you try again with a different query?"
    if len(found_info) > 3:
        return (
            f"😕 <b>'{query}' found in {len(found_info)} places!"
            "</b>\nCan you narrow your search query?"
        )
    for info in found_info:
        message_body += f"{info}\n\n"

    return message_body
