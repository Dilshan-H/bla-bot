"""
Get birthdays for a specific date from a CSV file and return wishes for each user with a random text

Functions:
    get_birthdays() -> List[str]

Author: @dilshan-h (https://github.com/dilshan-h)
"""

import os
from typing import List
import csv
from datetime import datetime
from random import choice
import pytz
from cryptography.fernet import Fernet

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
data_path: str = os.path.join(BASE_DIR, "DATA", "full_batch_data.csv.crypt")
TIME_ZONE: str = "Asia/Colombo"
fernet = Fernet(os.environ["SECRET_KEY"])

WISHES: List[str] = [
    "May this birthday be just the beginning of a year filled with wonderful moments...",
    "May the years continue to be good to you...",
    "May this year be the best of your life...",
    "May each and every passing year bring you wisdom, peace and cheer...",
    "Wishing you a wonderful day and fabulous year...",
    "Smile! It's your birthday...",
    "Best wishes for a happy day filled with laughter and love...",
    "Wishing you great happiness and a joy that never ends...",
    "Many happy returns of the day...",
    "Wishing you another wonderful year of happiness and joy...",
    "May this year be your best ever!",
    "Here's to celebrating you!",
    "May this day bring to you all things that make you smile...",
    "Life is a journey, so enjoy every mile...",
    "Count your life by smiles, not tears; Count your age by friends, not years...",
]


def get_birthdays() -> List[str]:
    """Check for users' birthdays"""
    now = datetime.now().astimezone(pytz.timezone(TIME_ZONE))
    names: List[str] = []
    with open(file=data_path, mode="rb") as data_file:
        stream = data_file.read()
        decrypted_data = fernet.decrypt(stream).decode().strip().split("\n")
        reader = csv.reader(decrypted_data)
        for row in reader:
            try:
                current_bday = datetime.strptime(row[2], "%Y-%m-%d")
                if now.month == current_bday.month and now.day == current_bday.day:
                    names.append(row[9])
            except ValueError:
                continue
    return names


def generate_wish() -> List[str]:
    """Get a random wish and construct the message body"""
    bday_wishes: List[str] = []
    names: List[str] = get_birthdays()
    if not names:
        return []

    for name in names:
        bday_wishes.append(
            "🎉🎉🎉🎉🎊🎈🎂🎈🎊🎉🎉🎉🎉"
            "\n\n"
            f"<b>{choice(WISHES)}</b>"
            "\n"
            f"ℍ𝔸ℙℙ𝕐 𝔹𝕀ℝ𝕋ℍ𝔻𝔸𝕐 {name}!"
            "\n\n"
            "🎉🎉🎉🎉🎊🎈🎂🎈🎊🎉🎉🎉🎉"
        )

    return bday_wishes
