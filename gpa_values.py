"""Get GPA values from results.csv for all users and filter according to the request"""
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
